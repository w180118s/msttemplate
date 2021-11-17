from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretket"

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/profile')
def profile():
    return render_template('/profile.html')

@app.route('/dashboard')
def dashboard():
    return render_template('/dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)