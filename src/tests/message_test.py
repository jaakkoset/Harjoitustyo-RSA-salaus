import unittest
from src.message import Message


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.msg = Message()

    def test_text_to_integer(self):
        examples = [
            {"text": "abcxyzåäö", "answer": 397398399120121122229228246},
            {"text": "AÖ", "answer": 365214},
            {"text": '19.!"()', "answer": 349357346333334340341},
        ]
        for e in examples:
            x = self.msg.text_to_integer(e["text"])
            self.assertEqual(x, e["answer"])
