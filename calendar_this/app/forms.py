from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class NewAppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    start_time = TimeField('Start Time',validators=[DataRequired()])
    end_time = TimeField('End Time',validators=[DataRequired()])
    description = TextAreaField('Description')
    private = BooleanField('private')
    submit = SubmitField("Add Appointment")
