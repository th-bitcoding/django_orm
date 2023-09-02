from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.create_members,name='members'),
    path('api/',views.CsvData.as_view(),name='CsvData'),
]