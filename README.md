# ToDo App (Flask + Docker)

Simple calendar-based To-Do app built with Flask and SQLite.  
Demonstrates basic CRUD operations and Docker containerization.

**Note:** The SQLite database (`tasks.db`) is local and not included in the repository.

## Run locally
```bash
git clone https://github.com/Pollyy2/todo-app.git
cd todo_app
python app.py
```

## Run with Docker
```bash
docker pull polia/todo-app
docker run -p 5000:5000 polia/todo-app
```

Open [http://localhost:5000](http://localhost:5000) in your browser.
