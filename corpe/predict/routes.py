from flask import (Flask, render_template, flash, Blueprint,
                   current_app, url_for, request, redirect,
                   make_response, session, abort)
from corpe import db
from corpe.models import Dataset
from corpe.predict.forms import PredictForm
from corpe.predict.knn import knn
import csv

# create blueprint
predict_bp = Blueprint('predict', __name__)

# route to generate dataset into database


@predict_bp.route('/gen-ds')
def generate_dataset():
    """ Endpoint to create datasets"""
    # if dataset was created
    if len(Dataset.query.all()) >= 303:
        # abort to 404
        abort(404)
    with open(current_app.instance_path+'/heart.csv', newline='') as csvfile:
        # read csv file
        heart_csv = csv.reader(csvfile)
        # skip the first row which a variable name
        next(heart_csv)
        # loop and add to session
        for row in heart_csv:
            data = Dataset(age=row[0], sex=row[1], cp=row[2], trestbps=row[3], chol=row[4],
                           fbs=row[5], restecg=row[6], thalach=row[7], exang=row[8], oldpeak=row[9],
                           slope=row[10], ca=row[11], thal=row[12], target=row[13])
            db.session.add(data)
    # commit and show basic response
    db.session.commit()
    return make_response('Dataset created')

# route to heart dissease prediction


@predict_bp.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    this function to get data and then post the data processing knn
    """
    # create instance PredictForm
    form = PredictForm()
    # form successful submitted
    if form.validate_on_submit():
        # load data on an array 'data'
        data = [form.age.data, form.sex.data, form.cp.data, form.trestbps.data,
                form.chol.data, form.fbs.data, form.restecg.data, form.thalach.data,
                form.exang.data, form.oldpeak.data, form.slope.data, form.ca.data, form.thal.data]
        # predict using knn module and get target result assign to 'result'
        result = knn(data)
        # dummy data
        # row = [572,1,1,154,232,0,0,164,0,0,2,1,2]
        # process to database
        ds = Dataset(age=data[0], sex=data[1], cp=data[2], trestbps=data[3], chol=data[4],
                     fbs=data[5], restecg=data[6], thalach=data[7], exang=data[8], oldpeak=data[9],
                     slope=data[10], ca=data[11], thal=data[12], target=str(result))
        db.session.add(ds)
        db.session.commit()
        session['predicted'] = ds.id
        # flash message and redirect to result page
        flash('Hore', 'success')
        # return redirect(url_for('predict.predicted', id=ds.id))
        return redirect(url_for('predict.result'))
    # route get
    return render_template('predict/predict.html', title='Cek', form=form)


@predict_bp.route('/predict/result')
def result():
    """
    show result of prediction
    """
    # catch error if session['predicted'] unset
    try:
        # get data by id(session['predicted'])
        result = Dataset.query.get(session['predicted'])
    except Exception as e:
        # redirect to home page
        return redirect(url_for('main.index'))
    return render_template('predict/result.html', title='Hasil', data=result)
