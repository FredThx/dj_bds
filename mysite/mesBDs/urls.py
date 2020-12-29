from django.urls import path

from . import views

app_name = 'mesBDs'
urlpatterns = [
    path('', views.SerieListView.as_view(), name='serie-list'),
    path('serie/<int:pk>/', views.SerieDetailView.as_view(), name='serie-detail'),
    path('livre/<int:pk>/', views.LivreDetailView.as_view(), name='livre-detail'),
]
