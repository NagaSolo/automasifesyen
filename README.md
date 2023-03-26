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