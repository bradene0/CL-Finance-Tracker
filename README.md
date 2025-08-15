# CL-Finance-Tracker 📊

A full-featured personal finance tracker web application built with Python and Django. This project is designed to showcase core web development skills, including database modeling, user authentication, session management, and a complete CRUD (Create, Read, Update, Delete) workflow.

The application features a seamless guest user system, allowing visitors to trial the full functionality without needing to register an account. All data is tied to the user's session.

### A Note on the User Interface

Please note that the primary focus of this project is to demonstrate backend development skills, including database modeling, business logic, and session management within the Django framework. The front-end is intentionally kept clean and functional, prioritizing a straightforward user experience to effectively showcase the underlying application logic.

## Features

* **Full CRUD Functionality:** Users can Create, Read, Update, and Delete financial transactions.
* **Guest User System:** Automatically creates a temporary user account for anonymous visitors using Django's session framework, providing an isolated sandbox for each user.
* **Dynamic Dashboard:** The homepage serves as a dashboard, displaying a real-time summary of total income and expenses.
* **User Authentication:** Includes Django's built-in system for user login and logout.
* **Responsive UI:** The front end is styled with the Bootstrap CSS framework for a clean, modern, and responsive user experience on any device.

## Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap 5
* **Database:** SQLite (for development)
* **Version Control:** Git

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/CL-Finance-Tracker.git](https://github.com/YOUR_USERNAME/CL-Finance-Tracker.git)
    cd CL-Finance-Tracker
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python3 manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python3 manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python3 manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## Usage

Visit the homepage to be automatically assigned a temporary guest session. You can immediately begin to add, view, edit, and delete transactions. All data you create is tied to your session and is isolated from other users.

To access the Django admin panel, navigate to `/admin/` and log in with the superuser credentials you created during setup.

## Future Improvements

* Implement data visualization (e.g., charts for spending by category).
* Add transaction filtering by date range and category.
* Develop a full user registration system to allow users to save their data permanently.
