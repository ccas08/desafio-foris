import sys 
from datetime import datetime



class Student:
    def __init__(self, name):
        self.name = name
        self.presences=[]
        self.attended_days  = set()
        
    def add_presence(self, presence):
        self.presences.append(presence)
        self.attended_days .add(presence.day)
        
    def total_minutes(self):
        return sum(p.duration() for p in self.presences)

    def total_days(self):
        return len(self.attended_days)
     
class Presence:
    def __init__(self,day,time_start,time_end,room):
        self.day = int(day)
        self.time_start = datetime.strptime(time_start, "%H:%M")
        self.time_end = datetime.strptime(time_end,"%H:%M")
        self.room = room
        
    def duration(self):
        duration = (self.time_end - self.time_start).total_seconds() / 60
        return duration if duration >= 5 else 0
    
class AttendanceTracker:
    def __init__(self):
        self.students={}
    
    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
    
    def add_presences(self, name, day, time_start, time_end, room):
        if name in self.students:
            presence= Presence(day, time_start, time_end, room)
            self.students[name].add_presence(presence)
                          
    def generate_report(self):
        report = []
        for student in self.students.values():
            total_minutes = student.total_minutes()
            total_days = student.total_days()
            report.append((student.name, total_minutes, total_days))
        
        report.sort(key=lambda x: (-x[1], x[0]))
        return report

    def process_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if parts[0] == "Student":
                    self.add_student(parts[1])
                elif parts[0] == "Presence":
                    self.add_presence(parts[1], parts[2], parts[3], parts[4], parts[5])

    def print_report(self):
        report = self.generate_report()
        for name, minutes, days in report:
            print(f"{name}: {minutes} minutes in {days} days")

if __name__ == "__main__":
    tracker = AttendanceTracker()
    if len(sys.argv) > 1:
        tracker.process_file(sys.argv[1])
        tracker.print_report()
    else:
        print("Usage: python attendance_tracker.py <input_file>")                             