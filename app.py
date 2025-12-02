from flask import Flask, request

app = Flask(__name__)

# Temporary in-memory "database"
tasks = []

@app.route('/')
def home():
    return {"message": "Hello, Backend World!"}

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return {"tasks": tasks}

# POST a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()  # Get JSON from request
    task_name = data.get("task")  # Extract "task" value
    if not task_name:
        return {"error": "Task name is required"}, 400
    
    task = {"id": len(tasks) + 1, "task": task_name}
    tasks.append(task)
    return {"message": "Task added successfully", "task": task}, 201

if __name__ == '__main__':
    app.run(debug=True)
