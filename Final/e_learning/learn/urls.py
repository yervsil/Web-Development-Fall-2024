from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . import viewSets


router = DefaultRouter()
router.register(r'users', viewSets.UserViewSet)
router.register(r'categories', viewSets.CategoryViewSet)
router.register(r'courses', viewSets.CourseViewSet)
router.register(r'enrollments', viewSets.EnrollmentViewSet)
router.register(r'lessons', viewSets.LessonViewSet)
router.register(r'reviews', viewSets.ReviewViewSet)
router.register(r'payments', viewSets.PaymentViewSet)
router.register(r'quizzes', viewSets.QuizViewSet)
router.register(r'quiz-questions', viewSets.QuizQuestionViewSet)
router.register(r'user-progress', viewSets.UserProgressViewSet)

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:course_id>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('api/', include(router.urls))
]