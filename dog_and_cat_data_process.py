#!/usr/bin/env python
# coding: utf-8

# In[16]:


from chart_studio import plotly as py
import pandas as pd
import plotly.io as pio


# In[2]:


import requests
import json
import csv
import plotly.graph_objs as go
import numpy as np
import plotly.express as px


# # All cat data 

# In[3]:


states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


# In[3]:


CLIENT_ID = "qpTmdgMQYrqLy2gjZ5BdVOoJiIEqtebaxrNCKhq1NWDTQizBJc"
CLIENT_SECRET = "6XmxIyvmAgZ9teC2AeJithx0qH0lnnaETrgkXPQb"
# token_json = !curl -d "grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}" https://api.petfinder.com/v2/oauth2/token


# In[21]:


CLIENT_ID = "6V6qjgwiK6c8fz66nBrhwNqlMtUURhuLqMxfhbS20O9KcWt4vG"
CLIENT_SECRET = "SbLL3KPrnHjnlWaldOxNVk9CEgUN9Y5Jijh8SB5y"


# In[ ]:


6V6qjgwiK6c8fz66nBrhwNqlMtUURhuLqMxfhbS20O9KcWt4vG


# In[22]:


in_val = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
url = "https://api.petfinder.com/v2/oauth2/token"
res = requests.post(url, data=in_val)
# res.status_code
ACCESS_TOKEN = res.json()['access_token']
# ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJLUmM4NTlrZlk3ZnNKSUxxZXlUZW90d1JxbFl3bThNRW5CTVNWUXQ0WmttZFNpZjlaSSIsImp0aSI6IjA4YTAyMDJmZmQ4NGE4NDFjZDVhZTU0MGVmZWZkMTU4YjM3MjFiMTlmMWEzNjQzZmE1MjFmYTZkNDUxMjFmODEwMjNlY2RkMTZjNjVlMTQxIiwiaWF0IjoxNjc3MTEzNjQ1LCJuYmYiOjE2NzcxMTM2NDUsImV4cCI6MTY3NzExNzI0NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.XT6THra8P6scb1l083ykPuMvJ4PXbUsQm0fUXvE5wPCWRnMx5ux0WXYGx6A1v5fwMYH75GDnz_gfmUFI8nmzrgK3LoF9lTinLNTteTcQqV26z0MBrdFi2Eld93YZZSV6nH0tdtaqdpG-aoqWbz0RCjBTIf347DPDMjCHdm0O28tjJXs2Ch7bNv_89wjZ0qdW-wEmJEvv4BD7lZhd7VqmOU2EmBlDs3OnJq0NtNJnFyf90rYbxMEGwo1hst_V41X7ONYTf88Wws43nY4POtyuScK0Rt3Pzl83-BcaVM__hJ8x_p3Z0MJqBDhj9tsg4dJy_FEO2h2a5nCM5PGu5_bf-w"


# In[23]:


# payload={'type':"cat","breeds":"",'location':'NJ'}
url = "https://api.petfinder.com/v2/types/cat/breeds"
header = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
response = requests.get(url, headers = header)
types=response.json()['breeds']
cat_breeds = [t['name'] for t in types]


# In[71]:


url = "https://api.petfinder.com/v2/animals"
cat_breed_count = {}
for loc in states:
    #for b in cat_breeds:
    payload={'type':"Cat","breed":'Domestic Short Hair','location':loc}
    response = requests.get(url, headers = header,params=payload)
    cat_breed_count[loc]=response.json()['pagination']['total_count']


# In[46]:


cat_breed_count


# In[109]:


df['text']


# In[ ]:





# In[14]:


url = "https://api.petfinder.com/v2/animals"
total_cat = {}
for s in states:
    total_cat[s] = {}
for loc in states:
    for b in cat_breeds:
        payload={'type':"Cat","breed":b,'location':loc}
        response = requests.get(url, headers = header,params=payload)
        total_cat[loc][b]=response.json()['pagination']['total_count']


# In[15]:


total_cat


# In[32]:


sorted_cat = {}
for s in states:
    #print(total_cat[s].items())
    sorted_cat[s] = sorted(total_cat[s].items(), key=lambda x:x[1], reverse = True)
