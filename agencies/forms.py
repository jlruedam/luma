from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class AgencyForm(FlaskForm):
    nit = StringField("NIT", validators=[DataRequired(), Length(max=10)])
    name_agency = StringField("Agency Name", validators=[DataRequired()])
    email_agency = StringField("Email", validators=[DataRequired(), Email()])
    tel_agency = StringField("Phone", validators=[DataRequired()])
    contact = StringField("Contact Person", validators=[DataRequired()])
    submit = SubmitField("Save")