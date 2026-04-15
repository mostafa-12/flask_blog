from app import create_app
from app.extensions import db
from app.models import User, Post, Comment
from faker import Faker
from werkzeug.security import generate_password_hash

app = create_app()
fake = Faker()

    
def seed_users(n=10):
    for _ in range(n):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=generate_password_hash("password123")
        )
        db.session.add(user)
    db.session.commit()
    
def seed_posts(n=20):
    users = User.query.all()
    for _ in range(n):
        post = Post(
            title=fake.sentence(),
            content=fake.text(),
            author_id=fake.random_element(users).id
        )
        db.session.add(post)
    db.session.commit()
    
    
def seed_comments(n=50):
    users = User.query.all()
    posts = Post.query.all()
    for _ in range(n):
        comment = Comment(
            content=fake.text(),
            author_id=fake.random_element(users).id,
            post_id=fake.random_element(posts).id
        )
        db.session.add(comment)
    db.session.commit()
    
    
if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_users()
        seed_posts()
        seed_comments()
    print("Database seeded successfully!")