from crawler.model import Post
from crawler.functional.crawler import Crawler


# main function
if __name__ == '__main__':
    crawler = Crawler("https://amis.misa.vn/65285/tro-choi-team-building-trong-nha/")

    # Lay ra meta title
    print(crawler.get_meta_title())

    # Lay ra list category
    crawler.get_list_category()

    # Lay ra url (khong lay domain)
    crawler.get_url()

    #Lay ra so luong tu trong bai viet (khong tinh tieu de)
    crawler.get_num_word()

    #lay ra danh sach cac internal link
    crawler.get_internal_link_list()