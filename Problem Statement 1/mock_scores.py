from flask import Flask, jsonify

app = Flask(__name__)  

@app.route('/scores')
def get_scores():
    data = [
        {"name": "Aarav Gupta", "score": 78},
        {"name": "Priya Verma", "score": 88},
        {"name": "Rohan Mehta", "score": 62},
        {"name": "Ananya Singh", "score": 91},
        {"name": "Kabir Jain", "score": 70},
        {"name": "Sneha Sharma", "score": 84},
        {"name": "Aditya Joshi", "score": 55},
        {"name": "Meera Agarwal", "score": 76},
        {"name": "Ishita Kapoor", "score": 93}
    ]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
