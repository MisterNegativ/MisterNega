from django.urls import path
from . import views
from .views import SchoolView, CustomUserView, DirectorView, view_syllabuses, add_instructor

urlpatterns = [
    path('', views.home, name="home"),
    path('create_syllabus', views.create_syllabus, name="create_syllabus"),
    path('literature_form/<int:syllabus_id>', views.add_literature, name="literature_form"),
    path('literature/delete/<int:pk>/<int:syllabus_id>', views.delete_literature, name='delete_literature'),
    path('module/delete/<int:pk>/<int:syllabus_id>', views.delete_module, name='delete_module'),
    path('next_step/<int:syllabus_id>', views.next_step, name="next_step"),
    path('add_module/<int:syllabus_id>', views.add_module, name="add_module"),
    path('half/<int:syllabus_id>', views.half, name="half"),
    path('add_policy/<int:syllabus_id>', views.add_policy, name="add_policy"),
    path('login/', views.login_v, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('my_syllabuses/', views.my_syllabuses, name='my_syllabuses'),
    path('delete_syllabus/<int:syllabus_id>', views.delete_syllabus, name="delete_syllabus"),
    path('syllabus_details/<int:syllabus_id>/', views.syllabus_details, name='syllabus_details'),
    path('continue_edit/<int:syllabus_id>', views.continue_edit, name="continue_edit"),
  # path('generate_syllabus/', views.generate_syllabus, name='generate_syllabus'),
    path('schools/', SchoolView.as_view(), name='school_list'),
    path('schools/add/', SchoolView.as_view(), name='add_school'),
    path('users/', CustomUserView.as_view(), name='user_list'),
    path('users/add/', CustomUserView.as_view(), name='add_user'),
    path('directors/', DirectorView.as_view(), name='director_list'),
    path('directors/add/', DirectorView.as_view(), name='add_director'),
    path('mysyllabuses/', view_syllabuses, name='view_syllabuses'),
    path('add_instructor/', add_instructor, name='add_instructor'),
    path('download_syllabus/word_rus/<int:syllabus_id>/', views.download_syllabus_as_word_rus, name='download_syllabus_word_rus'),
    path('download_syllabus/word_kz/<int:syllabus_id>/', views.download_syllabus_as_word_kz, name='download_syllabus_word_kz'),
    path('download_syllabus/pdf_rus/<int:syllabus_id>/', views.download_syllabus_as_pdf_rus, name='download_syllabus_pdf_rus'),
]