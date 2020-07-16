#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as rq
import bs4
import webbrowser


# In[6]:


a = input("Enter Name of Movie: ")
url = "https://tapritricks.blogspot.com/search?q={}" .format(a)
response = rq.get(url)
soup = bs4.BeautifulSoup(response.content , features="html.parser")
print(soup)
pict_attr = soup.find_all('a',{'class': "post-image-link"})
try:
    url2 = pict_attr[0].attrs['href']
    response2 = rq.get(url2)
    soup2 = bs4.BeautifulSoup(response2.content)
    img_attr = soup2.find_all('img')
    img = img_attr[1]
    x = input("Download Thumbnail(Y/N): ")
    if x.upper()=="Y":
        with open("{}.jpg" .format(a),"wb") as file:
            img_url = img.attrs['src']
            response = rq.get(img_url)
            file.write(response.content)
        a = input("Download Movie(Y/N): ")
        if a.upper()=="Y":
            try: 
                # link = soup2.find_all('img',{"alt": "@aur114920 Telegram"})
                # lk = link[0]
                # link_down = lk.parent.attrs['href']
                webbrowser.open(url2 , new =2)
            except KeyError:
                print("Link not Available")
                
except:
    print("Not Found")
    
    


# In[ ]:




