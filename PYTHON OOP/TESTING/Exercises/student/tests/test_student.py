from student.project.student import Student
import unittest


class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student('Miroslav', None)
        if self.student.courses is None:
            self.student.courses = {}
            # {course_name: [notes]}

    def test_init_method(self):
        self.assertEqual(self.student.name, 'Miroslav')
        self.assertEqual(self.student.courses, {})

    def test_if_students_courses_dict_is_not_none(self):
        self.student = Student('Miroslav', {'Python Advanced': ['first_part - passed', 'OOP part - to be taken exam']})
        self.assertEqual(self.student.courses, {'Python Advanced': ['first_part - passed', 'OOP part - to be taken exam']})

    def test_enroll_adds_the_course_name_in_the_courses_dict(self):
        self.assertEqual(self.student.enroll('Python Basic', 'passed', "N"),
                         "Course has been added.")
        self.assertEqual(self.student.courses, {'Python Basic': []})

        # TODO add test for -> if [course_name] NOT in the courses dict and [add_course_notes] is NOT [""] or ["Y"]
        # -->> CREATE AN EMPTY DICT self.courses[course_name] = [] and return "Course has been added."
    def test_enroll_adds_the_course_name_and_the_notes_to_the_courses_dict(self):
        self.assertEqual(self.student.enroll('Python Fundamentals', ['passed'], "Y"),
                         "Course and course notes have been added.")

    def test_enroll_adds_the_course_name_in_the_courses_dict_with_course_notes_blank(self):
        self.assertEqual(self.student.enroll('Python Fundamentals', ['passed'], ""),
                         "Course and course notes have been added.")

    def test_enroll_if_course_name_already_in_the_courses_dict_and_adds_the_new_notes(self):
        self.student.enroll('Python Fundamentals', ['passed'], "Y")
        self.assertEqual(self.student.enroll('Python Fundamentals', ['passed wih 6.00', 'more to be learned']),
                         "Course already added. Notes have been updated.")

    def test_enroll_if_course_name_already_in_the_courses_dict_and_adds_the_new_notes_with_blank_course_notes(self):
        self.student.enroll('Python Fundamentals', ['passed'], "")
        self.assertEqual(self.student.enroll('Python Fundamentals', ['passed wih 6.00', 'more to be learned']),
                         "Course already added. Notes have been updated.")

    def test_add_notes_if_course_name_not_in_the_courses_dict_raises_exception(self):
        self.student.enroll('Python Basic', ['passed'], )
        with self.assertRaises(Exception):
            self.student.add_notes('Python', ['to be passed soon'])

    def test_add_notes_if_the_course_name_in_the_courses_dict_and_add_the_notes(self):
        self.student.enroll('Python Fundamentals', ['passed'], "Y")
        self.assertEqual(self.student.add_notes('Python Fundamentals', ['not passed yet', 'new lectures ahead']),
                         "Notes have been updated")

    def test_add_notes_if_the_course_name_in_the_courses_dict_and_add_the_new_notes(self):
        self.student.enroll('Python Fundamentals', ['passed'], "")
        self.assertEqual(self.student.add_notes('Python Fundamentals', ['not passed yet', 'new lectures ahead']),
                         "Notes have been updated")

    def test_leave_course_successfully_removed_from_the_courses_dict(self):
        self.student.enroll('Python Fundamentals', ['passed'], "Y")
        self.assertEqual(self.student.leave_course('Python Fundamentals'), "Course has been removed")

    def test_leave_course_if_the_course_not_found_in_the_dict(self):
        self.student.enroll('Python Fundamentals', ['passed'], "Y")
        with self.assertRaises(Exception):
            self.student.leave_course('Python')


if __name__ == "__main__":
    unittest.main()

