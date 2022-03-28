import unittest
import typewise_alert
import unittest.mock
import io

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
  
  def test_classify_tempreture_breach_as_per_type_and_tempInC(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',50),'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',-10),'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',20),'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',50),'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',-10),'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',40),'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING',50),'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING',-10),'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING',30),'NORMAL')

  # @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  # def test_check_and_alert(self, mock_stdout):
  #   typewise_alert.check_and_alert('TO_CONTROLLER',{'coolingType':'PASSIVE_COOLING'},50)
    
  #   self.assertFalse(True,'65261, TOO_HIGH')
    


if __name__ == '__main__':
  unittest.main()