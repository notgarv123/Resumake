from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/main-resume')
def main_resume():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)