from core import controllers, views
from db.connection import Base, engine

Base.metadata.create_all(engine)

while True:
    views.show_menu()
    choice = input("Seleccione una opción: ")

    if choice == '1':
        name, email = views.get_student_data()
        controllers.create_student(name, email)
        print("Estudiante creado.")
    elif choice == '2':
        students = controllers.get_students()
        for s in students:
            print(f"ID: {s.id} | Nombre: {s.name} | Email: {s.email}")
    elif choice == '3':
        student_id = views.get_student_id()
        name, email = views.get_student_data()
        controllers.update_student(student_id, name, email)
        print("Estudiante actualizado.")
    elif choice == '4':
        student_id = views.get_student_id()
        controllers.delete_student(student_id)
        print("Estudiante eliminado.")
    elif choice == '5':
        name, specialty = views.get_teacher_data()
        controllers.create_teacher(name, specialty)
        print("Profesor creado.")
    elif choice == '6':
        teachers = controllers.get_teachers()
        for t in teachers:
            print(f"ID: {t.id} | Nombre: {t.name} | Especialidad: {t.specialty}")
    elif choice == '7':
        teacher_id = views.get_teacher_id()
        name, specialty = views.get_teacher_data()
        controllers.update_teacher(teacher_id, name, specialty)
        print("Profesor actualizado.")
    elif choice == '8':
        teacher_id = views.get_teacher_id()
        controllers.delete_teacher(teacher_id)
        print("Profesor eliminado.")
    elif choice == '9':
        name, description, teacher_id = views.get_course_data()
        controllers.create_course(name, description, teacher_id)
        print("Curso creado.")
    elif choice == '10':
        courses = controllers.get_courses()
        for c in courses:
            print(f"ID: {c.id} | Nombre: {c.name} | Descripción: {c.description} | Profesor ID: {c.teacher_id}")
    elif choice == '11':
        course_id = views.get_course_id()
        name, description, teacher_id = views.get_course_data()
        controllers.update_course(course_id, name, description, teacher_id)
        print("Curso actualizado.")
    elif choice == '12':
        course_id = views.get_course_id()
        controllers.delete_course(course_id)
        print("Curso eliminado.")
    elif choice == '13':
        student_id, course_id = views.get_student_and_course_ids()
        controllers.enroll_student_in_course(student_id, course_id)
    elif choice == '14':
        student_id = views.get_id("Estudiante")
        controllers.list_student_courses(student_id)
    elif choice == '15':
        course_id = views.get_id("Curso")
        controllers.list_course_students(course_id)
    elif choice == '16':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")
