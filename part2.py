import requests
import lxml.html as lh
import os
import urllib.request

print("Enter: <Form Value> <Start Year> <End Year>" )
input_ = input()
tokens = input_.split(' ')

while True: 
    if len(tokens) == 3 and tokens[1].isnumeric() and tokens[2].isnumeric():
        tokens[1] = int(tokens[1])
        tokens[2] = int(tokens[2])
        if tokens[1] < tokens[2] and tokens[1] >= 1950 and tokens[1] <= 2025 and tokens[2] >= 1950 and tokens[2] <= 2025:
            break

    print("Invalid input. Try again.")
    input_ = input()
    tokens = input_.split(' ')

form_value = tokens[0].upper()
min_year = tokens[1]
max_year = tokens[2]

url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value=" + form_value + "&isDescending=false"

#gets raw HTML data from url
page = requests.get(url)

#parse raw HTML
page_content = lh.fromstring(page.content)

#create folder under current dir
path = './Form ' + form_value
if not os.path.exists(path):
    os.makedirs(path)

for i in range(min_year, max_year + 1):
    xpathstring = '//tr[td[a[text() = "Form ' + form_value + '"]]][td[normalize-space() = "' + str(i) + '"]]'
    for data_set in page_content.xpath(xpathstring):
        for data in data_set:
            if data.get('class') == 'LeftCellSpacer':
                response = urllib.request.urlopen(data[0].get('href'))
                file_path = path + '/Form ' + form_value + ' - ' + str(i) + '.pdf'
                file = open(file_path, 'wb')
                file.write(response.read())
                file.close()
                print("saving to", os.path.abspath(file_path))
    