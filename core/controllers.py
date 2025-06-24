from db.connection import Session
from core.models import Student, Course, Teacher

session = Session()

def create_student(name, email):
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()

def create_teacher(name, specialty):
    teacher = Teacher(name=name, specialty=specialty)
    session.add(teacher)
    session.commit()

def create_course(name, description, teacher_id):
    course = Course(name=name, description=description, teacher_id=teacher_id)
    session.add(course)
    session.commit()

def get_students():
    return session.query(Student).all()

def get_courses():
    return session.query(Course).all()

def get_teachers():
    return session.query(Teacher).all()

def update_student(student_id, name=None, email=None):
    student = session.get(Student, student_id)
    if student:
        if name: student.name = name
        if email: student.email = email
        session.commit()

def update_teacher(teacher_id, name=None, specialty=None):
    teacher = session.get(Teacher, teacher_id)
    if teacher:
        if name: teacher.name = name
        if specialty: teacher.specialty = specialty
        session.commit()

def update_course(course_id, name=None, description=None, teacher_id=None):
    course = session.get(Course, course_id)
    if course:
        if name: course.name = name
        if description: course.description = description
        if teacher_id: course.teacher_id = teacher_id
        session.commit()

def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()

def delete_teacher(teacher_id):
    teacher = session.get(Teacher, teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()

def delete_course(course_id):
    course = session.get(Course, course_id)
    if course:
        session.delete(course)
        session.commit()

def enroll_student_in_course(student_id, course_id):
    student = session.get(Student, student_id)
    course = session.get(Course, course_id)
    if student and course:
        if course not in student.courses:
            student.courses.append(course)
            session.commit()
            print(f"Estudiante {student.name} inscrito en el curso {course.name}.")
        else:
            print("El estudiante ya está inscrito en este curso.")
    else:
        print("Estudiante o curso no encontrado.")

def list_student_courses(student_id):
    student = session.get(Student, student_id)
    if student:
        print(f"Cursos de {student.name}:")
        for course in student.courses:
            print(f"- {course.name}")
    else:
        print("Estudiante no encontrado.")

def list_course_students(course_id):
    course = session.get(Course, course_id)
    if course:
        print(f"Estudiantes inscritos en {course.name}:")
        for student in course.students:
            print(f"- {student.name}")
    else:
        print("Curso no encontrado.")
