// Обработка формы входа
async function handleLogin(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch('/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
        });
        
        const data = await response.json();
        
        if (response.ok) {
            localStorage.setItem('token', data.access_token);
            window.location.href = '/dashboard';
        } else {
            showNotification(data.detail || 'Login failed', 'error');
        }
    } catch (error) {
        showNotification('An error occurred', 'error');
    }
}

// Обработка формы регистрации
async function handleRegister(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch('/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                username,
                password
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showNotification('Registration successful!');
            window.location.href = '/login';
        } else {
            showNotification(data.detail || 'Registration failed', 'error');
        }
    } catch (error) {
        showNotification('An error occurred', 'error');
    }
}
