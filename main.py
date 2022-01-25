import requests
from bs4 import BeautifulSoup

#links this works for
url_1 = "https://games4edu.org/data.html"
url_2 = "https://games4edu.org/data2.html"
url_3 = "https://games4edu.org/data3.html"

#asks which website you want to pull from 
print("What url do you want to explore?")
print("1: " , url_1)
print("2: " , url_2)
print("3: " , url_3)
choice = input()
if(choice == 1):
  url = url_1
elif(choice == 2):
  url = url_1
else:
  url = url_3

data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')

#variables
movieArray = []
size1 = len(movieArray)
added = "false"
size = 0

#stores all the table
table = soup.find( "table", class_ = "wikitable sortable plainrowheaders" )

#goes table line by line 
for row in table.findAll("tr"):
  #splits the rows to get the info we want 
  rows = str(row.get_text())
  rows = rows.split()
  x = len(rows)
  year = (rows[x-4])
  gross = (rows[x-5])
  
  #if the year is a digit 
  if(year.isdigit()):
    #change the number down to just an int 
    gross = gross.replace('$', '')
    gross = gross.replace(',', '')
    gross = gross.replace('F8', '')
    gross = gross.replace('F', '')

    #set the numbers to ints 
    gross = int(gross)
    year = int(year)
  
    #variable resets
    x = 0
    added = "false"
    size = len(movieArray)

    #if array is empty add the info 
    if (size == 0):
      movieArray.append([int(gross),int(year)])
    #else check if the year is already in the array 
    else:
      #checks spot by spot 
      while (x < size):
        #set the current array position to a variable to check the year 
        values = movieArray[x]
        #checks the year to the one we want to add
        if year == values[1]:
            #pulls the old money value for that year 
            money = values[0]
            #add the new money vale to the old
            newValue = money+gross
            #adds the info back in to that array location 
            movieArray[x] = [int(newValue),int(year)]
            #exit the array
            x = size
            #tells you its been added 
            added = "true"
        #if its not that year moves on to the next 
        else:
          x = x+1
      
      #checks if its already been added 
      if added == "false":
        movieArray.append([int(gross),int(year)])

#sorts the array 
movieArray.sort()

#prints the array spot by spot following the format
x = 0
size = len(movieArray)
while (x < size):
  
  values = movieArray[x]
  year = values[1]
  totalEarnings = values[0]
  print('{:4}    ${:20,}'.format(year, totalEarnings))
  x = x+1  