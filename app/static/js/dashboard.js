// Модальные окна
function showAddNoteModal() {
    document.getElementById('noteModalTitle').textContent = 'Add Note';
    document.getElementById('noteId').value = '';
    document.getElementById('noteTitle').value = '';
    document.getElementById('noteContent').value = '';
    document.getElementById('noteModal').classList.remove('hidden');
}

function closeNoteModal() {
    document.getElementById('noteModal').classList.add('hidden');
}

function showAddTodoModal() {
    document.getElementById('todoModalTitle').textContent = 'Add Task';
    document.getElementById('todoId').value = '';
    document.getElementById('todoTitle').value = '';
    document.getElementById('todoDueDate').value = '';
    document.getElementById('todoPriority').value = '1';
    document.getElementById('todoModal').classList.remove('hidden');
}

function closeTodoModal() {
    document.getElementById('todoModal').classList.add('hidden');
}

// Работа с заметками
async function submitNote(event) {
    event.preventDefault();
    
    const noteId = document.getElementById('noteId').value;
    const title = document.getElementById('noteTitle').value;
    const content = document.getElementById('noteContent').value;
    
    const method = noteId ? 'PUT' : 'POST';
    const url = noteId ? `/api/notes/${noteId}` : '/api/notes';
    
    try {
        const response = await fetchWithAuth(url, {
            method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title,
                content
            })
        });
        
        if (response.ok) {
            closeNoteModal();
            location.reload();
        } else {
            const data = await response.json();
            showNotification(data.detail || 'Failed to save note', 'error');
        }
    } catch (error) {
        showNotification('An error occurred', 'error');
    }
}

async function editNote(noteId) {
    try {
        const response = await fetchWithAuth(`/api/notes/${noteId}`);
        const note = await response.json();
        
        document.getElementById('noteModalTitle').textContent = 'Edit Note';
        document.getElementById('noteId').value = noteId;
        document.getElementById('noteTitle').value = note.title;
        document.getElementById('noteContent').value = note.content;
        document.getElementById('noteModal').classList.remove('hidden');
    } catch (error) {
        showNotification('Failed to load note', 'error');
    }
}

async function deleteNote(noteId) {
    if (!confirm('Are you sure you want to delete this note?')) return;
    
    try {
        const response = await fetchWithAuth(`/api/notes/${noteId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            location.reload();
        } else {
            showNotification('Failed to delete note', 'error');
        }
    } catch (error) {
        showNotification('An error occurred', 'error');
    }
}

// Работа с задачами
async function submitTodo(event) {
    event.preventDefault();
    
    const todoId = document.getElementById('todoId').value;
    const title = document.getElementById('todoTitle').value;
    const dueDate = document.getElementById('todoDueDate').value;
    const priority = document.getElementById('todoPriority').value;
    
    const method = todoId ? 'PUT' : 'POST';
    const url = todoId ? `/api/todos/${todoId}` : '/api/todos';
    
    try {
        const response = await fetchWithAuth(url, {
            method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title,
                due_date: new Date(dueDate).toISOString(),
                priority: parseInt(priority)
            })
        });
        
        if (response.ok) {
            closeTodoModal();
            location.reload();
        } else {
            const data = await response.json();
            showNotification(data.detail || 'Failed to save task', 'error');
        }
    } catch (error) {
        showNotification('An error occurred', 'error');
    }
}

async function editTodo(todoId) {
    try {
        const response = await fetchWithAuth(`/api/todos/${todoId}`);
        const todo = await response.json();
        
        document.getElementById('todoModalTitle').textContent = 'Edit Task';
        document.getElementById('todoId').value = todoId;
        document.getElementById('todoTitle').value = todo.title;
        document.getElementById('todoDueDate').value = todo.due_date.split('T')[0];
        document.getElementById('todoPriority').value = todo.priority;
        document.getElementById('todoModal').classList.remove('hidden');
    } catch (error) {
        showNotification('Failed to load task', 'error');
    }
}

async function deleteTodo(todoId) {
    if (!confirm('Are you sure you want to delete this task?')) return;
    
    try {
        const response = await fetchWithAuth(`/api/todos/${todoId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            location.reload();
        } else {
            showNotification('Failed to delete task', 'error');
        }
    } catch (error) {
        showNotification('An error occurred', 'error');
    }
}

async function toggleTodo(todoId) {
    try {
        const response = await fetchWithAuth(`/api/todos/${todoId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                completed: true
            })
        });
        
        if (response.ok) {
            location.reload();
        } else {
            showNotification('Failed to update task', 'error');
        }
    } catch (error) {
        showNotification('An error occurred', 'error');
    }
}

// Проверяем авторизацию при загрузке страницы
document.addEventListener('DOMContentLoaded', checkAuth);
