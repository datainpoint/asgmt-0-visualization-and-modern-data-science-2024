import unittest
import importlib

class TestAssignmentZero(unittest.TestCase):
    def test_01_return_course_begin_and_end_dates(self):
        self.assertEqual(asgmt.return_course_begin_and_end_dates()[0], "2024-02-23")
        self.assertEqual(asgmt.return_course_begin_and_end_dates()[1], "2024-06-07")
    def test_02_how_to_register_this_course(self):
        self.assertEqual(asgmt.how_to_register_this_course(), "https://forms.gle/6vYUERwoq6HTpLcBA")
    def test_03_does_class_attendance_matter(self):
        self.assertFalse(asgmt.does_class_attendance_matter())
    def test_04_return_the_toolbox_of_this_course(self):
        self.assertEqual(asgmt.return_the_toolbox_of_this_course(), {'Tableau', 'SQL', 'Python'})
    def test_05_return_the_grading_schema(self):
        self.assertEqual(asgmt.return_the_grading_schema()["assignment_one"], 0.1)
        self.assertEqual(asgmt.return_the_grading_schema()["assignment_two"], 0.1)
        self.assertEqual(asgmt.return_the_grading_schema()["assignment_three"], 0.1)
        self.assertEqual(asgmt.return_the_grading_schema()["assignment_four"], 0.1)
        self.assertEqual(asgmt.return_the_grading_schema()["assignment_five"], 0.1)
        self.assertEqual(asgmt.return_the_grading_schema()["assignment_six"], 0.1)
        self.assertEqual(asgmt.return_the_grading_schema()["midterm"], 0.2)
        self.assertEqual(asgmt.return_the_grading_schema()["final"], 0.2)

asgmt = importlib.import_module("asgmt-zero")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentZero)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions. You will receive {number_of_successes} points in Assignment Zero.")