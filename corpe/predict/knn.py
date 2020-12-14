'''
KNN
'''

import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


def knn(data):
    '''
    K-Nearest Neighbors
    '''
    sql_engine = create_engine(
        'postgres://yteqsluiclaqqf:a68ff5634a2c9998a11a0bdf8086a48a9cfba042c80acda300c0d991bd4c5d60@ec2-52-206-15-227.compute-1.amazonaws.com:5432/dbuu5r7mpfu1re')

    db_connection = sql_engine.connect()

    dataset = pd.read_sql("select * from datasets", db_connection)

    pd.set_option('display.expand_frame_repr', False)

    # Lori: 1:-1 remove id from db and jump to age and next
    train_feature = dataset.iloc[:, 1:-1].values
    target = dataset.iloc[:, 14].values

    # Scaling and it uses Z-Score
    scaler = StandardScaler()
    scaler.fit(train_feature)
    # Scaling the dataset feature
    train_scaled = scaler.transform(train_feature)
    # user input
    test_input = np.array(data).reshape(1, -1)
    # Scaling the dataset feature
    test_input_scaled = scaler.transform(test_input)

    # PCA WORKS
    # Make an instance of the Model
    pca = PCA(2)
    # FIT the train set only
    pca.fit(train_scaled)
    # Transform pca to train and test
    train_pca = pca.transform(train_scaled)
    test_input_pca = pca.transform(test_input_scaled)

    # Set the KNN and the K with PCA
    classifier = KNeighborsClassifier(n_neighbors=7)
    classifier.fit(train_pca, target)
    # Scoring
    # result=classifier.score(train_pca, target)
    # Prediction
    result = classifier.predict(test_input_pca)

    # # Show result

    return result[0]
