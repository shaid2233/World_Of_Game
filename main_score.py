from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open('Scores.txt', 'r') as f:
            score = f.read().strip()
        
        return f'''
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        '''
    except Exception as e:
        return '''
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>Error</h1>
            <div id="score">Error occurred while reading the score</div>
        </body>
        </html>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)