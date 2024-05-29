import unittest

from asignacion_clases import AttendanceTracker

class TestAttendanceTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = AttendanceTracker()
        self.tracker.add_student("Marco")
        self.tracker.add_student("David")
        self.tracker.add_student("Fran")
        self.tracker.add_presences("Marco", 1, "09:02", "10:17", "R100")
        self.tracker.add_presences("Marco", 3, "10:58", "12:05", "R205")
        self.tracker.add_presences("David", 5, "14:02", "15:46", "F505")

    def test_report(self):
        expected_report = [
            ("Marco", 142, 2),
            ("David", 104, 1),
            ("Fran", 0, 0)
        ]
        report = self.tracker.generate_report()
        self.assertEqual(report, expected_report)

        
        print("Generated Report:")
        for student, minutes, days in report:
            print(f"{student}: {minutes} minutes in {days} days")

    def test_add_student(self):
        self.tracker.add_student("Pablo")
        self.assertIn("Pablo", self.tracker.students)

    def test_add_presence(self):
        self.tracker.add_student("Pablo")
        self.tracker.add_presences("Pablo", 2, "09:00", "10:00", "A101")
        student = self.tracker.students["Pablo"]
        self.assertEqual(student.total_minutes(), 60)
        self.assertIn(2, student.attended_days)

    
if __name__ == "__main__":
    unittest.main()
