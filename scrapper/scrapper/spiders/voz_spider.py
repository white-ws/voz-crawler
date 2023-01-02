import scrapy


class VozSpider(scrapy.Spider):
    name = "voz"

    def start_requests(self):
        urls = [
            'https://voz.vn/t/thread-tong-hop-chia-se-ve-muc-luong-tai-cac-cong-ty-part-2.515355',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # results = response.css('article.message-body div.bbWrapper').getall()
        commentSelectors = response.css('article.message-body')
        
        filename = f'result.html'

        # handle bad case
        with open(filename, 'w') as f:
            for selector in commentSelectors:
                stripped = filter(lambda s: s != '\n', selector.css('div.bbWrapper *::text').getall()) 
                text = '\n'.join(stripped)
                f.write(text)
                f.write("\n=====================================================================\n")
            f.close()
            
