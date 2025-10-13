from django.contrib import admin
from .models import Enquiry, Admission, Faculty, Lecture, AttendanceRecord, Payment

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'guardian_name', 'phone_number', 'get_preferred_course_display', 'enquiry_date', 'status']
    list_filter = ['status', 'preferred_course', 'enquiry_date', 'followup_date']
    search_fields = ['student_name', 'guardian_name', 'phone_number']
    list_editable = ['status']
    date_hierarchy = 'enquiry_date'
    ordering = ['-enquiry_date']
    
    def get_preferred_course_display(self, obj):
        return obj.get_preferred_course_display()
    get_preferred_course_display.short_description = 'Preferred Course'
    
    fieldsets = (
        ('Student Information', {
            'fields': ('student_name', 'guardian_name', 'phone_number', 'preferred_course')
        }),
        ('Enquiry Details', {
            'fields': ('enquiry_date', 'status', 'followup_date', 'notes')
        }),
    )
    
    readonly_fields = ['enquiry_date']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'standard', 'batch', 'mobile_1', 'school_college', 'submitted_at']
    list_filter = ['standard', 'stream', 'submitted_at', 'date_of_birth']
    search_fields = ['surname', 'name', 'middlename', 'mobile_1', 'mobile_2', 'school_college']
    list_editable = ['batch']
    date_hierarchy = 'submitted_at'
    ordering = ['-submitted_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('surname', 'name', 'middlename', 'photo', 'date_of_birth')
        }),
        ('Contact Information', {
            'fields': ('contact_number', 'mobile_1', 'mobile_2')
        }),
        ('Family Information', {
            'fields': ('mother_name', 'father_name', 'father_occupation')
        }),
        ('Academic Information', {
            'fields': ('standard', 'batch', 'school_college', 'previous_percentage', 'stream')
        }),
        ('System Information', {
            'fields': ('submitted_at',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['submitted_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True

# Customize admin site
admin.site.site_header = "Super20 Academy Administration"
admin.site.site_title = "Super20 Academy Admin"
admin.site.index_title = "Welcome to Super20 Academy Management System"


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'user', 'phone_number', 'is_active']
    list_filter = ['is_active']
    search_fields = ['full_name', 'user__username', 'phone_number']


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'start_time', 'end_time', 'standard', 'batch', 'faculty']
    list_filter = ['date', 'standard', 'batch', 'faculty']
    search_fields = ['title', 'description', 'batch', 'faculty__full_name']
    autocomplete_fields = ['faculty']


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'lecture', 'student', 'status', 'marked_by', 'marked_at']
    list_filter = ['status', 'lecture__date', 'lecture__standard', 'lecture__batch']
    search_fields = ['student__surname', 'student__name', 'lecture__title']
    autocomplete_fields = ['lecture']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'faculty', 'month', 'per_lecture_rate', 'amount_paid', 'due', 'pending']
    list_filter = ['month', 'faculty']
    search_fields = ['faculty__full_name', 'faculty__user__username']
    autocomplete_fields = ['faculty']
    list_editable = ['per_lecture_rate']

    def due(self, obj):
        return obj.amount_due

    def pending(self, obj):
        return obj.balance
