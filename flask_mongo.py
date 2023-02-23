from flask_pymongo import PyMongo
from flask  import Flask,jsonify,request
import flask
app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/todo_db")
db = mongodb_client.db
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return '<h1>Hello  I will perform crud operation  with mongodb  in this file so stay tuned/////..... </h1>'

@app.route("/data")
def home():
    todos = db.todos.find()
    return flask.jsonify([todo for todo in todos])
@app.route("/add_one")
def add_one():
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")



@app.route("/add_many")
def add_many():
    db.todos.insert_many([
        {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
        {'_id': 2, 'title': "todo title two", 'body': "todo body two"},
        {'_id': 3, 'title': "todo title three", 'body': "todo body three"},
        {'_id': 4, 'title': "todo title four", 'body': "todo body four"},
        {'_id': 5, 'title': "todo title five", 'body': "todo body five"},
        {'_id': 1, 'title': "todo title six", 'body': "todo body six"},
        ])
    return flask.jsonify(message="success")



@app.route("/get_todo/<int:todoId>")
def insert_one(todoId):
    todo = db.todos.find_one({"_id": todoId})
    return todo



@app.route("/replace_todo/<int:todoId>")
def replace_one(todoId):
    result = db.todos.replace_one({'_id': todoId}, {'title': "modified title"})
    return {'id': result.raw_result}

@app.route("/update_todo/<int:todoId>")
def update_one(todoId):
    result = db.todos.update_one({'_id': todoId}, {"$set": {'title': "updated title"}})
    return result.raw_result


@app.route("/delete_todo/<int:todoId>", methods=['DELETE'])
def delete_todo(todoId):
    todo = db.todos.delete_one({'_id': todoId})
    return todo.raw_result


@app.route('/delete_many', methods=['DELETE'])
def delete_many():
    todo = db.todos.delete_many({'title': 'todo title two'})
    return todo.raw_result


@app.route("/save_file", methods=['POST', 'GET'])
def save_file():
    upload_form = """<h1>Save file</h1>
                     <form method="POST" enctype="multipart/form-data">
                     <input type="file" name="file" id="file">
                     <br><br>
                     <input type="submit">
                     </form>"""

    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            mongodb_client.save_file(file.filename, file)
            return {"file name": file.filename}
    return upload_form
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()