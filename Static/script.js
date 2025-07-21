document.getElementById('registrationForm').addEventListener('submit', function(event) {
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!username || !email || !password) {
        alert('Todos os campos são obrigatórios!');
        event.preventDefault();
    } else if (!emailRegex.test(email)) {
        alert('Por favor, insira um e-mail válido.');
        event.preventDefault();
    }
});
