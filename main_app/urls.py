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
    path('applications/<int:app_id>/add-interview/', views.add_interview, name='add-interview'),
    path('applications/<int:app_id>/add-feedback/', views.add_feedback, name='add-feedback'),
    path('applications/<int:app_id>/add-followUp/', views.add_followUp, name='add-followUp'),
    path('applications/<int:app_id>/add-task/', views.add_task, name='add-task'),
    path('applications/<int:app_id>/add-offer/', views.add_offer, name='add-offer'),
    path('applications/<int:app_id>/add-contact/', views.add_contact, name='add-contact'),
    path('applications/<int:app_id>/add-note/', views.add_note, name='add-note'),
    path('accounts/signup/', views.signup, name='signup'),
]
