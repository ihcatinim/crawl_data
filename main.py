import string

import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://ww5.mangakakalot.tv/manga_list/?type=latest');
# print(res.content)
soup = BeautifulSoup(res.content, "html.parser")
manga_list = []

# print(soup)

list_manga_chapter = {
    'chapter_name':string,
    'chapter_link':string
}
manga_data = {}

for manga in soup.findAll('div', class_='list-truyen-item-wrap'):

    dt_manga = manga.find('a')
    # print(dt_manga)
    if dt_manga is not None:
        id = 0
        id = id + 1
        # manga_data['manga_name']= dt_manga.getText
        # manga_id = str(id+1);
        manga_data['manga_id'] = str(id+1)
        print(id)
        manga_data['manga_img'] = dt_manga.find('img').get('data-src')
        manga_link =manga_data['manga_link']= dt_manga.get('href')
        # print(manga_link)
        Link = 'https://ww5.mangakakalot.tv/' + manga_link
        # print(Link)
        res2 = requests.get(Link)
        soup2 = BeautifulSoup(res2.content, 'html.parser')
        # print('----------------------------------------------------------------')
        # print(manga_id)
        # print("Img:" + "https://ww4.mangakakalot.tv/" + manga_img)
        # print("Link:" + "https://ww4.mangakakalot.tv/" + manga_link)
        # manga_list.append(Manga(manga_id,
        #                         "https://ww4.mangakakalot.tv/" + manga_img,
        #                         "https://ww4.mangakakalot.tv/" + manga_link))
        for chapter in soup2.findAll('div', class_='row'):
            # dt_chapter = chapter.find('span')
            # print(dt_chapter)
            #     print(chapter)
            # print(soup2)
            dt_chapter = chapter.find('a')
            # print(dt_chapter)
            # chapter_name={}
            # chapter_link={}
            if dt_chapter is not None:
                manga_data['chapter_name'] = dt_chapter.get('title')
                manga_data['chapter_link'] = dt_chapter.get('href')
        id=id +1;
        manga_list.append(manga_data)
        json_str = json.dumps(manga_list)
        with open('file.json', 'w') as f:
            f.write(json_str)
