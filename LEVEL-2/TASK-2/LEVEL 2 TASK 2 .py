import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://books.toscrape.com"

# Get webpage content
response = requests.get(url)

# Check if website loaded successfully
if response.status_code == 200:

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book title sections
    books = soup.find_all("h3")

    # Create CSV file
    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # CSV Header
        writer.writerow(["Book Title"])

        # Extract and save book titles
        for book in books:
            title = book.a["title"]

            print(title)  # Display on screen

            writer.writerow([title])

    print("\nData scraped successfully!")
    print("Data saved in books.csv")

else:
    print("Failed to access the website.")