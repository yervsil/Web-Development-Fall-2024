
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_instructor': True})

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('completed', 'Completed')], default='active')

class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=now)

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, choices=[('success', 'Success'), ('failed', 'Failed')], default='success')

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    total_marks = models.PositiveIntegerField()

class QuizQuestion(models.Model):
    question_id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

class UserProgress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_lessons = models.PositiveIntegerField(default=0)
    quiz_scores = models.JSONField(default=dict)