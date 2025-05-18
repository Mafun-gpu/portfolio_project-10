from django.urls import path
from . import views
from .converters import FourDigitYearConverter

app_name = 'portfolio'
urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('detail/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
    path('archive/<yyyy:year>/', views.archive_by_year, name='archive_by_year'),
    path('category/<slug:cat_slug>/', views.category_detail, name='category_detail'),
    path('tag/<slug:tag_slug>/', views.tag_detail, name='tag_detail'),
    path('create-non-model/', views.portfolio_create_non_model, name='portfolio_create_non_model'),
    path('create/', views.portfolio_create, name='portfolio_create'),
    path('upload/', views.upload_file, name='upload_file'),
]