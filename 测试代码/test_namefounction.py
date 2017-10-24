'''import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
	"""测试name_founction.py"""

	def test_first_last_name(self):
		"""能够正确地处理像janis joplin这样的姓名吗？"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
unittest.main()'''
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_firstlastname(self):
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()