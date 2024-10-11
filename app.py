from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    error = ""
    if request.method == 'POST':
        user_input = request.form['command']
        try:
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
            output = result.stdout
            error = result.stderr
        except Exception as e:
            error = str(e)

    return render_template('index.html', output=output, error=error)

if __name__ == '__main__':
    app.run(debug=True)
