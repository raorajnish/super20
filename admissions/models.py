from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal
from datetime import date

# Create your models here.

class Enquiry(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    COURSE_CHOICES = [
        ('jr_kg', 'Jr. KG'),
        ('sr_kg', 'Sr. KG'),
        ('1', '1st Standard'),
        ('2', '2nd Standard'),
        ('3', '3rd Standard'),
        ('4', '4th Standard'),
        ('5', '5th Standard'),
        ('6', '6th Standard'),
        ('7', '7th Standard'),
        ('8', '8th Standard'),
        ('9', '9th Standard'),
        ('10', '10th Standard'),
        ('11_science', '11th Standard - Science'),
        ('11_commerce', '11th Standard - Commerce'),
        ('11_arts', '11th Standard - Arts'),
        ('12_science', '12th Standard - Science'),
        ('12_commerce', '12th Standard - Commerce'),
        ('12_arts', '12th Standard - Arts'),
    ]
    preferred_course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    
    enquiry_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    followup_date = models.DateField(blank=True, null=True)

    STATUS_CHOICES = [
        ('in_process', 'In Process'),
        ('converted', 'Converted'),
        ('not_interested', 'Not Interested'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_process')

    def __str__(self):
        return self.student_name

class Admission(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    contact_number = models.CharField(max_length=15)
    mobile_1 = models.CharField(max_length=15)
    mobile_2 = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)

    STANDARD_CHOICES = [
        ('jr_kg', 'Jr. KG'),
        ('sr_kg', 'Sr. KG'),
        ('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'),
        ('6', '6th'), ('7', '7th'), ('8', '8th'), ('9', '9th'), ('10', '10th'),
        ('11', '11th'), ('12', '12th'),
    ]
    standard = models.CharField(max_length=10, choices=STANDARD_CHOICES)

    batch = models.CharField(max_length=100)  # Define dropdown from views if required
    school_college = models.CharField(max_length=200)
    previous_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    stream = models.CharField(
        max_length=20,
        choices=[('science', 'Science'), ('commerce', 'Commerce'), ('arts', 'Arts')],
        blank=True,
        null=True,
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return f"{self.surname} {self.name} {self.middlename or ''}"

    def __str__(self):
        return self.full_name()


class Faculty(models.Model):
    """Faculty profile linked to Django auth User for login."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile')
    full_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class Lecture(models.Model):
    """Scheduled lecture assigned to a faculty and targeting a class/batch."""
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    standard = models.CharField(max_length=10, choices=Admission.STANDARD_CHOICES)
    batch = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='lectures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.title} - {self.get_standard_display()} ({self.batch}) on {self.date}"

    def get_target_students_queryset(self):
        return Admission.objects.filter(standard=self.standard, batch=self.batch).order_by('surname', 'name')


class AttendanceRecord(models.Model):
    """Per-student attendance record for a lecture."""
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )

    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='attendance_records')
    student = models.ForeignKey(Admission, on_delete=models.CASCADE, related_name='attendance_records')
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='present')
    marked_by = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='marked_attendance')
    marked_at = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('lecture', 'student')
        indexes = [
            models.Index(fields=['lecture', 'student']),
        ]

    def __str__(self):
        return f"{self.student.full_name()} - {self.lecture.title} - {self.status}"


class Payment(models.Model):
    """Monthly payment tracking for a faculty, including per-lecture rate and paid amount.

    The number of lectures for the month is derived from the `Lecture` model
    for the given `faculty` and `month` range.
    """
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='payments')
    # Use the first day of the month to represent the month (e.g., 2025-10-01)
    month = models.DateField(help_text="First day of month, e.g., 2025-10-01")
    per_lecture_rate = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('faculty', 'month')
        ordering = ['-month']

    def __str__(self):
        ym = self.month.strftime('%Y-%m')
        return f"{self.faculty.full_name} - {ym}"

    @staticmethod
    def month_start_for(d: date) -> date:
        return date(d.year, d.month, 1)

    @property
    def lectures_count(self) -> int:
        month_start = date(self.month.year, self.month.month, 1)
        if self.month.month == 12:
            next_month = date(self.month.year + 1, 1, 1)
        else:
            next_month = date(self.month.year, self.month.month + 1, 1)
        return self.faculty.lectures.filter(date__gte=month_start, date__lt=next_month).count()

    @property
    def amount_due(self) -> Decimal:
        return (self.per_lecture_rate or Decimal('0.00')) * Decimal(self.lectures_count)

    @property
    def balance(self) -> Decimal:
        return self.amount_due - (self.amount_paid or Decimal('0.00'))
