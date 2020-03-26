from flask import (Flask, render_template, flash, Blueprint,
                    current_app, url_for, request, redirect,
                    make_response)
from corpe import db
from corpe.models import Dataset
from corpe.predict.forms import PredictForm
from corpe.predict.knn import knn
import csv

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/a')
def a():
    """ Endpoint to create datasets"""
    if len(Dataset.query.all()) >= 303:
        return redirect('/')
    with open(current_app.instance_path+'/heart.csv', newline='') as csvfile:
        heart_csv = csv.reader(csvfile)
        next(heart_csv)
        for row in heart_csv:
            data = Dataset(age=row[0], sex=row[1], cp=row[2], trestbps=row[3], chol=row[4],\
                fbs=row[5], restecg=row[6], thalach=row[7], exang=row[8], oldpeak=row[9],\
                slope=row[10], ca=row[11], thal=row[12], target=row[13])
            db.session.add(data)
    db.session.commit()
    return make_response('Dataset created')

@predict_bp.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictForm()
    if form.validate_on_submit():
        result = knn(form.age.data)
        if result == 1:
            target = 1
        else:
            target = 0
        ds = Dataset(age=form.age.data, sex=form.sex.data, cp=3, target=target)
        db.session.add(ds)
        db.session.commit()
        flash('DONEEEKNN', 'success')
        return redirect(url_for('predict.predicted', id=ds.id))
        # return redirect(url_for('predict.predicted', id=3))
    return render_template('predict/index.html', title='Cek', form=form)

@predict_bp.route('/predict/result/<int:id>')
def predicted(id):
    data = Dataset.query.get_or_404(id)
    return render_template('predict/result.html', title='Hasil', data=data)