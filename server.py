from flask import Flask, render_template, redirect, session 

app = Flask(__name__)
app.secret_key = 'this is a secret key'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)