from bolt.items import Webpage, Image
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

import scrapy
import json


class GenericSpider(scrapy.Spider):
    name = "generic"

    start_urls = [
        "http://wiprodigital.com"
    ]

    def parse(self, response):
        """

        :param response: scrapy 'response' object that is automatically passed by the framework
        :return: returns an Item object or scrapy Requests to follow
        """
        page = Webpage()
        page['title'] = response.xpath('//title/text()').extract_first()
        page['links'] = self.parse_links(response)
        page['images'] = self.parse_images(response)
        page['status'] = response.status

        yield page

        for link in page['links']:
            yield scrapy.Request(link, callback=self.parse)

    def parse_images(self, response):
        """

        :param response:  scrapy 'response' object that is automatically passed by the framework
        :return: returns a list of images that have been extracted from the page
        """
        images = []
        imageSrc = []
        for image in response.xpath('//img'):
            imageUrl = str(image.xpath('.//@src').extract_first())
            if imageUrl not in imageSrc:
                imageSrc.append(imageUrl)
                imageObj = Image()
                imageObj['src'] = imageUrl
                imageObj['name'] = imageUrl.split('/')[-1]
                images.append(imageObj)
        return list(images)

    def parse_links(self, response):
        """

        :param response: scrapy 'response' object that is automatically passed by the framework
        :return: returns a list of links that are extracted
        """
        links = []

        # Naive way to extract links, later found that scrapy itself support LinkExtractors within a page #
        for link in response.xpath('//a'):
            hrefLink = str(link.xpath('.//@href').extract_first())
            indexOfAnchor = hrefLink.find('#')
            if indexOfAnchor > 0 or indexOfAnchor == -1:
                links.append(hrefLink[0:indexOfAnchor])
        linksSet = set(links)
        return list(linksSet)
