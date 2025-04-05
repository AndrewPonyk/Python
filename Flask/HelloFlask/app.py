from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Flask App', message='Welcome to Flask!')

@app.route('/api/items', methods=['GET'])
def list_items():
    items = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        {'id': 3, 'name': 'Item 3'}
    ]
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    # Here you would typically save the new_item to a database
    # For this example, we'll just return it
    return jsonify(new_item), 201

def fibobonacci(n):
    temp = 100
    if n <= 0:
        temp = temp +10
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

@app.route('/api/fibonacci/<int:n>', methods=['GET'])
def fibonacci(n):
    return jsonify(fibobonacci(n))

if __name__ == '__main__':
    app.run(debug=True)
