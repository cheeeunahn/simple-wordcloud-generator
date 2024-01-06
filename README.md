# (A Very Very) Simple Wordcloud Generator
This is a really simple python script that creates a wordcloud after reading text from an Excel file.

## How to run the script

### Step 1
Download (or clone) the repository and place your Excel file in `excel_file` folder. You may delete the `temp.xlsx` file.

### Step 2
Run `main.py` (make sure to have Python installed):
```
python3 main.py
```
The libraries used are the following (make sure to install them first before running the script):
- pandas
- matplotlib.pyplot
- wordcloud
- os
- sys
- tkinter

### Step 3
After running the script, a png file of the wordcloud is generated. The file name is `wordcloud_result.png`.
