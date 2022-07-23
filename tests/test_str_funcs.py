import unittest

# classes
from snippets.str_funcs import str_funcs


class TestStringMethods(unittest.TestCase):
    def test_url_sanitize(self):
        test = str_funcs()
        url_tests = {
            "Hood: Outlaws & Legends": "Hood-Outlaws-Legends",
            "This is a (test), or is it?": "This-is-a-test-or-is-it",
            "Blade & Sorcery": "Blade-Sorcery",
        }
        for string, ans in url_tests.items():
            result = test.url_sanitize(string)
            self.assertEqual(result, ans)

    def test_word_and_list(self):
        test = str_funcs()
        list_tests = [
            (["Test1"], "Test1"),
            (["Test1", "Test2"], "Test1 and Test2"),
            (["Test1", "Test2", "Test3"], "Test1, Test2 and Test3"),
        ]
        for list, ans in list_tests:
            result = test.word_and_list(list)
            self.assertEqual(result, ans)


if __name__ == "__main__":
    unittest.main()
