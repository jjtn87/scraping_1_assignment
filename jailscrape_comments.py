#This command is importing two functions from the bs4 toolkit. 
import requests, mechanize
from bs4 import BeautifulSoup

#This is the url of the website we are trying to scrape.
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'

#The first line (#10) shortens the command for mechanizing the browser. 
# Get the HTML of the page
br = mechanize.Browser()
#This opens the url on the browser. 
br.open(url)
#I'm not exactly sure about this one, but I think it helps feed the HTML of the website to BS.
html = br.response().read()

# Transforms the HTML into a BeautifulSoup object.
soup = BeautifulSoup(html, "html.parser")

# Finds the main table using both the "align" and "class" attributes.
main_table = soup.find('tbody',
    {'id': 'mrc_main_table'}
)

#This just changes the name from main_table... to row_list. 
row_list = main_table.find_all('tr')

# This gests the data from each table row.
for r in row_list:
	#I believe this finds everything in the cells. 
    cell_list = r.find_all('td')
    #If the cell is empty, it will print nothing. 
    if len(cell_list) > 0:
        for c in cell_list:
            print c.text.strip()

        print '----------'
#This will tell you that the scrape was successful. 
print 'IT WORKED!'