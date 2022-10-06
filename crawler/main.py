from crawler.model import Post
from crawler.functional.crawler import Crawler
import openpyxl
from bs4 import BeautifulSoup
# main function
if __name__ == '__main__':
    crawler = Crawler("https://amis.misa.vn/67142/tim-nguon-hang-thuc-pham/")

    # # Lay ra list category
    # print(crawler.get_list_category());
    #
    # # Lay ra url (khong lay domain)
    # print(crawler.get_url());
    #
    # # Lay ra so luong tu trong bai viet (khong tinh tieu de)
    # print(crawler.get_num_word())
    #
    # # lay ra danh sach cac internal link
    # print(crawler.get_internal_link_list())
    #
    # # lay ra danh sach cac external link
    # print(crawler.get_external_link_list())
    #
    # # lay ra danh sach cac tag (delay)
    # print(crawler.get_tag_list())
    #
    # # xem post do la index hay la noindex
    # print(crawler.index_or_no())
    #
    # # xem post do la follow hay la nofollow
    # print(crawler.follow_or_no())
    #
    # # lay ra hreflang
    # print(crawler.get_hreflang())
    #
    # # Lay ra meta title
    # print(crawler.get_meta_title())
    #
    # # Lay ra meta description
    # print(crawler.get_meta_description())
    #
    # # Lay ra  meta keyword
    #
    # # Lay ra canonical
    # print(crawler.get_canonical_link())

    listHeaders = ["STT","Chuyên mục", "Tác giả","URL cuối","Số lượng từ","Danh sách Internal Link trong bài",
                  "Danh sách External Link trong bài", "Tag", "Index/NoIndex", "follow", "Ahref-Lang", "Meta Title", "Meta Description", "Meta keyword", "canonical"]
    # Bắt đầu tạo file excel
    my_wb = openpyxl.Workbook()
    my_sheet = my_wb.active

    # Tạo header
    for header in listHeaders:
        columnHeader = my_sheet.cell(row=1, column=listHeaders.index(header) + 1)
        columnHeader.value = header
    # Tạo cột số thứ tự
    data = my_sheet.cell(row=2, column=1)
    data.value = 1
    # Tạo cột category
    data = my_sheet.cell(row=2, column=2)
    data.value = crawler.listToString(crawler.get_list_category())
    # Tạo cột url
    urlData = my_sheet.cell(row=2, column=4)
    urlData.value = crawler.get_url()

    # Tạo cột số lượng dữ liệu
    numberOfData = my_sheet.cell(row=2, column=5)
    numberOfData.value = crawler.get_num_word()

    # Tạo cột internalUrl

    internalData = my_sheet.cell(row=2, column=6)
    internalData.value = crawler.listToString(crawler.get_internal_link_list())

    # Tạo cột externalUrl

    externalData = my_sheet.cell(row=2, column=7)
    externalData.value = crawler.listToString(crawler.get_external_link_list())

    # Tạo cột tag
    tagListData = my_sheet.cell(row=2, column=8)
    tagListData.value = ','.join(str(tagData) for tagData in crawler.get_tag_list())

    # Tạo cột xác định index hay noindex
    isIndexData = my_sheet.cell(row=2, column=9)
    isIndexData.value = crawler.index_or_no()

    # Tạo cột xác định folow hay noFollow
    isFollowData = my_sheet.cell(row=2, column=10)
    isFollowData.value = crawler.follow_or_no()

    # Tạo cột hrefLanguage
    hrefLangData = my_sheet.cell(row=2, column=11)
    hrefLangData.value = crawler.get_hreflang()

    # Tạo cột mate title
    metaTitleData = my_sheet.cell(row=2, column=12)
    metaTitleData.value = str(crawler.get_meta_title())

    # Tạo cột meta description
    metaDescriptionData = my_sheet.cell(row=2, column=13)
    metaDescriptionData.value = crawler.get_meta_description()

    # Tạo cột canonicalUrl
    metaCanonicalData = my_sheet.cell(row=2, column=15)
    metaCanonicalData.value = crawler.get_canonical_link()

    my_wb.save("crawl_data.xlsx")
    print('DataFrame is written to Excel File successfully.')