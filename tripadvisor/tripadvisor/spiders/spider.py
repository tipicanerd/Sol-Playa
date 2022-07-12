import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from tripadvisor.items import TripadvisorItem

#24 y 25 de junio
"""
Mexcaltitán NO HAY HOTELES
ElRosarito NO HAY HOTELES
"""
class tripAdvisorSpider(CrawlSpider):
	name = 'tripadvisor'
	item_count = 0
	allowed_domain = ['https://www.tripadvisor.com.mx']
	pages = 0
	start_urls = [
	"https://www.tripadvisor.com.mx/Hotels-g150777-Todos_Santos_Baja_California-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g150772-Loreto_Baja_California-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g6368948-Isla_Aguada_Yucatan_Peninsula-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g445056-Sayulita_Pacific_Coast-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g1767159-Compostela_Pacific_Coast-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g658264-Mazunte_Southern_Mexico-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g1202648-Bacalar_Yucatan_Peninsula-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g150810-Isla_Mujeres_Yucatan_Peninsula-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g150813-Tulum_Yucatan_Peninsula-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g1202651-Papantla_Central_Mexico_and_Gulf_Coast-Hotels.html",
	"https://www.tripadvisor.com.mx/Hotels-g2550231-Sisal_Yucatan_Peninsula-Hotels.html"
	]

	rules = {
		Rule(LinkExtractor(
			allow = (),
			restrict_xpaths = ('//div[contains(@class,"listing_title")]/a')
			),
			callback = 'parse_item',
		),
		Rule(LinkExtractor(
			allow=(),
			restrict_xpaths= ('//div[@class="unified ui_pagination standard_pagination ui_section listFooter"]/a[@class="nav next ui_button primary"]')
			)
		)
	}

	

	def parse_item(self,response):
		ta_item = TripadvisorItem()
		ta_item['city'] = response.xpath('/html/body/div[1]/div/div[2]/div[6]/div/div/div/div[2]/ul/li[4]/a/span/text()').extract()
		ta_item['name'] = response.xpath('//h1/text()').extract_first()
		ta_item['stars'] = response.xpath('//div[@class="drcGn _R MC S4 _a H"]/span/*[local-name()="svg"]/@aria-label').extract()
		ta_item['rating'] = response.xpath('//span[@class="bvcwU P"]/text()').extract_first()
		ta_item['prices'] = response.xpath('//span[@class="fnypd Z1 _U"]/text()').extract()
		ta_item['quality_price'] = response.xpath('//div[@class="cmZRz dfnfs"]/span/@class').extract()
		ta_item['comments'] = response.xpath('//span[@class="btQSs q Wi z Wc"]/text()').extract()
		ta_item['services'] = response.xpath('//div[@class="exmBD K"]/div/text()').extract()
		ta_item["url"] = response.url

		yield ta_item

		
		
