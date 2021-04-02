import unittest
from dictionary.app import InteractiveDictionary

class appTests(unittest.TestCase):

    def test_translate_with_proper_word(self):
        app = InteractiveDictionary()
        word = "rain"
        expected = ['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in drops of water.']
        data = app.translate(word)
        self.assertEqual(expected, data)

    def test_translate_with_random_word(self):
        app = InteractiveDictionary()
        word = "aaabbsadfdsd"
        expected = "The word doesn't exist. Please double check it."
        data = app.translate(word)
        self.assertEqual(expected, data)

if __name__ == '__main__':
    unittest.main()

    