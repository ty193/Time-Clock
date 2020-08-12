"""SQLAlchemy models fro Warbler."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class Time(db.Model):
    """Tracks employees time."""

    __tablename__ = 'time'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey('employees.id'),
    )

    date = db.Column(
        db.DateTime,
    )

    clock_in = db.Column(
        db.Float,
    )

    clock_out = db.Column(
        db.Float,
    )


class Employee(db.Model):
    """Employees in the system."""

    __tablename__ = 'employees'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    admin = db.Column(
        db.Boolean,
    )

    def __repr__(self):
        return f"<Employee #{self.id}: {self.name}, {self.username}>"

    @classmethod
    def signup(cls, name, username, password, admin):
        """Sign up user, hashes password and adds user to system."""

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        employee = Employee(
            name=name,
            username=username,
            password=hashed_pwd,
            admin=admin,
        )

        db.session.add(employee)
        return employee

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        employee = cls.query.filter_by(username=username).first()

        if employee:
            is_auth = bcrypt.check_password_hash(employee.password, password)
            if is_auth:
                return employee

        return False


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in you Flask app.
    """

    db.app = app
    db.init_app(app)