import requests
from bs4 import BeautifulSoup
import json
import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
# Send a GET request to the website

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://intern2grow.onrender.com/programs')
html = driver.page_source

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

print(soup)

# Find all the program divs
program_divs = soup.find_all("div", class_="programs_programWrapper__7HVj9")

# Create a list to store the program details
programs = []

# Extract the details for each program
for program_div in program_divs:
    # Extract the title
    title = program_div.find("h3").get_text(strip=True)
    
    # Extract the description
    desc = program_div.find("p").get_text(strip=True)
    
    # Extract the tools
    tools = [tool.get_text(strip=True) for tool in program_div.find_all("span", class_="programs_programWrapperSkillWrapper__kGKoP")]
    
    # Create a dictionary for the program details
    program = {
        "title": title,
        "desc": desc,
        "tools": tools
    }
    
    # Add the program details to the list
    programs.append(program)

# Create a JSON object
json_output = json.dumps(programs, indent=4)

# Print the JSON output
print(json_output)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_output)

print('Done')
