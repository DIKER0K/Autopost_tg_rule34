import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import json

ua = UserAgent()

print(ua.random)

proxies = {
    'http': 'socks5://user126136:njm6eh@91.239.62.36:12980',
    'https': 'socks5://user126136:njm6eh@91.239.62.36:12980',
}

header = {'User-Agent': str(ua.random)}

url = []

state = int(input("Сколько страниц загрузить (на каждой странице по 42 фото): "))
indent = int(input("Отступ (по умолчанию 0): "))

total = (state+indent)*42

e = int(0)
while e < 42*state:
    URL_TEMPLATE = (f"https://rule34.xxx/index.php?page=post&s=list&tags=-femboy+-abs+-furry+-futanari+-gay+-fat"
                    f"+-huge_breasts+-huge_ass+-anthro+-balloons+-animal+-animal_penis+-big_breasts+-censored+-armor"
                    f"+-domestic_dog+-solo_male+-fat_arms+-2boys+-horse+-3boys+-male_only+-blue_skin+-hybrid_penis"
                    f"+-fart+-captivemimic++-fat_ass++-transgender+-1animal+-animal_genitalia+-absurd_res+-intersex"
                    f"+-wolf+-ambiguous_gender+-paws+-ponytail++-shitting++-red_body+-male+-beastmilk+-cyndaquil"
                    f"+-shark+-2d_%28artwork%29+-glitch+-tentacle+-bunny_boy+-animated+-hyper+-pokemon+-purple_body"
                    f"+-arknights+-blood+-comic+-overweight+-3d+-video+-mushroom+-african+-big_penis+-anilingus"
                    f"+-size_difference+-adult+-alien+-rimjob+-inflatable+-inflatable_transformation+-manga+-timfy3d"
                    f"+-fully_clothed+-sf5+-1futa+-high_heels+-overstimulation+-tagme+-fan_character+-visual_novel"
                    f"+-sketch+-satyr+-clothes+-tomboy+-dildo+-white_body+-text+-pregnant+-bent_over+-clothed"
                    f"++-takerskiy+-dark_skin+-monkey+-the_incredibles+-demon+-fortnite+-funny+-gigantic_breasts"
                    f"+-countryhumans+&pid={e+(indent*42)}")
    r = requests.get(URL_TEMPLATE, headers=header)

    soup = bs(r.text, "html.parser")

    for i in soup.find_all('span', class_='thumb'):
        url_index = (i.a['href'])
        url_img = ("https://rule34.xxx" + url_index)
        url.append(url_img)

    e += 42

print("Всего фото: ", len(url))
a = 0

list_image = []
list_alt = []

while a < len(url):
    r_img = requests.get(url[a], headers=header)
    a += 1
    print("Загрузка URL фото №:", a)
    soup = bs(r_img.text, "html.parser")
    img = soup.find_all('div', class_="flexi")
    for image in img:
        if image.img:
            image = (image.img['src'])
            list_image.append(image)
    for alt in img:
        if alt.img:
            alt = (alt.img['alt'])
            list_alt.append(alt)
full_post = dict(zip(list_image, list_alt))

with open("full_post.json", "w") as file:
    print("Сохранение фото и описания в full_post.json...")
    json.dump(full_post, file, indent=4, ensure_ascii=False)
