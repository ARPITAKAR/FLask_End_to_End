from flask_wtf import FlaskForm
# in what format we eant the input from the user
from wtforms import(
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)
# whar can be maximum length and permissible characters for the input
# validation to check wheather the field is empty and the length is as per required
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)
# Datarequired has it's own message or we can pass of our own, Length min,max as parameters

class SignupForm(FlaskForm):
    username= StringField(
        "Username",
        validators=[DataRequired(),Length(8,30)]
    )
    email= StringField(
        "Email",
        validators=[DataRequired()]
    )
    gender=SelectField("Gender",
                       choices=["Male","Female"],
                       validators=[Optional()]
                       )
    dob=DateField("Date Of Birth",
                  validators=[Optional()])

    password=PasswordField("Password",validators=[DataRequired(),Length(5,25)])
    confirm_password=PasswordField("Confirm pass",validators=[DataRequired(),Length(5,25),EqualTo("password")])
    submit=SubmitField("Sign UP")


class LoginForm(FlaskForm):
    email= StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    password=PasswordField("Password",validators=[DataRequired(),Length(5,25)])
    remember_me=BooleanField("Remember Me")
    submit=SubmitField("Login")