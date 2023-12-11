
from . import views
from django.urls import path, include

urlpatterns = [
    path('product/', views.ProductAPIView.as_view(), name='product')
]