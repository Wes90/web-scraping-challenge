import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = "https://mars.nasa.gov/news/"
browser.visit(url)

soup = bs(browser.html, 'html.parser')


#Paragraph

titles = soup.find_all(name='div', class_='content_title')
p_text = soup.find_all(name='div', class_='article_teaser_body')

#print(titles[1].text)
#print(p_text[0].text)

news_para = p_text[0].text
print(news_para)

# Latest title

title_list = []
for x in titles[1]:
    title_list.append(x.text.strip('\n'))
#print(title_list)

news_title = title_list[0]
#print(news_title)

#Featured Image

url1= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url1)

soup = bs(browser.html, 'html.parser')


full_img_box = browser.find_by_id('full_image')
#print(full_img_box.click())

next_box = browser.find_link_by_partial_text('more info')
#print(next_box.click())

html1=browser.html
soup1 =bs(html1, 'html.parser')
#print(soup1.prettify)

find_image = soup1.find('figure.lede a img')

find_image_1 = soup1.find_all('figure', class_='lede')
#find_image_1[0]
results = find_image_1[0].a['href']
#print(results)

featured_image= 'https://www.jpl.nasa.gov' + results
featured_image

#hemisphere Data Table

url2= "https://space-facts.com/mars/"
browser.visit(url2)

soup = bs(browser.html,'html.parser')
type(soup)

find_table = soup.find('tbody row-1 odd')

table_body = pd.read_html(url2)

mars_table = pd.DataFrame(table_body[0])
mars_table

url3= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url3)

soup = bs(browser.html,'html.parser')
type(soup)

#hemisphere image list

hem_images = []

mars_hem_img = soup.find_all('div', class_= 'item')

for hem in mars_hem_img:
   
    cere_find = hem.select('a') 
    cere_ref = cere_find[0].get('href')
    cere_ref_1 =  'https://astrogeology.usgs.gov' + cere_ref 
    #cere_ref_1
    browser.visit(cere_ref_1)
    soup = bs(browser.html,'html.parser')
    #type(soup)
    pull_img_cere = soup.find('img', class_='wide-image')
    full_cere_ref = pull_img_cere.get('src') 
    full_cere_img = 'https://astrogeology.usgs.gov' + full_cere_ref
    #full_cere_img
    hem_images.append(full_cere_img)


#print(hem_images)

url3= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url3)

soup = bs(browser.html,'html.parser')
#type(soup)

#hemisphere title list

hem_titles = []

counter = 0
mars_hem_find = soup.find_all('div', class_= 'description')


for hem_title in mars_hem_find:
    
    mars_hem_pull= mars_hem_find[0].select('h3')
    mars_hem_title=mars_hem_pull[0].text
    hem_titles.append(mars_hem_title)
    counter += 1
    
    if counter == 1:
        
        mars_hem_pull= mars_hem_find[1].select('h3')
        mars_hem_title=mars_hem_pull[0].text
        hem_titles.append(mars_hem_title)
        counter += 1
        
        if counter == 2:
            
            mars_hem_pull= mars_hem_find[2].select('h3')
            mars_hem_title=mars_hem_pull[0].text
            hem_titles.append(mars_hem_title)
            counter += 1
            
            if counter == 3:
                
                mars_hem_pull= mars_hem_find[3].select('h3')
                mars_hem_title=mars_hem_pull[0].text
                hem_titles.append(mars_hem_title)
                counter += 1
            
            break

            
#print(hem_titles)

hem_1 = {'title':'', 'img_url':''}
hem_2 = {'title':'', 'img_url':''}
hem_3 = {'title':'', 'img_url':''}
hem_4 = {'title':'', 'img_url':''}

hem_1.update({'title': hem_titles[0], 'img_url': hem_images[0]})
hem_2.update({'title': hem_titles[1], 'img_url': hem_images[1]})
hem_3.update({'title': hem_titles[2], 'img_url': hem_images[2]})
hem_4.update({'title': hem_titles[3], 'img_url': hem_images[3]})

hem_image_url = []

hem_image_url.append(hem_1)
hem_image_url.append(hem_2)
hem_image_url.append(hem_3)
hem_image_url.append(hem_4)

#print(hem_image_url)
