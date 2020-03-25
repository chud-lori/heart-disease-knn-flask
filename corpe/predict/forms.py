from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange, InputRequired

class PredictForm(FlaskForm):
    age = IntegerField('Umur', validators=[DataRequired(), NumberRange(min=0, max=200, message='blbla')])
    sex = SelectField('Jenis Kelamin', choices=[(1, 'Laki-laki'), (0, 'Perempuan')],
                     validators=[InputRequired()], coerce=int)
    submit = SubmitField('Cek')