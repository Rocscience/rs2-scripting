import unittest
import types
import os
import sys
import subprocess

class TestExampleFiles(unittest.TestCase):
	pathToPythonExecutable = None

	@unittest.skipIf(not pathToPythonExecutable, "Requires path to the python executable to use to run the example files. ex: python or C:\env\Scripts\python.exe")  
	def test_run_example_files(self):
		example_files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'example_code')
		for filename in os.listdir(example_files_dir):

			# Skip directories (for __pycache__)
			filePath = os.path.join(example_files_dir, filename)
			if os.path.isdir(filePath):
				continue

			if not filePath.endswith('.py'):
				continue

			print(f"Running: {filename}...")
			subprocess.run([self.pathToPythonExecutable, filePath], check=True)
			print("Finished:" + filename)
