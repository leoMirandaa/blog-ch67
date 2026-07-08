# Steps to create a Django Project

1. Create the folder of the project
2. Open a terminal at that folder
3. Create the virtual environment

    - Mac: python3 -m venv venv
    - Windows: python -m venv venv

4. Activate the virtual environment

    - Mac: source venv/bin/activate
    - Windows: .\venv\Scripts\activate

5. Install the required dependencies

    - Both OS: pip install django

6. Create the django project structure

    - Both OS: django-admin startproject NAME_FOLDER .

7. Initialize the database (first time only)

    - Both OS: python3 manage.py migrate

8. Finish the project structure
    - Create an app to start
    - Create the templates and static folder
    - Link them on the setting.py
    - Create the .gitignore file 

## Django commands

- **python3 manage.py startapp APP_NAME** | Allow us to create new applications in  our project