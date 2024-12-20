import scrapy
import csv
import string


class KompasSpider(scrapy.Spider):
  name = "NewsScraper"
  # allowed_domains = ["okezone.com"]

  start_urls = [
      "https://health.okezone.com",
      "https://health.okezone.com/sehatterkini",
      "https://health.okezone.com/hidupsehat",
      "https://health.okezone.com/medicalcheckup",
      "https://edukasi.okezone.com",
      "https://edukasi.okezone.com/sekolah",
      "https://edukasi.okezone.com/kampus",
      "https://sports.okezone.com",
      "https://bola.okezone.com",
      "https://sports.okezone.com/f1",
      "https://sports.okezone.com/motogp",
      "https://sports.okezone.com/netting",
      "https://sports.okezone.com/basket",
      "https://sports.okezone.com/sportlain",
      "https://travel.okezone.com",
      "https://travel.okezone.com/infowisata",
      "https://travel.okezone.com/destinasi",
      "https://travel.okezone.com/jalan-jalan",
      "https://travel.okezone.com/wisatakuliner"
      ]


  def parse(self, response):

    # ambil link link berita
    article_links = self.getArticleLink(response)
    
    for link in article_links:
      yield scrapy.Request(link, callback=self.parse_article)

  def getArticleLink(self, response):
    if 'okezone' in response.url:
      if 'travel.okezone' in response.url:
        return response.css('a.desc-text::attr(href)').extract()
      else:
        return response.css('a.gabreaking::attr(href)').extract()
    elif 'kompas' in response.url:
    # buat kompas dll
      pass

  def parseOkezone(self, response, url):
    
    # print('konten', konten)
    if 'travel.okezone' in url:
      
      judul = self.remove_text(response.css('.title-article h1::text').get())
      waktu = self.remove_text(response.css('.journalist span::text').get())
      waktu = response.css('.journalist span::text').get()
      waktu = waktu.replace('Jurnalis', '')
      waktu = waktu.replace('"', '')
      waktu = waktu[3::]
      translator = str.maketrans('', '', string.punctuation)
      # Menghapus tanda baca dari teks menggunakan tabel translasi
      waktu = waktu.translate(translator)
      
      kelas = 'pariwisata'
    else:
      judul = self.remove_text(response.css('div.title h1::text').get())
      if 'health.okezone.com' in url:
        waktu = response.css('.tanggal::text').get()
        kelas = 'kesehatan'
      else:
        waktu = response.css('.namerep b::text').get()
        if 'edukasi.okezone.com' in url:
          kelas = 'pendidikan'
        elif 'bola.okezone.com' in url or 'sports.okezone' in url:
          kelas = 'olahraga'
        else:
          return False
        
    konten = self.remove_text(' '.join(response.css('p').xpath('string()').getall()))

    return judul, konten, waktu, kelas

  def parse_article(self, response):
      
      
      url = response.url
      
      if 'okezone' in url:
        result = self.parseOkezone(response, url)
        if result:
          judul, konten, waktu, kelas = self.parseOkezone(response, url)
        else:
          return False

      elif 'kompas' in url:
         self.parseKompas()

      
      # kelas = response.css('li.breadcrumb__item:nth-child(2) span::text').get()

      # Menyimpan data ke dalam file CSV
      with open('okezoneNews.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # print('berhasil')
        # Menulis baris data
        if file.tell() == 0:
            # Menulis nama kolom jika file masih kosong
            writer.writerow(['Judul', 'Waktu', 'URL', 'Kelas', 'Konten'])
        writer.writerow([judul, waktu, url, kelas, konten.strip()])

  def remove_text(self, text):
      # Membuat tabel translasi untuk menghapus tanda baca
      text = text.replace('\n', ' ')
      text = text.replace('\t', ' ')
      # text = text.replace('-', ' ')
      translator = str.maketrans('', '', string.punctuation)
      
      # Menghapus tanda baca dari teks menggunakan tabel translasi
      text = text.translate(translator)
      
      # Menghapus karakter whitespace ekstra
      text = ' '.join(text.split())
      
      return text