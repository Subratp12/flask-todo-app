import json


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'


def test_get_todos_empty(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json == []


def test_create_todo(client):
    response = client.post(
        '/todos',
        data=json.dumps({'title': 'Buy groceries'}),
        content_type='application/json',
    )
    assert response.status_code == 201
    data = response.json
    assert data['title'] == 'Buy groceries'
    assert data['done'] is False
    assert 'id' in data


def test_create_todo_missing_title(client):
    response = client.post(
        '/todos',
        data=json.dumps({}),
        content_type='application/json',
    )
    assert response.status_code == 400


def test_get_todo(client):
    create_resp = client.post(
        '/todos',
        data=json.dumps({'title': 'Learn Docker'}),
        content_type='application/json',
    )
    todo_id = create_resp.json['id']

    response = client.get(f'/todos/{todo_id}')
    assert response.status_code == 200
    assert response.json['id'] == todo_id


def test_get_todo_not_found(client):
    response = client.get('/todos/nonexistent-id')
    assert response.status_code == 404


def test_update_todo(client):
    create_resp = client.post(
        '/todos',
        data=json.dumps({'title': 'Learn Terraform'}),
        content_type='application/json',
    )
    todo_id = create_resp.json['id']

    response = client.put(
        f'/todos/{todo_id}',
        data=json.dumps({'done': True}),
        content_type='application/json',
    )
    assert response.status_code == 200
    assert response.json['done'] is True


def test_update_todo_not_found(client):
    response = client.put(
        '/todos/nonexistent-id',
        data=json.dumps({'done': True}),
        content_type='application/json',
    )
    assert response.status_code == 404


def test_delete_todo(client):
    create_resp = client.post(
        '/todos',
        data=json.dumps({'title': 'Delete me'}),
        content_type='application/json',
    )
    todo_id = create_resp.json['id']

    response = client.delete(f'/todos/{todo_id}')
    assert response.status_code == 200

    get_response = client.get(f'/todos/{todo_id}')
    assert get_response.status_code == 404


def test_delete_todo_not_found(client):
    response = client.delete('/todos/nonexistent-id')
    assert response.status_code == 404
