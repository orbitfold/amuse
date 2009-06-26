import unittest

from amuse.experiments.plummer import *
import pickle

random_state =  r"""(S'MT19937'
p0
cnumpy.core.multiarray
_reconstruct
p1
(cnumpy
ndarray
p2
(I0
tp3
S'b'
p4
tp5
Rp6
(I1
(I624
tp7
cnumpy
dtype
p8
(S'u4'
p9
I0
I1
tp10
Rp11
(I3
S'<'
p12
NNNI-1
I-1
I0
tp13
bI00
S'\xe2v\xfb\xf7\xb41\xe6AX\x9c\xb1\xeb\xda\xd5\xe2\xa3\x0e\xd8\x18.\xa4pB\xf8\xcc\xda\xfcDL\x7f#\x95~%\xb7\xa4\x84&\xb2/\x16s,?\xad4\xf3\x07\xaa\x81\x10\x1f\x9f=\xa1\x0fcu\xcf\xbb\x1a\xe2D|u\xa0\xbd\xd9zO6\xb8v\xa31\x03O\x85 \x8c\xb5p\x8b_Z`h\x17\x0c\xeb\xfd>\xd8\x9d\xc9\x84\xb5~\x13\x17\xc6\xff\xef=\xcd\xf3\xa6\xbf.\x14\t!3\xa1\xb2\xf7\xbc)e\x01[\xc6\xdf.\x83\xb8\xb8*\x1f\xf4\xdd\xfe\x0cT\xb5A+\xdd\x02#Q\xf7\x08\xc7\x02\x90\xb0E\x94nT\xfd\xa9\xd9\xba\xcc\x9fK\xa4J"\xa0\x17\x92:([\x99\xea_?\x95z-\xde~\xbd2\xf3\x12\xbf_\xb1\xa4\xe3\x0c\x8a\xdc\xda\x05\xe2\x02%\xb5o\xc6-\xeb\xee|\x97\x94Xe\x11\xbd\xef\x0e\xc5\xed\xb6\x81g\xf6\xcb\xe1e\x98\xc9q\xe8\xeb\x1c=e\x9dA\x84\xb2\xe9\xc71\xe14\xd0Aq\x10\x0e\xd1.\xa7#\x87\xd2\x19\n\x04\x9bgE\xaf\xa0Z\xa7\xa9$6\xd3%\xb9z\xe4\xbe\xabsDj"*\x84\xa2*$S\xb3\xb3\x0b\n8\x11t\xe2\xc2{\x02f\x8d\x0c\xad\xb55\xd2$g1\xd5\xdd\x92\xacr\x08k\x18\xf24\xc5\xfe\xa3WS\x11U\x9fb\xf5v\x06\xb5\r]\x83,\r\x02\x10\x82\xcf\x1f\xd1a1=\xb0\x90\x12\xe0n\x14K\xd8\xccOl}\x93&n?Hffp\x01\xa8\x85=\xd78\x08\xbcb\xc4y\xce\xb1\xa2\xc7tD\xfc\x9f0\x92\x10\xa3\xfc\x11\x9e\xa0\x16/1\xd69\xf2E\x16\x93J\x19\xfd\x1d-\xdb\xc3\xa2\x8d\x8d\x13\xc3\x8f\x8d\xd4\xf0e\x80f\xea\xac\x8f\xdc\xe9sU\x9e\x17W\xe4\xc0\x15\t\x91\xe3QD\x1fS\xed\x84\n\xfd\xc0\x91\x03=\xd1\x97\xab\xe0\x05\xcc&\\\x9d\xc7>\xa8\x9f\xc1\xab\x92R\xb6\xad\x1fr\x8fq\x1a\xb5\x17<\x00\xc3\x92j\xa3\x17o\xf6t\x0b\x8c_\xfd\xac.\xaaW\xb1y"\xf0\xbb\xc3\xf2M\xe3\x15\x9c\xfb\xe2\xc0G\xf2j\xd0D\xa0bO4\xe7\x8d\xb1\xfc`}x\x1e\xf5>\x96\xba"\xf4\xf0\xd5\xff\x07\xb6\x8d\xf0\x19th\xda\xa0,\xe5\x04\x1d\x1b\xf5\xb1\xd3\x0c\x8cB\xc8\x00\x07\x0f\xc3\xf5\xd9\xff\x82\xb4\xfb\x02\x14\x87\xca\x16\x1e\xac\xb6\x9do#\x05\xd1\x9a\xff\x98\xf4\xda\xa2\x90`n\xaf\xd4J\x05*\xb3\xe2\xd2zq\x9b\x8bw\x94\x92\x05\x04\x8aHh\xc4\xdd\xfbeo\x95\\\xed\x83\xa1\xb9<R\xb5E\xae\xe4\xbch\x16=\xe8\xe3 e\x14\x8d\x00\xf2\x8a,\xaa\xa9]\x06\xec\xb7\xf93kG\xb2+\xee\xfe\xf7{\x06&=ySrK\xbf\xbb\x92OD"\x9f\xc3\xeb\xb0\x93\r\x01[\xf8\x00-\xf73\x15Y\x9b_\x8c\xe74{\xa9\xd2/\xfaLb3\x13`\xc78X2\xde\x11A+\x97[\x1b@\xbfZ\xb3{KO\xa2)NHX\x1e\x84\x84I\xaa\xfa*\xcd(e\x84\xde>\xb3\x03\xb5b\x1c\xef2\xcf\xe2\x12xS7\x01/\xdf\xf4\x16\xf2[=\xf7\xde\x97\xaa4\x82\x8f]\xf9jD\xb9\xf7\x87pA\xaf\x9a\x98\xf2\xa6[\xdaGy\xc8\x85\xe0:E[TS\x16\xae\xa0|\xc6`\x91\xdb\'\x8e1\xad\xe7<\x0c\x8b\xdc\xc9S\x84\xc6\x88\x84>ck\xf6\xf1\xaa\xa0\x85\r6\x88\xf9\xea\xc47\xefa\x05(\x9d\xa4\xde4\xe7s\x84)s\xb2]\xa4\xe4\xd1\x81m|=\xad\xa8w\xcaM\x9b\xbc\xed\x1a\x91\x81\xa2vt\x07x\xa2\xecK\x8d\x1e\xa3|\xdf{\xab\x95a:\xc5iM`\xa6i\xfe\x08\xb6W}\xba\xb9\xed&\xac;\\\x9f\x06iB\xca\x11\x14x\xff\xa2\x9a\rt\xcf-C$\xeb\xd5\xf0\xa8\x1b\x86iF\xaa\x88p+\x03\xa9C\x04S$\xd5Utf\x1bk\x0e\xf8"Y\xfb\x94r\xa2-E\x95\tIx\xab\xc2\xe2D\x8b\xc9\xc2\xf6\x81\x99VT\\\xd1\x1bf\x19\xcd\xc5\xc9g\x00R\xaa\x1f+\x18Y\t\x9f\xfa\xd0\xbf\x1d~c\x82\xc2R\x84lQ\x0b\xde\xbf;\xe9\x1e\xd5\x91\xb1d/\x00\xfc\xaf\x1dJ\x89\xe1\xd9\x86\xf9\xee{<\xad\x90/\xfc\xda\x1f\x1e\xd6s\xe2\xc8\xe7\xfagV\x08~<\xf020I}\xf2O\xf7j\xa7B\xc1\xff[\x0b\xb9\xe2\x05\x00V\x18\xa0\x89%\xc1vD\xb4t\x04\xfa\xcf$\xcf\xf5.}\xc0\x9c\x1b\xec\x147\x89\\P\x87\x9f\xecq%9U\x08\x9a\xba\x93\xf6X\xea\x9bG89\x11\xe2\xe6#U\x0f\x93(\xd6!\x0eJ\xc2\x08\xa2\xe8,\x0f\xc9\xb5\n\xc5\xc7{\x86\x93\xa5(\xe6q~OS\xc9\xcf\x1b"\x0cS\xe4,c\xd5\xa1\xdf\xf8\xe1\xefU\xd9ag\x1dKGd\x0cqI\x8c\x7f\xa4\x8d\x05(\x96:\xd0|\xf4\xb4\xeb\x97\xf4\xbe\xba\rk\xd0V\xe3\xf7\xc9\x16R\xed\xe6\xa6I\x16\xa5\xec\xdb\xfa\xbbL3K\xbd\xdf\xa5\xc4,\xa7F,D8\xdf\xa0\xbcF\x12\xad\xfe5dy\x82\xc0yk=>\x9c\x88\x12\xc7[G\xc4B\xbb\xbd\x99\xed\xfd\x95<)-k%j\x9c$\xe6Q\xbdh\xc9[\x80\xe4Sx\xe1c\xe5\xcd\x113\x8ec\xdf\xbeoe\xc7D~\xfad\xfa\xb6\xfal\x9b\x8f\xf5\xaf\xab\x9cc\x80MU\xf6\x96\xa5\x0e~\x17\x11v\x157\xdb\xbe\xfek\xfc\xe1\xba\x03\xb17.\t\x93~\x06\x9f_bv\x00%wa\x04\x94\xf6(g\x137\x94X\xf9\xef\xf4"\x1cEij\xddBv\x83\xb7z\xe2\xe7)\x0b51X\xc6\xa4\xf4\xf4\x10f\xf3\xb5\x82\x8f\x8e"\xd4\x04\xf1\xdd;D\x85PH\xe8\xad\xbe\x92m_\xf8F\xe5K\x8f\xcf\xdd+g\xa9\x92\xabb_R\xdea\x9a\xeck\x93V}\xa9n[\xaa\xc2\x8c\x00\xf8G\xc7M\x88\x0c\xdb[\x8a+\xd8\xda\x8bD{y\xec\n\xe0\xd7\xb0k\x10B\xbc\xf4\x8eC\xf3\x87\x89;\x93\xb7_z<e\xea\xcd\xabK\x053z\xe9\x06\xd3\xf0e\xc9\xf0\xac\x8a7\x12\xc26\xc9\xd0\xf9\x0b\xf5\xcb\x0c\xd4\xca\x16\x16\x9e3\xee%\x8e\xca/\xef\xe1\x0fX\xbd\xbe\xf5\xe0\x11\x9fG\x8b\x00\xd9\xa3\x809&\x9d5p,\xf43g\x0ci\xca\xf7\xd9\xe4<\x8f\xcd\xd3!\xea\x89tW\xa3\x9f\xe0\xa3\xb8CO\x0b\xeb\x13\x05\xc9\x10\xbfnq\x91\x04-\xdd\xa7\ny\r\x1a\x08\xc0Et\xb5\x06 \x9bJJ;`\x02~?\xefPBzk1f\x1c \x80m\xba\x1a\x00\x80\xc5\xd7C\xf0h\x994\x9dU\x06/\x95M}\xbc<\xb6\xd0p>\x85\xdb\xc0&\xad@\xdfZ\xc1\xd8\xdf\x0e\x9e\xf9\x18\x91\xc2|\xefM\xf3\x89\xa4=:i\x7f\xa1\x97R\xad\xa6\xd4\xe3\xb7:c\xc3G\xff\x95\xb1w\x9b\xd5{\xee3a\xfcEP\xad@R\x0b\xe6\xcfv\x17j\xfe\xb6\xa7\xc2o\xaf!P\xd1\xb8{?/\x01=q\xbeb\xbcw-Yx\xb9\x8fd\x05.\xedk\x17H\xf6\xf7\x95]\t|^\xe8\x04nJ\x16\x94\xf4\xf0\xc3I\xc9\x80\xd955\xd0O,\xb4j6\xe86\xbeC\xae\xbd@\xc1\\C#\xf4\xb1\xc4|\x17\x02\x1c\xbe\xbc\x1e\xdc\xef\xfe\xe0\x07/<\x14\xed6\x1d\x90RF\xfd\xee.\x8c\xca\xca\xaf\xbbP\xb27\xb9\xd0\x03\x8f2\xca\xff\x1a\x0c\xef\xee\xb0s\x17+\x1d\xf3!\x92\x81n\xd5\x13\xf3\xa8\x8e+j\xc2x\xbe\xb6\x89\xd5>\x0f\xa8M2/\xb1\xf0\xda|\x03\x8bPnG\xaa\x95u\x13,\xeeH7\x0f\x80\xe3v\xe0\xc0\xd0\x83\x0c\xdas\xb0lK\xd8T\x93\xf3\x1a\xa9\xd6\x08\xbd\x99I\xaaj\xf7\xb1\xdaN\xb2,U\xf0\xe1^\x12[wG\xb1W\x05\x11\xdd\xe2\xf8T\xe5\xcb\x1f\xe9\x18\x1c\x17O\xe7\xc5\xb7g\xe4g\x8c\x17M\xfd\xce\xf8\x92\xbd\xcf\xb0;\\\xe46~\xf2.\xf8\xb5\x90\x92\x84\xd7\xbf\x8c\x90\xd9/P\xbe\xa8\x13L\xde\xdb5\xa3\xcf\xaa\xdd[oa\xd4\x85!\xddc\x19\xbf\x85\xa6\xd5\xa0\xefQ\xe2\xd5\x95\xba\x85\xb7WOV\xce\xe7\xcd39\xd4\xd0QT\x11\xaer\xa0\xef\xe7P\xd5f\xa6\xbb\xcb\xa8\xd8\xb2o(\xb1"\xf0t\xb5\x0b\x02\xaf\xabp\xe2\'\xf43\xcfr\xbb\xec\x1f<\x10\xea\xdb\r\x17\xff\x99\xe8\xeb\xc0\xb9S>C\x0cM\rK\xbb\x18t\x18N\x94eF\x81\xe5\'y\x83\xef\xba\x06\xc5\\\xc3hk\xcb\xd7\x10\x1b^P\xbe`,\xee\xb9\xb8Z\x84\x8d\xea\x07$kb_8\x0c\xeb\xde$U\xc0\x82\xbd\x03\x14@J\x8bP:}rn_\xf2)\xf1v&\x1c\x81 \xado\x85\x19\xe9eK\xac^\xbbB\xea\xb6\xd7\xb0\x9d\xb8oq\xeaP\x02e\xc5\x94|\x0e\x9e*\x06\x17\xd1\xd3CR\xd8\x8c]u$\xf1\x94](\x86=y\x86\xef\xfav!\xd7;C\xbf]\xb9+>q\xdd\x16\x17\x11/\x9f\x17>\xd6(I\xd5\x83J[!\x12\x80\xbf\x19\xf0\xd9\x11\xd0m\xf9H\x85d\xcet\x8e(0\xf2\x02\x8b?\x17\x1b\x9e\xce\xd1J\xa5]@Q\xa3!\xa0\x1d\xbd\xb8\xd5Y\xc9\x03c\x02"\x8cO\xddC\xde[\'(\x0e\xeb\xf6?\xb6~\xd7*\x89\x92\xad%\x0c\xc0k\xffF3\xa8\xb3M\xd5\x16X\xc0\x0b\xb0\x1e\x0fi\xb4\x11\x0b\tXl/\x99\x88\xb9na9\x9d\x8f\xfb\xa4x-u\xdc\xcca\xfbx\xde*b\xbdr\x82\xecF\x9e\x05\xe5QY\xa5T\xac\xafkXc\xdc)\xe6}\xcc\xf7\x94S\xa8\xf7\x84\x99B\x8b\xd3\xaf\xc8P\x93_\xb1^\xd4\xc80r\xd2\x06\x0bR_J9\xc2\xa0)\xe2\xa2\x86\xac\xf5\xc8\'\xff\xc43j\xc9A\xaa\xeelV\x9f\xe8@\x16v\xde\xbbV\xe1\xd9\x99\x94\xac\x9a\x16\x86\xcc\x1f\xc3,\x98\xf5\xe0s\xd1c\x9b\xd2?\x0b+\x91f>(\x96\xb8\x17\xfc8 \x87\xb5~\xfc\x14\xce\x04\xd7T\xbe~\x02\x85T\x17\x1f\xe9>\x8e\xd1Fi\x0f\x94\xd8]iO%=\xb0\xea\xa0V\xd3g\xa2R\x1a\xeazQ\xb6.z@$\xac\x844I\'B\x18\xb7l^w\xf9}\xcdj\xc9\xa6\xa7\xb6\x0b\xfeR\x97<\xe5M\x91\xe5\xb4\xad\xb8\xb6\xb5\xad\x98\xff\'\xcf\xbd3]\xa4C\x0b\x9bB\xa65L\xf7\x8a\r\x01J\xc6\xb8^**n\xdcs^g\xe9C?\x1b\xaeg`\xf9\x18f&\x0f\x86{\xc1\xc5\xf7\x02\xaf'
p14
tp15
bI624
I0
F7.0414221137944499e-09
tp16
."""

class TestData(unittest.TestCase):
   pass
   
class TestPlummer(TestData):
    def test1(self):
        state = pickle.loads(random_state)
        m =  MakePlummerModel(2, random_state = state)
        m1, p, v = m.new_model()
        self.assertEquals(m1[0,0], 0.5)
        self.assertEquals(m1[1,0], 0.5)
        self.assertAlmostEqual(p[0,0],  -0.0015779879, 5)
        self.assertAlmostEqual(p[1,0],  0.89936253, 5)
        self.assertAlmostEqual(p[0,1],  0.097179498979, 5)
        self.assertAlmostEqual(p[1,1],  -0.434732898, 5)
        