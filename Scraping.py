# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import datetime as dt

def scrape_all():
    # Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title,news_paragraph=mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_fact(),
      "last_modified": dt.datetime.now()                    
        }
    # Ending the browser session
    browser.quit()
    return data

# Functions are called inside scrape all

# # Article Scraping
def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay
    browser.is_element_present_by_css('dev.list_text',wait_time=1)

    # Setting up the parser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Extract the title
        news_title=slide_elem.find('div',class_="content_title").get_text()        
        # Extract the summary
        news_summary=slide_elem.find('div',class_="article_teaser_body").get_text()
    except AttributeError:
        return None,None

    return news_title,news_summary  

# # Image Scraping
def featured_image(browser):
    # Visit the image site
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Navigating to the image
    full_image_tag=browser.find_by_tag('button')[1]
    full_image_tag.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Extract the Rel URL
        img_rel_url=img_soup.find('img',class_="fancybox-image").get('src')
    except AttributeError:
        return None

    # Use base URL to create absolute URL
    abs_url=f"https://spaceimages-mars.com/{img_rel_url}"
    return abs_url                                     

# # Fact scraping
def mars_fact():

    try:
        # Navigating to the facts page and extracting the first table
        df=pd.read_html("https://galaxyfacts-mars.com/")[0]                                                                  
    except BaseException:
        return None

    #Formatting    
    df.columns=["Description","Mars","Earth"]
    df.set_index("Description", inplace=True) 
    # Parsing the table to html for future use
    return df.to_html()

#if __name__ == "__main__":
    # If running as script, print scraped data
 #   print(scrape_all())




