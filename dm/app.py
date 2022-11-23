import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
import plotly.graph_objects as go

# read csv from local file
# df = pd.read_csv(r'/Users/pradeepbanjade/Desktop/bank.csv')
df = pd.read_csv(r'/Users/pradeepbanjade/Desktop/banjade/dm/bank.csv')



st.set_page_config(
    page_title = 'Real-Time Data Science Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time / Live Data Science Dashboard")

# top-level filters 

job_filter = st.selectbox("Select the Job", pd.unique(df['job']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df[df['job']==job_filter]

# near real-time / live feed simulation 

for seconds in range(2000):
#while True: 
    
    df['age_new'] = df['age'] * np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))
    df['age_new'] = df['age'] ### turn on to turn off real time data 

    # creating KPIs 
    avg_age = np.mean(df['age_new']) 

    count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))

    count_secondary = int(df[(df["education"]=='secondary')]['education'].count() + np.random.choice(range(1,30)))
    
    count_yes = int(df[(df["housing"]=='yes')]['housing'].count() + np.random.choice(range(1,30)))

    balance = np.mean(df['balance_new'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        

        # create two columns for charts 
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("###      Diversity of Marital status")
            fig1 = px.histogram(data_frame= df, x='marital')
            st.write(fig1)
        with fig_col2:
            st.markdown("###     Outliers in Balance column")
            fig2 = px.box(df, y="balance")
            #fig2 = px.histogram(data_frame = df, x = 'age_new')
            st.write(fig2)
        time.sleep(1)

    

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("###    Heat Map Graph")
            fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
            st.write(fig)
        with fig_col2:
            st.markdown("###     Histogram for Age")
            fig2 = px.histogram(data_frame = df, x = 'age_new')
            st.write(fig2)


        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("###    Scatter Plot")
            fig = px.scatter(data_frame=df, x = 'age_new', y = 'balance')
            st.write(fig)
        with fig_col2:
            st.markdown("###     Correlation Graph")
            #fig2 = px.histogram(data_frame = df, x = 'age_new')x
            df_corr = df.corr() # Generate correlation matrix

            fig2 = go.Figure()
            fig2.add_trace(
                go.Heatmap(
                    x = df_corr.columns,
                    y = df_corr.index,
                    z = np.array(df_corr)))

            st.write(fig2)

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("###      Bar chart for Education")
            fig1 = px.histogram(data_frame= df, x='education')
            st.write(fig1)
        with fig_col2:
            st.markdown("###     Bar chart for Housing")
            fig2 = px.histogram(data_frame = df, x = 'housing')
            st.write(fig2)





        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()
    


