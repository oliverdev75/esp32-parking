from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class VehicleForm(FlaskForm):
    id = HiddenField()
    name = StringField('Name', validators=[DataRequired()])
    plate_number = StringField('Plate number', validators=[DataRequired()])
    submit = SubmitField('Register')

    def __init__(self):
        super().__init__()