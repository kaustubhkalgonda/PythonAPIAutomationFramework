class Payments:
    paymentMethod = None
    amount = None
    courseName = None
    date = None
    studentName = None
    payments = []

    def total_payments(self):
        total = 0
        for payment in self.payments:
            total += payment["amount"]
        return total

    def add_payment(self, amount, date, paymentMethod, courseName, studentName):
        self.payments.append(
            {"amount": amount, "date": date, "payment method": paymentMethod, "course name": courseName,
             "student name": studentName})

    def display_payments(self):
        for payment in self.payments:
            print(
                f"Amount: {payment['amount']}, Date: {payment['date']}, Payment Method: {payment['payment method']}, "
                f"Course Name: {payment['course name']}, Student Name: {payment['student name']}")


payment1 = Payments()
payment1.add_payment(9999, "02/19/2024", "Google Pay",
                     "PythonATB2x", "Kaustubh Kalgonda")
payments2 = Payments()
payment1.add_payment(9999, "02/19/2024", "Cash",
                     "PythonATB2x", "Yuvaan Kalgonda")
payment1.display_payments()
print(payment1.total_payments())
