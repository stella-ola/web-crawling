import scrapy


class jumiaphonesSpider(scrapy.Spider):
    name = 'phones'
    start_urls = ['https://www.jumia.com.ng/catalog/?q=samsung+phones' ,
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=2#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=3#catalog-listing'
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=4#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=5#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=6#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=7#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=8#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=9#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=10#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=11#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=12#catalog-listing'
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=13#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=14#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=15#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=16#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=17#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=18#catalog-listing'
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=19#catalog-listing' 
                   'https://www.jumia.com.ng/catalog/?q=samsung+phones&page=20#catalog-listing' 
    ]
    def parse (self, response):
        for products in response.css('div.info'):
            yield {
                'name': products.css('h3.name ::text').get(),
                'price':products.css('div.prc::text').get().replace('₦',''),
            }
        