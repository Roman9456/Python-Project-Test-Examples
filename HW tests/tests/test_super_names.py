import unittest
import sys
from io import StringIO
sys.path.append("E:\\PY\\HW tests")#Your path to module
from super_names import mentors_names, get_course_mentors  
exec(open("super_names.py", encoding="utf-8").read())

class TestCourseMentors(unittest.TestCase):

    def test_course_mentors(self):
        expected_output = [
            "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим",
            "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман",
            "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений",
            "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим",
            "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений",
            "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар"
        ]

        captured_output = list(get_course_mentors())

        self.assertEqual(captured_output, expected_output)

if __name__ == '__main__':
    unittest.main()


