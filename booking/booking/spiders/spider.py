import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from booking.items import BookingItem
#24 y 25 de junio

TodosSantos = 'https://booking.com/searchresults.es.html?ss=Todos+Santos&ssne=Todos+Santos&ssne_untouched=Todos+Santos&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1706206&dest_type=city&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
ts_url = [TodosSantos]

Loreto = 'https://www.booking.com/searchresults.es.html?ss=Loreto%2C+Baja+California+Sur%2C+M%C3%A9xico&ssne=Todos+Santos&ssne_untouched=Todos+Santos&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1680155&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=4895a372308f0319&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
lr_url = [Loreto]

IslaAguada = 'https://www.booking.com/searchresults.es.html?ss=Isla+Aguada%2C+Campeche%2C+M%C3%A9xico&ssne=Loreto&ssne_untouched=Loreto&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1671462&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b80ba3956491017e&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
ia_url = [IslaAguada]

Sayulita = 'https://www.booking.com/searchresults.es.html?ss=Sayulita%2C+Nayarit%2C+M%C3%A9xico&ssne=Isla+Aguada&ssne_untouched=Isla+Aguada&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1702968&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=e588a3ad69fd018b&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
sa_url = [Sayulita+f"&offset={25*i}" for i in range(2)]


Mexcaltitán = ''#No hay hoteles 
me_url = []

Compostela = 'https://www.booking.com/searchresults.es.html?ss=Compostela%2C+Nayarit%2C+M%C3%A9xico&ssne=Mexcaltit%C3%A1n%2C+Nayarit%2C+Mexico&ssne_untouched=Mexcaltit%C3%A1n%2C+Nayarit%2C+Mexico&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1658964&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=5240a409574e0269&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
co_url = [Compostela]

Mazunte = 'https://www.booking.com/searchresults.es.html?ss=Mazunte%2C+Oaxaca%2C+M%C3%A9xico&ssne=Compostela&ssne_untouched=Compostela&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=900050716&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=384fa415b33e00d8&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
ma_url = [Mazunte]

Bacalar = 'https://www.booking.com/searchresults.es.html?ss=Bacalar%2C+Quintana+Roo%2C+M%C3%A9xico&ssne=Mazunte&ssne_untouched=Mazunte&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1652041&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=60e3a43cb8ef014f&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
ba_url = [Bacalar+f"&offset={25*i}" for i in range(9)]

IslaMujeres = 'https://www.booking.com/searchresults.es.html?ss=Isla+Mujeres%2C+Quintana+Roo%2C+M%C3%A9xico&ssne=Bacalar&ssne_untouched=Bacalar&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1671478&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3ca6a44ba7890195&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
iu_url = [IslaMujeres+f"&offset={25*i}" for i in range(4)]

Tulum = 'https://www.booking.com/searchresults.es.html?ss=Tulum%2C+Quintana+Roo%2C+M%C3%A9xico&ssne=Isla+Mujeres&ssne_untouched=Isla+Mujeres&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1707023&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=94dca46ad77a037e&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
tu_url = [Tulum+f"&offset={25*i}" for i in range(23)]

ElRosario = '' #No hay hoteles
eo_url = []

Papantla = 'https://www.booking.com/searchresults.es.html?ss=Papantla+de+Olarte%2C+Veracruz%2C+M%C3%A9xico&ssne=El+Rosarito&ssne_untouched=El+Rosarito&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1687314&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=3&search_selected=true&search_pageview_id=b5daa4b7e3710050&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
pa_url = [Papantla]

Sisal = 'https://www.booking.com/searchresults.es.html?ss=Sisal%2C+Yucat%C3%A1n%2C+M%C3%A9xico&ssne=Papantla+de+Olarte&ssne_untouched=Papantla+de+Olarte&label=eco156bi-1BCAEoggI46AdIM1gDaKABiAEBmAEKuAEZyAEM2AEB6AEBiAIBqAIDuALr77qUBsACAdICJGQ1ODBjZTMzLTA0NmUtNGMzZS1hNTA3LTdlNDJmZjViN2I1MNgCBeACAQ&sid=727fe81adc4a2d47b502637ad18231b3&aid=1588647&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id=-1703255&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=6c2aa4c563ca0143&checkin=2022-06-24&checkout=2022-06-25&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
si_url = [Sisal]


start_urls = ts_url+lr_url+ia_url+sa_url+me_url+co_url+ma_url+ba_url+iu_url+tu_url+eo_url+pa_url+si_url

class BookingSpider(CrawlSpider):
	name = 'booking'
	item_count = 0
	allowed_domain = ['https://www.booking.com/']
	pages = 0

	start_urls = start_urls

	rules = {
		Rule(LinkExtractor(
			allow = (),
			restrict_xpaths = ('//div[contains(@class,"dd023375f5")]/h3/a')
			),
			callback = 'parse_item',
		)
	}


	def parse_item(self,response):
		bk_item = BookingItem()
		bk_item['city'] = response.xpath('//div[@class="bui-breadcrumb__text"]/a[contains(@title,"en ")]/text()').extract()
		if bk_item['city'] != None and type(bk_item)==list:
			bk_item['city'] = bk_item['city'][-1]
		bk_item['name'] = response.xpath('//h2[@class="hp__hotel-name"]/text()[2]').extract_first()
		bk_item['stars'] = len(response.xpath('//div[@class="c276b6d5a5"]/span/span/@class').extract())
		bk_item['rating'] = response.xpath('//div[@class="a1b3f50dcd cbb2d85c33 a1f3ecff04 db7f07f643 d19ba76520 f4e25490ec d02f1578ba d17b3fe5e2"]/div[@class="b5cd09854e d10a6220b4"]/text()').extract()
		bk_item['prices'] = response.xpath('//span[@class="prco-valign-middle-helper"]/text()').extract()
		bk_item['quality_price'] = response.xpath('//div[@class = "c-score-bar"][contains(span,"Relación calidad-precio")]/span[2]/text()').extract_first()
		bk_item['comments'] = response.xpath('//div[@class="a1b3f50dcd cbb2d85c33 a1f3ecff04 db7f07f643 d19ba76520 f4e25490ec d02f1578ba d17b3fe5e2"]/div[@class="b1e6dd8416 b48795b3df"]/div[@class="d8eab2cf7f c90c0a70d3 db63693c62"]/text()').extract()
		bk_item['popular_services'] = response.xpath('//div[@class="important_facility"]').extract()
		bk_item['services'] = response.xpath('//ul[@class="bui-list bui-list--text bui-list--icon hotel-facilities-group__list"]/li//text()').extract()
		bk_item['beaches'] = response.xpath('//div[@class="hp_location_block__section_container"][contains(div,"Playas")]/span/text()').extract()
		bk_item['airports'] = response.xpath('//div[@class="hp_location_block__section_container transport_airport"]/span/text()').extract()
		bk_item['url'] = response.url
		yield bk_item

		
		
