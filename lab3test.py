import unittest
import lab3

class Lab3Test(unittest.TestCase):
	def setUp(self):
		pass
	def test_shout(self):
		self.assertEqual("ABC!", lab3.shout("abc"))
		self.assertEqual("CAT!", lab3.shout("cat?"))
		self.assertEqual("DOG!", lab3.shout("dog!"))
		
	def test_reverseletters(self):
		self.assertEqual("cba", lab3.reverse("abc"))
		self.assertEqual("!olleh", lab3.reverse("hello!"))
		
	def test_reversewords(self):
		self.assertEqual(".world hello", lab3.reversewords("hello world."))
		self.assertEqual("! punctuation this move let's So,", lab3.reversewords("So, let's move this punctuation!"))
		self.assertEqual("? you are How .world Hello", lab3.reversewords("Hello world. How are you?"))
	
	def test_reversewordssentences(self):
		self.assertEqual("olleh dlrow.", lab3.reversewordletters("hello world."))


if __name__ == '__main__':
	unittest.main()