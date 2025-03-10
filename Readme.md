# Django Bookshelf

This is a book management system built with Django, designed for laboratory use.

## About
This project was developed as a final assignment for the Programming Language II Python course.(2023/06/22)

## Features
- Book listing, adding, editing, and deletion functionality
- Category management through the admin interface
- User authentication and access control
- Responsive design using Bootstrap

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup
1. Clone this repository:
```
git clone https://github.com/yourusername/django-book-management-system.git
cd django-book-management-system
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the server:
```
python manage.py runserver
```

4. Access the application at:
```
http://127.0.0.1:8000/
```

### Admin Access
The admin interface is available at:
```
http://127.0.0.1:8000/admin
```

Default credentials:
- Username: admin
- Password: test_1234

## Technology Stack
- Django 3.2.16
- django-bootstrap-form
- django-bootstrap5
- dj-static
- python-decouple

## Considerations
I chose Django over Bottle for this project because:
1. Django offers a wide range of built-in features for web applications
2. Strong security measures
3. High scalability
4. Easier maintenance after graduation
5. Good documentation and community support

The category management feature is accessible through the admin page for easy editing.