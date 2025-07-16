import joblib

MODEL_PATH='artifacts/model.joblib'

model_data = joblib.load(MODEL_PATH)
model = model_data['model']
count_vec = model_data['count_vec']

def predict_lt(data):
    data_count = count_vec.transform([data])
    p = model.predict(data_count)
    return p


