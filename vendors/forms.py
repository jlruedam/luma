from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email

class VendorForm(FlaskForm):
    type_doc = SelectField("Document Type", choices=[
        ("CC", "Cédula de Ciudadanía"),
        ("TI", "Tarjeta de Identidad"),
        ("CE", "Cédula de Extranjería"),
        ("PA", "Pasaporte")
    ], validators=[DataRequired()])
    
    num_doc = StringField("Document Number", validators=[DataRequired(), Length(max=50)])
    name = StringField("Full Name", validators=[DataRequired(), Length(max=200)])
    tel = StringField("Phone", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    
    submit = SubmitField("Save")