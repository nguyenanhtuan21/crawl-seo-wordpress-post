from bs4 import BeautifulSoup
import requests
import html5lib


class Crawler:
    def __init__(self, url):
        pass
        html_text = requests.get(url)
        self.html_response = BeautifulSoup(html_text.text, 'lxml')

    def get_meta_title(self):
        return self.html_response.title.string

    def get_list_category(self):
        lst_category = self.html_response.find_all('a', {'class': 'entry-crumb'})
        lst_category_name = []
        for cat in lst_category:
            lst_category_name.append(cat.get_text())
        print(lst_category_name)

    def get_url(self):
        url_tag = self.html_response.find('meta', {'property': 'og:url'})
        print(url_tag['content'])

    def get_num_word(self):
        content_post = self.html_response.find('div', {'class': 'td-post-content'})
        num_word = len(content_post.text.split())
        print(num_word)

    def get_internal_link_list(self):
        pass

    def get_external_link_list(self):
        pass




