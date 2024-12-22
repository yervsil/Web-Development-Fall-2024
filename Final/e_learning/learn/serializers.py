from . import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollment
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = '__all__'

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizQuestion
        fields = '__all__'

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProgress
        fields = '__all__'