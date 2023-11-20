import mechanicalsoup as ms  
import redis

def crawl(r, browser, link):
    browser.open(link)
    # parse for links
    atags = browser.page.find_all("a")
    hrefs = [a.get("href") for a in atags]

    # add links to redis queue
    domain = "https://en.wikipedia.org"
    links = [(domain + href) for href in hrefs if href and href.startswith("/wiki/")]
    r.lpush("links", *links)

r = redis.Redis()
#root url  
browser = ms.StatefulBrowser()
# download webpage
start_url = "https://en.wikipedia.org/wiki/BMW"
r.rpush("links", start_url)

while link := r.rpop("links"):
    crawl(r, browser, link)
    print("crawling " + str(link))

