from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # response = requests.get('http://localhost:8080/api/records')
    response = requests.get('http://host.docker.internal:8080/api/records')
    data = response.json()
    return render_template('table.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
