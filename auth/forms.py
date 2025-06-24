from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField("User", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("log in")



class RegisterForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    confirm = PasswordField("Confirmar contraseña", validators=[
        DataRequired(),
        EqualTo('password', message='Las contraseñas no coinciden.')
    ])
    submit = SubmitField("Registrarse")