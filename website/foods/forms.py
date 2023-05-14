from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FloatField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    picture = FileField('Add item\'s image', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    submit = SubmitField('Add')


class UpdateForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    picture = FileField('Add item\'s image', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    submit = SubmitField('Update')
