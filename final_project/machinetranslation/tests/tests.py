import unittest

from translator import frenchToEnglish, englishToFrench

class Testf2e(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def test2(self):
        self.assertNotEqual(frenchToEnglish('None'),'')
    def test3(self):
        self.assertNotEqual(frenchToEnglish(0),0)

class Teste2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test2(self):
        self.assertNotEqual(englishToFrench('None'),'')
    def test3(self):
        self.assertNotEqual(englishToFrench(0),0)

unittest.main()