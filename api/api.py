from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

# >>> db.create_all()
# >>> from api import Todo
# >>> todo = Todo(content='I need to eat')
# >>> db.session.add(todo)
# >>> db.session.commit()
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id}'


def todo_serializer(todo):
    return {
        'id': todo.id,
        'content': todo.content
    }


@app.route("/api", methods=['GET'])
def index():
    return jsonify([*map(todo_serializer, Todo.query.all())])

@app.route("/api/create", methods=['POST'])
def create():
    request_data = json.loads(request.data)
    todo = Todo(content=request_data['content'])
    db.session.add(todo)
    db.session.commit()

    return {'201':'todo created succesfully'}
    


if __name__ == '__main__':
    app.run(debug=True)