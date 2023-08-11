import unittest
import sys
sys.path.append("E:\\PY\\HW tests") #Your path to module
from popular_names import calculate_popularity, get_top_n_popular_names, mentors

class TestPopularNames(unittest.TestCase):

    def test_popular_list(self):
        popular = calculate_popularity(mentors)
        expected_names = ['Александр', 'Евгений', 'Максим']
        actual_names = [name for name, _ in popular[:3]]
        self.assertEqual(actual_names, expected_names)

    def test_top_3(self):
        expected_top_3 = [
            ['Александр', 10],
            ['Евгений', 5],
            ['Максим', 4]
        ]
        top_3 = get_top_n_popular_names(mentors)
        self.assertEqual(top_3, expected_top_3)

if __name__ == '__main__':
    unittest.main()

