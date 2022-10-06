import time
from crawler.functional.crawler import Crawler
import openpyxl


def open_file(path):
    f = open(path, "r")
    result = f.read()
    id_website = list(result.splitlines())
    list_crawler = []
    for idData in id_website:
        print(idData)
        if idData != "":
            crawler = Crawler("https://amis.misa.vn/" + idData)
            list_crawler.append(crawler)

    return list_crawler


def export_excel(list_crawl, i):
    my_wb = openpyxl.Workbook()
    my_sheet = my_wb.active
    list_headers = ["STT", "Chuyên mục", "Tác giả", "URL cuối", "Số lượng từ", "Danh sách Internal Link trong bài",
                    "Danh sách External Link trong bài", "Tag", "Index/NoIndex", "follow", "Ahref-Lang", "Meta Title",
                    "Meta Description", "Meta keyword", "canonical"]
    index = 1
    for header in list_headers:
        column_header = my_sheet.cell(row=1, column=list_headers.index(header) + 1)
        column_header.value = header
    for idCrawler in list_crawl:
        index += 1
        # Tạo cột số thứ tự
        data = my_sheet.cell(row=index, column=1)
        data.value = index - 1
        # Tạo cột category
        data = my_sheet.cell(row=index, column=2)
        data.value = idCrawler.listToString(idCrawler.get_list_category())
        # Tạo cột url
        url_data = my_sheet.cell(row=index, column=4)
        url_data.value = idCrawler.get_url()

        # Tạo cột số lượng dữ liệu
        number_of_data = my_sheet.cell(row=index, column=5)
        print(idCrawler.get_num_word())
        number_of_data.value = idCrawler.get_num_word()

        # Tạo cột internalUrl

        internal_data = my_sheet.cell(row=index, column=6)
        internal_data.value = idCrawler.listToString(idCrawler.get_internal_link_list())

        # Tạo cột externalUrl

        external_data = my_sheet.cell(row=index, column=7)
        external_data.value = idCrawler.listToString(idCrawler.get_external_link_list())

        # Tạo cột tag
        tag_list_data = my_sheet.cell(row=index, column=8)
        tag_list_data.value = ','.join(str(tagData) for tagData in idCrawler.get_tag_list())

        # Tạo cột xác định index hay noindex
        is_index_data = my_sheet.cell(row=index, column=9)
        is_index_data.value = idCrawler.index_or_no()

        # Tạo cột xác định folow hay noFollow
        is_follow_data = my_sheet.cell(row=index, column=10)
        is_follow_data.value = idCrawler.follow_or_no()

        # Tạo cột hrefLanguage
        href_lang_data = my_sheet.cell(row=index, column=11)
        href_lang_data.value = idCrawler.get_hreflang()

        # Tạo cột meta title
        meta_title_data = my_sheet.cell(row=index, column=12)
        meta_title_data.value = str(idCrawler.get_meta_title())

        # Tạo cột meta description
        meta_description_data = my_sheet.cell(row=index, column=13)
        meta_description_data.value = idCrawler.get_meta_description()

        # Tạo cột canonicalUrl
        meta_canonical_data = my_sheet.cell(row=index, column=15)
        meta_canonical_data.value = idCrawler.get_canonical_link()

    my_wb.save("crawl_data" + i + ".xlsx")
    print('DataFrame is written to Excel File successfully.')


# main function
if __name__ == '__main__':
    listCrawler1 = open_file("idWebsite1.txt")
    print("start export")
    export_excel(listCrawler1, '1')
    time.sleep(5)
    listCrawler2 = open_file("idWebsite2.txt")
    export_excel(listCrawler2, '2')
    time.sleep(5)
    listCrawler3 = open_file("idWebsite3.txt")
    export_excel(listCrawler2, '3')
    time.sleep(5)
    listCrawler4 = open_file("idWebsite4.txt")
    export_excel(listCrawler2, '4')
    time.sleep(5)
    listCrawler5 = open_file("idWebsite5.txt")
    export_excel(listCrawler2, '5')
    time.sleep(5)
    listCrawler6 = open_file("idWebsite6.txt")
    export_excel(listCrawler2, '6')
