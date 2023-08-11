import unittest
import sys
sys.path.append("E:\\PY\\HW tests") #Your path to module
import mentor_names
from popular_names import unique_names, popular, top_3

class TestMentorNames(unittest.TestCase):
    def test_unique_mentor_names(self):
        result = mentor_names.get_unique_mentor_names(mentor_names.mentors) 
        expected = "Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()  
    
