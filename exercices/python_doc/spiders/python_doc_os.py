import scrapy


class PythonDocOsSpider(scrapy.Spider):
    name = 'python_doc_os'
    allowed_domains = ['python.org']
    start_urls = ['https://docs.python.org/fr/3/library/os.html']

    def parse(self, response):
        print("[parse] BEGIN")
        print(response)
        print("[parse] END")
