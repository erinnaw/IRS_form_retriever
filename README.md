# IRS_form_retriever
---
# part1.py
**Returns data in JSON format based on the form value(s) input on the console terminal**
- Run the program on the console terminal.
- Input a list of form values of any size, each separated by a space. Exclude the word "form". Example input, "w-2 w-2g w-3 990-w".
- The script will return a list of dictionary in JSOn format, detailing the form value, form title, minimum year and maximum year of each form value requested.

# part2.py
**Downloads all PDF forms based on the form value and the year range input on the console terminal**
- Run the program on the console terminal.
- Input in the format of "<Form Value> <Start Year> <End Year>". Exclude the word "form". Example input, "w-2 2000 2008".
- The script will create a subdirectory within the project folder with the name of the form number, and download all forms with the exact form value in the year range requested. All PDF forms will be saved in the subdirectory. 
