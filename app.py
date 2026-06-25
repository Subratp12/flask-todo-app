from flask import Flask, jsonify, request, abort
import uuid

app = Flask(__name__)

# In-memory store
todos = {}


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(list(todos.values())), 200


@app.route('/todos/<todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        abort(404)
    return jsonify(todo), 200


@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        abort(400)
    todo_id = str(uuid.uuid4())
    todo = {
        'id': todo_id,
        'title': data['title'],
        'done': False,
    }
    todos[todo_id] = todo
    return jsonify(todo), 201


@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400)
    todo['title'] = data.get('title', todo['title'])
    todo['done'] = data.get('done', todo['done'])
    return jsonify(todo), 200


@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = todos.pop(todo_id, None)
    if not todo:
        abort(404)
    return jsonify({'message': 'Deleted'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
