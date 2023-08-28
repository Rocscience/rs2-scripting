import unittest
import types
import os
from importlib.machinery import SourceFileLoader

class TestExampleFiles(unittest.TestCase):
	def test_run_example_files(self):
		example_files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'example_code')
		for filename in os.listdir(example_files_dir):
			fullname = filename[:-3]
			try:
				loader = SourceFileLoader(fullname, os.path.join(example_files_dir, filename))
				pythonModuleToTest = types.ModuleType(loader.name)
				loader.exec_module(pythonModuleToTest)
				
			except Exception as e:
				self.fail(f"Failed to run {filename}: {e}")
