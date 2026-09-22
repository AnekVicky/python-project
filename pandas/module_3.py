import pandas as pd

# descriptive methods in panda
data = {
    'employee_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'name': ['Anek', 'Vicky', None, 'Priya', 'Rahul', 'Neha', 'Arjun', None],
    'department': ['AI', 'ML', 'Data Science', None, 'Cloud', 'AI', 'HR', 'Finance'],
    'mission': ['Chatbot', 'Prediction Model', 'Analytics Dashboard', 'Deployment Pipeline', None, 'Vision System', 'Hiring Drive', 'Budget Planning'],
    'experience_years': [2, 4, None, 5, 1, 3, 6, None],
    'salary_lpa': [8.5, 12.0, 10.75, None, 6.25, 9.8, None, 11.4],
    'performance_score': [4.3, None, 4.1, 4.8, 3.9, None, 4.5, 4.0],
    'is_active': [True, True, False, True, None, True, False, None]
}

df = pd.DataFrame(data=data)
print(df.index)

#head
print(f'df.head \n{df.head()}')

#summary
print(f'df.summary \n{df.info()}')
print(f'df.describe.transpose \n{df.describe().T}')
print(f'df.value_count \n {df['is_active'].value_counts()}')

## Indexing and Slicing
##########################


print(f"df['name'] \n {df['name']}")





