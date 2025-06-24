def show_menu():
    print("\n--- CRUD Aplicación Escolar ---")
    print("1. Crear estudiante")
    print("2. Ver estudiantes")
    print("3. Editar estudiante")
    print("4. Eliminar estudiante")
    print("5. Crear profesor")
    print("6. Ver profesores")
    print("7. Editar profesor")
    print("8. Eliminar profesor")
    print("9. Crear curso")
    print("10. Ver cursos")
    print("11. Editar curso")
    print("12. Eliminar curso")
    print("13. Inscribir estudiante en curso")
    print("14. Ver cursos de un estudiante")
    print("15. Ver estudiantes de un curso")
    print("16. Salir")

def get_student_data():
    name = input("Nombre: ")
    email = input("Email: ")
    return name, email

def get_student_id():
    return int(input("ID del estudiante: "))

def get_teacher_data():
    name = input("Nombre del profesor: ")
    specialty = input("Especialidad: ")
    return name, specialty

def get_teacher_id():
    return int(input("ID del profesor: "))

def get_course_data():
    name = input("Nombre del curso: ")
    description = input("Descripción: ")
    teacher_id = int(input("ID del profesor a cargo: "))
    return name, description, teacher_id

def get_course_id():
    return int(input("ID del curso: "))

def get_student_and_course_ids():
    student_id = int(input("ID del estudiante: "))
    course_id = int(input("ID del curso: "))
    return student_id, course_id

def get_id(prompt):
    return int(input(f"{prompt} ID: "))
