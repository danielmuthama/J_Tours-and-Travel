from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import Required, DataRequired, Length, Email, EqualTo
from ..models import User
from wtforms import ValidationError


# class RegisterForm(FlaskForm):
#     name = TextField("Name", validators=[DataRequired()])

#     username = StringField("Username",
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField("Email",
#                         validators=[DataRequired(), Email()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     # confirm_password = PasswordField("Confirm Password",
#     #                                  validators=[DataRequired(), EqualTo("password")])
#     submit = SubmitField("Sign Up")

class RegistrationForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required(), Length(min=5, max=20)])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
