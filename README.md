## Explanation and Instruction of Our Project
# Description 
# Guidance
* Notebook for data analysis and data visualization: there is notebook called eda.ipynb. There are graphs and heatmap of data visualization.
* Run comment: "python ml_project_metaflow.py run" to train and test model in metaflow. From the console, you could see the MAE of the test data.
* Run comment: "streamlit run deploy.py" to show the user interface. It can shows the top 5 stock and bottom 5 stock by selecting a date. And it can show a stock price change by entering the stock id. You could play around here by adding values to get prediction or uploading files for prediction. But The uploaed file has to be have a right format. 
# Checklist
(1). Dataset
* This problem is suitable to be solve through machine learning model because it has training data which are all numerical, and then it can get a prediction by applying regression model.
* This dataset is provided from an investiment company called Optiver from Kaggle. So the dataset is large enough and trustworthy.
