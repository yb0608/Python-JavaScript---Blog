from django.urls import path
from .views import IndexView,ProjectDetailView,ShareProjectView, EditProjectView,DeleteProjectView,AddCategoryView,CommentView
from . import views

urlpatterns = [
    path ('', views.HomeView, name="home"),
    path ('manifesto', views.ManifestoView, name="manifesto"),
    path ('index', IndexView.as_view(), name = "index" ),
    path ('project/<int:pk>', ProjectDetailView.as_view(), name = 'detail'),
    path ('share', ShareProjectView.as_view(), name='share'),
    path ('shared_projects', views.SharedProjectView, name="allshared"),
    path ('newcategory',AddCategoryView.as_view(), name='new_category'),
    path ('project/edit/<int:pk>', EditProjectView.as_view(), name='edit'),
    path ('project/delete/<int:pk>', DeleteProjectView.as_view(), name='delete'),
    path ('category/<str:category>', views.CategoryView, name= 'category'),
    path ("project/like/<int:project_id>", views.Like, name="like"),
    path ('project/<int:pk>/comment', CommentView.as_view(), name='comment'),
    ]