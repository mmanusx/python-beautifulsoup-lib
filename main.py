# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
# import lxml // eğer site xml ile yazılmışsa parse etmek için bu ktp

with open("website.html", encoding="utf-8") as file: # emojiden dolayı encoding hatası verdi, utf-8 olduğunu belirttim
    contents = file.read()
    # print(contents) bütün siteyi bir stringin içine attı ve yazabiliyor
    # print(type(contents)) stringin içinden elementleri seçmek için BS ktp kullanılacak


soup = BeautifulSoup(contents, "html.parser") ### Parse işlemi # site lxml ise ktp import edildikten sonra "lxml" yazılır
# print(soup.title)
# print(soup.title.name) # name of the title tag is also "title"
# print(soup.title.string) # title elementinin içindeki stringi verir
# print(soup.prettify()) # print html file with indentation to console
# print(soup.a) # birden fazla element varsa ilk bulduğu elementi tutar
# istediğimiz tüm elementleri tutmak için doc tan find_all() fonksiyonunu buldum
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href")) # achor tag ların href link kısımlarını aldım
    #pass

heading = soup.find(name="h1", id="name") # birtane olduğu için find_all() kullanmadık
print(heading)

section_heading = soup.find(name="h3", class_="heading") # class keyword is reserved keyword with python yani python bu kelimeyi kullanıyor, bu yüzden kütüphane de class yerine class_ attribute yapmışlar
# print(section_heading.getText()) elementin içindeki texti verir
print(section_heading.get("class")) # belirli attribute deki değeri döndürür class ı heading

############## Aynı elementden birden fazla olduğunda sorun çıkıyor
############## Bunu engellemek için o elementin neyi eşsiz diye bakmamız lazım

# ??? analamadığım yer bazı yerlerde find bazı yerlerde select kullanılması aradaki fark???
# find yada find_all tag, class, id de // select() css syntax da kullanılıyor childirin  olaylarında "h1 a{}" yapmak istediğimizde

# company_url = soup.select_one(selector="p a") # select_one select den farklı yalnızca ilk eşeleşeni alır
# print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings) # liste dönecek
