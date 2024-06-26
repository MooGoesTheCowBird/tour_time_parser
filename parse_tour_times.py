import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

'''
1. In your browser, open the developer tools
2. Go to the site, and login
3. After the login, go to the network tab, and then refresh the page
At this point, you should see a list of requests, the top one being the actual site 
- and that will be our focus, because it contains the data with the identity we 
can use for Python and BeautifulSoup to scrape it
4. Right click the site request (the top one), hover over copy, and then copy as  cURL
5. Then go to this site which converts cURL into python requests: https://curlconverter.com/
6. Take the python code and use the generated cookies and headers to proceed with the scraping
'''

cookies = {
    
}

headers = {
    
}

response = requests.get('https://campustours.berkeley.edu/student', cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', id="my-tours")

a = table.find_all("a", target="_blank")
arr = []

#Extract elements from table
for i in a:
    temp = []
    role = i.next_element.next_element.next_element
    temp.append(role.get_text())
    date = role.next_element.next_element.next_element
    temp.append(date.get_text())
    start_time = date.next_element.next_element.next_element
    temp.append(start_time.get_text())
    temp.append(date.get_text())
    end_time = start_time.next_element.next_element.next_element
    temp.append(end_time.get_text())
    arr.append(temp)
arr = np.array(arr)

df = pd.DataFrame(arr, columns = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time'])

df.to_csv("work_dates_times.csv", index = False)
