""" 
Projects Name: Find Sitemap Url 
Technology: BeautifulSoup, Requests 
Todo: 
1. go to the sitemap xml file open 
2. find the last one of the list of total xml file 
3. get this like with the last xml file 
4. scrap the url using regular expression  
 
""" 
import requests 
from bs4 import BeautifulSoup  

#get the url  
all_site = []
base_url = input("ENTER THE SITEMAP URL: ") 
headers_agent = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
get_link = requests.get(base_url,headers=headers_agent)  
response = get_link.text  
soup = BeautifulSoup(response,features="xml") 
sitemap_xml = soup.find_all('loc')  
# print(sitemap_xml) 
for i in sitemap_xml:  
    xml = i.text 
    all_site.append(xml) 

for xml in all_site: 
    domain = base_url.split('/')[-2]
    params = xml.split("/")[-1] 
    query  = f"https://{domain}/{params}" 
    get_all_page_url = requests.get(query,headers=headers_agent) 
    soup = BeautifulSoup(get_all_page_url.text,'xml') 
    find_urls = soup.find_all('loc') 
    cnt = 0  
    total_cnt = 0

    with open(f'file{domain}.txt', 'a') as file:
        for find_url in find_urls: 
            for i in find_url:
                url_text = i.text 
                if url_text.endswith('/'):  
                    print(url_text)
                    file.write(url_text + '\n')  

    print("File write operation completed.")



 



