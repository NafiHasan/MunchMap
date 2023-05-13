from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = SelectField('Location', choices=[('Shyamoli', 'Shyamoli'), (
        'Adabor', 'Adabor'), ('Mirpur', 'Mirpur'), ('Shahbag', 'Shahbag'), ('Baily Road', 'Baily Road'), ('Uttara', 'Uttara')], validators=[DataRequired()])
    detail_location = TextAreaField(
        'Detail Location', validators=[DataRequired()])
    picture = FileField('Add restaurant\'s image', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Create')


class UpdateForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = SelectField('Location', choices=[('Shyamoli', 'Shyamoli'), (
        'Adabor', 'Adabor'), ('Mirpur', 'Mirpur'), ('Shahbag', 'Shahbag'), ('Baily Road', 'Baily Road'), ('Uttara', 'Uttara')], validators=[DataRequired()])
    detail_location = TextAreaField(
        'Detail Location', validators=[DataRequired()])
    picture = FileField('Add restaurant\'s image', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('update')
