from django.urls import path


from . import views

urlpatterns = [
    path('', views.index),
    path('trends/', views.trends),
    path('reports/', views.reports),
    path('projects/', views.projects),
    path('projects/projects_list/', views.projects_list),
    path('trends/trends_list/', views.trends_list),
    path('reports/reports_list/', views.reports_list),
    path('trends/<str:post_id>/', views.trends_content),
    path('reports/<str:post_id>/', views.reports_content),
    path('projects/<str:post_id>/', views.projects_content),
]
