from django.views.generic import ListView
from bs4 import BeautifulSoup
import requests


class NewsList(ListView):
    template_name = "pages/news_list.html"

    def get_queryset(self):
        url = "https://news.yahoo.co.jp/search?p=%E3%82%B2%E3%83%BC%E3%83%A0&ei=utf-8"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        a_tags = soup.select("li.newsFeed_item-normal > a", limit=5)
        object_list = []
        for a_tag in a_tags:
            link = a_tag.get('href')
            div = a_tag.select_one('div > div.newsFeed_item_text')
            title = div.select_one('div.newsFeed_item_title').text
            news_r = requests.get(link)
            news_soup = BeautifulSoup(news_r.content, 'lxml')
            body = news_soup.select_one('div.article_body > div > p').text[:150] + "..."

            obj = {
                "link": link,
                "title": title,
                "body": body
            }
            object_list.append(obj)

        return object_list
