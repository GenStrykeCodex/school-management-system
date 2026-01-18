class Student:

    def __init__(self, student_id, name, student_class, roll_no, marks):

        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.roll_no = roll_no
        self.marks = marks

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self):
        return self.total_marks() / len(self.marks)

    # convert object to dictionary for JSON storage
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "class": self.student_class,
            "roll_no": self.roll_no,
            "marks": self.marks
        }
