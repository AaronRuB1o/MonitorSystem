from django.urls import path
from . import views
urlpatterns = [
    #path('', views.your_view, name='your_view')
    path('', views.monitoring, name='monitoring'),
    path('CompanyTree/', views.companyTree, name='companyTree'),
    path('search/', views.search_data, name='search_data')
]