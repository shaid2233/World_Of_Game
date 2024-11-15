from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

app.debug = True  # Enable debug mode

@app.route('/')
def score_server():
    try:
        with open('scores.txt', 'r') as file:
            score = file.read().strip()
        return render_template('index.html', score=score)
    except:
        return render_template('index.html', score='ERROR')

if __name__ == '__main__':
    app.run()