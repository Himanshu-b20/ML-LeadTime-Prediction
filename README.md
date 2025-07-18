# ML Lead Time Prediction (Telecom Domain)

This project focuses on predicting the lead time required to complete a task using supervised machine learning techniques. It leverages structured features such as task name, product group, region, and other metadata to estimate how long a particular task might take from initiation to completion.

The pipeline includes preprocessing of categorical data, vectorization (e.g., using CountVectorizer), and model training using XGBoost algorithms.

This predictive system helps businesses streamline planning, allocate resources effectively, and reduce delays by providing accurate lead time estimates before execution begins.

## Techstack
- **Python**
- **Streamlit for frontend development**
- **XGBoost Algorithmn for Model training**


## Project Structure

- **main.py and prediction_helper.py**: Contains Streamlit and model prediction code.
- **notebooks and artifacts folder**: Contains all the jupyter notebook and required data. 
- **requirements.txt**: Lists the required Python packages.
- **artifact folder**: Contains the exported model as joblib file


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Himanshu-b20/ML-LeadTime-Prediction.git
   ```
2. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run the Streamlit app:**:   
   ```commandline
    streamlit run /main.py
   ```

## Stremlit UI

<img width="1823" height="1256" alt="image" src="https://github.com/user-attachments/assets/b05f1431-e0af-4587-8ed3-1a0ac12c8384" />

