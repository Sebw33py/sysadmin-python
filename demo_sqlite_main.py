from datetime import datetime
from demo_sqlite.models import db, Professor, Course, Student, StudentToCourse

def db_call():
    pass

def main():
    # Connect to our database.
    db.connect()
    # Create the tables ... if needed
    db.create_tables([Professor, Student, Course, StudentToCourse])
    # Creating a Professor line.
    prof = Professor(
        first_name="Alexandre",
        last_name="Raspaud",
        creation_date=datetime.datetime.now()
    )
    prof_id = prof.save()
    # Creating a Course
    course = Course(
        name="Python3 SysAdmin",
        professor=prof_id,
        creation_date=datetime.now()
    )
    course_id = course.save()
    # Creating two Students
    student1 = Student(
        first_name="Patrick",
        last_name="Dupont",
        creation_date=datetime.now()
    )
    student1_id = student1.save()
    student2 = Student(
        first_name="Jean",
        last_name="Dupont",
        creation_date=datetime.now()
    )
    student2_id = student2.save()
    # Many-to-Many
    relation1 = StudentToCourse(
        student=student1_id,
        course=course_id
    )
    relation1.save()
    relation2 = StudentToCourse(
        student=student2_id,
        course=course_id
    )
    relation2.save()

    # Let's read our reccords !
    try:
        query = Professor.get_by_id(1)
        print(query.first_name, query.last_name)
        print(query.full_name)
    except DoesNotExist as ex:
        print(f"Professor with id {id} does not exist ! Quitting !")
        return

if __name__ == "__main__":
    main()