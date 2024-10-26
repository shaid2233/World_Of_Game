from flask import render_template_string
render_template_string('''<html>
  <head>
    <title>Scores Game</title>
  </head>
  <body>
    <h1>The score is:</h1>
    <div id="score">{SCORE}</div>
  </body>
</html>
''')