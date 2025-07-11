**🫀 Heart Disease Risk Prediction Using Machine Learning**
**📌 Project Overview**
This project aims to predict the risk of heart disease in individuals using machine learning models trained on the UCI Heart Disease dataset. It provides a simple and interactive Flask web application where users can input their medical information and get a prediction of whether they are at high or low risk.

**📊 Dataset Information**
The model is trained on the UCI Heart Disease dataset, which includes clinical parameters such as:

Age

Sex (Male/Female)

Chest Pain Type (ASY, NAP, ATA, TA)

Resting Blood Pressure

Cholesterol Level

Fasting Blood Sugar

Resting ECG Results

Maximum Heart Rate Achieved

Exercise-Induced Angina

ST Depression (Oldpeak)

ST Slope Type

![Dataset](https://github.com/sinchana1408/Heart-Disease-Risk-Predictor/blob/a7ca2aec553c3bb786e5d459ac82a3a285c67689/Screenshot%202025-07-11%20175246.png)


This cleaned dataset is widely used in healthcare machine learning research.

**🧠 Machine Learning Model**
A Decision Tree Classifier is used to train the model for binary classification:

0 → Low Risk

1 → High Risk

The model is saved as decision_tree_model.pkl using Python's pickle module.

**🖥️ Tech Stack**
Python (NumPy, scikit-learn, Flask)

HTML/CSS for frontend

Flask for backend web framework

Pickle for model serialization

**🚀 Features**
Interactive form to collect user medical data

Predict heart disease risk instantly

User-friendly interface

Clean and readable code structure

**⚙️ How to Run**
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the App:

bash
Copy
Edit
python app.py
Then open your browser at: http://127.0.0.1:5000

**📁 Folder Structure**

![Folder Structure](https://github.com/sinchana1408/Heart-Disease-Risk-Predictor/blob/6dedb5187b9ac1afff924e877f0a70170a415f6b/Screenshot%202025-07-11%20173245.png)

**Screenshots**
![Input](https://github.com/sinchana1408/Heart-Disease-Risk-Predictor/blob/6dedb5187b9ac1afff924e877f0a70170a415f6b/Screenshot%202025-07-11%20172819.png)

![Output](https://github.com/sinchana1408/Heart-Disease-Risk-Predictor/blob/6dedb5187b9ac1afff924e877f0a70170a415f6b/Screenshot%202025-07-11%20173111.png)


**🧾 License**
This project is open-source and available under the MIT License.
