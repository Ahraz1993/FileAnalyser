#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
File Analyzer
Author: Ahraz Athar
Description:
    This script analyzes a text file and provides:
    - Total number of lines
    - Total number of words
    - Total number of characters
    - The longest and shortest lines (with position)
    - Top 3 most frequent words (ignoring punctuation)
    - Creates a backup copy of the file in a 'backupDir' folder

Usage:
    Run this file in Jupyter Notebook or Python.
    When prompted, enter the full path or name of your text file.
"""


# In[2]:


from pathlib import Path


# In[3]:


import shutil


# In[4]:


import string
from collections import Counter


# In[5]:


import os


# In[6]:


cwd=Path.cwd()
print(cwd)


# In[7]:


userPath=Path(input("Please Enter The file Path : "))
if not userPath.is_absolute():
   userPath=Path(__file__).parent/userPath

   


# In[8]:


userPath.resolve()


# Main Logic of File Analyser

# In[9]:


def countWordsLinesChars(path):
    # Counts words,Lines and Characters in the given file
    with open(path,"r") as f:
      Lines=f.readlines()  #Reads Lines and stores them as a list in Lines
      countofWords=0
      countofChars=0      
      for line in Lines:
         countofChars+=len(line)  #Each line's Length is actual number of chars including spaces
         listWords=line.strip().split() #List of words excluding spaces
         countofWords+=len(listWords) #Each line has many words.All words are seperated in a list using split().Length of that List is actual number of words in that line.
    print("\n📊 File Analysis Summary:")     
    print(f"Total Lines      : {len(Lines)}")
    print(f"Total Words      : {countofWords}")
    print(f"Total Characters : {countofChars}")


# In[10]:


def makeBackup(path):

    #Makes Backup 
    
    backupDir=Path(path.resolve().parent/"backupDir") #Path Object with name backupDir is being made
      
    backupDir.mkdir(parents=True,exist_ok=True) #Making the directory with name backupDir
    # print(backupDir.is_dir())
    backupFile=Path(backupDir/path.name) #New File's Location is being decided.New Path Object is being created which will have Path Name as /backupDir/userPath.name
    #userPath.name gives the name of file without extension
    shutil.copy(path,backupFile) #copies from source to destination
    print(f"A copy of your file has been made available at {backupFile}") 



def longestShortestLineandIndices(path):
  with open(path,"r") as f:
    lines=f.readlines()
    wordCount=Counter() #This creates a Counter Object which is empty.It can be converted into dictionary.This is very useful to add up dictionaries
    
    
     
     
    
      
      
      
    
    for line in lines:
        
        table=str.maketrans("","",string.punctuation)
        cleanLowerCaseLine=line.lower().translate(table)
        wordCount+=Counter(cleanLowerCaseLine.split())
        
    longestLine=""
    longestIndex=0
    longestLen=0
     
    # shortestLine=min(lines,key=len)
    # shortestLen=len(shortestLine)  
    shortestLen=float('inf')  
    shortestIndex=0
      
    for index,line in enumerate(lines):
        if(len(line)>longestLen):
            longestIndex=index
            longestLine=line
            longestLen=len(line)
        if(len(line)<shortestLen):
            shortestIndex=index
            shortestLen=len(line)
            shortestLine=line
    print(f"The longest line  is {longestLine} and it is at {longestIndex}.Its Length is {longestLen}")        
    print(f"The shortest line  is {shortestLine},and it is at {shortestIndex}.Its Length is {shortestLen}") 
    return wordCount
      
    


# In[13]:


def topWords(number,wordCount):
     top=wordCount.most_common(number)
     for i,(word,count) in enumerate(top,1):
        print(f"{i}. '{word}' appears {count} times")

# In[11]:

def main():
   
  if not userPath.is_file():
    print("The file doesn't exist")
    
    
        
         
           

  else:
    try:  
    #Counting words,Lines,Characters
      countWordsLinesChars(userPath)
    ##Backup Dir
      makeBackup(userPath)
    
      
    except Exception as e:
      print(f"The error is {e}")  
      


# Additional Logic of Top 5 Words and Longest Line

# In[12]:



    


# In[14]:


    try:
    
      wordCount=longestShortestLineandIndices(userPath)
     
    # shortestLine=min(lines,key=len)
    # shortestLen=len(shortestLine)  
    
            
        
        
            
            
            
        

    
      try:
         topnumbers=int(input("Please enter how much top numbers you want? :").strip())
        
      except ValueError:
        
         print("Invalid Input ,Defaulting to top 3")
         topnumbers=3
      topWords(topnumbers,wordCount)  
      
    
    except Exception as e:
      print(e)


# In[ ]:





# In[ ]:

if __name__=="__main__":
   main()



# %%
