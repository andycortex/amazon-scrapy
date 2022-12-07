import scrapy

reviews_url = 'https://www.amazon.com/product-reviews/{}'
asin_list = ['B00DBL0NLQ']

class ReviewsSpider(scrapy.Spider):
    name = 'reviews'

    def start_requests(self):
        for asin in asin_list:
            url = reviews_url.format(asin)
            yield scrapy.Request(url)

    def parse(self, response):
        for review in response.css('[data-hook="review"]'):
            item = {
                'name': review.css('.a-profile-name ::text').get(),
                'start': review.css('[data-hook="review-date"] ::text').get(),
                'title': review.css('[data-hook="review-title"] span ::text').get(),
                'review': review.xpath('.//*[@data-hook="review-body"]').get()
            }
            yield item
        