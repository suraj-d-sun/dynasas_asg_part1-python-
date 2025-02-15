# dynasas_asg_part1-python (blog_project)

This is a Django-based project with PostgreSQL integration and a REST API to manage blog posts.

## Requirements

- Python 3.x
- PostgreSQL
- Virtualenv(via django)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Set Up the Virtual Environment

# On Windows

```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
python -m venv env

# Activate the virtual environment
env\Scripts\activate
```

# Linux
```bash
Copy code
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate
```

### 3. Install Project Dependencies
 Install all required dependencies from the requirements.txt file.

``` bash
pip install -r requirements.txt
```

### 4. PostgreSQL Database Setup
Step 1: Install PostgreSQL
# On Windows:

- Download and install PostgreSQL from the official site.
- During the installation, remember the password you set.

# On Linux/Ubuntu:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Step 2: Create a PostgreSQL Database and User

# On Windows:

- Open pgAdmin(GUI) or the PostgreSQL shell (psql) to execute the commands.

# On Linux/Ubuntu: 
- Open the PostgreSQL shell by running:

```bash
sudo -u postgres psql
```

``` 
Create a new database
Create a new user and assign a password
Grant privileges to the user on the database
Exit the PostgreSQL shell
```


Step 3: Update Django Settings for PostgreSQL

Modify your DATABASES setting in settings.py to use PostgreSQL

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',  # Replace with your database name
        'USER': 'myuser',      # Replace with your database user
        'PASSWORD': 'mypassword',  # Replace with your password
        'HOST': 'localhost',
        'PORT': '5432',  # Default PostgreSQL port
    }
}
```



### 5. Run Database Migrations
Once your database is set up, apply migrations to create the required tables:

```bash
python manage.py migrate
```

If you need admin access to the Django admin interface, create a superuser: [OPTIONAL]

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
Start the Django development server to run the project locally:

```bash
pytnon manage.py runserver
```

You should be able to access the project at http://127.0.0.1:8000/

### 7. Testing API Requests
- Fetch Blog Posts (GET) : 
To retrieve all blog posts, send a GET request to  
```http://127.0.0.1:8000/api/posts/ ```

Example Response:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Post_1",
            "content": "This is my first blog post!",
            "created_at": "2024-10-17T06:18:07.592588Z",
            "updated_at": "2024-10-17T06:18:07.592588Z",
            "author": 1
        },
        {
            "id": 2,
            "title": "Post_2",
            "content": "This is my second blog post!",
            "created_at": "2024-10-17T06:38:32.131404Z",
            "updated_at": "2024-10-17T06:38:32.132405Z",
            "author": 1
        }
    ]
}
```
- Create a New Blog Post (POST)
To create a new blog post, send a POST request to:

```http://127.0.0.1:8000/api/posts/```

Request Body:

```json
{
    "title": "First Post",
    "content": "This is my first blog post!",
    "author": 1  
}
```

- Obtain Token (POST)
To obtain a token for authentication, send a POST request to

```
http://127.0.0.1:8000/api/token/
```
Remeber the username and password set while creating the superuser, they are required over here

Request Body:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

- Authentication Header
For protected API endpoints, include the token in the Authorization header:

```makefile
Authorization: Bearer <your_access_token>
```
<hr>
### Screenshots
<img src="https://github.com/user-attachments/assets/d0593ef8-5811-4878-9eb9-fd49144898ea" alt="Image 1" width="1000" height="350">

<img src="https://github.com/user-attachments/assets/a9e57fd5-a772-45b0-84d5-ea82c73dcf80" alt="Image 2" width="1000" height="350">

<img src="https://github.com/user-attachments/assets/e16f79f1-152b-40fe-b1e5-0d0fba367c33" alt="Image 3" width="700" height="500">

<img src="https://github.com/user-attachments/assets/56db532a-86fa-4c27-9b47-0ebed7c358ee" alt="Image 4" width="700" height="500">

<img src="https://github.com/user-attachments/assets/79e65fde-62eb-4e3a-8f61-d9cf46a7209d" alt="Image 5" width="700" height="600">

