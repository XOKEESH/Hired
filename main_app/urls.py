from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('applications/', views.app_index, name='app-index'),     
    path('applications/<int:app_id>/', views.app_detail, name='app-detail'),
    path('applications/create/', views.AppCreate.as_view(), name='app-create'),
    path('applications/<int:pk>/update/', views.AppUpdate.as_view(), name='app-update'),
    path('applications/<int:pk>/delete/', views.AppDelete.as_view(), name='app-delete'),
    path('accounts/signup/', views.signup, name='signup'),

]
