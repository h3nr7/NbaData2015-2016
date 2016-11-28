import pandas as pd


points = pd.read_csv('NBApoints.csv')
salary = pd.read_csv('nbasalaries.csv')


points_salary_merge = points.merge(salary, on='Player', how='outer')

points_salary_merge.to_csv('nbasalariespoints.csv',encoding='utf-8')
