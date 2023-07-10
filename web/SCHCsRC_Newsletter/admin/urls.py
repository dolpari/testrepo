from django.urls import path
import newsletter.views


from . import views

urlpatterns = [
    path('', views.login),
    path('index/', newsletter.views.index),
    path('trends/', newsletter.views.trends),
    path('trends/trends_list/', newsletter.views.trends_list),
    path('trends/post/', views.trends_post),
    path('reports/', newsletter.views.reports),
    path('projects/', newsletter.views.projects),
    path('projects/projects_list/', newsletter.views.projects_list),
    path('projects/post/', views.projects_post),
    path('reports/reports_list/', newsletter.views.reports_list),
    path('reports/post/', views.reports_post),
    path('logout/', views.logout),
    path('trends/<str:post_id>/', newsletter.views.trends_content),
    path('reports/<str:post_id>/', newsletter.views.reports_content),
    path('projects/<str:post_id>/', newsletter.views.projects_content),
    path('trends/<str:post_id>/modify_post/', views.trends_modify),
    path('reports/<str:post_id>/modify_post/', views.reports_modify),
    path('projects/<str:post_id>/modify_post/', views.projects_modify),
    path('trends/<str:post_id>/delete_post/', views.trends_delete),
    path('reports/<str:post_id>/delete_post/', views.reports_delete),
    path('projects/<str:post_id>/delete_post/', views.projects_delete),
]
