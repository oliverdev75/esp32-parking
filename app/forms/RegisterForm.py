from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat_password', validators=[DataRequired()])
    contact = IntegerField('Contact', validators=[DataRequired()])
    car_name = StringField('Car name', validators=[DataRequired()])
    car_plate = StringField('Car_plate', validators=[DataRequired()])
    submit = SubmitField('Register')

    def __init__(self):
        super().__init__()