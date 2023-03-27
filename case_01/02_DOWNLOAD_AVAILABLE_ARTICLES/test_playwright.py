from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import os, random
import requests

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

# Use sync version of Playwright
with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch()

    # Open a new browser page
    page = browser.new_page()

    # Set headers to prevent ACCESS DENIED issues
    page.set_extra_http_headers({"User-Agent": random.choice(user_agents_list)})

    # Create a URI for our test file
    # page_path = "file://" + os.getcwd() + "/test.html"
    page_path = "https://www2.hm.com/en_my/productpage.0684021184.html"

    # Open our test file in the opened page
    page.goto(page_path)
    page_content = page.content()

    # Process extracted content with BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    images = soup.find_all("img", class_="product-detail-thumbnail-image")
    
    main_image = soup.find_all("img")
    the_main_src = []
    for image in main_image:
        src_url = image["src"]
        if '=url[file:/product/main]' in src_url:
            the_main_src.append(src_url)
        else:
            continue

    print(the_main_src)
    # # Save images
    # for count, image in enumerate(images):
    #     src_url = 'https:' + image['src']
    
    #     img_data = requests.get(src_url, headers={'User-Agent': random.choice(user_agents_list)}).content 

    #     with open(f'tests/{count}.jpg', 'wb') as handler:
    #         handler.write(img_data)

    # for image in images:
    #     print(image["src"])
    #     print("\n")

    # Close browser
    browser.close()