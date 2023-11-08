from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase(TestCase):
    def test_example_one(self):
        self.assertEqual(solution(["arp", "live", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]), ["arp", "live", "strong"])
    def test_example_two(self):
        self.assertEqual(solution(["tarp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"]), [])
    def test_empty(self):
        self.assertEqual(solution([],[]), [])
    def test_more(self):
        self.assertEqual(solution(["cod", "code", "wars", "ewar"],["lively", "alive", "harp", "sharp", "armstrong", "codewars"]), ["cod", "code", "ewar", "wars"])
    def test_no_dups(self):
        self.assertEqual(solution(["duplicates", "duplicates"],["duplicates", "duplicates"] ),["duplicates"] )
    def test_symbols(self):
        self.assertEqual(solution(["&()", "code", "1346", "1028", "ar"],["12&()95", "coderange", "46", "1066", "par"]),["&()", "ar", "code"])