from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

videos = {}

def abort_if_not_found(video_id):
  if video_id not in videos:
    abort(404, message="Video ID not found...")

def abort_if_found(video_id):
  if video_id in videos:
    abort(409, message="Video ID already exists...")

class Video(Resource):
  def get(self, video_id):
    abort_if_not_found(video_id)
    return videos[video_id], 201
  
  def put(self, video_id):
    abort_if_found(video_id)
    args = video_put_args.parse_args()
    videos[video_id] = args
    return videos[video_id], 201
  
  def delete(self, video_id):
    abort_if_not_found(video_id)
    del videos[video_id]
    return '', 204
  
api.add_resource(Video, "/video/<int:video_id>")

# names = {
#   "samuel": {"age": 26, "gender": "male"},
#   "linda": {"age": 29, "gender": "female"}
# }

# class HelloWorld(Resource):
#   def get(self, name):
#     return names[name]

# api.add_resource(HelloWorld, "/<string:name>")

if __name__ == "__main__":
  # db.create_all()
  app.run(debug=True)
  