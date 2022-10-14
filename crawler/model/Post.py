# Declare post object for crawl data from WordPress

class Post:
    def __init__(self, order, category, url, word_num, internal_link, external_link, tag, index,
                 ahref_lang, meta_title, meta_description, meta_keyword, canonical):
        self.order = order
        self.category = category
        self.url = url
        self.word_num = word_num
        self.internal_link = internal_link
        self.external_link = external_link
        self.tag = tag
        self.index = index
        self.ahref_lang = ahref_lang
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keyword = meta_keyword
        self.canonical = canonical

    def __str__(self):
        return self.meta_title
