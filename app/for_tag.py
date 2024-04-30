import models
from app import db
from app import app
from models import Post, Tag

with app.app_context():
    t = Tag.query.first()
    post1 = Post.query.filter(Post.id == 1).first()
    post1.tags.append(t)
    db.session.add(post1)
    db.session.commit()


