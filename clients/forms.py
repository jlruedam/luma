from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email

class ClientForm(FlaskForm):
    tipo_doc = SelectField("Document Type", choices=[
        ("CC", "Cédula de Ciudadanía"),
        ("TI", "Tarjeta de Identidad"),
        ("CE", "Cédula de Extranjería"),
        ("PA", "Pasaporte")
    ], validators=[DataRequired()])
    
    num_doc = StringField("Document Number", validators=[DataRequired(), Length(max=10)])
    name = StringField("Full Name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=200)])
    tel = IntegerField("Phone", validators=[])
    hotel = StringField("Hotel", validators=[DataRequired(), Length(max=200)])
    
    submit = SubmitField("Save")