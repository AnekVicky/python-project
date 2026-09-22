import numpy as np
import pandas as pd

#df = pd.read_csv("./data/anek_vicky_data.csv")

# way 1
data = {
    'Name':['Anek','Vicky'],
    'Age': [35,36],
    'Course': ['AI','ML']
}
df = pd.DataFrame(data=data)
print(df)


# way 2
print("="*30+"way2")
data = [
    #pd.Series(['Anek',10,'AI']),
    pd.Series(['Vicky',20,'ML'],index=['name','count','course'])
]
df = pd.DataFrame(data=data)#,columns=['name','count','course'])
print(df)

s1 = pd.Series([10, 20], index=['A', 'B'])
s2 = pd.Series([100, 200], index=['B', 'C'])

print(s1,s2)

# way3
print("="*30+"way3")
data = [
    ['Anek',10,'AI',10000.0],
    ['Vicky',np.nan,'ML',999000.9],
    ['Sameer', 40, 'CS',None]
]
df = pd.DataFrame(data=data,columns=['name','count','course','salay'])
print(df)

print(df.dtypes)
print(df.index)

## Missing value force it float

# descriptive methods in panda

data = {
    'employee_id': [101, 102, 103, 104],
    'name': ['Anek', 'Vicky', 'Ravi', 'Priya'],
    'department': ['AI', 'ML', 'Data Science', 'Cloud'],
    'mission': ['Chatbot', 'Prediction Model', 'Analytics Dashboard', 'Deployment Pipeline'],
    'experience_years': [2, 4, 3, 5],
    'salary_lpa': [8.5, 12.0, 10.75, 15.25],
    'performance_score': [4.3, 4.6, 4.1, 4.8],
    'is_active': [True, True, False, True]
}

df = pd.DataFrame(data=data)
print(df.index)


