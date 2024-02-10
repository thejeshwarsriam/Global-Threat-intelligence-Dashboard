import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Cyber+attacks+against+india&sca_esv=b39a61d476f9348b&source=hp&ei=IxfHZfzLNsOr0-kP0rqzkA0&iflsig=ANes7DEAAAAAZcclM8PRP_u3hMTm4Oq3bPda1CkZu_2g&ved=0ahUKEwi86d2GkqCEAxXD1TQHHVLdDNIQ4dUDCA0&uact=5&oq=Cyber+attacks+against+india&gs_lp=Egdnd3Mtd2l6IhtDeWJlciBhdHRhY2tzIGFnYWluc3QgaW5kaWEyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHkifVFCoC1jIT3AHeACQAQCYAb0BoAHJIaoBBDAuMzO4AQPIAQD4AQGoAgrCAhAQABgDGI8BGOUCGOoCGIwDwgIQEC4YAxiPARjlAhjqAhiMA8ICCxAAGIAEGLEDGIMBwgILEC4YgAQYsQMYgwHCAhEQLhiABBixAxiDARjHARjRA8ICCBAAGIAEGLEDwgIFEAAYgATCAg4QLhiABBixAxiDARjUAsICCxAAGIAEGIoFGIYD&sclient=gws-wiz'
response = requests.get(url)
print("1")
if response.status_code == 200:
    html_content = response.text
    # Now you have the HTML content of the webpage
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
print("2")
soup = BeautifulSoup(html_content, 'html.parser')
print("3")
# Example: Extracting all the links from the page
links = soup.find_all('India')
for link in links:
    print(link.get('href'))
print("4")
# Example: Extracting text from paragraphs
# paragraphs = soup.find_all('p')
# for paragraph in paragraphs:
#     print(paragraph.text)
