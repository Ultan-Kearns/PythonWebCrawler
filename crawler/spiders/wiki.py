import scrapy

urls = [
    'https://en.wikipedia.org/wiki/Portal:History'
]
class wiki(scrapy.Spider):
    name = "wiki"
    def start_requests(self):
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'wiki-%s.html' % page
        with open(filename, 'wb') as f:
            #write out the body
            f.write(response.body)
        #Print out save message
        self.log('Saved file %s' % filename)
