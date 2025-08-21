# Requests module allows you to send HTTP/HTTPS requests to web servers
# BeautifulSoup module is used for parsing HTML and XML documents
# csv module allows you to read and write to a CSV file
import requests
from bs4 import BeautifulSoup
import csv

# These variables store the website and browser going to be used
url = "https://finance.yahoo.com/quote/GOOGL/?&.tsrc=fin-srch"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0"}
html_page = requests.get(url, headers=headers)

# Creating and writing to a CSV file
csv_file = open("D:\\Web_Scraping\\scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Stock Name", "Current Price", "Previous Close", "Open", "Bid", "Ask", "Day Range", "52 Week Range", "Volume", "Avg. Volume"])

# Gets all the content of the website
soup = BeautifulSoup(html_page.content, "lxml")

# Finds the title "Header" text
stock_title = soup.find_all("section", attrs={"data-testid": "quote-hdr"})[0].find("h1").get_text()
stock_statistic = soup.find_all("section", attrs={"data-testid": "price-statistic"})[0].get_text()
table_info = soup.find_all("div", attrs={"data-testid": "quote-statistics"})[0].find_all("li")

# Table Labels/Values
stock = []
stock.append(stock_title)
stock.append(stock_statistic)

# Finds all values in the table listed on the website
for i in range(0,8):
    value = table_info[i].find_all("span")[1].get_text()
    stock.append(value)
# Writes the new appended data to the csv file
csv_writer.writerow(stock)

print("Data Transcribed")
