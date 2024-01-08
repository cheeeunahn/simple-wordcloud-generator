# (A Very Very) Simple Wordcloud Generator
This is a really simple python script that creates a wordcloud after reading text from an Excel file.

## How to run the script

### Step 1
Download (or clone) the repository and place your Excel file in `excel_file` folder. You may delete the `temp.xlsx` file if you wish.

### Step 2
Run `main.py` (make sure to have a recent version of Python installed):
```
python3 main.py
```
The libraries used are the following (make sure to install them first before running the script):
- pandas
- matplotlib
- wordcloud
- openpyxl
- os
- sys
- tkinter

(If you have pip installed, you can either install each library separately or run the following:)
```
pip install pandas matplotlib wordcloud openpyxl tkinter os sys
```
Depending on which pip version you have, you might have to enter `pip3` instead of `pip`.
Check pip version using `pip --version` or `pip3 --version`.

### Step 3
After running the script, the script will create a png file of the resulting wordcloud. The file name is `wordcloud_result.png`.

### Note
After running `python3 main.py` you may find a document named `comment_list.txt` in the directory. This is a temporary file that gets deleted every time the script is run.
