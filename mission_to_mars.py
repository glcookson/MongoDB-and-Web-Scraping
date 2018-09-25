from bs4 import BeautifulSoup as bs
import pymongo
import requests
import pandas as pd
from splinter import Browser

url_1 = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

url_3 = 'https://twitter.com/marswxreport?lang=en'

url_4 = 'https://space-facts.com/mars/'

url_5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'




def scrape():
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path, headless=True)
	
	browser.visit(url_1)
	html1 = browser.html

	soup = bs(html1, 'html.parser')

	slide_elem = soup.select_one('ul.item_list li.slide')
	news_title = slide_elem.find("div", class_='content_title')
	slide_elem
	news_title.text
	
	para = soup.find_all('div', class_='article_teaser_body')
	para[0].text
	
	browser.visit(url_2)
	browser.click_link_by_partial_text('FULL IMAGE')
	html2 = browser.html
	soup2 = bs(html2, 'html.parser')
	
	
	image = soup2.find('img', class_='fancybox-image')

	featured_image_url = image['src']
	featured_image_url
	
	browser.visit(url_3)
	html3 = browser.html

	soup3 = bs(html3, 'html.parser')
	
	
	mars_weather = soup3.find_all('div', class_='js-tweet-text-container')

	mars_weather[0].text
	
	
	tables, = pd.read_html(url_4)
	tables
	
	
	tables.to_html(header=False,index=False)
	
	
	browser.visit(url_5)
	html5 = browser.html

	soup5 = bs(html5, 'html.parser')
	
	hemisphere_image_urls = []
	Mars_hem_title = soup5.find_all('h3')
	Mars_hem_title_ls = []
	Mars_hem_title_img = []
	for hem in Mars_hem_title:
		Mars_hem_title_ls.append(hem.text)
		browser.click_link_by_partial_text(hem.text)
		new_soup = bs(browser.html, 'html.parser')
		mars_img = new_soup.find('img', class_='wide-image')
		Mars_hem_title_img.append(mars_img['src'])
		browser.back()
		
	hemisphere_image_urls = []
	for x in range(len(Mars_hem_title_ls)):
		dic = {'title':Mars_hem_title_ls[x], 'img_url':Mars_hem_title_img[x]}
		hemisphere_image_urls.append(dic)
	hemisphere_image_urls
	return {'News Title':news_title.text, 'Mars Paragraph':para[0].text, 'Featured Image':featured_image_url, 'Mars Weather':mars_weather[0].text, 'Mars Facts':tables, 'Facts HTML':facts_html, 'Mars Dictionary':hemisphere_image_urls}
	
	if __name__ == "__main__":
		print()
	