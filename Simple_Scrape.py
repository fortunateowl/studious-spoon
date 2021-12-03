# Call the necessary packages for the program
import requests 
from bs4 import BeautifulSoup

# get the Wikipedia homepage and assign it to the variable "response"
url = "https://www.wikipedia.org/"
response = requests.get(url)

# assign the content of the webpage to the variable "content"
content = response.content

# call BeautifulSoup to parse the information on the webpage.
soup = BeautifulSoup(content, "lxml")

# Create a variable "links," loop through the the content with an "a" tag
# to find links and assign the links to the variable.
all_a = soup.find_all("a")
links = []
for i in all_a:
    if i.get("href") != '#':        # skips href that are not actual links, this needs to be generalized
        links.append(i.get("href"))
 
# Write links to a file
with open('urls.txt', 'w') as file:
      file_content = "\n".join(links)
 
      file.write(file_content)


file.close()

# Print and count the links
print (*links, sep = "\n")
print ("\n \nThe number of links on the Wikipedia homepage is: ", len(links))

