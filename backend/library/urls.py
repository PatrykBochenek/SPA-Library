from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReaderViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'readers', ReaderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
