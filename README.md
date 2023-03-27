##### Case 1
The Business Excellence team would like to build an automated solution to automate a manual
scraping process in the Commercial department. The team has given you this task, and they
would like to see you demonstrate your abilities by automating the scraping of product media
(images and videos) for items on the H&M website.
The task is as follows:
- Write a script in Python to scrape all product media (images and video) for the SKUs
listed down in dataset (please refer to the file provided)
- You are required to send us your script and the product media (result)
- The script must allow for all the product media to be easily obtained for all the items
without having to manually access or open the website
- All media must be placed into different subfolders of items, i.e. each subfolder must
have images and videos for only 1 item.
- For example, for this item (Article Number “1122404001”), based on the item's product
display view (PDV), there are 3 product images associated with this item. The script must
ensure that the 3 images are automatically scraped (downloaded) into a folder labeled
“1122404001” in your PC, before scraping the product media for the next item or
(Article Number) in the list.
- Please submit the code on a git repo, try to follow best practices as much as possible
from writing good commit messages, clean code, testing, having scalability in mind as
well, provide your suggested architecture and why you chose each component.

##### Case 1 Approach
- Based on given example of the given url, https://www2.hm.com/en_my/productpage.1122404001.html , it can be concluded that, items from the `Article Number` column can be substituted with given number of the url.
- However, after extracting input needed from provided dataset, some of items number can not be substituted into the url. For example, first row with article number `684021184` supposed to be `0684021184`, but once the file has been opened in the current workspace, initial zero has been truncated.
- The file also contains many Nan values.
- To mitigate issue temporarily, we will be using pandas to read excel file, drop rows with Nan values, and read `Article Number` column as integer then as string.

- further processing by + '0' to the article number that has less than 10 characters.

- Initial run using scrapy and validation, some of items cannot be found list of items that have not been found is as follows:
    - Article Number | Product Name | Color
    - 0970818051 | Relaxed Fit Sweatshirt | Light grey marl
    - 1009953017 | Nylon cargo joggers | Light grey
    - 1025932014 | Ribbed top | Light purple
    - 1107360014 | Wide twill trousers | Dark brown
    - 1119685001 | Reversible-sequin T-shirt | Light green/T. rex
    - 1119685003 | Reversible-sequin T-shirt | Grey/Dragon
    - 1121412001 | Short-sleeved cotton shirt | Light blue/Striped
    - 1150469003 | Cotton T-shirt | Light green

- Failure to find remaining images using BeautifulSoup4
- Too complex to scrape using scrapy for now
- Not enough time to properly scrap using Selenium
- Downloading using playwright (able to load dynamic pages but less configuration compared to selenium)

##### Case 1 Process

- at folder `01_CHECKING_ARTICLES_URLS`, we first read provided input using `file_reader.py`
- next using scrapy, we checked for valid article url using `HMProductPage.py`  and output it to `available_articles.csv`, unavailable files could be found above.
- at folder `02_DOWNLOADING_ARTICLES`, we used data from first step `available_articles.csv` to scrape necessary images.
- script to scrape is using `playwright` package and name `PlaywrightDownload.py`.
- all output images are available at `Output` folder directory.