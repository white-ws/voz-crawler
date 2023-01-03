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
        commentSelectors = response.css('article.message-body')
        
        filename1 = f'result.tsv'
        filename2 = f'exception.txt'

        
        with open(filename1, 'a') as f1:
            with open(filename2, 'a') as f2:
                for commentSelector in commentSelectors:
                    if len(commentSelector.css('div ul')) == 0:
                        # handle bad case
                        stripped = filter(lambda s: s != '\n', commentSelector.css('div.bbWrapper *::text').getall()) 
                        text = '\n'.join(stripped)
                        f2.write(text)
                        f2.write("\n=====================================================================\n")
                    else:
                        # handle legit case
                        for selector in commentSelector.css('div ul'):
                            stripped = filter(lambda s: s != '\n', selector.css('li *::text').getall()) 
                            text = '\t'.join(stripped)
                            f1.write(text + "\n")
                f2.close()
            f1.close()
        
        next_page = response.css('a.pageNav-jump--next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

            
