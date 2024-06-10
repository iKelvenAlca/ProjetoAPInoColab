from flask import Flask, jsonify

app = Flask(__name__)

# Dados da planilha
data = [
    {"Number": 1, "Name": "Mahash", "Age": 25, "City": "Bangalore", "Country": "India"},
    {"Number": 2, "Name": "Alex", "Age": 26, "City": "London", "Country": "UK"},
    {"Number": 3, "Name": "David", "Age": 27, "City": "San Francisco", "Country": "USA"},
    {"Number": 4, "Name": "John", "Age": 28, "City": "Toronto", "Country": "Canada"},
    {"Number": 5, "Name": "Chris", "Age": 29, "City": "Paris", "Country": "France"}
]

print("API Rodando em http://127.0.0.1:5000/index")

@app.route('/index')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

