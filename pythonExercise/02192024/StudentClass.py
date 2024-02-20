class Student:
    name = None
    age = None
    gender = None
    address = None
    courseEnrolled = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_courseenrolled(self):
        return self.courseEnrolled

    def set_courseenrolled(self, courseEnrolled):
        self.courseEnrolled = courseEnrolled

    def display_info(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
            f"Address: {self.address}, Course Enrolled: {self.courseEnrolled}")


# Example usage:
student1 = Student()
student1.set_name("John")
student1.set_age("25")
student1.set_gender("Male")
student1.set_address("Sunnyvale, CA")
student1.set_courseenrolled("PythonATB2x")
student1.display_info()

