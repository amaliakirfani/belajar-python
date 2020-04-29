from django.shortcuts import render, HttpResponse, redirect
from . models import StudentModel, LecturerModel, CoursesModel, GradeModel
from django.contrib import messages

# show student
def show_students(request):
    if request.method == 'POST':
        nim = request.POST['nim']
        nama = request.POST['nama']

        students = StudentModel(student_nim=nim, student_name=nama)
        students.save()
        return redirect('/assessment/students/')

    students = StudentModel.objects.all()

    context = {
        'title' : 'Dashboard | Students',
        'student' : students
    }
    return render(request, 'students.html', context)

# show lecturer
def show_lecturer(request):
    if request.method == 'POST':
        nidn = request.POST['nidn']
        nama = request.POST['nama']

        lecturer = LecturerModel(lecturer_nidn=nidn, lecturer_name=nama)
        lecturer.save()
        return redirect('/assessment/lecturer/')

    lecturer = LecturerModel.objects.all()

    context = {
        'title' : 'Dashboard | Lecturer',
        'lecturer' : lecturer
    }
    return render(request, 'lecturer.html', context)
    return HttpResponse('Hello, World!')

# show courses
def show_courses(request):
    if request.method == 'POST':
        code = request.POST['code']
        nama = request.POST['nama']

        courses = CoursesModel(courses_code=code, courses_name=nama)
        courses.save()
        return redirect('/assessment/courses/')

    courses = CoursesModel.objects.all()

    context = {
        'title' : 'Dashboard | Courses',
        'courses' : courses
    }
    return render(request, 'courses.html', context)
    return HttpResponse('This is Courses')

# show grade
def show_grade(request):
    if request.method == 'POST':
        no = request.POST['no']
        nim = request.POST['nim']
        nama_mahasiswa = request.POST['nama_mahasiswa']
        nama_dosen = request.POST['nama_dosen']
        mata_kuliah = request.POST['mata_kuliah']
        nilai = request.POST['nilai']

        grade = GradeModel(grade_code=code, grade_name=nama)
        grade.save()
        return redirect('/assessment/grade/')

    grade = GradeModel.objects.all()

    context = {
        'title' : 'Dashboard | Grade',
        'grade' : grade
    }
    return render(request, 'grade.html', context)
    return HttpResponse('This is Grade')

# edit student
def edit_data(request, id):
    #students=StudentModel.objects.get(id=id)
    students = StudentModel.objects.filter(student_nim=id).first()

    if request.method == 'POST':
        nim = request.POST['nim']
        nama = request.POST['nama']

        students.student_nim=nim
        students.student_name=nama
        students.save()

        return redirect('/assessment/students/')

    context = {
        'students' : students,
        'title' : 'Edit Data'
    }

    return render(request, 'student_edit.html', context)

# edit lecturer
def edit_data(request, id):
    #lecturer=LecturerModel.objects.get(id=id)
    lecturer = LecturerModel.objects.filter(id=id).first()

    if request.method == 'POST':
        nidn = request.POST['nidn']
        nama = request.POST['nama']

        lecturer.lecturer_nidn=nidn
        lecturer.lecturer_name=nama
        lecturer.save()

        return redirect('/assessment/lecturer/')

    context = {
        'lecturer' : lecturer,
        'title' : 'Edit Data'
    }

    return render(request, 'lecturer_edit.html', context)

# edit courses
def edit_data(request, id):
    #courses=CoursesModel.objects.get(id=id)
    courses = CoursesModel.objects.filter(id=id).first()

    if request.method == 'POST':
        code = request.POST['code']
        nama = request.POST['nama']

        courses.courses_code=code
        courses.courses_name=nama
        courses.save()

        return redirect('/assessment/courses/')

    context = {
        'courses' : courses,
        'title' : 'Edit Data'
    }

    return render(request, 'courses_edit.html', context)

