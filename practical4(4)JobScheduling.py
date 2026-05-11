jobs = [('J1',100), ('J2',50), ('J3',150)]

jobs.sort(key=lambda x:x[1], reverse=True)

print("Job Order:")

for job in jobs:
    print(job[0], job[1])