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
        results = response.css('article.message-body').getall()
        
        filename = f'result.html'
        with open(filename, 'w') as f:
            for x in results: 
                f.write(str(x))
            f.close()
            
