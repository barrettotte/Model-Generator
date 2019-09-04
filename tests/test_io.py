import unittest, generator, os

# IO Unit inspired testing

class Test_IO(unittest.TestCase):
    
    def setUp(self):
        print("  Running test: " + str(self._testMethodName))
        generator.main() # generate actual values
        self.expected_dir = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'expected'
        self.actual_dir = self.expected_dir.split(os.sep + 'tests' + os.sep)[0] + os.sep + 'generated'

    def test_main(self):
        for subdir, _, files in os.walk(self.expected_dir):
            for file in files:
                print("     Comparing " + subdir + os.sep + file)
                fp = (subdir + os.sep + file).split(os.sep + 'expected' + os.sep)[-1]
                with open((self.expected_dir + os.sep + fp), 'r') as f: expected = f.read()
                with open((self.actual_dir + os.sep + fp), 'r')   as f: actual = f.read()
                self.assertEqual(expected, actual)

if __name__ == "__main__": unittest.main()
