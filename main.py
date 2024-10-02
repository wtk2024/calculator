from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def evaluate_expression(expression):
    try:
        # Replace operators with safe versions
        safe_expression = re.sub(r'[^0-9+\-*/.]', '', expression)
        result = eval(safe_expression)
        return result
    except Exception as e:
        return str(e)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    result = evaluate_expression(expression)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
