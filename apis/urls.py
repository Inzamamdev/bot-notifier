from django.urls import path
from .views import PublicView, ProtectedView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]