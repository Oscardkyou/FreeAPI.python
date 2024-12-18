// Функция для отображения уведомлений
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 p-4 rounded-lg text-white ${
        type === 'success' ? 'bg-green-500' : 'bg-red-500'
    }`;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Функция для выхода
async function logout() {
    localStorage.removeItem('token');
    window.location.href = '/login';
}

// Функция для проверки авторизации
function checkAuth() {
    const token = localStorage.getItem('token');
    if (!token && window.location.pathname !== '/login' && window.location.pathname !== '/register') {
        window.location.href = '/login';
    }
}

// Добавляем токен к каждому запросу
async function fetchWithAuth(url, options = {}) {
    const token = localStorage.getItem('token');
    if (token) {
        options.headers = {
            ...options.headers,
            'Authorization': `Bearer ${token}`
        };
    }
    const response = await fetch(url, options);
    if (response.status === 401) {
        localStorage.removeItem('token');
        window.location.href = '/login';
        return;
    }
    return response;
}
