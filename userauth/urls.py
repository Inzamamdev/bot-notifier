from django.urls import path
from .views import login_view, logout_view, home_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', register_view, name='register'),
    path('home/', home_view, name='home'),
]