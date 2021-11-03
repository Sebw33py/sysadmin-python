from python_doc.spiders.python_doc_os import PythonDocOsSpider
from scrapyd_api import ScrapydAPI
from uuid import uuid4

# connect scrapyd service
scrapyd = ScrapydAPI('http://localhost:6800')


def main():
    print("BEGIN")
    settings = {
        'unique_id': str(uuid4()),  # unique ID for each record for DB
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }
    task = scrapyd.schedule('default', 'python_doc', settings=settings)
    print("END")

if __name__ == '__main__':
    main()