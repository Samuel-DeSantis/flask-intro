from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  views = db.Column(db.Integer, nullable=False)
  likes = db.Column(db.Integer, nullable=False)
  
  def __repr__(self):
    return f'Video(name = {name}, views = {views}, likes = {likes})'

db.create_all() # Only run once

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

resource_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'views': fields.Integer,
  'likes': fields.Integer
}

class Video(Resource):
  @marshal_with(resource_fields)
  def get(self, video_id):
    result = VideoModel.query.get(id=video_id)
    return result
  
  @marshal_with(resource_fields)
  def put(self, video_id):
    args = video_put_args.parse_args()
    video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
    db.session.add(video) # temp add
    db.session.commit()   # save to database
    return video, 201
  
  def delete(self, video_id):
    del videos[video_id]
    return '', 204
  
api.add_resource(Video, "/video/<int:video_id>")

# def abort_if_not_found(video_id):
#   if video_id not in videos:
#     abort(404, message="Video ID not found...")

# def abort_if_found(video_id):
#   if video_id in videos:
#     abort(409, message="Video ID already exists...")

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
  