import models
from app import db
from app import app
from models import Tag
with app.app_context():
    db.create_all()

from models import Post
p = Post(title='first post', body ='first post body')
with app.app_context():
    db.session.add(p)
    db.session.commit()

p1 = Post(title='Second post', body ='Second post body')
with app.app_context():
    db.session.add(p1)
    db.session.commit()

p2 = Post(title='Third post! 3-test', body ='Third post body')
with app.app_context():
    db.session.add(p2)
    db.session.commit()

tag = Tag(name="python")
with app.app_context():
    db.session.add(tag)
    db.session.commit()
