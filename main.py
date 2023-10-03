# Import necessary libraries
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# API endpoint to get tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# API endpoint to add a new task
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {'id': len(tasks) + 1, 'title': data['title'], 'completed': False}
    tasks.append(task)
    return jsonify(task), 201

# API endpoint to update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['completed'] = not task['completed']
        return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

# API endpoint to delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
# Import necessary libraries
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# API endpoint to get tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# API endpoint to add a new task
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {'id': len(tasks) + 1, 'title': data['title'], 'completed': False}
    tasks.append(task)
    return jsonify(task), 201

# API endpoint to update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['completed'] = not task['completed']
        return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

# API endpoint to delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
