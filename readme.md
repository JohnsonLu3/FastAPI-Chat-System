# FastAPI Chat System

This project is a chat system built with FastAPI that communicates with a frontend, stores data in a PostgreSQL database, and includes user authentication.

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd <repository-directory>
```
2. Set Up a Virtual Environment
On macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```
On Windows
3. Install Dependencies
```
python -m venv venv
.\venv\Scripts\activate
```


4. Set Up PostgreSQL Database
Install PostgreSQL: Follow the instructions on the PostgreSQL website to install PostgreSQL on your machine.

Create a Database: Open your PostgreSQL client and run the following commands to create a new database and user:

5. Configure Database Connection String
Create a .env file in the root directory of your project and add the following environment variables:
```
DATABASE_URL=postgresql+asyncpg://chat_user:your_password@localhost/chat_db
SECRET_KEY=your_secret_key
```

6. Run Database Migrations
```
alembic upgrade head
```

7. Run the FastAPI Application
```
uvicorn main:app --reload
```

8. Run Unit Tests
```
pytest
```

Additional Information
API Documentation: Once the server is running, you can access the interactive API documentation at http://127.0.0.1:8000/docs.
Environment Variables: Ensure that the .env file is not committed to version control for security reasons.
Feel free to modify the instructions as needed for your specific setup.


