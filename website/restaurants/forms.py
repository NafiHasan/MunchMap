from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = SelectField('Location', choices=[('Shyamoli', 'Shyamoli'), (
        'Adabor', 'Adabor'), ('Mirpur-1', 'Mirpur-1'), ('Shahbag', 'Shahbag'), ('Baily Road', 'Baily Road'), ('Uttara', 'Uttara'), ('Mohammadpur', 'Mohammadpur'), ('Dhanmondi', 'Dhanmondi'), ('Jhigatola', 'Jhigatola'), ('Gulshan', 'Gulshan'), ('Banani', 'Banani'), ('Mirpur-10', 'Mirpur-10'), ('College-Gate', 'College Gate'), ('Science-Lab', 'Science Lab'), ('Farmgate', 'Farmgate'), ('Shankar', 'Shankar'), ('New-Market', 'New Market'), ('Kalabagan', 'Kalabagan'), ('Panthapath', 'Panthapath'), ('Gabtoli', 'Gabtoli'), ('LalBag', 'LalBag'), ('Banasree', 'Banasree'), ('Shantinagar', 'Shantinagar'), ('Asad-Gate', 'Asad Gate'), ('Kallyanpur', 'Kallyanpur')], validators=[DataRequired()])
    detail_location = TextAreaField(
        'Detail Location', validators=[DataRequired()])
    picture = FileField('Add restaurant\'s image', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    submit = SubmitField('Create')


class UpdateForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = SelectField('Location', choices=[('Shyamoli', 'Shyamoli'), (
        'Adabor', 'Adabor'), ('Mirpur-1', 'Mirpur-1'), ('Shahbag', 'Shahbag'), ('Baily Road', 'Baily Road'), ('Uttara', 'Uttara'), ('Mohammadpur', 'Mohammadpur'), ('Dhanmondi', 'Dhanmondi'), ('Jhigatola', 'Jhigatola'), ('Gulshan', 'Gulshan'), ('Banani', 'Banani'), ('Mirpur-10', 'Mirpur-10'), ('College-Gate', 'College Gate'), ('Science-Lab', 'Science Lab'), ('Farmgate', 'Farmgate'), ('Shankar', 'Shankar'), ('New-Market', 'New Market'), ('Kalabagan', 'Kalabagan'), ('Panthapath', 'Panthapath'), ('Gabtoli', 'Gabtoli'), ('LalBag', 'LalBag'), ('Banasree', 'Banasree'), ('Shantinagar', 'Shantinagar'), ('Asad-Gate', 'Asad Gate'), ('Kallyanpur', 'Kallyanpur')], validators=[DataRequired()])
    detail_location = TextAreaField(
        'Detail Location', validators=[DataRequired()])
    picture = FileField('Add restaurant\'s image', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg', 'webp'])])
    submit = SubmitField('update')
