import requests
import pickle
from bs4 import BeautifulSoup
url = 'https://www.doogal.co.uk/UKPhoneCodes.php'

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'lxml')
# Get the main table on the page
pcodetable = soup.find('table', attrs={'class': 'phoneCodeTable'})
pcodetable_data = pcodetable.find_all('tr')
# Remove the <th> row
pcodetable_data = pcodetable_data[1:]

textdata = []
# For each row in the table
for tr in pcodetable_data:
    # each cell in the row
    td = tr.find_all('td')
    # Remove the html from the text
    row = [i.text for i in td]
    # ditch the example number column
    del row[2]
    textdata.append(row)

textdata = [[s.replace(' ', '') for s in l] for l in textdata]

# save the final list as a pickle file
with open("codes.pickle", "wb") as f:
    pickle.dump(textdata, f)