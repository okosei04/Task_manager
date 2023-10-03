document.addEventListener('DOMContentLoaded', function () {
    loadTasks();
});

function loadTasks() {
    fetch('/api/tasks')
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = '';
            data.forEach(task => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <span>${task.title}</span>
                    <button onclick="toggleTask(${task.id})">${task.completed ? 'Undo' : 'Complete'}</button>
                    <button onclick="deleteTask(${task.id})">Delete</button>
                `;
                taskList.appendChild(li);
            });
        });
}

function addTask() {
    const taskInput = document.getElementById('task-input');
    const title = taskInput.value.trim();
    if (title !== '') {
        fetch('/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title }),
        })
        .then(response => response.json())
        .then(data => {
            taskInput.value = '';
            loadTasks();
        });
    }
}

function toggleTask(id) {
    fetch(`/api/tasks/${id}`, {
        method: 'PUT',
    })
    .then(response => response.json())
    .then(data => {
        loadTasks();
    });
}

function deleteTask(id) {
    fetch(`/api/tasks/${id}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        loadTasks();
    });
}
