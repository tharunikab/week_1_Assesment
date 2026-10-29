import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

student_marks = np.array([90,95,94,90,99,97,92,94])
print("Student Average: {}".format(student_marks.mean()))

departments_content = """department,head,budget
Sales,Alice,500000
HR,Bob,300000
IT,Charlie,800000
Finance,David,400000
Marketing,Eve,200000"""

with open("departments.csv", "w", encoding="utf-8") as f:
    f.write(departments_content)

employees_content = """id,name,department,salary,city
1,Ajay,Sales,30000,Chennai
2,Agaran,HR,45000,Chennai
3,Sarath,IT,60000,Odisa
4,Tharu,IT,75000,Chennai
5,Kiruthik,Finance,90000,kolkata
6,Monisha,Sales,52000,Bangalore
7,Santhosh,IT,68000,Chennai
8,Yalini,HR,48000,Pune"""

with open("employees.csv", "w", encoding="utf-8") as f:
    f.write(employees_content)

df_emp = pd.read_csv("employees.csv")
df_dept = pd.read_csv("departments.csv")

df_emp.columns = df_emp.columns.str.strip()
df_dept.columns = df_dept.columns.str.strip()

grouped = df_emp.groupby("department").agg(
    headcount=("name", "count"),
    avg_salary=("salary", "mean")
).reset_index()

hc_sales = grouped.loc[grouped["department"] == "Sales", "headcount"].values[0]
hc_hr = grouped.loc[grouped["department"] == "HR", "headcount"].values[0]
hc_it = grouped.loc[grouped["department"] == "IT", "headcount"].values[0]
hc_finance = grouped.loc[grouped["department"] == "Finance", "headcount"].values[0]

print("HEADCOUNT: Sales {} | HR {} | IT {} | Finance {}".format(hc_sales, hc_hr, hc_it, hc_finance))

out_merge = pd.merge(df_emp, df_dept, on="department", how="outer")
empty_dept = out_merge[out_merge["id"].isna()]["department"].values[0]
print("Outer join: {} department with no employees listed".format(empty_dept))

plt.figure(figsize=(6, 4))
plt.bar(grouped["department"], grouped["headcount"], color='pink', label='Headcount')
plt.title("EMPLOYEE HEADCOUNT PER DEPARTMENT")
plt.xlabel("Department")
plt.ylabel("Headcount")
plt.legend()
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

plt.figure(figsize=(6,4))
plt.hist(df_emp["salary"], bins=5, color='lightgreen', edgecolor='black', label='Salary Frequency')
plt.title("SALARY DISTRIBUTION OVERVIEW")
plt.xlabel("Salary Ranges")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("histogram_chart.png")
plt.close()

plt.figure(figsize=(6,4))
plt.scatter(df_emp["id"], df_emp["salary"], color='coral', label='Employee Level')
plt.title("EMPLOYEE ID VS SALARY LEVELS")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("scatter_chart.png")
plt.close()

plt.figure(figsize=(6, 4))
plt.plot(grouped["department"], grouped["avg_salary"], marker='o', color='purple', label='Avg Salary')
plt.title("AVERAGE DEPARTMENTAL SALARIES")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()