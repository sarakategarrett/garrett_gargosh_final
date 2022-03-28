from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AssetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    ##allocation_percent = ('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TickerForm(FlaskForm):
    ticker_symbol = StringField('Ticker Symbol', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    asset_class = SelectField('Asset Class', choices=[])
    submit = SubmitField('Submit')


