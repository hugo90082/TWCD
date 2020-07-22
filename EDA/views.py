from django.shortcuts import render
from datetime import datetime
from EDA.models import EDAData
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from django.db import connection

# Create your views here.
def hello_view(request):
    gender = ["gender0","gender1"]
    genderDataFrame = pd.DataFrame()
    count = []
    gender0 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='0').count()
    gender1 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='1').count()

    count.append(gender0)
    count.append(gender1)
    genderDataFrame["gender"]=gender
    genderDataFrame["count"]=count

 
 
    with connection.cursor() as cursor:
        cursor.execute('SELECT date FROM EDAData GROUP by date')
        dataDate = cursor.fetchall()


    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
        'current_time': str(datetime.now()),
        'gender0': dataDate,
        # 'gender0': EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='0').count(),
        # 'gender1': EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='1').count(),
        # 'check_list': EDAData.objects.values_list('date', 'number', 'gender', 'age', 'edu', 'homeOwnership', 'job1', 'job2', 'job3', 'job4', 'industry1', 'industry2', 'industry3', 'industry4', 'industry5', 'CDLabel4Month').filter(date='2018/10/31'),
    })

def show(request):
    def scatter():

        gender = ["gender0","gender1"]
        gender_df = pd.DataFrame()
        count =[]
        gender0 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='0').count()
        gender1 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='1').count()
        count.append(gender0)
        count.append(gender1)
        gender_df["gender"]=gender
        gender_df["count"]=count


        fig = px.bar(gender_df, x="gender", y="count", title='10月性別圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }

    return render(request, 'welcome.html', context)