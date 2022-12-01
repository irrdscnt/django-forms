from django.urls import path
from . import views

app_name='cinema'

urlpatterns = [
    path('', views.series_all, name = 'series_all' ),
    path('series_detail/<int:id>/', views.find_by_id, name='series_detail'),
    path('add/', views.AddSeries.as_view(), name='add'),
    path('delete/<int:pk>', views.SerieDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.SerieUpdateView.as_view(), name="update"),
    ]
