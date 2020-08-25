from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, DateTimeField, DateField, HiddenField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from app import session


class UserAddForm(FlaskForm):
    """From for adding users."""

    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6), EqualTo('confirm', message='Password must match.')])
    confirm = PasswordField('Confirm password')
    admin = BooleanField("Administrator")


class UserEditForm(FlaskForm):
    """Form for editing users."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


# class ClockInForm(FlaskForm):
#     """Sends Date and time to database"""
#     employee_id = HiddenField('Employee_ID', default=session.employee.id, validators=[DataRequired()])
#     in_time = HiddenField('In_Time', default=datetime.now(), validators=[DataRequired()])

# class ClockOutForm(FlaskForm):
#     """Sends Date and time to database"""


class TimeClockForm(FlaskForm):
    """Time period select form."""

    clock_in = BooleanField("Clock in")

class TimePeriodForm(FlaskForm):
    """Time period select form."""

    start = StringField('Start Date', validators=[DataRequired()])
    end = StringField('End Date', validators=[DataRequired()])



