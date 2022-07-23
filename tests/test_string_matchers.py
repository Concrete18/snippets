import unittest
import datetime as dt

# classes
from snippets.string_matchers import sim_matcher


class TestStringMethods(unittest.TestCase):
    def test_lev_distance(self):
        test = sim_matcher()
        string_tests = [
            # insert
            {"word1": "test", "word2": "tests", "ans": 1},
            # delete
            {"word1": "bolt", "word2": "bot", "ans": 1},
            # replace
            {"word1": "spell", "word2": "spelt", "ans": 1},
            # insert, delete and replace
            {"word1": "Thinking", "word2": "Thoughts", "ans": 6},
        ]
        for a in string_tests:
            result = test.lev_distance(a["word1"], a["word2"])
            self.assertEqual(result, a["ans"])

    def test_sim_matcher(self):
        test = sim_matcher()
        test_list = [
            "This is a test, yay",
            "this is not it, arg",
            "Find the batman!",
            "Shadow Tactics: Blades of the Shogun - Aiko's Choice",
            "The Last of Us",
            "Elden Ring",
            "The Last of Us Part I",
            "The Last of Us Part II",
            "Waltz of the Wizard: Natural Magic",
            "Life is Strange™",
            "The Witcher 3: Wild Hunt",
            "Marvel's Spider-Man: Miles Morales",
            "Crypt Of The Necrodancer: Nintendo Switch Edition",
        ]
        string_tests = {
            "This is a test": "This is a test, yay",
            "find th bamtan": "Find the batman!",
            "Eldn Rings": "Elden Ring",
            "Shadow Tactics Blades of the Shougn Aikos Choce": "Shadow Tactics: Blades of the Shogun - Aiko's Choice",
            "the last of us": "The Last of Us",
            "Walk of the Wizard: Natural Magik": "Waltz of the Wizard: Natural Magic",
            "The last of us Part I": "The Last of Us Part I",
            "Life is Strange 1": "Life is Strange™",
            "Witcher 3: The Wild Hunt": "The Witcher 3: Wild Hunt",
            "Spider-Man: Miles Morales": "Marvel's Spider-Man: Miles Morales",
            "grave Of The deaddancer: Switch Edition": "Crypt Of The Necrodancer: Nintendo Switch Edition",
        }
        for string, answer in string_tests.items():
            result = test.lev_dist_matcher(string, test_list, debug=True)[0]
            self.assertEqual(result, answer)
            # self.assertEqual(tester.sim_matcher(string, test_list, debug=True), answer)