# edit grade
def edit_data(request, id):
    #grade=GradeModel.objects.get(id=id)
    grade = GradeModel.objects.filter(id=id).first()

    if request.method == 'POST':
        no = request.POST['no']
        nim = request.POST['nim']
        nama_mahasiswa = request.POST['nama_mahasiswa']
        nama_dosen = request.POST['nama_dosen']
        mata_kuliah = request.POST['mata_kuliah']
        nilai = request.POST['nilai']

        grade.grade_code=code
        grade.grade_name=nama
        grade.save()

        return redirect('/assessment/grade/')

    context = {
        'grade' : grade,
        'title' : 'Edit Data'
    }

    return render(request, 'grade_edit.html', context)

 # delete student   
def delete_student(request, id):
    student = StudentModel.objects.get(pk=id)
    if student.delete():
       messages.success(request, 'Berhasil Delete Data')
       return redirect('/assessment/students/')
    return HttpResponse("ID Tidak Ditemukan")

def delete_data(request, id):
    students=StudentModel.objects.get(id=id)
    students = StudentModel.objects.filter(student_nim=id).first()

    if request.method == 'POST':
        nim = request.POST['nim']
        nama = request.POST['nama']

        students.student_nim=nim
        students.student_name=nama
        students.save()

        return redirect('/assessment/students/')

    context = {
        'students' : students,
        'title' : 'Delete Data'
    }

    return render(request, 'student_delete.html', context)

# delete lecturer
def delete_lecturer(request, id):
    lecturer = LecturerModel.objects.get(pk=id)
    if lecturer.delete():
       messages.success(request, 'Berhasil Delete Data Lecturer')
       return redirect('/assessment/lecturer/')
    return HttpResponse("ID Tidak Ditemukan")

def delete_data(request, id):
    lecturer=LecturerModel.objects.get(id=id)
    lecturer = LecturerModel.objects.filter(lecturer_nidn=id).first()

    if request.method == 'POST':
        nidn = request.POST['nidn']
        nama = request.POST['nama']

        lecturer.lecturer_nidn=nidn
        lecturer.lecturer_name=nama
        lecturer.save()

        return redirect('/assessment/lecturer/')

    context = {
        'lecturer' : lecturer,
        'title' : 'Delete Data'
    }

    return render(request, 'lecturer_delete.html', context)

# delete courses
def delete_courses(request, id):
    courses = CoursesModel.objects.get(pk=id)
    if courses.delete():
       messages.success(request, 'Berhasil Delete Data Courses')
       return redirect('/assessment/courses/')
    return HttpResponse("ID Tidak Ditemukan")

def delete_data(request, id):
    courses=CoursesModel.objects.get(id=id)
    courses = CoursesModel.objects.filter(courses_code=id).first()

    if request.method == 'POST':
        code = request.POST['code']
        nama = request.POST['nama']

        courses.courses_code=code
        courses.courses_name=nama
        courses.save()

        return redirect('/assessment/courses/')

    context = {
        'courses' : courses,
        'title' : 'Delete Data'
    }

    return render(request, 'courses_delete.html', context)

# delete grade
def delete_grade(request, id):
    grade = GradeModel.objects.get(pk=id)
    if grade.delete():
       messages.success(request, 'Berhasil Delete Data Grade')
       return redirect('/assessment/grade/')
    return HttpResponse("ID Tidak Ditemukan")

def delete_data(request, id):
    grade=GradeModel.objects.get(id=id)
    grade = GradeModel.objects.filter(grade_no=id).first()

    if request.method == 'POST':
        no = request.POST['no']
        nim = request.POST['nim']
        nama_mahasiswa = request.POST['nama_mahasiswa']
        nama_dosen = request.POST['nama_dosen']
        mata_kuliah = request.POST['mata_kuliah']
        nilai = request.POST['nilai']

        grade.grade_code=code
        grade.grade_name=nama
        grade.save()

        return redirect('/assessment/grade/')

    context = {
        'grade' : grade,
        'title' : 'Delete Data'
    }

    return render(request, 'grade_delete.html', context)