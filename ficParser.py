'''
ficParser.py by Elisabeth (Elsie) Eigerman
Created on 3/18/21

This program takes an html file downloaded from the dowload function on Ao3 and splits it into smaller chapter html files.
'''
#This imports the BeautfulSoup package for html
from bs4 import BeautifulSoup

#This opens the html file you downloaded (note the output will be saved to the same location as you saved the initial file).
link = open("[YOUR FILE PATH HERE]",  encoding="utf-8")

#Parses the file and then calls the section that is just the chapters of the fic
soup = BeautifulSoup(link, 'html.parser')
soup2 = soup.find("div", id="chapters")

#This calls all the chapter headings and chapter text and puts them into a list
heading = soup2.find_all(class_ = "heading")
chapt = soup2.find_all("div", class_ = "userstuff" )

#This creates some strings that will make the chapter html files work and look right
first_line = '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">'
last_line = '</body> </html>'
opener = '<body>'

#The loop goes for the length of the list of chapter headings 
for i in range(len(heading)):
    #Takes the chapter and headings and changes them to strings to be put in to the new html file
    chapt1 = chapt[i]
    heading1 = heading[i]
    chapt1 = str(chapt1)
    heading1 = str(heading1)
    #This takes the chapters, headings, and earlier strings to create a complete html file
    fullChapt = first_line + str(soup.head) + opener + heading1 + chapt1 + last_line
    #This creates a unique name for the file
    doc_title = "chapter" + str(i) + ".html"
    #This writes the html file, note if the file already exists it won't overwrite it
    f = open(doc_title, "x", encoding="utf-8")
    f.write(fullChapt)
    f.close
