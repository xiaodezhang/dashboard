from mydashboard.models import person,people,waiter_info,area_management,cash_terminal,
     shipping_info
            
import random
import re

"""
people_name = []
with open('people_name.txt','rt') as f:
    data = re.split(',|\n',f.read())
    for d in data:
        dl = d.lstrip()
        people_name.append(dl)

for name in people_name:
    aperson = people(name = name,phone_number = random.randrange(12100000000,18900000000),sex = random.choice(['fe','male']))
    aperson.save()

"""

"""
people_name = []
with open('people_name.txt','rt') as f:
    data = re.split(',|\n',f.read())
    for d in data:
        dl = d.lstrip()
        people_name.append(dl)

for name in people_name[:200]:
    aperson = person(name = name,phone_number = random.randrange(12100000000,18900000000),sex = random.choice(['fe','male']))
    aperson.save()
    aperson.waiter.create(waiter_number = aperson.phone_number)
"""


"""
areas = ['A','B','C','D']
desk_numbers = [2,2,2,2,2,2,2,2,2,2,
                4,4,4,4,4,4,4,
                6,6,6,6,6,
                8,8,8,8,
                10,10,10,
                12,12,
                14,14,
                16,16]
for j in range(4):
    for i in range(8):
        area = area_management(area_name = areas[j],desk_number = i,
                                    area_customers_sum = random.choice(desk_numbers))
        area.save()
"""

"""
models = ['A','B','C','D']
for i in range(20):
    cash = cash_terminal(cash_terminal_model = random.choice(models)+str(random.randrange(0,10))+str(random.randrange(0,10))+str(random.randrange(0,10))+str(random.randrange(0,10)))
    cash.save()
"""

"""
shipping_status = ['配送中','已送达','已接单']
shipping = shipping_info(status = random.choice(shipping_status),sender = )
"""
