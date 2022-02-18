import requests
import lxml.html as lh
import json
import os

print("Enter: <Form Value> ..." )
input_ = input().upper()
tokens = input_.split(' ')
output = []

for token in tokens:
    form_number = 'Form ' + token
    url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value=" + token + "&isDescending=false"

    #gets raw HTML data from url
    page = requests.get(url)

    #parse raw HTML
    page_content = lh.fromstring(page.content)

    xpathstring = '//tr[td[a[text() = "Form ' + token + '"]]]'
    data_list = page_content.xpath(xpathstring)

    #find form_title of form
    if len(data_list) > 0: 
        form_title = data_list[0].find_class('MiddleCellSpacer')[0].text.lstrip().rstrip()
    else:
        form_title = 'NA'

    #find max_year of form    
    if len(data_list) > 0: 
        max_year = data_list[0].find_class('EndCellSpacer')[0].text.lstrip().rstrip()
    else:
        max_year = 'NA'
        
    #find min_year of form
    if len(data_list) > 0: 
        min_year = data_list[len(data_list)-1].find_class('EndCellSpacer')[0].text.lstrip().rstrip()
    else:
        min_year = 'NA'

    data = {
        'form_number': form_number, 
        'form_title': form_title , 
        'min_year': min_year, 
        'max_year': max_year
    }

    output.append(data)

print(output)
json.dumps(output)