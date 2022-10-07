import time
from crawler.functional.crawler import Crawler
import openpyxl
import _thread


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


def export_excel(path, i):
    my_wb = openpyxl.Workbook()
    my_sheet = my_wb.active
    list_headers = ["STT", "Chuyên mục", "Tác giả", "URL cuối", "Số lượng từ", "Danh sách Internal Link trong bài",
                    "Danh sách External Link trong bài", "Tag", "Index/NoIndex", "follow", "Ahref-Lang", "Meta Title",
                    "Meta Description", "Meta keyword", "canonical"]
    index = 1
    list_crawl = open_file(path)
    for idCrawler in list_crawl:
        if str(idCrawler.check_link()) == "None":
            index += 1
            # Tạo cột số thứ tự
            data = my_sheet.cell(row=index, column=1)
            data.value = index - 1
            # Tạo cột category
            data = my_sheet.cell(row=index, column=2)
            data.value = idCrawler.list_to_string(idCrawler.get_list_category())
            # Tạo cột url
            url_data = my_sheet.cell(row=index, column=4)
            url_data.value = idCrawler.get_url()

            # Tạo cột số lượng dữ liệu
            number_of_data = my_sheet.cell(row=index, column=5)
            number_of_data.value = idCrawler.get_num_word()

            # Tạo cột internalUrl

            internal_data = my_sheet.cell(row=index, column=6)
            internal_data.value = idCrawler.list_to_string(idCrawler.get_internal_link_list())

            # Tạo cột externalUrl

            external_data = my_sheet.cell(row=index, column=7)
            external_data.value = idCrawler.list_to_string(idCrawler.get_external_link_list())

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
        else:
            print("next")


# main function
if __name__ == '__main__':
    print("start export")
    export_excel("idWebsite1.txt", "1")
    export_excel("idWebsite2.txt", "2")
    export_excel("idWebsite3.txt", "3")
    export_excel("idWebsite4.txt", "4")
    export_excel("idWebsite5.txt", "5")
    export_excel("idWebsite6.txt", "6")
    print("end export")
