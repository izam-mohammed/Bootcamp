# 📦 Project Installation Guide

## 🌟 Project Overview
A brief description of your project. Explain what it does and why it's useful.

## 🛠️ Prerequisites
Ensure you have the following installed before proceeding:
- Python 3.x
- Poetry
- Django

## 🚀 Installing

### Step 1: Clone the Repository
First, clone the repository to your local machine.

```sh
git clone https://github.com/izam-mohammed/bootcamp.git
cd week_06_django_2/django-blog
```

### Step 2: Install Dependencies
Install all necessary dependencies using Poetry.

```sh
poetry install
```

### Step 3: Enter the Environment
Activate the virtual environment created by Poetry.

```sh
poetry shell
```

### Step 4: Apply Database Migrations
Run these commands to set up your database. Execute these only if there are any database-level changes.

```sh
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Admin Access)
If you haven't created a superuser yet, run the following command and follow the instructions.

```sh
python manage.py createsuperuser
```

### Step 6: Collect Static Files
Gather all static files into one location.

```sh
python manage.py collectstatic
```

## 🏃‍♂️ Running the Server
Start the development server using the command below.

```sh
python manage.py runserver
```

## 🤝 Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## ⚠️ Common Issues
### Issue 1: Poetry Not Found
Make sure Poetry is installed and added to your PATH. You can install it using the following command:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### Issue 2: Database Errors
If you encounter database errors, ensure your database configuration is correct in `settings.py`.

## 📫 Contact
For any questions or support, please contact [this email](mailto:izamdeveloper1@gmail.com).
