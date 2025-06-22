# Bot Notifier

Bot Notifier is a Django-based web application with a Telegram bot integration. It allows users to register via a web interface, receive welcome emails via Celery, and interact with a Telegram bot that saves usernames to the database. The project includes a protected API endpoint for authenticated users.

## Features
- **Web Registration**: Users can register with a username, email, and password, triggering a welcome email sent via Celery.
- **Telegram Bot**: Responds to the `/start` command, saves the user's Telegram username, and triggers a welcome email.
- **Protected API**: A REST API endpoint accessible only to authenticated users via JWT.
- **Celery with Redis**: Handles background email tasks using Redis as the message broker.
- **Django Admin**: Manage registered users and Telegram usernames.

## Prerequisites
- **Python**: 3.8 or higher
- **Docker**: For running Redis (Windows-compatible)
- **Git**: For cloning the repository
- **Telegram Account**: To interact with the bot and obtain a bot token
- **Gmail Account**: For sending emails (optional for console testing)

## Setup Instructions (Windows)
- **Clone the Repository**:
  
   ```bash
   git clone https://github.com/your-username/bot-notifier.git
   cd bot-notifier
   ```
- **Create and Activate a Virtual Environment**:
  
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
   ```
- **Install Dependencies**:
   ```bash
  pip install -r requirements.txt
   ```
## Set Up Redis with Docker (Windows)
- **Install Docker DeskTop and ensure it's running**
- **Start a redis container**:
  
  ```bash
  docker run -d -p 6379:6379 --name redis redis
   ```

## Configure Environment Variables
- **Copy this and add in .env file**
- **Edit .env with your values**
  ```bash
  SECRET_KEY = your-secret-key-here
  DEBUG = True
  REDIS_URL=redis://localhost:6379/0
  EMAIL_HOST=smtp.gmail.com
  EMAIL_PORT=587
  EMAIL_HOST_USER=your-email@gmail.com
  EMAIL_HOST_PASSWORD=your-email-app-password
  TELEGRAM_BOT_TOKEN = your-telegram-bot-token
   ```

- **Generate a SECRET_KEY**:
  
  ```bash
  python -c "import secrets; print(secrets.token_urlsafe(50))"
  ```
- **Get a `TELEGRAM_BOT_TOKEN` from [BotFather](https://t.me/BotFather) by creating a new bot**

- **Use a Gmail [App Password](https://support.google.com/accounts/answer/185833) for `EMAIL_HOST_PASSWORD` if 2FA is enabled**

- **Apply Database Migrations**:
  
   ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
   
- **Create a Superuser for Admin Access**:
  
    ```bash
  python manage.py createsuperuser
  ```
    
# How to Run Locally

## Start Redis
Ensure Docker Desktop is running and start the Redis container:

```bash
docker start redis
````

## Run the Django Development Server

Open a Command Prompt, activate the virtual environment, and run:

```bash
.venv\Scripts\activate
python manage.py runserver
```

Access at [http://localhost:8000/](http://localhost:8000/).

## Run the Celery Worker

In a new Command Prompt:

```bash
.venv\Scripts\activate
celery -A bot_notifier worker -l info --pool=solo
```

> The `--pool=solo` flag ensures compatibility with Windows.

## Run the Telegram Bot

In another Command Prompt:

```bash
.venv\Scripts\activate
python manage.py runbot
```

## Test the Application

### Web Interface

* Register at: http://localhost:8000/
* Log in at: http://localhost:8000/login/
* View the home page: http://localhost:8000/home/
* Access the admin: http://localhost:8000/admin/ with superuser credentials

### Telegram Bot

* Find your bot in Telegram (e.g., `@BotNotifier`)
* Send `/start` to save your username and trigger a welcome email
* Verify saved usernames in the admin under **Telegram Users**

# API Documentation

The project provides a 2 API endpoint using Django REST Framework and JWT authentication.


* **Endpoint**: `/api/public/`
* **Method**: `GET`
* **Description**: Returns a message for all users

### Response Example:

```json
{
    "message": "This is a public endpoint!"
}
```

---

* **Endpoint**: `/api/protected/`
* **Method**: `GET`
* **Description**: Returns a message for authenticated users
* **Authentication**: Requires a JWT access token in the Authorization header

### Request Example:

```bash
curl -H "Authorization: Bearer your-jwt-access-token" http://localhost:8000/api/protected/
```

### Response Example:

```json
{
    "message": "This is a protected endpoint!"
}
```

---

## Obtaining a JWT Token

1. Register a user at http://localhost:8000/
2. Obtain a token pair via the `/api/token/` endpoint:

```bash
curl -X POST -d "username=your-username&password=your-password" http://localhost:8000/api/token/
```
**OR**

**POSTMAN**

```json
{
    "username": "your-username",
    "password": "your-password"
}
```

### Response:

```json
{
    "access": "your-jwt-access-token",
    "refresh": "your-jwt-refresh-token"
}
```

Use the access token in the Authorization header for protected endpoints.

---

## Refreshing a JWT Token

* **Endpoint**: `/api/token/refresh/`
* **Method**: `POST`

### Request Example:

```bash
curl -X POST -d "refresh=your-jwt-refresh-token" http://localhost:8000/api/token/refresh/
```

### Response:

```json
{
    "access": "new-jwt-access-token"
}
```

```



