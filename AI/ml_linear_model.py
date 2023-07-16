import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow

# import os
# print(os.getcwd())

df = pd.read_csv("AI_test.CSV")

print(df.head())

# x_train = ""
# y_train = ""

# x_val = ""
# y_val = ""

# mlflow_uri = ""
# mlflow.set_tracking_uri(mlflow_uri)

# # 코드로 mlflow exp를 생성한다. id를 반환한다.
# # target_exp_id = mlflow.create_experiment("exp1")

# target_exp_id = 0

# with mlflow.start_run(experiment_id=target_exp_id):
#     model = LinearRegression()
#     model.fit(x_train, y_train)
    
#     y_pred = model.predict(x_val)
    
#     rmse = mean_squared_error(y_val, y_pred,squared=False)
    
#     mlflow.log_metric("rmse", rmse)
#     mlflow.sklearn.log_model(model, "linear_model", registered_model_name="linear_model_test")
    