import unittest
import contraption
import pyvisa
class TestContraptionGeneral(unittest.TestCase):
    def test_init(self):
        self.assertTrue(True)

class TestLecroyWavepro(unittest.TestCase):
    def test_connect(self):
        IP="192.168.1.12"
        lecroy=contraption.LecroyScope(IP)
        lecroy.arm_trigger(1,.0)
        lecroy.set_timeout(60000)
        lecroy.create_dir('william_data')
        #print(lecroy.query("DIR? DISK,HDD,CREATE"))
        lecroy.save_waveform_local()

if __name__=='__main__':
    unittest.main()

