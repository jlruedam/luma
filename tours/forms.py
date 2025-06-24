from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, URL

class TourForm(FlaskForm):
    name_tour = StringField("Tour Name", validators=[DataRequired(), Length(max=100)])
    description = TextAreaField("Description", validators=[DataRequired(), Length(max=500)])
    price_sale = FloatField("Sale Price", validators=[DataRequired(), NumberRange(min=0)])
    price_total = FloatField("Total Price", validators=[DataRequired(), NumberRange(min=0)])
    image_path = StringField("Image Path (static/)", validators=[DataRequired(), Length(max=200)])
    agency_id = SelectField("Agency", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Save")