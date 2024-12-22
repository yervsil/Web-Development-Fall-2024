from . import models
from rest_framework import viewsets
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, permissions.IsAuthorOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer

class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = models.QuizQuestion.objects.all()
    serializer_class = serializers.QuizQuestionSerializer

class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = models.UserProgress.objects.all()
    serializer_class = serializers.UserProgressSerializer