sorted_cat


# In[72]:


total_count_per_state = {}
for state in states:
    total = 0
    for k,v in sorted_cat[state]:
        total += v
    total_count_per_state[state] = total
total_count_per_state


# In[36]:


top5_cat_per_states = {}
ranks = ['top1','top2','top3','top4','top5']
for r in ranks:
    top5_cat_per_states[r]=[]
for state in states:
    i=0
    for k,v in sorted_cat[state]:
        top5_cat_per_states[ranks[i]].append(k)
        i+=1
        if i==5: break


# In[50]:


for r in ranks:
    l = len(top5_cat_per_states[r])
    for i in range(l,51):
        top5_cat_per_states[r].append(" ")


# In[112]:


top5_cat_per_states


# Day2 Data 

# In[10]:


states2 = [ 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


# In[8]:


url = "https://api.petfinder.com/v2/animals"
total_cat2 = {}
for s in states2:
    total_cat2[s] = {}
for loc in states2:
    for b in cat_breeds:
        payload={'type':"Cat","breed":b,'location':loc}
        response = requests.get(url, headers = header,params=payload)
        total_cat2[loc][b]=response.json()['pagination']['total_count']


# In[11]:


sorted_cat2 = {}
for s in states2:
    #print(total_cat[s].items())
    sorted_cat2[s] = sorted(total_cat2[s].items(), key=lambda x:x[1], reverse = True)
sorted_cat2


# In[12]:


total_count_per_state2 = {}
for state in states2:
    total = 0
    for k,v in sorted_cat2[state]:
        total += v
    total_count_per_state2[state] = total
total_count_per_state2


# In[11]:


top5_cat_per_states2 = {}
ranks = ['top1','top2','top3','top4','top5']
for r in ranks:
    top5_cat_per_states2[r]=[]
for state in states2:
    i=0
    for k,v in sorted_cat2[state]:
        top5_cat_per_states2[ranks[i]].append(k)
        i+=1
        if i==5: break


# In[12]:


top5_cat_per_states2


# Day3 Data

# In[15]:


states3 = [ 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


# In[16]:


url = "https://api.petfinder.com/v2/animals"
total_cat3 = {}
for s in states3:
    total_cat3[s] = {}
for loc in states3:
    for b in cat_breeds:
        payload={'type':"Cat","breed":b,'location':loc}
        response = requests.get(url, headers = header,params=payload)
        total_cat3[loc][b]=response.json()['pagination']['total_count']


# In[17]:


sorted_cat3 = {}
for s in states3:
    #print(total_cat[s].items())
    sorted_cat3[s] = sorted(total_cat3[s].items(), key=lambda x:x[1], reverse = True)
sorted_cat3


# In[13]:


url = "https://api.petfinder.com/v2/animals"
payload={'type':"Cat","breed":"Tuxedo",'location':'AR'}
response = requests.get(url, headers = header,params=payload)
temp=response.json()['pagination']


# In[14]:


temp


# In[18]:


total_count_per_state3 = {}
for state in states3:
    total = 0
    for k,v in sorted_cat3[state]:
        total += v
    total_count_per_state3[state] = total
total_count_per_state3


# In[19]:


top5_cat_per_states3 = {}
ranks = ['top1','top2','top3','top4','top5']
for r in ranks:
    top5_cat_per_states3[r]=[]
for state in states3:
    i=0
    for k,v in sorted_cat3[state]:
        top5_cat_per_states3[ranks[i]].append(k)
        i+=1
        if i==5: break


# In[20]:


top5_cat_per_states3


# Day4

# In[52]:


states4 = ['WV', 'WY']


# In[53]:


url = "https://api.petfinder.com/v2/animals"
total_cat4 = {}
for s in states4:
    total_cat4[s] = {}
for loc in states4:
    for b in cat_breeds:
        payload={'type':"Cat","breed":b,'location':loc}
        response = requests.get(url, headers = header,params=payload)
        total_cat4[loc][b]=response.json()['pagination']['total_count']


# In[54]:


sorted_cat4 = {}
for s in states4:
    #print(total_cat[s].items())
    sorted_cat4[s] = sorted(total_cat4[s].items(), key=lambda x:x[1], reverse = True)
sorted_cat4


# In[55]:


total_count_per_state4 = {}
for state in states4:
    total = 0
    for k,v in sorted_cat4[state]:
        total += v
    total_count_per_state4[state] = total
total_count_per_state4


# In[56]:


top5_cat_per_states4 = {}
ranks = ['top1','top2','top3','top4','top5']
for r in ranks:
    top5_cat_per_states4[r]=[]
for state in states4:
    i=0
    for k,v in sorted_cat4[state]:
        top5_cat_per_states4[ranks[i]].append(k)
        i+=1
        if i==5: break
top5_cat_per_states4


# In[ ]:





# # All dog data

import requests
import json
import csv
import plotly.graph_objs as go
import numpy as np
import plotly.express as px
from collections import defaultdict


# In[4]:


states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


# In[159]:


#Yu1
CLIENT_ID = "qpTmdgMQYrqLy2gjZ5BdVOoJiIEqtebaxrNCKhq1NWDTQizBJc"
CLIENT_SECRET = "6XmxIyvmAgZ9teC2AeJithx0qH0lnnaETrgkXPQb"
# token_json = !curl -d "grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}" https://api.petfinder.com/v2/oauth2/token


# In[166]:


#Yu2
CLIENT_ID = "6V6qjgwiK6c8fz66nBrhwNqlMtUURhuLqMxfhbS20O9KcWt4vG"
CLIENT_SECRET = "SbLL3KPrnHjnlWaldOxNVk9CEgUN9Y5Jijh8SB5y"


# In[173]:


#Yu3
CLIENT_ID = "ob0i8VtHIq7HNvqZMyj4tvLX5N2azyrujhmKxLLEq4lQ4TofuP"
CLIENT_SECRET = "cVKJZqfDRqNWhGtfnbBjkKdKdsRy7g4VxoTQ1hof"


# In[180]:


#colin1
CLIENT_ID = "4MyAPYLZzT39Mg2uWdPr81OcAl0p6HvIxQMSeDdPXo8NfB4fdz"
CLIENT_SECRET = "50FpLw3MoR3c704a0DeAX5UaAg9JVM1eaOL9Fpqy"


# In[152]:


#colin2
CLIENT_ID = "N3h2pTlFHWuzoomZ7vQigj2PxjdV6r9jMDGLaxmo6twv2m4aLz"
CLIENT_SECRET = "XshtEhHdsoh4quFMvc9WhuB1u7hCmjOzhCFzKfvI"


# In[181]:


in_val = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
url = "https://api.petfinder.com/v2/oauth2/token"
res = requests.post(url, data=in_val)
# res.status_code
ACCESS_TOKEN = res.json()['access_token']
# ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJLUmM4NTlrZlk3ZnNKSUxxZXlUZW90d1JxbFl3bThNRW5CTVNWUXQ0WmttZFNpZjlaSSIsImp0aSI6IjA4YTAyMDJmZmQ4NGE4NDFjZDVhZTU0MGVmZWZkMTU4YjM3MjFiMTlmMWEzNjQzZmE1MjFmYTZkNDUxMjFmODEwMjNlY2RkMTZjNjVlMTQxIiwiaWF0IjoxNjc3MTEzNjQ1LCJuYmYiOjE2NzcxMTM2NDUsImV4cCI6MTY3NzExNzI0NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.XT6THra8P6scb1l083ykPuMvJ4PXbUsQm0fUXvE5wPCWRnMx5ux0WXYGx6A1v5fwMYH75GDnz_gfmUFI8nmzrgK3LoF9lTinLNTteTcQqV26z0MBrdFi2Eld93YZZSV6nH0tdtaqdpG-aoqWbz0RCjBTIf347DPDMjCHdm0O28tjJXs2Ch7bNv_89wjZ0qdW-wEmJEvv4BD7lZhd7VqmOU2EmBlDs3OnJq0NtNJnFyf90rYbxMEGwo1hst_V41X7ONYTf88Wws43nY4POtyuScK0Rt3Pzl83-BcaVM__hJ8x_p3Z0MJqBDhj9tsg4dJy_FEO2h2a5nCM5PGu5_bf-w"


# In[182]:


# payload={'type':"Dog","breeds":"",'location':'NJ'}
url = "https://api.petfinder.com/v2/types/dog/breeds"
header = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
response = requests.get(url, headers = header)
types=response.json()['breeds']
dog_breeds = [t['name'] for t in types]


# In[183]:


dog_breeds


# In[141]:


# Open file for writing
url = "https://api.petfinder.com/v2/animals"

payload = {'type':'Dog', 'page': 2417}

# Make API request
response = requests.get(url, headers = header, params=payload)

# Parse JSON response
temp_data = response.json()


# In[143]:


len(temp_data)


# In[184]:


# Open file for writing
page = 7001
url = "https://api.petfinder.com/v2/animals"
all_data = []
# Loop until API usage is 1000
while page < 8001:
    payload={'type':'Dog', 'page': str(page)}
    response = requests.get(url, headers = header, params=payload)

    if response.status_code == 200:
        pet_data = response.json()
        all_data.extend(pet_data['animals'])

    # Increment counter
    page += 1
    #print(page)


# In[185]:


len(all_data)


# In[186]:


with open("dog_data7001-....json", "w") as f:
    json.dump(all_data, f, indent=3)


# ## process json file

# In[200]:


with open('dog_data1-1001.json', 'r') as f:
    data = json.load(f)

state_breed = defaultdict(list)

for i in range(len(data)):
    breed = data[i]['breeds']['primary']
    state = data[i]['contact']['address']['state']
    state_breed[state].append(breed)


# In[220]:


with open('dog_data1001-2001.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    breed = data[i]['breeds']['primary']
    state = data[i]['contact']['address']['state']
    state_breed[state].append(breed)


# In[221]:


len(state_breed['TX'])


# In[222]:


with open('dog_data2001-3001.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    breed = data[i]['breeds']['primary']
    state = data[i]['contact']['address']['state']
    state_breed[state].append(breed)


# In[223]:


len(state_breed['TX'])


# In[224]:


with open('dog_data3001-4001.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    breed = data[i]['breeds']['primary']
    state = data[i]['contact']['address']['state']
    state_breed[state].append(breed)


# In[225]:


len(state_breed['TX'])


# In[226]:


with open('dog_data4001-5001.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    breed = data[i]['breeds']['primary']
    state = data[i]['contact']['address']['state']
    state_breed[state].append(breed)


# In[227]:


len(state_breed['TX'])


# In[228]:


with open('dog_data5001-6001.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    breed = data[i]['breeds']['primary']
    state = data[i]['contact']['address']['state']
    state_breed[state].append(breed)


# In[229]:


len(state_breed['TX'])


# In[230]:


with open('dog_data6001-7001.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    breed = data[i]['breeds']['primary']
    state = data[i]['contact']['address']['state']
    state_breed[state].append(breed)


# In[231]:


len(state_breed['TX'])


# In[232]:


with open('dog_data7001-....json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    breed = data[i]['breeds']['primary']
    state = data[i]['contact']['address']['state']
    state_breed[state].append(breed)


# In[233]:


len(state_breed['TX'])


# In[281]:


all_state_dog = defaultdict(list)
breed_count = defaultdict(list)
for s in states:
    for b in dog_breeds:
        breed_count[b] = state_breed[s].count(b)
    #print(len(breed_count))
    #print(s)
    all_state_dog[s] = sorted(breed_count.items(), key=lambda x:x[1], reverse = True)


# In[291]:


all_state_dog['TX']


# In[287]:


total_count_per_state = {}
for state in states:
    total = 0
    for k,v in all_state_dog[state]:
        total += v
    total_count_per_state[state] = total
total_count_per_state


# In[292]:


top5_dog_per_states = {}
ranks = ['top1','top2','top3','top4','top5']
for r in ranks:
    top5_dog_per_states[r]=[]
for state in states:
    i=0
    for k,v in all_state_dog[state]:
        top5_dog_per_states[ranks[i]].append(k)
        i+=1
        if i==5: break




