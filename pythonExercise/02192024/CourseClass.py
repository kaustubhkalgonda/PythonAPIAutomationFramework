class Course:
    name = None
    duration = None
    fees = None
    studentsEnrolled = None
    mode = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_fees(self):
        return self.fees

    def set_fees(self, fees):
        self.fees = fees

    def get_studentsenrolled(self):
        return self.studentsEnrolled

    def set_studentsenrolled(self, studentsEnrolled):
        self.studentsEnrolled = studentsEnrolled

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode

    def display_info(self):
        print(
            f"Name: {self.name}\nDuration: {self.duration}\nFees: {self.fees}\n"
            f"Students Enrolled: {self.studentsEnrolled}\nMode: {self.mode}\n")


course1 = Course()
course1.set_name("PythonATB2x")
course1.set_fees("9999 Rs")
course1.set_duration("3 Months")
course1.set_studentsenrolled("Kaustubh, John, Pramod")
course1.set_mode("Online")

course1.display_info()
