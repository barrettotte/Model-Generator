import unittest, utils, generator, warnings

class Test_General(unittest.TestCase):
    
    def setUp(self):
        print("  Running test: " + str(self._testMethodName))
        self.config = {
            'schemaDirectory': 'C:\\'
        }

    def test_validate_config(self):
        generator.validate_config(self.config)
        
        self.config['schemaDirectory'] = 'F:\\somewhere'
        with self.assertRaises(Exception) as context:
            generator.validate_config(self.config)
        self.assertEqual(type(context), unittest.case._AssertRaisesContext)
        


if __name__ == "__main__": unittest.main()
