import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os, sys
import tkinter as tk
from tkinter import simpledialog, messagebox

def read_excel():
    try: 
        # create input dialog
        root = tk.Tk()
        root.withdraw() 
        
        excel_file_name = simpledialog.askstring(title="File Name", prompt="엑셀 파일 명을 입력해주세요:")
        # print(excel_file_name)
        if excel_file_name is None:
            print(f"Exiting...")
            sys.exit()
        
        column_name = simpledialog.askstring(title="Column Title", prompt="유저 코멘트들이 모아져있는 행 제목 (column title)을 입력해주세요: ")
        # print(column_name)
        if column_name is None:
            print(f"Exiting...")
            sys.exit()
        
        # read the excel file
        filename = './excel_file/'+excel_file_name+'.xlsx'
        df = pd.read_excel(filename, engine='openpyxl')
        colName = column_name
        df[colName].to_csv('comment_list.txt', header=None, index=None, sep=' ', mode='a')
        return 0
    except TypeError:
        print(f"Exiting...")
        sys.exit()
    except Exception as e:
        print(f"An error occurred! Please try again.")
        return 1

def make_wordcloud():

    file_path = 'comment_list.txt'

    try:
        os.remove(file_path)
        print(f"{file_path} has been successfully deleted.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission error: unable to delete {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    #read excel file
    while 1:
        if read_excel()==0:
            break # if no error occurs, proceed to wordcloud generation
        else:
            if not messagebox.askretrycancel("We were unable to create your wordcloud.", "엑셀 파일 명을 잘못 입력하셨거나 행 이름을 잘못 입력하셨습니다. 다시 입력해주세요!"):
                print(f"Exiting...")
                sys.exit()
    
    # the path which korean font is stored
    font_path = './font/NanumBarunGothic.ttf'

    # generate word cloud
    wordcloud = WordCloud(
        font_path = font_path,
        background_color="white",
        width = 800,
        height = 800)

    text=open('comment_list.txt').read()
    wordcloud = wordcloud.generate(text)

    fig = plt.figure(figsize=(12,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    fig.savefig('wordcloud_result'+'.png')