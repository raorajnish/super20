from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enquiry/', views.enquiry_form, name='enquiry_form'),
    path('admission/', views.admission_form, name='admission_form'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enquiries/', views.enquiry_list, name='enquiry_list'),
    path('enquiry/<int:id>/edit/', views.edit_enquiry, name='edit_enquiry'),
    path('export-enquiries/', views.export_enquiries, name='export_enquiries'),
    path('admissions/', views.admission_list, name='admission_list'),
    path('admission/<int:id>/', views.admission_detail, name='admission_detail'),
    path('export-admissions/', views.export_admissions, name='export_admissions'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),

    # Faculty auth and dashboard
    path('faculty/login/', views.faculty_login, name='faculty_login'),
    path('faculty/logout/', views.faculty_logout, name='faculty_logout'),
    path('faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('faculty/<int:faculty_id>/', views.faculty_profile, name='faculty_profile'),

    # Lecture schedule and attendance
    path('lectures/', views.lecture_list, name='lecture_list'),
    path('lectures/create/', views.lecture_create, name='lecture_create'),
    path('lectures/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
    path('lectures/<int:lecture_id>/edit/', views.lecture_edit, name='lecture_edit'),
    path('lectures/<int:lecture_id>/delete/', views.lecture_delete, name='lecture_delete'),
    path('lectures/<int:lecture_id>/attendance/', views.lecture_attendance, name='lecture_attendance'),
] 