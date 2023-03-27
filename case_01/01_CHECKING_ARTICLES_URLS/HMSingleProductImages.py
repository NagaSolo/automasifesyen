# import necessary libraries
from bs4 import BeautifulSoup
import requests
import random
  
  
# function to extract html document from given url
def get_html_document(url):
    
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

      
    # request for HTML document of given url
    response = requests.get(url, headers=HEADERS)
      
    # response will be provided in JSON format
    return response.text
  
    
# assign required credentials
# assign URL
url_to_scrape = "https://www2.hm.com/en_my/productpage.0684021184.html"
  
# create document
html_document = get_html_document(url_to_scrape)

# print(html_document)
  
# create soap object
soup = BeautifulSoup(html_document, 'html.parser')
  
  
# Find all images using select()
images = soup.find_all("img")

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]
# 'https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F5d%2F49%2F5d49ca1f8e17e283545fc73395ed8eca155af68c.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/fullscreen]'
# 'https://lp2.hm.com/hmgoepprod?set=format%5Bwebp%5D%2Cquality%5B79%5D%2Csource%5B%2F5d%2F49%2F5d49ca1f8e17e283545fc73395ed8eca155af68c.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url%5Bfile%3A%2Fproduct%2Fmain%5D'
# 'https://lp2.hm.com/hmgoepprod?set=format%5Bwebp%5D%2Cquality%5B79%5D%2Csource%5B%2F5d%2F49%2F5d49ca1f8e17e283545fc73395ed8eca155af68c.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url%5Bfile%3A%2Fproduct%2Fmain%5D'
# 'https://lp2.hm.com/hmgoepprod?set=format%5Bwebp%5D%2Cquality%5B79%5D%2Csource%5B%2Ff6%2Fe8%2Ff6e867af55c32d580b17b2e40e9ce9097e9997c0.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVEDETAIL%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url%5Bfile%3A%2Fproduct%2Fmain%5D'
# 'https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fcc%2F59%2Fcc59e7e962c650f01879fac4dfdbfd154e42d261.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BLOOKBOOK%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/main]'

# 'https://lp2.hm.com/hmgoepprod?set=format%5Bwebp%5D%2Cquality%5B79%5D%2Csource%5B%2F63%2F18%2F6318e2c109f19a80bea08bacb174730382dafcce.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bmen_tshirtstanks_printed%5D%2Ctype%5BDESCRIPTIVEDETAIL%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url%5Bfile%3A%2Fproduct%2Fmain%5D'

# # Save images
# for count, image in enumerate(images[1:]):
#     src_url = 'https:' + image['src']
    
#     img_data = requests.get(src_url, headers={'User-Agent': random.choice(user_agents_list)}).content 

#     with open(f'tests/{count}.jpg', 'wb') as handler:
#         handler.write(img_data)