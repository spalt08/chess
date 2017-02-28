import unittest
import subprocess

class ChessTests(unittest.TestCase):
# 	
#     def _test_main(self):
#         subprocess.run(['python', 'app.py'])
#         with open('output.txt', 'r') as f:
#             output = f.read()
#             output = output.replace('\n', '')
#         with open('expected_output.txt', 'r') as f:
#             expected_output = f.read()
#             expected_output = expected_output.replace('\n', '')
#         self.assertEqual(output, expected_output)

    def test_main_all(self):
	    
        for i in range(1, 4):
            with self.subTest(i = i):
            
                input_file = 'TestCases/' + str(i) + '_input.txt'
                output_file = 'output.txt'
                expected_output_file = 'TestCases/' + str(i) + '_output.txt'
                
                subprocess.run(['python', 'app.py', '-i', input_file, '-o', output_file])
                
                with open(output_file, 'r') as f:
                    output = f.read()
                    
                with open(expected_output_file, 'r') as f:
                    expected_output = f.read()
                    
                self.assertEqual(output, expected_output)


if __name__ == '__main__':
	unittest.main()