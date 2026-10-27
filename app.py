from flask import Flask
app = Flask( name )

@app.route('/')
def home():
  return '<h1>DevOps Class Activity: Docker & GitHub Actions Pipeline Active!</h1>'

if name == ' main ':
  app.run(host='0.0.0.0', port=5000)
