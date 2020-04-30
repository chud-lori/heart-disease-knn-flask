from flask import (Flask, render_template, flash, Blueprint,
                    current_app, url_for, request, redirect,
                    make_response, session)
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
        abort(404)
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
        data = [form.age.data, form.sex.data, form.cp.data, form.trestbps.data,
                form.chol.data, form.fbs.data, form.restecg.data, form.thalach.data,
                form.exang.data, form.oldpeak.data, form.slope.data, form.ca.data, form.thal.data]
        result = knn(form.age.data)
        # row = [572,1,1,154,232,0,0,164,0,0,2,1,2]
        ds = Dataset(age=data[0], sex=data[1], cp=data[2], trestbps=data[3], chol=data[4],\
                fbs=data[5], restecg=data[6], thalach=data[7], exang=data[8], oldpeak=data[9],\
                slope=data[10], ca=data[11], thal=data[12], target=result)
        db.session.add(ds)
        db.session.commit()
        # session['predicted'] = ds.id
        flash('Hore', 'success')
        return redirect(url_for('predict.predicted', id=ds.id))
        # return redirect(url_for('predict.result'))
    return render_template('predict/index.html', title='Cek', form=form)

@predict_bp.route('/predict/result/<int:id>')
def predicted(id):
    data = Dataset.query.get_or_404(id)
    return render_template('predict/result.html', title='Hasil', data=data)

@predict_bp.route('/predict/result')
def result():
    if session['predicted']:
        session.clear()
        return str(session['predicted'])
    else:
        return 'no session'
    # return render_template('predict/result.html', title='Hasil', data=data)