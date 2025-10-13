from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_faculty_lecture_attendancerecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(help_text='First day of month, e.g., 2025-10-01')),
                ('per_lecture_rate', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('faculty', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='payments', to='admissions.faculty')),
            ],
            options={
                'ordering': ['-month'],
                'unique_together': {('faculty', 'month')},
            },
        ),
    ]


