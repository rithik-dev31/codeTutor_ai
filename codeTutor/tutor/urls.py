from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/analyze/', views.analyze_code, name='analyze_code'),
    path('api/analyze/mock/', views.analyze_code_mock, name='analyze_mock'),
    path('api/corrected-code/', views.get_corrected_code, name='corrected_code'),
    # New endpoints for enhanced features
    path('api/get_hint/', views.get_hint, name='get_hint'),

    path('api/correction-strategy/', views.get_correction_strategy, name='correction_strategy'),
]