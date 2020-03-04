import scrapy


class QuotesSpider(scrapy.Spider):
    def start_requests(self):
        urls = ["https://mtl.gzhuibei.com/images/img/20713/1.jpg",
                "https://mtl.gzhuibei.com/images/img/20713/56.jpg"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        page = response.url.split("/")[-2]
        filename = 'pic-%s.jpg' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

