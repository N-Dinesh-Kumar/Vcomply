

import datetime as dt
from datetime import datetime

li = [
      {emp_id: 1, leaveFrom: 14-12-2020, leaveUpto: 18-12-2020},
      {emp_id: 3, leaveFrom: 22-12-2020, leaveUpto: 24-12-2020},
     {emp_id: 7, leaveFrom: 27-12-2020, leaveUpto: 30-12-2020},
     {emp_id: 29, leaveFrom: 02-12-2020, leaveUpto: 10-12-2020},
     {emp_id 45, leaveFrom: 24-02-2021, leaveUpto: 17-03-2021}
     ]

reqlev = { leaveFrom: 19-12-2020, leaveUpto : 20-12-2020}

arr = []
for i in li:
    st = datetime.strptime(i["leaveFrom"], '%d-%m-%y').date()
    en = datetime.strptime(i["leaveUpto"], '%d-%m-%y').date()
    arr.append([st,en])
    
flag = 0

for i in arr:
    if(reqlev['leaveFrom']>=i[0] and reqlev['leaveFrom']<=i[1]):
        print("Can't be approved")
        flag = 1
        break
    
if(flag==0):
    print("Leave can be approved")
