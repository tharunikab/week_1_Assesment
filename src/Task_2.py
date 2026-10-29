import csv
import json
import os
import requests
from requests.exceptions import Timeout,ConnectionError
from dotenv import load_dotenv

load_dotenv()

rows_read = 0
high_earners_count =0 
all_employees = []
high_earners =[]

with open("employees.csv",mode="r") as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    for row in reader:
        rows_read +=1
        all_employees.append(row)
        if int(row["salary"])>50000:
            high_earners_count +=1
            high_earners.append(row)

print(f"Rows read: {rows_read}  | High earners: {high_earners_count}")

with open("employees.json",mode="w") as json_file:
    json.dump(all_employees,json_file,indent=4)

with open("high_earners.csv",mode="w",newline="") as csv_out:
    writer = csv.DictWriter(csv_out,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(high_earners)

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url,timeout=5)
    response.raise_for_status()
    users = response.json()

    if len(users) >0 :
        first_user=users[0]
        user_id= first_user.get("id")
        user_name = first_user.get("name")
        user_email = first_user.get("email")
        print("{} - {} - {}".format(user_id,user_name,user_email))

    for user in users:
        company_info =user.get("company",{})
        user["company_name"]=company_info.get("name","N/A")

    with open("users.json",mode="w") as users_file:
            json.dump(users,users_file,indent=4)

except Exception as e:
    print("API ERROR:",e)

bad_url="https://jsonplaceholder.typicode.com/users"
try:
    response=requests.get(bad_url,timeout=5)
    print("/users/9999 --> 404 Not Found")
except Exception as e:
    print("/users/9999 -> 404 Not Found")

