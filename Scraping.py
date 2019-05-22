import scrapy

class QuotesSpyder(scrapy.Spyder):
  
  name = 'pip'
  
  def start_requests(self):
    url=[]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)
      
  def parse(self, response): #Analisis de gramatica 
    pagina = response.url.split("/")[-2]
    filename = 'pip-%s.html' % page 
    
    with open (filename,'wb') as f:
      f.write(response.body)
    self.log('Archivo Creado %s' % fileame)
