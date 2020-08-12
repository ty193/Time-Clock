from app import db
from models import Employee, Time

db.drop_all()
db.create_all()