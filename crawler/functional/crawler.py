from bs4 import BeautifulSoup
import requests
import html5lib


def is_internal_link(url):
    if ((url.find('http') < 0) or (url.find('//amis.misa.vn') > 0)) and (url != '#') and (url.find('tel', 0, 3) < 0) and (url.find('mailto', 0, 6) < 0):
        return True
    return False


def is_external_link(url):
    if (url.find('http') >= 0) and (url.find('//amis.misa.vn') < 0):
        return True
    return False


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
        internal_a_list = self.html_response.find_all('a', href=True)
        links = []
        for a_tag in internal_a_list:
            links.append(a_tag['href'])
        # filter internal link
        internal_links = []
        for link in links:
            if is_internal_link(link):
                internal_links.append(link)

        print(internal_links)

    def get_external_link_list(self):
        pass
        external_a_list = self.html_response.find_all('a', href=True)
        links = []
        for a_tag in external_a_list:
            links.append(a_tag['href'])
        # filter external link
        external_links = []
        for link in links:
            if is_external_link(link):
                external_links.append(link)

        print(external_links)

    def get_tag_list(self):
        pass
        tag_tag_list = self.html_response.select(".td-tags a")
        tags = []
        if len(tag_tag_list) > 0:
            for tag in tag_tag_list:
                # print(tag)
                tags.append(tag)
        else:
            print("don't have tag")

    def index_or_no(self):
        pass
        meta_robots = self.html_response.find_all('meta', {'name': ['robots', 'googlebot', 'bingbot']})
        for meta in meta_robots:
            # print(meta['content'])
            if meta['content'].find('noindex') >= 0:
                # print(meta['content'])
                return 'noindex'
        return 'index'

    def follow_or_no(self):
        pass
        meta_robots = self.html_response.find_all('meta', {'name': ['robots', 'googlebot', 'bingbot']})
        for meta in meta_robots:
            # print(meta['content'])
            if meta['content'].find('nofollow') >= 0:
                # print(meta['content'])
                return 'nofollow'
        return 'follow'

    def get_hreflang(self):
        pass
        link_tags = self.html_response.find('link', {'hreflang': True})
        # for link_tag in link_tags:
        return link_tags['hreflang']

    def get_meta_description(self):
        pass
        meta_descriptions = self.html_response.find('meta', {'name': 'description'})
        meta_des = meta_descriptions['content']
        return meta_des

    def get_canonical_link(self):
        pass
        canonical_tag = self.html_response.find('link', {'rel': 'canonical'})
        return canonical_tag['href']



