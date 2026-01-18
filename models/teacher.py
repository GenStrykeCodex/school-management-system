class Teacher:
    
    def __init__(self, teacher_id, name, subject, salary):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.salary = salary

    def to_dict(self):
        return {
            "teacher_id": self.teacher_id,
            "name": self.name,
            "subject": self.subject,
            "salary": self.salary
        }
