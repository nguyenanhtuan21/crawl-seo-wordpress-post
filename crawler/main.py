from crawler.model import Post
from crawler.functional.crawler import Crawler
import openpyxl
from bs4 import BeautifulSoup
# main function
if __name__ == '__main__':
    crawler = Crawler("https://amis.misa.vn/67142/tim-nguon-hang-thuc-pham/")

    # Lay ra list category
    print(crawler.get_list_category());

    # Lay ra url (khong lay domain)
    print(crawler.get_url());

    # Lay ra so luong tu trong bai viet (khong tinh tieu de)
    print(crawler.get_num_word())

    # lay ra danh sach cac internal link
    print(crawler.get_internal_link_list())

    # lay ra danh sach cac external link
    print(crawler.get_external_link_list())

    # lay ra danh sach cac tag (delay)
    print(crawler.get_tag_list())

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
    # column1 = "Chuyên mục"
    # column2= "Url cuối"
    #
    # marks_data = pd.DataFrame({column1:crawler.get_list_category(), column2: crawler.get_url()})
    #
    # # determining the name of the file
    # file_name = 'Data.xlsx'
    #
    # # saving the excel
    # marks_data.to_excel(file_name)
    listHeaders = ["Chuyên mục", "Tác giả","URL cuối","Số lượng từ","Danh sách Internal Link trong bài",
                  "Danh sách External Link trong bài", "Tag", "Index/NoIndex", "follow", "Ahref-Lang", "Meta Title", "Meta Description", "Meta keyword", "canonical"]
    my_wb = openpyxl.Workbook()
    my_sheet = my_wb.active
    for header in listHeaders:
        columnHeader = my_sheet.cell(row=1, column=listHeaders.index(header) + 1)
        columnHeader.value = header

    for category in crawler.get_list_category():
        data = my_sheet.cell(row=crawler.get_list_category().index(category)+2, column=1)
        data.value = category

    urlData = my_sheet.cell(row=2, column=3)
    urlData.value = crawler.get_url()

    numberOfData = my_sheet.cell(row=2, column=4)
    numberOfData.value = crawler.get_num_word()
    for internalUrl in crawler.get_internal_link_list():
        internalData = my_sheet.cell(row=crawler.get_internal_link_list().index(internalUrl)+2, column=5)
        internalData.value = internalUrl

    for externalUrl in crawler.get_external_link_list():
        internalData = my_sheet.cell(row=crawler.get_external_link_list().index(externalUrl)+2, column=6)
        internalData.value = externalUrl

    for tagList in crawler.get_tag_list():
        tagListData = my_sheet.cell(row=crawler.get_tag_list().index(tagList)+2, column=7)
        soup = BeautifulSoup(tagList)
        p_tag_text = soup.get_text()
        print(p_tag_text)
        print(type(p_tag_text))

        print(type(tagList))
    my_wb.save("sample_data3.xlsx")
    print('DataFrame is written to Excel File successfully.')







