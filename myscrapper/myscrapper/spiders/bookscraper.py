import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def get_next_url(self, next_page):
        if next_page:
            if "catalogue" not in next_page:
                next_page = "catalogue/" + next_page
            next_url = BookscraperSpider.start_urls[0] + "/" + next_page
            return next_url

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            url = book.css("h3 a::attr('href')").get()
            next_absolute_url = self.get_next_url(url)
            if next_absolute_url:
                yield response.follow(next_absolute_url, callback=self.parse_book)

        next_page = response.css(".next a::attr('href')").get()

        if next_page:
            if "catalogue" not in next_page:
                next_page = "catalogue/" + next_page
            next_url = BookscraperSpider.start_urls[0] + "/" + next_page

        yield response.follow(next_url, callback=self.parse)

    def parse_book(self, response):
        table_rows = response.css("table tr")

        star_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "zero": "0",
        }
        rating = response.css("p.star-rating").attrib["class"]

        yield {
            "name": response.xpath(
                '//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()'
            ).get(),
            "product_desc": response.css("#product_description + p::text").get(),
            "url": response.url,
            "price (Exl tax)": table_rows[2].css("td::text").get(),
            "price (Inc tax)": table_rows[3].css("td::text").get(),
            "tax": table_rows[4].css("td::text").get(),
            "availability": table_rows[5].css("td::text").get(),
            "num_reviews": table_rows[6].css("td::text").get(),
            "rating": f"{star_map[rating.split()[-1].lower()]}/5",
        }
