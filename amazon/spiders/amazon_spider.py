import scrapy
from ..items import AmazonItem
from scrapy.loader import ItemLoader


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/s?bbn=4&rh=n%3A283155%2Cn%3A%211000%2Cn%3A4%2Cp_n_feature_five_browse-bin%3A2578999011%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1599381392&rnid=1250225011&ref=lp_2578999011_nr_p_n_publication_date_0']

    def parse(self, response):
        l = ItemLoader(item= AmazonItem(), response=response)
        # extracting info
        l.add_css('product_name','.a-color-base.a-text-normal::text')
        l.add_css('author','.a-size-base.a-link-normal:nth-child(2)::text')
        l.add_css('price','.a-offscreen')
        l.add_css("image_link", '.s-image::attr(src)')
        l.add_css('stars',".a-icon-alt::text")

        yield l.load_item()
        next_page = response.css('li.a-last ::attr(href)').extract_first()
        next_page = response.urljoin(next_page)
        yield scrapy.Request(url = next_page,callback=self.parse)
