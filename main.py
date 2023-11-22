from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

names = {
  "samuel": {"age": 26, "gender": "male"},
  "linda": {"age": 29, "gender": "female"}
}

class HelloWorld(Resource):
  def get(self, name):
    return names[name]

api.add_resource(HelloWorld, "/<string:name>")

if __name__ == "__main__":
  # db.create_all()
  app.run(debug=True)
  