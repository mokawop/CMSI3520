import mechanicalsoup as ms  
import redis
from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read('example.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)

browser = ms.StatefulBrowser()
url = "https://en.wikipedia.org/wiki/BMW"
browser.open(url)
html = browser.page
html = str(html)

es.index(
 index="webpages",
 document={
  'url': url,
  'html': html
 })

result = es.search(
 index="webpages",
  query={
    'match': {'html': 'BMW'}
  }
 )

#print(result['hits']['hits'])
print("Total documents found: ", result['hits']['total']['value'])

