import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

def knn(data):
    if data[0] % 2 == 0:
        return 1
    return 0

def knns(data):
    sqlEngine        = create_engine('mysql+pymysql://root:root@localhost/heart')

    dbConnection    = sqlEngine.connect()

    dataset           = pd.read_sql("select * from heart.datasets", dbConnection);

    pd.set_option('display.expand_frame_repr', False)

    # Lori: 1:-1 remove id from db and jump to age and next
    train_feature = dataset.iloc[:, 1:-1].values
    target = dataset.iloc[:, 14].values

    # Scaling
    scaler = StandardScaler()
    scaler.fit(train_feature)
    # Scaling the dataset feature
    train_scaled = scaler.transform(train_feature)
    # user input
    test_input=np.array(data).reshape(1,-1)
    # Scaling the dataset feature
    test_input_scaled = scaler.transform(test_input)

    # PCA WORKS
    # Make an instance of the Model
    pca = PCA(.95)
    # FIT the train set only
    pca.fit(train_scaled)
    # Transform pca to train and test
    train_pca = pca.transform(train_scaled)
    test_input_pca = pca.transform(test_input_scaled)

    # Set the KNN and the K with PCA
    classifier = KNeighborsClassifier(n_neighbors=4)
    classifier.fit(train_pca, target)
    result=classifier.score(train_pca, target)
    # Prediction
    result=classifier.predict(test_input_pca)

    # # Show result

    return result[0]