**Website Crawler for Product URLs
Overview:**
This project is a Python-based web crawler designed to extract product-related URLs from specified websites. By identifying patterns such as /product, /item, or /listing, the crawler efficiently scans pages and consolidates results into a downloadable text file. It is lightweight, scalable, and adheres to web scraping best practices, ensuring compliance with server policies through retries and delays.

The project is deployed via GitHub Actions, enabling seamless automation of the crawling process with just a few clicks.

**Features:**
1) Efficient Crawling: Identifies and collects product-related URLs based on predefined patterns.
2) Polite Scraping: Includes retries, delays, and timeout settings to avoid overloading servers.
3) Automated Pipeline: Fully integrated with GitHub Actions for easy execution and artifact retrieval.

**How It Works:**
1) Input Domain List: The script scans websites from a list of domains specified in the code.
2) Process URLs: Filters out non-product pages and collects product-related links.
3) Save Results: Outputs all extracted product URLs to a file, product_urls.txt.

**How to Run the Deployed Pipeline**
1. Access the GitHub Repository
Go to the GitHub repository where the project is hosted. Ensure you have the required permissions to trigger workflows.

2. Trigger the Workflow
Navigate to the Actions tab in the repository.
Select the workflow titled Python Crawler from the list of workflows.
Click the Run Workflow button on the top-right corner.
Optionally, input custom parameters if the workflow supports them (e.g., domain list, delay, retries).

3. Monitor the Workflow
Once started, the workflow will display logs of the crawling process in real-time.
Logs will include:
URLs visited
Errors encountered (if any)
Progress updates

4. Retrieve the Results
After the workflow completes, scroll to the Artifacts section on the workflow summary page.
Download the product_urls.txt file containing all extracted product URLs.

**Example Workflow Run:**
1. Open the repository’s Actions tab.
2. Trigger the Python Crawler workflow.
3. Monitor progress and wait for the job to complete.
4. Download the product_urls.txt artifact to view the results.

**Technical Details:**
****Language**:** Python 3.x
**Libraries Used:**
requests for HTTP requests
beautifulsoup4 for HTML parsing
urllib.parse for URL manipulation
**Deployment:** GitHub Actions for automation
**Output:** Consolidates product URLs into a single file.
