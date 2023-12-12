## Explanation and Instruction of Our Project
# Description 
# Guidance
* Notebook for data analysis and data visualization: there is notebook called eda.ipynb. There are graphs and heatmap of data visualization.
* Run comment: "python ml_project_metaflow.py run" to train and test model in metaflow. From the console, you could see the MAE of the test data.
* Run comment: "streamlit run deploy.py" to show the user interface. It can shows the top 5 stock and bottom 5 stock by selecting a date. And it can show a stock price change by entering the stock id. You could play around here by adding values to get prediction or uploading files for prediction. But The uploaed file has to be have a right format.
* 
# Checklist
(1) Dataset
* This problem is suitable to be solve through machine learning model because it has training data which are all numerical, and then it can get a prediction by applying regression model.
* This dataset is provided from an investiment company called Optiver from Kaggle. So the dataset is large enough and trustworthy.\

(2) EDA
* We explored the dataset and added more features according to the financial model.
* The impalanced feature between prices are more promising for our model. Because the prediction is mostly relied on the imbalanced data. \

(3) Data preparation
* We preprocessed data to remove the Nah and infinite data in the dataset.\

(4) Code Structure
* We well structured the metaflow and had comment for code instruction.
* We have our local virtual environment seperate from the other environment to make sure there is no conflict between dependencies.\

(5) Training and optimization
* Yes. The dataset is originally well splitted. So we don't need to worry about this problem.
* We picked the model from boosting library including CatBoost, XGBoost and LightXGB. Because this model are efficiency and robust.
* Yes. We included the validation procedure and used grid search to tune hyperparameters.\

(6) Tracking
* We added the comet to track the data right before the step(end). \

(7) Testing
* We picked MAE as the metrics which is suitable for this problem and regression problem.
* We've create qualitative test to check the general direction of price movement, for double checking.\

(8) Deployment
* We built a user interface by streamlit to show the graph of predictions. Also, user can make prediction by adding values or uploading csv files.\

(9) Environment
