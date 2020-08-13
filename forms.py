from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, DateTimeField, DateField, HiddenField
from wtforms.validators import DataRequired, Email, Length
from app import session


class UserAddForm(FlaskForm):
    """From for adding users."""

    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    admin = BooleanField("Administrator")


class UserEditForm(FlaskForm):
    """Form for editing users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
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


class TimePeriodForm(FlaskForm):
    """Time period select form."""

    start = DateField('Start Date', validators=[DataRequired()])
    end = DateField('End Date', validators=[DataRequired()])



