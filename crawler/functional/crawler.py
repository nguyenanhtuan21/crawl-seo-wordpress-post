from bs4 import BeautifulSoup
import requests
# import html5lib


def is_internal_link(url):
    if ((url.find('http') < 0) or (url.find('//amis.misa.vn') > 0)) and (url != '#') and (url.find('tel', 0, 3) < 0) \
            and (url.find('mailto', 0, 6) < 0):
        return True
    return False


def is_external_link(url):
    if (url.find('http') >= 0) and (url.find('//amis.misa.vn') < 0):
        return True
    return False


class Crawler:
    def __init__(self, url):
        try:
            html_text = requests.get(url, timeout=10)
            self.html_response = BeautifulSoup(html_text.text, 'lxml')
        except requests.exceptions.Timeout:
            self.html_response = "TIME OUT"

    def get_meta_title(self):
        if self.html_response == "TIME OUT":
            result = "No Data"
        else:
            result = self.html_response.title.string
        return result

    def get_author(self):
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            lst_author = self.html_response.find_all('meta', {'name': 'author'})
            author = lst_author[0]['content']
            return author

    def get_list_category(self):
        lst_category_name = []
        if self.html_response == "TIME OUT":
            lst_category_name = []
        else:
            lst_category = self.html_response.find_all('a', {'class': 'entry-crumb'})
            for cat in lst_category:
                lst_category_name.append(cat.get_text())

        return lst_category_name

    def get_url(self):
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            url_tag = self.html_response.find('meta', {'property': 'og:url'})
            return url_tag['content']

    def get_num_word(self):
        if self.html_response == "TIME OUT":
            return 0
        else:
            content_post = self.html_response.find('div', {'class': 'td-post-content'})
            num_word = len(content_post.text.split())
            return num_word

    def get_internal_link_list(self):
        if self.html_response == "TIME OUT":
            return []
        else:
            internal_a_list = self.html_response.find_all('a', href=True)
            links = []
            for a_tag in internal_a_list:
                links.append(a_tag['href'])
            # filter internal link
            internal_links = []
            for link in links:
                if is_internal_link(link):
                    internal_links.append(link)

            return internal_links

    def get_external_link_list(self):
        if self.html_response == "TIME OUT":
            return []
        else:
            external_a_list = self.html_response.find_all('a', href=True)
            links = []
            for a_tag in external_a_list:
                links.append(a_tag['href'])
            # filter external link
            external_links = []
            for link in links:
                if is_external_link(link):
                    external_links.append(link)

            return external_links

    def get_tag_list(self):
        if self.html_response == "TIME OUT":
            return ""
        else:
            tag_tag_list = self.html_response.select(".td-tags a")
            tags = []
            if len(tag_tag_list) > 0:
                for tag in tag_tag_list:
                    tags.append(tag.text)
                return tags
            else:
                return ""

    def index_or_no(self):
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            meta_robots = self.html_response.find_all('meta', {'name': ['robots', 'googlebot', 'bingbot']})
            for meta in meta_robots:
                # print(meta['content'])
                if meta['content'].find('noindex') >= 0:
                    # print(meta['content'])
                    return 'noindex'
            return 'index'

    def follow_or_no(self):
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            meta_robots = self.html_response.find_all('meta', {'name': ['robots', 'googlebot', 'bingbot']})
            for meta in meta_robots:
                # print(meta['content'])
                if meta['content'].find('nofollow') >= 0:
                    # print(meta['content'])
                    return 'nofollow'
            return 'follow'

    def get_hreflang(self):
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            link_tags = self.html_response.find('link', {'hreflang': True})
            # for link_tag in link_tags:
            return link_tags['hreflang']

    def get_meta_description(self):
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            meta_descriptions = self.html_response.find('meta', {'name': 'description'})
            meta_des = meta_descriptions['content']
            return meta_des

    def get_canonical_link(self):
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            canonical_tag = self.html_response.find('link', {'rel': 'canonical'})
            return canonical_tag['href']

    def get_date_published(self):
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            lst_published = self.html_response.find_all('meta', {'property': 'article:published_time'})
            date_published = lst_published[0]['content']
            return date_published

    def get_date_modified(self):
        date_modified = ""
        if self.html_response == "TIME OUT":
            return "No Data"
        else:
            lst_modified = self.html_response.find_all('meta', {'property': 'article:modified_time'})
            lst_modified1 = self.html_response.find_all('meta', {'itemprop': 'datePublished'})
            if len(lst_modified) > 0:
                date_modified = lst_modified[0]['content']
            if len(lst_modified1) > 0:
                date_modified = lst_modified1[0]['content']
            return date_modified

    @staticmethod
    def list_to_string(s):
        string = ", ".join(s)
        return string
