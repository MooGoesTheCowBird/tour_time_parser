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
    'nmstat': 'e1a5f699-f1db-9bf9-e87b-68352d2e2c65',
    '_ga_WN2637J60X': 'GS1.1.1712018365.1.0.1712018365.0.0.0',
    '_ga_W6R8HFWLMD': 'GS1.1.1712018364.1.0.1712018366.0.0.0',
    'AMCV_1B6E34B85282A0AC0A490D44%40AdobeOrg': 'MCMID|14620354045443075303578425152322541708',
    '_fbp': 'fb.1.1712463684827.1791723574',
    'rskxRunCookie': '0',
    'rCookie': 'ex9h1hvmqrr69umbggh3zlup0ny06',
    '_ga_6VXTC1Y945': 'GS1.1.1712638855.2.1.1712639117.0.0.0',
    '_ga_JS9JCE5TNQ': 'GS1.1.1712638855.2.1.1712639117.0.0.0',
    'kndctr_1B6E34B85282A0AC0A490D44_AdobeOrg_identity': 'CiYxNDYyMDM1NDA0NTQ0MzA3NTMwMzU3ODQyNTE1MjMyMjU0MTcwOFIQCNzAqLbrMRgBKgNPUjIwAfABo7jkhO0x',
    '_clck': '2iarhw%7C2%7Cfkv%7C0%7C1558',
    '_gcl_au': '1.1.2001510558.1712198620.1328946364.1712896681.1712896680',
    'lastRskxRun': '1712896681845',
    '_ga_9C4T5P6PP6': 'GS1.1.1712942473.4.0.1712942473.60.0.0',
    '_ga_QVD9JY2JRF': 'GS1.2.1713114631.3.0.1713114631.0.0.0',
    '_ga_QQKCJ20GWP': 'GS1.2.1713482765.17.1.1713482857.0.0.0',
    '_hjSessionUser_2595508': 'eyJpZCI6IjVkM2RmOGU5LThhZmEtNWIzYy1hYzI2LTI4OThjZjIzMWQxNSIsImNyZWF0ZWQiOjE3MTM4MjU5OTk2MjQsImV4aXN0aW5nIjpmYWxzZX0=',
    '_uetvid': '4bd4cfd0f49611eea9f2f3e1cc7ad369',
    '_tt_enable_cookie': '1',
    '_ttp': 'AGNAvJkczbYRDC-eDd6U1NFZkEa',
    '_ga_V3L7VWCMG4': 'GS1.1.1713825999.1.1.1713826025.34.0.0',
    '_hjSessionUser_3120009': 'eyJpZCI6ImE0Y2MxYjQxLTdkMTUtNTI2ZC05MjQ3LTlkMDc4N2RhMjVkZSIsImNyZWF0ZWQiOjE3MTI0NjI1MDg2MjIsImV4aXN0aW5nIjp0cnVlfQ==',
    '__gads': 'ID=b3cb5a9dc3550955:T=1712462510:RT=1714009599:S=ALNI_Mayy3lqu-5hZsn2Zx9FuG3g2ZL84g',
    '__gpi': 'UID=00000ddcd58b94c4:T=1712462510:RT=1714009599:S=ALNI_MYF1XWZGtrH-RRQ90e0jpJTJiFrsw',
    '__eoi': 'ID=79763d42bcdf51c3:T=1712462510:RT=1714009599:S=AA-AfjbcRDQDb-SyrtRpGMZ3tDK4',
    '_ga_Q72ZQB7GTR': 'GS1.1.1714104932.4.0.1714104932.60.0.0',
    '_ga_ESS0NB66T4': 'GS1.1.1714104932.4.0.1714104932.0.0.0',
    '_ga_JD06GX6S4V': 'GS1.1.1714104971.6.0.1714104971.0.0.0',
    '_ga_54G0BC6W6Y': 'GS1.1.1714513134.16.0.1714513134.60.0.0',
    '_ga_Y496P1REVX': 'GS1.1.1714515625.5.0.1714515625.0.0.0',
    '_ga_7B9KWHP1CH': 'GS1.1.1714610581.80.1.1714611574.0.0.0',
    '_ga_7XBDZWMDKC': 'GS1.1.1714672459.1.0.1714672461.0.0.0',
    '_ga_DHXZN2TMLR': 'GS1.1.1714789804.1.0.1714789812.0.0.0',
    '_ga_RNYWDR7C56': 'GS1.1.1714961896.6.0.1714961896.0.0.0',
    '_ga_F4NTEFFFMS': 'GS1.1.1715130173.7.1.1715130191.0.0.0',
    '_ga_TK19WL2S7C': 'GS1.1.1716157614.1.1.1716157708.0.0.0',
    '_ga_LC250GQGVR': 'GS1.1.1716390202.22.1.1716390214.0.0.0',
    '_hp2_props.3001039959': '%7B%22Base.appName%22%3A%22Canvas%22%7D',
    '_hp2_id.3001039959': '%7B%22userId%22%3A%224640491298657537%22%2C%22pageviewId%22%3A%222056495138247049%22%2C%22sessionId%22%3A%224215319172434685%22%2C%22identity%22%3A%22uu-2-bd1b68272a152685c70453d46099b5e118b33db25a3d0bfb0c7a9ad782db55bf-yGkEvpxAPyTeKLHaHOxZqJNjMXbA5ZV86ZZ6139o%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D',
    '_ga_YR5HHD87QB': 'GS1.1.1718083195.4.0.1718083195.0.0.0',
    '_ga_R7GWSHH1MW': 'GS1.1.1718130854.3.0.1718130854.0.0.0',
    '_ga_KH7JY99KNG': 'GS1.1.1718309423.94.1.1718309448.0.0.0',
    '_ga_0YGZRR964T': 'GS1.1.1718310359.14.1.1718310359.0.0.0',
    '_gid': 'GA1.2.1604836900.1718310360',
    '_ga_0DL8PPJWXB': 'GS1.1.1718310390.5.0.1718310390.0.0.0',
    '_ga': 'GA1.1.847196044.1711129113',
    'vs_csrf': 'b523b6365a969199a7c030ff287486a2',
    '_ga_LXK6Q6NZNN': 'GS1.1.1718309449.64.1.1718310662.0.0.0',
    'PHPSESSID': 'ee8211d9dc3afe3ca90821ef427f7ee224ef4b9bd175b54e23c1f893a1a8df49',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'nmstat=e1a5f699-f1db-9bf9-e87b-68352d2e2c65; _ga_WN2637J60X=GS1.1.1712018365.1.0.1712018365.0.0.0; _ga_W6R8HFWLMD=GS1.1.1712018364.1.0.1712018366.0.0.0; AMCV_1B6E34B85282A0AC0A490D44%40AdobeOrg=MCMID|14620354045443075303578425152322541708; _fbp=fb.1.1712463684827.1791723574; rskxRunCookie=0; rCookie=ex9h1hvmqrr69umbggh3zlup0ny06; _ga_6VXTC1Y945=GS1.1.1712638855.2.1.1712639117.0.0.0; _ga_JS9JCE5TNQ=GS1.1.1712638855.2.1.1712639117.0.0.0; kndctr_1B6E34B85282A0AC0A490D44_AdobeOrg_identity=CiYxNDYyMDM1NDA0NTQ0MzA3NTMwMzU3ODQyNTE1MjMyMjU0MTcwOFIQCNzAqLbrMRgBKgNPUjIwAfABo7jkhO0x; _clck=2iarhw%7C2%7Cfkv%7C0%7C1558; _gcl_au=1.1.2001510558.1712198620.1328946364.1712896681.1712896680; lastRskxRun=1712896681845; _ga_9C4T5P6PP6=GS1.1.1712942473.4.0.1712942473.60.0.0; _ga_QVD9JY2JRF=GS1.2.1713114631.3.0.1713114631.0.0.0; _ga_QQKCJ20GWP=GS1.2.1713482765.17.1.1713482857.0.0.0; _hjSessionUser_2595508=eyJpZCI6IjVkM2RmOGU5LThhZmEtNWIzYy1hYzI2LTI4OThjZjIzMWQxNSIsImNyZWF0ZWQiOjE3MTM4MjU5OTk2MjQsImV4aXN0aW5nIjpmYWxzZX0=; _uetvid=4bd4cfd0f49611eea9f2f3e1cc7ad369; _tt_enable_cookie=1; _ttp=AGNAvJkczbYRDC-eDd6U1NFZkEa; _ga_V3L7VWCMG4=GS1.1.1713825999.1.1.1713826025.34.0.0; _hjSessionUser_3120009=eyJpZCI6ImE0Y2MxYjQxLTdkMTUtNTI2ZC05MjQ3LTlkMDc4N2RhMjVkZSIsImNyZWF0ZWQiOjE3MTI0NjI1MDg2MjIsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=b3cb5a9dc3550955:T=1712462510:RT=1714009599:S=ALNI_Mayy3lqu-5hZsn2Zx9FuG3g2ZL84g; __gpi=UID=00000ddcd58b94c4:T=1712462510:RT=1714009599:S=ALNI_MYF1XWZGtrH-RRQ90e0jpJTJiFrsw; __eoi=ID=79763d42bcdf51c3:T=1712462510:RT=1714009599:S=AA-AfjbcRDQDb-SyrtRpGMZ3tDK4; _ga_Q72ZQB7GTR=GS1.1.1714104932.4.0.1714104932.60.0.0; _ga_ESS0NB66T4=GS1.1.1714104932.4.0.1714104932.0.0.0; _ga_JD06GX6S4V=GS1.1.1714104971.6.0.1714104971.0.0.0; _ga_54G0BC6W6Y=GS1.1.1714513134.16.0.1714513134.60.0.0; _ga_Y496P1REVX=GS1.1.1714515625.5.0.1714515625.0.0.0; _ga_7B9KWHP1CH=GS1.1.1714610581.80.1.1714611574.0.0.0; _ga_7XBDZWMDKC=GS1.1.1714672459.1.0.1714672461.0.0.0; _ga_DHXZN2TMLR=GS1.1.1714789804.1.0.1714789812.0.0.0; _ga_RNYWDR7C56=GS1.1.1714961896.6.0.1714961896.0.0.0; _ga_F4NTEFFFMS=GS1.1.1715130173.7.1.1715130191.0.0.0; _ga_TK19WL2S7C=GS1.1.1716157614.1.1.1716157708.0.0.0; _ga_LC250GQGVR=GS1.1.1716390202.22.1.1716390214.0.0.0; _hp2_props.3001039959=%7B%22Base.appName%22%3A%22Canvas%22%7D; _hp2_id.3001039959=%7B%22userId%22%3A%224640491298657537%22%2C%22pageviewId%22%3A%222056495138247049%22%2C%22sessionId%22%3A%224215319172434685%22%2C%22identity%22%3A%22uu-2-bd1b68272a152685c70453d46099b5e118b33db25a3d0bfb0c7a9ad782db55bf-yGkEvpxAPyTeKLHaHOxZqJNjMXbA5ZV86ZZ6139o%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; _ga_YR5HHD87QB=GS1.1.1718083195.4.0.1718083195.0.0.0; _ga_R7GWSHH1MW=GS1.1.1718130854.3.0.1718130854.0.0.0; _ga_KH7JY99KNG=GS1.1.1718309423.94.1.1718309448.0.0.0; _ga_0YGZRR964T=GS1.1.1718310359.14.1.1718310359.0.0.0; _gid=GA1.2.1604836900.1718310360; _ga_0DL8PPJWXB=GS1.1.1718310390.5.0.1718310390.0.0.0; _ga=GA1.1.847196044.1711129113; vs_csrf=b523b6365a969199a7c030ff287486a2; _ga_LXK6Q6NZNN=GS1.1.1718309449.64.1.1718310662.0.0.0; PHPSESSID=ee8211d9dc3afe3ca90821ef427f7ee224ef4b9bd175b54e23c1f893a1a8df49',
    'Referer': 'https://api-6b447a0c.duosecurity.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
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
