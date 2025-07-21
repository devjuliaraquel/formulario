from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

usuarios = []

@app.route('/')
def index():
    return redirect(url_for('registrarUsuario'))

@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not username or not email or not password:
            flash('Todos os campos são obrigatórios!', 'danger')
        else:
            usuarios.append({
                'username': username,
                'email': email,
                'password': password
            })
            flash(f'Usuário {username} cadastrado com sucesso!', 'success')
            return redirect(url_for('registrarUsuario'))

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)


