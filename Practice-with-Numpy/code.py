# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_records = np.array(new_record)

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data, new_records))

age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = round(np.mean(age),2)
age_std = round(np.std(age),2)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

race0,race1,race2,race3,race4 = [], [], [], [], []
for i in census:
    if(i[2] == 0):
        race0.append(i)
    elif(i[2] == 1):
        race1.append(i)
    elif(i[2] == 2):
        race2.append(i)
    elif(i[2] == 3):
        race3.append(i)
    elif(i[2] == 4):
        race4.append(i)
    

race_0 = np.array(race0)
race_1 = np.array(race1)
race_2 = np.array(race2)
race_3 = np.array(race3)
race_4 = np.array(race4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = 3

seniors = []

for i in census:
    if(i[0] > 60):
        seniors.append(i)

senior_citizens = np.array(seniors)

working_hours_sum=0
for j in senior_citizens:
    working_hours_sum += j[6] 
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)

avg_working_hours = round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)

ed_high, ed_low = [],[]

for i in census:
    if(i[1]>10):
        ed_high.append(i)

for j in census:
    if(j[1]<=10):
        ed_low.append(j)

high = np.array(ed_high)
low = np.array(ed_low)

pay_high_sum = 0
for i in high:
    pay_high_sum += i[7]

avg_pay_high = pay_high_sum/len(high)
print(round(avg_pay_high,2))

pay_low_sum = 0

for j in low:
    pay_low_sum += j[7]

avg_pay_low = pay_low_sum/len(low)

print(round(avg_pay_low,2))


