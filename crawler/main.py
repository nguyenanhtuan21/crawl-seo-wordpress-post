from crawler.model import Post
from crawler.functional.crawler import Crawler

# main function
if __name__ == '__main__':
    crawler = Crawler("https://amis.misa.vn/67142/tim-nguon-hang-thuc-pham/")

    # Lay ra list category
    crawler.get_list_category()

    # Lay ra url (khong lay domain)
    crawler.get_url()

    # Lay ra so luong tu trong bai viet (khong tinh tieu de)
    crawler.get_num_word()

    # lay ra danh sach cac internal link
    crawler.get_internal_link_list()

    # lay ra danh sach cac external link
    crawler.get_external_link_list()

    # lay ra danh sach cac tag (delay)
    crawler.get_tag_list()

    # xem post do la index hay la noindex
    print(crawler.index_or_no())

    # xem post do la follow hay la nofollow
    print(crawler.follow_or_no())

    # lay ra hreflang
    print(crawler.get_hreflang())

    # Lay ra meta title
    print(crawler.get_meta_title())

    # Lay ra meta description
    print(crawler.get_meta_description())

    # Lay ra  meta keyword

    # Lay ra canonical
    print(crawler.get_canonical_link())








