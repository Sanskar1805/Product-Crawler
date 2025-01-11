import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

def is_product_url(url):
    """Checks if a URL is likely a product page based on patterns."""
    product_patterns = ['/product', '/item', '/dp/', '/p/', '/listing']
    return any(pattern in url for pattern in product_patterns)

def crawl_website(domain, headers, timeout, delay, max_retries):
    """Crawls a website to find product URLs."""
    visited = set()
    product_urls = set()
    queue = [domain]
    
    while queue:
        current_url = queue.pop(0)
        if current_url in visited:
            continue
        
        print(f"Visiting: {current_url}")
        visited.add(current_url)
        
        for _ in range(max_retries):
            try:
                response = requests.get(current_url, headers=headers, timeout=timeout)
                response.raise_for_status()
                break
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}. Retrying...")
                time.sleep(delay)
        else:
            print(f"Failed to fetch {current_url} after {max_retries} retries.")
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        for link in soup.find_all("a", href=True):
            href = urljoin(domain, link['href'])  # Resolve relative URLs
            parsed_url = urlparse(href)
            
            # Filter out external URLs and duplicates
            if parsed_url.netloc != urlparse(domain).netloc or href in visited:
                continue
            
            if is_product_url(href):
                product_urls.add(href)
            else:
                queue.append(href)
        
        time.sleep(delay)  # Respectful crawling

    return product_urls

def main(domains):
    """Main function to crawl multiple domains and output product URLs."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    timeout = 10  # Timeout in seconds
    delay = 2  # Delay between requests in seconds
    max_retries = 3  # Number of retries for failed requests
    
    result = {}
    for domain in domains:
        print(f"\nCrawling domain: {domain}")
        try:
            product_urls = crawl_website(domain, headers, timeout, delay, max_retries)
            result[domain] = list(product_urls)
            print(f"Found {len(product_urls)} product URLs on {domain}")
        except Exception as e:
            print(f"Error crawling {domain}: {e}")
    
    # Save results to file
    with open("product_urls.txt", "w") as f:
        for domain, urls in result.items():
            f.write(f"Domain: {domain}\n")
            for url in urls:
                f.write(f"{url}\n")
            f.write("\n")
    
    print("\nResults saved to product_urls.txt")

if __name__ == "__main__":
    # Example domains for testing
    test_domains = [
        "https://www.amazon.com",
        "https://www.ebay.com",
        "https://www.walmart.com",
        "https://www.bestbuy.com",
        "https://www.newegg.com"
    ]
    main(test_domains)
