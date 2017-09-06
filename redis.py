#-*- coding: utf-8 -*-                                                                                         
import scrapy                                                                                                  
from redis import Redis                                                                                        
                                                                                                               
class RedisSpider(scrapy.Spider):                                                                              
    name = 'redis'                                                                                             
    allowed_domains = ['haodf.com']                                                                            
    start_urls = ['http://haodf.com/']                                                                         
    redis_key = 'myspider:58_urls'                                                                             
                                                                                                               
    def parse(self, response):                                                                                 
        r = Redis(host='34.224.8.126',port=6379,password='ClLBIss1709g',db=0)                                  
        print('OK')                                                                                            
        r.lpush('testurl', 'http://www.haodf.com/')                                                   
        print('__OK')                                                                                          
        pass  