from flask import (Flask, render_template, flash, Blueprint,
                    current_app, url_for, request, redirect,
                    make_response)
from corpe import db
from corpe.models import Dataset
from corpe.predict.forms import PredictForm
from corpe.predict.knn import knn

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/a')
def a():
    """ Endpoint to create datasets"""
    ds = Dataset(age=50, sex=2, cp=1, target=0)
    db.session.add(ds)
    db.session.commit()
    return make_response("Dataset created!")

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