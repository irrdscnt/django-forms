from django.urls import path
from . import views

app_name = 'parser'

urlpatterns = [
    path('parser_laptops/', views.ParserFormView.as_view(), name='parse_func'),
    path('parser_laptops_view/', views.ParserView.as_view(), name='parse_view'),
]