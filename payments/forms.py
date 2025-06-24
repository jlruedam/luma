from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from models import Sale

class PaymentForm(FlaskForm):
    id_sale = SelectField("Sale", coerce=int, validators=[DataRequired()])
    value = FloatField("Payment Value", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Save")