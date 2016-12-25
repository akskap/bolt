import scrapy

class GenericSpider(scrapy.Spider):
	
	name = "generic"

	start_urls = [
		"http://wiprodigital.com"
	]

	def parse(self, response):
		print response.status
