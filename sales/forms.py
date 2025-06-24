from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SaleForm(FlaskForm):
    tour_id = SelectField("Tour", coerce=int, validators=[DataRequired()])
    client_id = SelectField("Cliente", coerce=int, validators=[DataRequired()])
    vendor1_id = SelectField("Vendedor principal", coerce=int, validators=[DataRequired()])
    vendor2_id = SelectField("Vendedor secundario", coerce=int, validators=[DataRequired()])
    quantity = IntegerField("Cantidad", validators=[DataRequired(), NumberRange(min=1)])
    options_payment = StringField("Forma de pago", validators=[DataRequired()])
    observations = StringField("Observaciones")
    submit = SubmitField("Registrar venta")