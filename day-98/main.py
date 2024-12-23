from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv
import os
from dotenv import load_dotenv

load_dotenv()

# List of websites to test
websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.facebook.com",
    "https://www.amazon.com"
]

# Set up Selenium WebDriver (use ChromeDriver here)
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    chrome_options.add_argument("--disable-gpu")  # Optional for better performance
    service = Service(os.environ['driver_path'])  # Replace with the actual path to your chromedriver
    return webdriver.Chrome(service=service, options=chrome_options)

# Test website availability and response time
def test_websites(driver, websites):
    results = []
    for website in websites:
        try:
            print(f"Testing {website}...")
            start_time = time.time()  # Start timer
            driver.get(website)  # Navigate to the website
            load_time = time.time() - start_time  # Calculate load time
            status = "Available" if driver.title else "Unavailable"
            results.append({"Website": website, "Status": status, "Load Time (s)": round(load_time, 2)})
        except Exception as e:
            results.append({"Website": website, "Status": "Error", "Load Time (s)": "N/A"})
            print(f"Error testing {website}: {e}")
    return results

# Save results to CSV
def save_to_csv(results, filename="website_performance.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Website", "Status", "Load Time (s)"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved to {filename}")

# Main function
if __name__ == "__main__":
    driver = setup_driver()
    try:
        results = test_websites(driver, websites)
        save_to_csv(results)
    finally:
        driver.quit()  # Close the browser
