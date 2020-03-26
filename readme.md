# Heart Disease Predictor using KNN Algorithm and Flask Micro Web Framework

Nothing.

## Requirements
* Python 3.6
* IDE (I use VScode)

## Set Up
* Create an virtual enviroment and make sure to run inside it
* Run   `pip install -r requirements.txt`
* Set the config.py for the database and etc.
* Create a database named `corpe`
* Place `heart.csv` inside `instance` directory or create the directory if not exist
* In python interpreter run
```python
    from corpe import db, create_app
    db.create_all(app=create_app())
```
## Run
Run this command and access the web app at `localhost:5000`
```bash
flask run
```
Access `localhost:5000/gen` to seed admin\
Access `localhost:5000/a` to seed datasets

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
