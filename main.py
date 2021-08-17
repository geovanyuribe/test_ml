from fastapi import FastAPI, Request
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import joblib
import pandas as pd

app = FastAPI()

@app.post("/predict")
async def get_body(request: Request):
    data = await request.json()
    data = pd.DataFrame(data)
    random_forest = joblib.load('models/random_forest.joblib')
    data['prediction'] = random_forest.predict(data)
    data = pd.DataFrame.to_dict(data)
    return {"prediction":data}

@app.post("/cluster")
async def get_body(request: Request):
    data = await request.json()
    data = pd.DataFrame(data)
    kmeans = joblib.load('models/kmeans.joblib')
    data_cluster = pd.read_csv('models/data_cluster.csv', index_col=0)
    data_cluster = data_cluster.append(data)
    data_cluster['Income_standar'] = StandardScaler().fit_transform(data_cluster[['Income']])
    data_cluster['Recency_standar'] = StandardScaler().fit_transform(data_cluster[['Recency']])
    data_cluster['DaysRegistered_standar'] = StandardScaler().fit_transform(data_cluster[['DaysRegistered']])
    data_cluster['AcceptedCmpAll_standar'] = StandardScaler().fit_transform(data_cluster[['AcceptedCmpAll']])
    data_cluster['MntTotal_standar'] = StandardScaler().fit_transform(data_cluster[['MntTotal']])
    pca = PCA(n_components=2)
    transform_pca = pca.fit_transform(data_cluster[['Income_standar', 'Recency_standar', 'DaysRegistered_standar','AcceptedCmpAll_standar', 'MntTotal_standar']])
    data_cluster['principal_feature1'] = transform_pca[:,0]
    data_cluster['principal_feature2'] = transform_pca[:,1]
    final_data_cluster = data_cluster[-len(data):]
    final_data_cluster['cluster'] = kmeans.predict(final_data_cluster[['principal_feature1', 'principal_feature2']])
    final_data_cluster = final_data_cluster.drop(columns=['Income_standar', 'Recency_standar', 'DaysRegistered_standar', 'AcceptedCmpAll_standar', 'MntTotal_standar'])
    final_data_cluster = pd.DataFrame.to_dict(final_data_cluster)
    return {"clustering":final_data_cluster}