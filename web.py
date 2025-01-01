import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL of the website you want to scrape
url = "https://example-blog.com"

# Step 2: Send a GET request to the website
response = requests.get(url)

# Step 3: Check the response status
if response.status_code == 200:
    # Step 4: Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 5: Find elements containing the information you need
    # In this case, we'll look for article titles inside <h2> tags
    titles = soup.find_all('h2', class_='post-title')  # Adjust the tag and class based on the website's structure
    
    print("Article Titles:")
    for title in titles:
        print(title.text.strip())  # Strip removes leading/trailing whitespace
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
