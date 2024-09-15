
## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/hani-momo/Mock-Blog
2. Change to the project directory:
   ```bash
   cd blog.project
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
4. Install the required packages, dependencies:
   ```bash
   pip install -r requirements.txt
5. Run migrations:
   ```bash
   cd blog_project
   python manage.py makemigrations
   python manage.py migrate
6. Start the server:
   ```bash
   python manage.py runserver
7. Go to http://127.0.0.1:8000/home in your browser to see the front work

   To deactivate the venv (optional):
    ```bash
    deactivate
