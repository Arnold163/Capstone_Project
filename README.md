Library Management System API

Overview
This project implements a comprehensive Library Management System API using Django and Django REST Framework. 
It provides functionalities for managing books, users, and transactions related to borrowing and returning books. 
The system is designed with RESTful principles and includes robust authentication mechanisms.

Setup Instructions
1. Clone the repository.
2. Set up a virtual environment:
   ```bash
   python -m venv env
   ```   
 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
 Apply migrations:
   ```bash
   python manage.py migrate
   ```
Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
Start the server:
   ```bash
   python manage.py runserver
   ```
Features
Core Features
 1. User Management (CRUD)
- Create, update, view, and delete user accounts.
- Manage user roles (admin and regular users).
- Implemented using Django’s authentication system.
- Users can log in and view their borrowing history.

2. Book Management (CRUD)
- Add, update, view, and delete books.
- Track book availability by the number of copies.
- Filter books by availability, title, author, or ISBN.

3. Borrowing and Returning Books
- Check-out books:
  - Ensure only one copy can be borrowed per user.
  - Reduce the number of available copies when a book is checked out.
  - Log the borrowing details (user, book, date).
- Return books:
  - Increase the number of available copies upon return.
  - Log the return details (user, book, date).
- Prevent users from borrowing unavailable books.

4. Transaction Management
- Maintain logs of all check-out and return transactions.
- Track borrowing and return dates.

5. Search and Filter
- Search books by title, author, genre, or ISBN.
- Filter books by availability and publication date.
- 
API Endpoints

Authentication
- **Login**: `/api/token/` (POST)
- **Refresh Token**: `/api/token/refresh/` (POST)

Books
- **List All Books**: `/api/books/` (GET)
- **Create a Book**: `/api/books/` (POST)
- **Retrieve a Book**: `/api/books/<id>/` (GET)
- **Update a Book**: `/api/books/<id>/` (PUT/PATCH)
- **Delete a Book**: `/api/books/<id>/` (DELETE)

Users
- **List All Users**: `/api/users/` (GET)
- **Create a User**: `/api/users/` (POST)
- **Retrieve a User**: `/api/users/<id>/` (GET)
- **Update a User**: `/api/users/<id>/` (PUT/PATCH)
- **Delete a User**: `/api/users/<id>/` (DELETE)

Transactions
- **Check-Out a Book**: `/api/transactions/checkout/` (POST)
- **Return a Book**: `/api/transactions/return/` (POST)

---

Deployment
- The application is designed to be deployed on platforms such as Heroku or PythonAnywhere.
- Ensure to set up environment variables for sensitive data (e.g., SECRET_KEY, database credentials).

---

Technical Details
Database
- **Models**:
  - Books
  - Users
  - Transactions
- Managed using Django ORM.

Authentication
- Basic authentication using Django’s built-in system.

API Design
- Built with Django REST Framework.
- Follows RESTful principles with appropriate HTTP methods and status codes.

---

Future Enhancements
- Notifications for overdue books.
- Advanced reporting (most borrowed books, user activity reports).
- Role-based access control (e.g., librarian-specific functionalities).
- Integration with third-party services (e.g., email notifications).





