# Super20 Academy Management System

A comprehensive Django-based web application for managing student enquiries and admissions for Super20 Academy.

## 🎯 Project Overview

The Super20 Academy Management System is designed to streamline the process of handling student enquiries and admissions. It provides a clean, modern interface for both public users (to submit enquiries and applications) and administrators (to manage and track all data).

## ✨ Features

### Public Features
- **Home Page**: Hero section with academy information, courses, testimonials
- **Enquiry Form**: Simple form for potential students to submit enquiries
- **Admission Form**: Comprehensive form for confirmed admissions with photo upload
- **About Us**: Detailed information about the academy
- **Contact**: Contact information and contact form

### Admin Features
- **Dashboard**: Overview with statistics and recent activities
- **Enquiry Management**: View, search, filter, and update enquiry status
- **Admission Management**: View, search, filter, and manage student admissions
- **Student Profiles**: Detailed view of individual student information
- **Admin Interface**: Full Django admin integration

### Technical Features
- **Responsive Design**: Mobile-friendly Bootstrap 5 interface
- **Form Validation**: Client and server-side validation
- **Image Upload**: Student photo upload with preview
- **Search & Filter**: Advanced search and filtering capabilities
- **Pagination**: Efficient data pagination
- **Security**: Authentication and authorization
- **Modern UI**: Clean, professional design with animations

## 🛠️ Technology Stack

- **Backend**: Django 5.1
- **Frontend**: Bootstrap 5, Font Awesome
- **Database**: SQLite (default), supports PostgreSQL/MySQL
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Image Processing**: Pillow
- **Additional**: Django Widget Tweaks

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Super20
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

### 8. Access the Application
- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
Super20/
├── manage.py
├── requirements.txt
├── README.md
├── super20/                 # Main project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── admissions/             # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── migrations/
├── templates/              # HTML templates
│   └── admissions/
│       ├── base.html
│       ├── home.html
│       ├── enquiry_form.html
│       ├── admission_form.html
│       ├── admin_dashboard.html
│       ├── enquiry_list.html
│       ├── admission_list.html
│       ├── admission_detail.html
│       ├── edit_enquiry.html
│       ├── admin_login.html
│       ├── about_us.html
│       └── contact.html
├── static/                 # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── media/                  # User uploaded files
    └── photos/
```

## 🗄️ Database Models

### Enquiry Model
- Student name, guardian name, phone number
- Preferred course, enquiry date
- Status tracking (In Process, Converted, Not Interested)
- Notes and follow-up date

### Admission Model
- Complete student information (personal, contact, academic)
- Photo upload capability
- Standard and stream selection
- Previous academic details

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Database Configuration
The default configuration uses SQLite. For production, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'super20_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🎨 Customization

### Styling
- Modify `static/css/style.css` for custom styles
- Update Bootstrap theme colors in CSS variables
- Add custom animations and effects

### Templates
- All templates are in `templates/admissions/`
- Base template: `base.html`
- Extend base template for new pages

### Forms
- Form classes in `admissions/forms.py`
- Custom validation and widgets
- Crispy Forms integration

## 🔒 Security Features

- CSRF protection enabled
- Form validation (client and server-side)
- Authentication required for admin areas
- Secure file upload handling
- SQL injection protection

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🚀 Deployment

### Production Setup
1. Set `DEBUG = False` in settings
2. Configure production database
3. Set up static file serving
4. Configure media file storage
5. Set up web server (Nginx/Apache)
6. Use WSGI server (Gunicorn/uWSGI)

### Docker Deployment
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic
EXPOSE 8000
CMD ["gunicorn", "super20.wsgi:application"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Email: support@super20academy.com
- Documentation: [Project Wiki]
- Issues: [GitHub Issues]

## 🔄 Version History

- **v1.0.0** - Initial release with basic functionality
- **v1.1.0** - Added advanced search and filtering
- **v1.2.0** - Enhanced UI/UX and responsive design

## 📊 System Requirements

- **Python**: 3.8+
- **Django**: 5.1+
- **Database**: SQLite/PostgreSQL/MySQL
- **Web Server**: Any WSGI-compatible server
- **Browser**: Modern browsers with JavaScript enabled

## 🎯 Roadmap

- [ ] Email notifications
- [ ] SMS integration
- [ ] Advanced analytics dashboard
- [ ] Mobile app
- [ ] API endpoints
- [ ] Multi-language support
- [ ] Payment integration
- [ ] Student portal

---

**Developed with ❤️ for Super20 Academy** 