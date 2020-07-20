from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange, InputRequired

class PredictForm(FlaskForm):
    age = IntegerField('Umur', validators=[DataRequired(), NumberRange(min=0, max=200, message='Tidak valid')])
    sex = SelectField('Jenis Kelamin', choices=[(0, 'Perempuan'), (1, 'Laki-laki')],
                     validators=[InputRequired()], coerce=int)
    cp = SelectField('Chest pain type', choices=[(1, 'Typical angina'), (2, 'Atypical angina'), 
                    (3, 'Non-anginal pain'), (4, 'Asymptomatic')],
                    validators=[InputRequired()], coerce=int)
    trestbps = IntegerField('Resting blood pressure', validators=[DataRequired(), NumberRange(min=0, max=500, message='Tidak valid')])
    chol = IntegerField('Serum cholestoral in mg/dl', validators=[DataRequired(), NumberRange(min=0, max=500, message='Tidak valid')])
    fbs = SelectField('Fasting blood sugar > 120 mg/dl', choices=[(1, 'Ya'), (0, 'Tidak')],
                     validators=[InputRequired()], coerce=int)
    restecg = SelectField('Resting electrocardiographic results', choices=[(0, 'Normal'), (1, 'Having ST-T wave abnormality'), 
                    (2, 'Showing probable or definite left ventricular hypertrophy by Estes criteria')],
                    validators=[InputRequired()], coerce=int)
    thalach = IntegerField('Maximum heart rate achieved', validators=[DataRequired(), NumberRange(min=0, max=500, message='Tidak valid')])
    exang = SelectField('Exercise induced angina', choices=[(1, 'Ya'), (0, 'Tidak')],
                     validators=[InputRequired()], coerce=int)
    oldpeak = DecimalField('ST depression induced by exercise relative to rest', places=2, validators=[DataRequired(),
                    NumberRange(min=0.0, max=10.0, message='Tidak valid')])
    slope = SelectField('The slope of the peak exercise ST segment', choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')],
                    validators=[InputRequired()], coerce=int)
    ca = SelectField('Number of major vessels (0-3) colored by flourosopy', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
                    validators=[InputRequired()], coerce=int)
    # ca = IntegerField('Number of major vessels (0-3) colored by flourosopy', validators=[DataRequired(), 
    #                 NumberRange(min=0, max=3, message='Tidak valid')])
    thal = SelectField('Pemeriksaan thalassemia', choices=[(1, 'Fixed defect'), (2, 'Normal'), (3, 'Reversable defect')],
                    validators=[InputRequired()], coerce=int) # selectornya masih bingung belum pas | 
                                                                #  katanya kalo 0 sih ga ada nilai, jadi pake 1,2,3
                                                                # 0 null
    
    submit = SubmitField('Cek')
