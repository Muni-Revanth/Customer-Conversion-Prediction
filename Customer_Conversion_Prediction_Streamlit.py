#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import warnings
warnings.filterwarnings("ignore")


# In[2]:


st.set_page_config(page_title="Customer Conversion Prediction", page_icon="pred.png", layout="centered")


# In[3]:


st.title("Customer Conversion Prediction")


# In[4]:


def predict_note_authentication(marital,call_type,day,mon,dur,num_calls,prev_outcome):   
    prediction=xggg.predict([[marital,call_type,day,mon,dur,num_calls,prev_outcome]])
    if prediction[0]==0:
        return "This customer has very less chance of conversion"
    else:
        return "This customer has a great chance to be converted"


# In[5]:


def main():
    html_temp = """
    <div style="background-color:black;padding:7px">
    <h2 style="color:grey;text-align:center;">Enter the required details</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.slider("AGE",0,100,step=1)
    job = st.number_input("JOB",0,10,step=1)
    marital = st.number_input("MARITAL",0,2,step=1)
    education_qual = st.number_input("EDUCATION QUAL",0,2,step=1)
    call_type = st.number_input("CALL TYPE",0,2,step=1)
    day = st.number_input("DAY",0,30,step=1)
    mon = st.number_input("MONTH",0,11,step=1)
    dur = st.number_input("DURATION",0,635,step=1)
    num_calls = st.number_input("NUM CALLS",0,15,step=1)
    prev_outcome = st.number_input("PREV OUTCOME",0,2,step=1)
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(marital,call_type,day,mon,dur,num_calls,prev_outcome)
        with st.spinner("Predicting..."):
            time.sleep(3)
        st.success(result)


# In[6]:


job = pd.read_csv("Job_Codes.csv")
job.set_index("Job Code", inplace=True)


# In[7]:


marital = pd.read_csv("Marital_Code.csv")
marital.set_index("Marital Code", inplace=True)


# In[8]:


education = pd.read_csv("Education_Qual.csv")
education.set_index("Education Code", inplace=True)


# In[9]:


calltype = pd.read_csv("Calltype.csv")
calltype.set_index("Call Type Code", inplace=True)


# In[10]:


month = pd.read_csv("Monthcode.csv")
month.set_index("Month Code", inplace=True)


# In[11]:


prev = pd.read_csv("prev_outcome.csv")
prev.set_index("Prev_Outcome Code", inplace=True)


# In[12]:


nav = st.sidebar.radio(label = "NAVIGATOR MENU",options=["Home","Predictor"])


# In[13]:


if nav=="Home":
    st.image("Insurance.jpg")
    st.write("The codes for various categories are listed below. Please refer to the codes and enter it in the Predictor page")
    col1, col2 = st.columns(2)
    with col1:
        if st.checkbox("Job Codes"):
            st.table(job)
        if st.checkbox("Marital Codes"):
            st.table(marital)
        if st.checkbox("Education Qualification Codes"):
            st.table(education)
        if st.checkbox("Call Type Codes"):
            st.table(calltype)
        if st.checkbox("Month Codes"):
            st.table(month)
        if st.checkbox("Previous Outcome Codes"):
            st.table(prev)
    with col2:
        st.image("encoding.png", width=200)


# In[14]:


if nav=="Predictor":
    st.image("insucover.jpeg")
    pickle_open = open("Cust_Conv_Pred.pkl","rb")
    xggg=pickle.load(pickle_open)
    if __name__=='__main__':
        main()


# In[ ]:




