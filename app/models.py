from app.extensions import db
from flask_login import UserMixin
import datetime
GET_TIME_NOW = lambda: datetime.datetime.now(datetime.timezone.utc)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), default="user")
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    joined_at = db.Column(db.DateTime, default=GET_TIME_NOW)
    profile_picture = db.Column(db.String(256), default= "default.jpg")
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    comments = db.relationship("Comment", backref="author", lazy="dynamic")
    def __repr__(self):
        return f"<User {self.username}, {self.email}, {self.joined_at}>"
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")
    @password.setter
    def password(self, password):
        from werkzeug.security import generate_password_hash
        self.hashed_password = generate_password_hash(password)
    def verify_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.hashed_password, password)
    
    
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=GET_TIME_NOW)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    comments = db.relationship("Comment", backref="post", lazy="dynamic")
    cover_image = db.Column(db.String(256), default="default_post.jpg")
    def __repr__(self):
        return f"<Post {self.title}, {self.timestamp}>"
    
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=GET_TIME_NOW)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    
    def __repr__(self):
        return f"<Comment {self.content[:20]}, {self.timestamp}>"