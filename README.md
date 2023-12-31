## Explanation and Instructions of Our Project
# Description 
Stock exchanges are fast-paced, high-stakes environments where every second counts. The intensity escalates as the trading day approaches its end, peaking in the critical final ten minutes. These moments, often characterised by heightened volatility and rapid price fluctuations, play a pivotal role in shaping the global economic narrative for the day. Each trading day on the Nasdaq Stock Exchange concludes with the Nasdaq Closing Cross auction. This process establishes the official closing prices for securities listed on the exchange. These closing prices serve as key indicators for investors, analysts and other market participants in evaluating the performance of individual securities and the market as a whole.

The goal of this project is to **develop a model capable of predicting the closing price movements for hundreds of Nasdaq listed stocks using data from the order book and the closing auction of the stock**. Information from the auction can be used to adjust prices, assess supply and demand dynamics, and identify trading opportunities.

# Guidance
* **Data**: Find in the folder *<ins>CSV</ins>*. Three data files for our projects: *<ins>train.csv*</ins>, *<ins>test.csv*</ins>, *<ins>revealed_targets.csv*</ins>.
  （📒 The train.csv is too large that you can see the file in this google dirve link: https://drive.google.com/file/d/1JyCTNr8rMrCxhV0K6KCsW62foBr056tq/view?usp=drive_link）
* **EDA**:  *<ins>eda.ipynb</ins>* detailedly analyze three .csv files we used for our project. There are also graphs and heatmap of data visualization.
* **Metaflow and Comet**:
  * Find in *<ins>project_metaflow.py</ins>*. `python ml_project_metaflow.py run` to train the test model and predict in metaflow. From the console, you could see the MAE of the test data.
  * There is a step in this flow which will upload the results to commet. You can see the dashboard screenshot named *<ins>commet_dashboard_screenshot.png</ins>*.
* **Streamlit**: Find in *<ins>deploy.py</ins>*. Run `streamlit run deploy.py` to show the user interface. It has the following functions:
  * 1️⃣ top 5 stock and bottom 5 stock by selecting a date;
  * 2️⃣ stock price change graph by entering the stock id;
  * 3️⃣ adding values to get prediction for the specific stock, date and second;
  * 4️⃣ uploading files for prediction（📒 the uploaed file has to be in a right format, you could use assertion_data.csv or assertion_data_1.csv for now).
* **Demo**: Visit url: https://ml7773projectdeploy.streamlit.app/ for the cloud demonstration of it. Or you can run the deploy.py file to check the demo.
* **Slides**：Find in *<ins>presentation_slides.pdf</ins>*.

# Checklist
(1) Dataset
* This problem is suitable to be solve through machine learning model because it has training data which are all numerical, and then it can get a prediction by applying regression model.
* This dataset is provided from an investiment company called Optiver from Kaggle. So the dataset is large enough and trustworthy.

(2) EDA
* We explored the dataset and added more features according to the financial model.
* Our model is doing prediction, data imbalance and augmentation do not apply.

(3) Data preparation
* We preprocessed data to remove the Nah and infinite data in the dataset.

(4) Code Structure
* We well structured the metaflow and had comment for code instruction.
* We have our local virtual environment seperate from the other environment to make sure there is no conflict between dependencies.

(5) Training and optimization
* Yes. The dataset is originally well splitted. So we don't need to worry about this problem.
* We picked the model from boosting library including CatBoost, XGBoost and LightXGB. Because this model are efficiency and robust.
* Yes. We included the validation procedure and used grid search to tune hyperparameters.

(6) Tracking
* We added the comet to track the data right before the step(end). 

(7) Testing
* We picked MAE as the metrics which is suitable for this problem and regression problem.
* We've create qualitative test to check the general direction of price movement, for double checking.

(8) Deployment
* We built a user interface by streamlit to show the graph of predictions. Also, user can make prediction by adding values or uploading csv files.

(9) Environment
* We've created the **.lock** and **requirement.txt** files for user to update the computer environment to run our project. 
