from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

def crawl(url, visited=None):
    if visited is None:
        visited = set()
    urls = set()
    if url in visited:
        return urls
    visited.add(url)

    try:
        res = requests.get(url, timeout=10, verify=Fals>
        soup = BeautifulSoup(res.text, "html.parser")
        for a in soup.find_all("a", href=True):
            full_url = urljoin(url, a['href'])
            if urlparse(full_url).netloc == urlparse(ur>
                if full_url not in visited:
                    urls.add(full_url)
                    urls |= crawl(full_url, visited)
    except:
        pass
    return urls

