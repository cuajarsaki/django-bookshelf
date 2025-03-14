English | [日本語](./docs/Readme-ja.md) 

<p align="left">
  <img src="https://img.shields.io/badge/-python-darkblue.svg?logo=python&style=flat">
  <img src="https://img.shields.io/badge/-django-092E20.svg?logo=django&style=flat">
  <img src="https://img.shields.io/badge/-html-grey.svg?logo=html5&style=flat">
  <img src="https://img.shields.io/badge/-css-302683.svg?logo=css&style=flat">
</p>

# Django Bookshelf

This repository contains the final project for the **Programming Language II Python** beginner course. 

The project is a **book management system** built using **Django**, designed to be used in a laboratory or study environment.

## 📌 Features
- Built with **Django 3.2.16**
- Uses **django-bootstrap5** for styling
- Includes an **admin panel** for managing categories
- No database initialization required (uses SQLite)
- Simple installation with `pip install -r requirements.txt`
- Run locally using `python manage.py runserver`

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/cuajarsaki/django-bookshelf.git
   cd django-bookshelf]
   ```
   
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   
3. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
   
4. **Access the application:**
- Open `http://127.0.0.1:8000/` to view the book management system.
- To access the admin panel, go to `http://127.0.0.1:8000/admin`
- Admin credentials:
- Username: `admin`
- Password: `test_1234`

## 🖥️ Project Screenshots

![image](https://github.com/user-attachments/assets/b360fa92-186f-4767-a6e4-33bef77ae4dd)

## 🛠️ Project Structure
```mermaid
flowchart TD
    subgraph Client
        Browser[Web Browser]
    end

    subgraph URLs["URLs (book/urls.py)"]
        RootURL["/ (book_list)"]
        CreateURL["/create/ (create)"]
        UpdateURL["/update/:pk/ (book_update)"]
        DeleteURL["/delete/:pk/ (book_delete)"]
        DetailURL["/detail/:pk/ (book_detail)"]
    end

    subgraph Views["Views (book/views.py)"]
        ListV[BookListView]
        CreateV[BookCreateView]
        UpdateV[BookUpdateView]
        DeleteV[BookDeleteView]
        DetailV[BookDetailView]
    end

    subgraph Forms["Forms (book/forms.py)"]
        F1[BookForm]
        F2[BookForm2]
    end

    subgraph Models["Models (book/models.py)"]
        BookM[Book]
        CategoryM[Category]
    end

    subgraph Templates
        BaseT[base.html]
        ListT[book_list.html]
        FormT[book_form.html]
        Form2T[book_form2.html]
        DeleteT[book_confirm_delete.html]
        DetailT[book_detail.html]
    end

    subgraph Database
        DB[(SQLite DB)]
    end

    Browser -->|HTTP Request| URLs
    
    RootURL --> ListV
    CreateURL --> CreateV
    UpdateURL --> UpdateV
    DeleteURL --> DeleteV
    DetailURL --> DetailV
    
    ListV --> ListT
    CreateV --> FormT
    UpdateV --> Form2T
    DeleteV --> DeleteT
    DetailV --> DetailT
    
    CreateV -->|Uses| F1
    UpdateV -->|Uses| F2
    
    F1 -->|Validates| BookM
    F2 -->|Validates| BookM
    
    BookM -->|ForeignKey| CategoryM
    
    ListT -->|Extends| BaseT
    FormT -->|Extends| BaseT
    Form2T -->|Extends| BaseT
    DeleteT -->|Extends| BaseT
    DetailT -->|Extends| BaseT
    
    BookM <-->|CRUD| DB
    CategoryM <-->|CRUD| DB
    
    ListV -->|queryset| BookM
```

## ⚠️ Database Management
- The project uses SQLite as the default database.
- If you want to reset the database, delete the db.sqlite3 file from the project directory.

## 🏗️ Technology Stack
- Django 3.2.16
- django-bootstrap-form
- django-bootstrap5
- dj-static
- python-decouple

## 🤔Considerations
I chose Django over Bottle for this project because:
1. Django offers a wide range of built-in features for web applications
2. Strong security measures
3. High scalability
4. Easier maintenance after graduation
5. Good documentation and community support

Additionally, the category management feature is available through the admin panel for convenient editing.

## 🏫 About
- Course: Programming Language II (Python)
- Year: 2023
