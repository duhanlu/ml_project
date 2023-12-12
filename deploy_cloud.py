import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

df = pd.read_csv('validation_data0.csv')
st.title("Stock Price Movement Prediction")
tab1, tab2 = st.tabs(["Display", "Prediction"])

### First Tab
with tab1:
   st.header("Display of The Stock Trend")
   st.subheader('The Ranking of Stocks',divider = 'rainbow')
   csv_path = 'new_test_data.csv'
   data = pd.read_csv(csv_path, dtype={'stock_id': int})

   # Filter data for 'seconds_in_bucket' equal to 540
   filtered_data = data[data['seconds_in_bucket'] == 540]
   # Date selector
   selected_date = st.selectbox('Choose Date', filtered_data['date_id'].unique())
   # Get data for the selected date
   selected_data = filtered_data[filtered_data['date_id'] == selected_date]
   # Get the Top 5 and Bottom 5 stocks
   top_stocks = selected_data.nlargest(5, 'predicted_target')[['stock_id', 'predicted_target']]
   bottom_stocks = selected_data.nsmallest(5, 'predicted_target')[['stock_id', 'predicted_target']]
   # Convert 'stock_id' to integer
   top_stocks['stock_id'] = top_stocks['stock_id'].astype(int)
   bottom_stocks['stock_id'] = bottom_stocks['stock_id'].astype(int)
   # Create a two-column layout
   col1, col2 = st.columns(2)

   def generate_table_html(df, header_color):
            # Generate an HTML table
            table_html = f"<table style='width:100%; border-collapse: collapse;'><thead style='background-color:{header_color};color:white'>"
            for col in df.columns:
                table_html += f"<th style='border: 1px solid black; padding: 8px;'>{col}</th>"
            table_html += "</thead><tbody>"
            for i, row in df.iterrows():
                table_html += "<tr>"
                for val in row:
                    table_html += f"<td style='border: 1px solid black; padding: 8px; background-color: white; color: black;'>{val}</td>"
                table_html += "</tr>"
            table_html += "</tbody></table>"
            return table_html

        # Display the Top 5 stocks
   with col1:
            st.subheader('Top 5 Stocks')
            st.markdown(generate_table_html(top_stocks, "green"), unsafe_allow_html=True)

        # Display the Bottom 5 stocks
   with col2:
            st.subheader('Bottom 5 Stocks')
            st.markdown(generate_table_html(bottom_stocks, "red"), unsafe_allow_html=True)
        
   st.subheader('Select a stock to check how does it change recently!', divider='rainbow')
   input = st.number_input("Insert Stock ID", value=1, placeholder="Type stock ID...")
   st.write('The current selection: ', input)
   value_to_filter = [0,100,200,300,400,500]
   selected_rows = df[df['stock_id'] == input]
   selected_rows = selected_rows[selected_rows['date_id'] == 479]
   #selected_rows = selected_rows[selected_rows['seconds_in_bucket'].isin(value_to_filter)]
   print(selected_rows)
   chart_data = pd.DataFrame(selected_rows,columns=['seconds_in_bucket','predictions','revealed_target'])

   st.line_chart(chart_data,x='seconds_in_bucket',y=['predictions'])