import logging


from amuse.community import *
from amuse.community.interface.common import CommonCodeInterface
from amuse.community.interface.common import CommonCode
from amuse.support import options
from amuse.rfi.channel import DistributedChannel

from distributed_datamodel import Resources, Resource
from distributed_datamodel import Pilots, Pilot
from distributed_datamodel import ScriptJobs, ScriptJob
from distributed_datamodel import FunctionJobs, FunctionJob

import pickle

logger = logging.getLogger(__name__)

class DistributedAmuseInterface(CodeInterface, CommonCodeInterface, LiteratureReferencesMixIn):
    """
	Distributed Amuse Code
    
        .. [#] The Distributed Amuse project is a collaboration between Sterrewacht Leiden and The Netherlands eScience Center.
    """

    classpath = ['.', 'worker.jar', 'src/dist/*']

# keeping a reference is no longer necessary
        
    def __init__(self, **keyword_arguments):
        CodeInterface.__init__(self, name_of_the_worker="distributed_worker_java", **keyword_arguments)
        LiteratureReferencesMixIn.__init__(self)


    @option(choices=['mpi','remote','distributed', 'sockets'], sections=("channel",))
    def channel_type(self):
        return 'sockets'
    
    @option(type="boolean", sections=("channel",))
    def initialize_mpi(self):
        """Is MPI initialized in the code or not. Defaults to True if MPI is available"""
        return False
    
    @legacy_function
    def get_worker_port():
        """
        Returns the server socket port of the code. Used by the distributed channel
        """
        function = LegacyFunctionSpecification()
        function.addParameter("worker_port", dtype='int32', direction=function.OUT)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_debug():
        """
	    Returns if debugging is enabled
        """
        function = LegacyFunctionSpecification()
        function.addParameter("debug", dtype='int32', direction=function.OUT)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def set_debug():
        """
        Enable or disable debugging
        """
        function = LegacyFunctionSpecification()
        function.addParameter("debug", dtype='int32', direction=function.IN)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_start_hubs():
        """
        Returns if starting hubs is enabled
        """
        function = LegacyFunctionSpecification()
        function.addParameter("start_hubs", dtype='int32', direction=function.OUT)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def set_start_hubs():
        """
        Enable or disable starting hubs.
        """
        function = LegacyFunctionSpecification()
        function.addParameter("start_hubs", dtype='int32', direction=function.IN)
        function.result_type = 'int32'
        return function

    @legacy_function
    def get_webinterface_port():
        """
        Returns the port the webinterface is running on
        """
        function = LegacyFunctionSpecification()
        function.addParameter("webinterface_port", dtype='int32', direction=function.OUT)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def set_webinterface_port():
        """
        Set the port the webinterface is running on
        """
        function = LegacyFunctionSpecification()
        function.addParameter("webinterface_port", dtype='int32', direction=function.IN)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_worker_startup_timeout():
        """
        Returns the port the webinterface is running on
        """
        function = LegacyFunctionSpecification()
        function.addParameter("worker_startup_timeout", dtype='int32', unit=units.s, direction=function.OUT)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def set_worker_startup_timeout():
        """
        Set the port the webinterface is running on
        """
        function = LegacyFunctionSpecification()
        function.addParameter("worker_startup_timeout", dtype='int32', unit=units.s, direction=function.IN)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def new_resource():
        """
        Define a new resource. This function returns an index that can be used to refer
        to this resource.
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('resource_id', dtype='int32', direction=function.OUT)
        function.addParameter("name", dtype='string', direction=function.IN)
        function.addParameter("location", dtype='string', direction=function.IN)
        function.addParameter("amuse_dir", dtype='string', direction=function.IN)
        function.addParameter("gateway", dtype='string', direction=function.IN, default=[""])
        function.addParameter("scheduler_type", dtype='string', direction=function.IN, default=["ssh"])
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_resource_state():
        """
        Get all the attributes of a resource.
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('resource_id', dtype='int32', direction=function.IN)
        function.addParameter("name", dtype='string', direction=function.OUT)
        function.addParameter("location", dtype='string', direction=function.OUT)
        function.addParameter("gateway", dtype='string', direction=function.OUT)
        function.addParameter("amuse_dir", dtype='string', direction=function.OUT)
        function.addParameter("scheduler_type", dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function

    @legacy_function
    def delete_resource():
        """
        Remove the definition of resource from the code. After calling this function the resource is
        no longer part of the model evolution. It is up to the code if the index will be reused.
        This function is optional.
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('resource_id', dtype='int32', direction=function.IN,
            description = "Index of the resource to be removed. This index must have been returned by an earlier call to :meth:`new_resource`")

        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        function.result_doc = """
        0 - OK
            resource was removed from the model
        -1 - ERROR
            resource could not be removed
        -2 - ERROR
            not yet implemented
        """
        return function
    
    @legacy_function
    def new_pilot():
        """
        Reserve one or more nodes for later use by the simulation.
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('pilot_id', dtype='int32', direction=function.OUT)
        function.addParameter("resource_name", dtype='string', direction=function.IN)
        function.addParameter("queue_name", dtype='string', direction=function.IN, default=[""])
        function.addParameter("node_count", dtype='int32', direction=function.IN, default = 1)
        function.addParameter("time", dtype='int32', direction=function.IN, unit = units.minute, default = 60)
        function.addParameter("slots_per_node", dtype='int32', direction=function.IN, default = 1)
        function.addParameter("label", dtype='string', direction=function.IN, default = ["default"])
        function.addParameter("options", dtype='string', direction=function.IN, default = [""])
        function.addParameter('count', dtype='int32', direction=function.LENGTH)

        function.result_type = 'int32'
        return function
    
 

    @legacy_function
    def get_pilot_state():
        """
        Get all attributes of a pilot
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('pilot_id', dtype='int32', direction=function.IN)
        function.addParameter("resource_name", dtype='string', direction=function.OUT)
        function.addParameter("queue_name", dtype='string', direction=function.OUT)
        function.addParameter("node_count", dtype='int32', direction=function.OUT)
        function.addParameter("time", dtype='int32', direction=function.OUT, unit = units.minute)
        function.addParameter("slots_per_node", dtype='int32', direction=function.OUT)
        function.addParameter("label", dtype='string', direction=function.OUT)
        function.addParameter("options", dtype='string', direction=function.OUT)
        function.addParameter('status', dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)

        function.result_type = 'int32'
        return function

    
    @legacy_function
    def get_pilot_status():
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('pilot_id', dtype='int32', direction=function.IN)
        function.addParameter('status', dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def delete_pilot():
        """
        Delete (stop) a pilot.
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('pilot_id', dtype='int32', direction=function.IN)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def wait_for_pilots():
        """
        Wait until all pilots are started, and all nodes are available to run jobs and/or workers
        """
        function = LegacyFunctionSpecification()
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def submit_script_job():
        """
        Submit a job, specified by a script
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.OUT)
        function.addParameter('script_dir', dtype='string', direction=function.IN)
        function.addParameter('script_name', dtype='string', direction=function.IN)
        function.addParameter('arguments', dtype='string', direction=function.IN, default = [""])
        function.addParameter('input_dir', dtype='string', direction=function.IN, default = [""])
        function.addParameter('output_dir', dtype='string', direction=function.IN, default = [""])
        function.addParameter('stdout_file', dtype='string', direction=function.IN, default = [""])
        function.addParameter('stderr_file', dtype='string', direction=function.IN, default = [""])
        function.addParameter("label", dtype='string', direction=function.IN, default = [""])
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_script_job_state():
        """
        Get all attributes of a script job
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.IN)
        function.addParameter('script_dir', dtype='string', direction=function.OUT)
        function.addParameter('script_name', dtype='string', direction=function.OUT)
        function.addParameter('arguments', dtype='string', direction=function.OUT)
        function.addParameter('input_dir', dtype='string', direction=function.OUT)
        function.addParameter('output_dir', dtype='string', direction=function.OUT)
        function.addParameter('stdout_file', dtype='string', direction=function.OUT)
        function.addParameter('stderr_file', dtype='string', direction=function.OUT)
        function.addParameter("label", dtype='string', direction=function.OUT)
        function.addParameter("status", dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_script_job_status():
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.IN)
        function.addParameter('status', dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def delete_script_job():
        """
        Delete (cancel) a script job
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.IN)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def wait_for_script_jobs():
        """
        Wait until all script jobs are done.
        """
        function = LegacyFunctionSpecification()
        function.result_type = 'int32'
        return function

    @legacy_function
    def submit_function_job():
        """
        Submit a job, specified by a pickle of the function, and a pickle of the arguments.
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.OUT)
        function.addParameter('function', dtype='string', direction=function.IN)
        function.addParameter('arguments', dtype='string', direction=function.IN)
        function.addParameter('kwarguments', dtype='string', direction=function.IN)
        function.addParameter('stdout_file', dtype='string', direction=function.IN)
        function.addParameter('stderr_file', dtype='string', direction=function.IN)
        function.addParameter("label", dtype='string', direction=function.IN, default = ["default"])
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
     
    @legacy_function
    def get_function_job_state():
        """
        Get all attributes of a pickled job
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.IN)
        function.addParameter('stdout_file', dtype='string', direction=function.OUT)
        function.addParameter('stderr_file', dtype='string', direction=function.OUT)
        function.addParameter("label", dtype='string', direction=function.OUT)
        function.addParameter("status", dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
     
     
     
    @legacy_function
    def get_function_job_status():
        """
        Get all attributes of a pickled job
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.IN)
        function.addParameter("status", dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
     
    @legacy_function
    def get_function_job_result():
        """
        Get a result of a picked function job. Will block until the result is available
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.IN)
        function.addParameter('result', dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
     
    @legacy_function
    def delete_function_job():
        """
        Delete (cancel) a script job
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('job_id', dtype='int32', direction=function.IN)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
     
    @legacy_function
    def get_worker_state():
        """
        Get all attributes of a pickled job
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('worker_id', dtype='int32', direction=function.IN)

        function.addParameter('executable', dtype='string', direction=function.OUT)
        function.addParameter("label", dtype='string', direction=function.OUT)
        function.addParameter("worker_count", dtype='int32', direction=function.OUT)
        function.addParameter("thread_count", dtype='int32', direction=function.OUT)
        function.addParameter("status", dtype='string', direction=function.OUT)
        
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_worker_status():
        """
        Get all attributes of a worker
        """
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('worker_id', dtype='int32', direction=function.IN)
        function.addParameter("status", dtype='string', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_number_of_workers():
        function = LegacyFunctionSpecification()
        function.addParameter('number_of_workers', dtype='int32', direction=function.OUT)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_worker_ids():
        function = LegacyFunctionSpecification()
        function.must_handle_array = True
        function.addParameter('index', dtype='int32', direction=function.IN) # probably unused, but required to get 'count'
        function.addParameter('id_of_the_worker', dtype='int32', direction=function.OUT)
        function.addParameter('count', dtype='int32', direction=function.LENGTH)
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def get_current_error():
        """When a function returns an error, this will retrieve
        a description (if possible)
        """
        function = LegacyFunctionSpecification()  
        function.addParameter('string', 
            dtype='string',
            direction=function.OUT,
            description = "description of the error"
        )
        function.result_type = 'int32'
        return function
    
    @legacy_function
    def end_all():
        """
        Stop all jobs, resources and pilots
        """
        function = LegacyFunctionSpecification()
        function.result_type = 'int32'
        return function
    
    def cleanup_code(self):
        self.end_all()
        return 0
    
    def new_worker(self):
        raise exceptions.AmuseException("Can't add to 'workers' directly. Create community code instances in the usual way instead.")
    
    def delete_worker(self):
        raise exceptions.AmuseException("Can't remove from 'workers' directly. Stop community code instances in the usual way instead.")

class DistributedAmuse(CommonCode):

    def __init__(self, **options):
        CommonCode.__init__(self,  DistributedAmuseInterface(**options), **options)
    
    def submit_function_job(self, label, stdout_file, stderr_file, function, *args, **kwargs):
        # pickle the input function
        
        pickled_function = pickle.dumps(function,0)
        pickled_arguments = pickle.dumps(args,0)
        pickled_kwarguments = pickle.dumps(kwargs,0)
        
        return self.overridden().submit_function_job(function=pickled_function, arguments=pickled_arguments, kwarguments=pickled_kwarguments, label=label, stdout_file=stdout_file, stderr_file=stderr_file)
    
    def get_function_job_result(self, job_id):
        pickled_result = self.overridden().get_function_job_result(job_id)
        
        result = pickle.load(pickled_result)
        
        return result
    
    def get_webinterface_url(self):
        return "http://localhost:" + str(self.parameters.webinterface_port)
    
    def commit_parameters(self):
        self.parameters.send_not_set_parameters_to_code()
        self.parameters.send_cached_parameters_to_code()
        self.overridden().commit_parameters()

        self.port = self.get_worker_port()

        if  DistributedChannel.defaultDistributedInstance is None:
          DistributedChannel.defaultDistributedInstance=self
        
        #logging.basicConfig(level=logging.DEBUG)
        
        logger.debug("running on port %d", self.port)

#        self.stdoutHandler = OutputHandler(sys.stdout, port)
#        self.stderrHandler = OutputHandler(sys.stderr, port)

    def set_as_default(self):
        DistributedChannel.defaultDistributedInstance=self
        
    def set_as_default_for_all_workers(self):
        DistributedChannel.defaultDistributedInstance=self
        options.GlobalOptions.instance().override_value_for_option("channel_type", "distributed")

    def cleanup_code(self):
        if DistributedChannel.defaultDistributedInstance is self:
            DistributedChannel.defaultDistributedInstance=None
            if options.GlobalOptions.instance().overriden_options.has_key("channel_type"):
              del options.GlobalOptions.instance().overriden_options["channel_type"]
        self.overridden().cleanup_code()
        
    def define_state(self, object): 
        CommonCode.define_state(self, object)   
        object.add_transition('INITIALIZED','RUN','commit_parameters')
        object.add_transition('RUN','CHANGE_PARAMETERS_RUN','before_set_parameter', False)
        object.add_transition('CHANGE_PARAMETERS_RUN','RUN','recommit_parameters')
        
        object.add_method('CHANGE_PARAMETERS_RUN', 'before_set_parameter')
        object.add_method('CHANGE_PARAMETERS_RUN', 'before_get_parameter')
        object.add_method('RUN', 'before_get_parameter')
        
        
        object.add_method('RUN', 'new_resource')
        object.add_method('RUN', 'new_pilot')
        object.add_method('RUN', 'submit_script_job')
        object.add_method('RUN', 'submit_function_job')
        object.add_method('RUN', 'get_resource_state')
        object.add_method('RUN', 'get_pilot_state')
        object.add_method('RUN', 'get_pilot_status')
        object.add_method('RUN', 'get_script_job_state')
        object.add_method('RUN', 'get_script_job_status')
        object.add_method('RUN', 'get_function_job_state')
        object.add_method('RUN', 'get_function_job_status')
        object.add_method('RUN', 'get_worker_state')
        object.add_method('RUN', 'get_worker_status')
        object.add_method('RUN', 'set_as_default')
        object.add_method('RUN', 'set_as_default_for_all_workers')
    
    def define_parameters(self, object):
              
        object.add_boolean_parameter(
            "get_debug",
            "set_debug",
            "debug", 
            "If true, will output additional debugging information and logs", 
            default_value = False
        )
        
        object.add_boolean_parameter(
            "get_start_hubs",
            "set_start_hubs",
            "start_hubs", 
            "If true, start a communication support hub on each resource", 
            default_value = True
        )
        
        object.add_method_parameter(
            "get_worker_port",
            None,
            "worker_port", 
            "Port that the distributed code uses to handle new worker requests on from the distributed channel", 
            default_value = 0
        )
        
        object.add_method_parameter(
            "get_webinterface_port",
            "set_webinterface_port",
            "webinterface_port", 
            "Port for monitoring webinterface", 
            default_value = 0
        )
        
        object.add_method_parameter(
            "get_worker_startup_timeout",
            "set_worker_startup_timeout",
            "worker_startup_timeout", 
            "Port for monitoring webinterface", 
            default_value = 60 | units.s
        )

    
    def define_particle_sets(self, object):
        object.define_super_set('items', ['resources', 'pilots', 'script_jobs', 'function_jobs', '_workers'])
        
        #resources
        object.define_set('resources', 'resource_id')
        object.set_new('resources', 'new_resource')
        object.set_delete('resources', 'delete_resource')
        object.add_getter('resources', 'get_resource_state')
        object.mapping_from_name_to_set_definition['resources'].particles_factory = Resources
        
        #pilots
        object.define_set('pilots', 'pilot_id')
        object.set_new('pilots', 'new_pilot')
        object.set_delete('pilots', 'delete_pilot')
        object.add_getter('pilots', 'get_pilot_state')
        object.add_getter('pilots', 'get_pilot_status', names = ('status',))
        object.mapping_from_name_to_set_definition['pilots'].particles_factory = Pilots
        
        #script jobs
        object.define_set('script_jobs', 'job_id')
        object.set_new('script_jobs', 'submit_script_job')
        object.set_delete('script_jobs', 'delete_script_job')
        object.add_getter('script_jobs', 'get_script_job_state')
        object.add_getter('script_jobs', 'get_script_job_status', names = ('status',))
        object.mapping_from_name_to_set_definition['script_jobs'].particles_factory = ScriptJobs

        
        #function jobs
        object.define_set('function_jobs', 'job_id')
        object.set_new('function_jobs', 'submit_function_job')
        object.set_delete('function_jobs', 'delete_function_job')
        object.add_getter('function_jobs', 'get_function_job_state')
        object.add_getter('function_jobs', 'get_function_job_status')
        object.mapping_from_name_to_set_definition['function_jobs'].particles_factory = FunctionJobs
        
        #workers
        object.define_set('_workers', 'worker_id')
        object.set_new('_workers', 'new_worker')
        object.set_delete('_workers', 'delete_worker')
        object.add_getter('_workers', 'get_worker_state')
        object.add_getter('_workers', 'get_worker_status', names = ('status',))
        
    @property
    def workers(self):
        self.update_workers_particle_set()
        return self._workers
    
    def update_workers_particle_set(self):
        """
        Update the "workers" particle set after new instances of codes have been
        created or previously created instances have been stopped.
        """
        old_ids = set(self._workers.get_all_indices_in_store())
        number_of_workers = self.get_number_of_workers()
        if not number_of_workers == 0:
            new_ids = set(self.get_worker_ids(range(number_of_workers)))
        else:
            new_ids=set()
        
        ids_to_remove = old_ids - new_ids
        ids_to_add = new_ids - old_ids
        if not len(ids_to_remove) == 0:
            self._workers._remove_indices_in_attribute_storage(list(ids_to_remove))
        if not len(ids_to_add) == 0:
            self._workers._add_indices_in_attribute_storage(list(ids_to_add))
    
