import unittest
from translator import english_to_french , french_to_english

class  TestEnglishToFrench(unittest.TestCase):
    """Test English to French"""
    def testEnglishToFrench(self):
        """Test English to French"""
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    """Test French"""

    def testEnglishToFrench(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()      