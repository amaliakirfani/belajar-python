from django.db import models

# Create your models here.
class StudentModel(models.Model):
    student_nim = models.CharField(max_length=30, unique=True)
    student_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "students_table"

class LecturerModel(models.Model):
    lecturer_nidn = models.CharField(max_length=30, unique=True)
    lecturer_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "lecturer_table"

class CoursesModel(models.Model):
    courses_code = models.CharField(max_length=30, unique=True)
    courses_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "courses_table"

class GradeModel(models.Model):
    grade_code = models.CharField(max_length=30, unique=True)
    grade_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "grade_table"

class StudentsGradeModel(models.Model):
    student_nim = models.ForeignKey(StudentModel, to_field='student_nim', on_delete=models.CASCADE)
    lecturer_nidn = models.ForeignKey(LecturerModel, to_field='lecturer_nidn', on_delete=models.CASCADE)
    courses_code = models.ForeignKey(CoursesModel, to_field='courses_code', on_delete=models.CASCADE)
    student_grade = models.FloatField(null=True)

    class Meta:
        db_table = 'student_grade'