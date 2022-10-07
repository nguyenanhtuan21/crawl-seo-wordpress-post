import time
from crawler.functional.crawler import Crawler
import openpyxl
import _thread


def export_excel(path, i):
    my_wb = openpyxl.Workbook()
    my_sheet = my_wb.active
    list_headers = ["STT", "Chuyên mục", "Tác giả", "URL cuối", "Số lượng từ", "Danh sách Internal Link trong bài",
                    "Danh sách External Link trong bài", "Tag", "Index/NoIndex", "follow", "Ahref-Lang", "Meta Title",
                    "Meta Description", "Meta keyword", "canonical"]
    index = 1
    f = open(path, "r")
    result = f.read()
    id_website = list(result.splitlines())
    for header in list_headers:
        column_header = my_sheet.cell(row=1, column=list_headers.index(header) + 1)
        column_header.value = header
    for idData in id_website:
        print(idData)
        if idData != "":
            id_crawler = Crawler("https://amis.misa.vn/" + idData)
            if str(id_crawler.check_link()) == "None":
                index += 1
                # Tạo cột số thứ tự
                data = my_sheet.cell(row=index, column=1)
                data.value = index - 1
                # Tạo cột category
                data = my_sheet.cell(row=index, column=2)
                data.value = id_crawler.list_to_string(id_crawler.get_list_category())
                # Tạo cột url
                url_data = my_sheet.cell(row=index, column=4)
                url_data.value = id_crawler.get_url()

                # Tạo cột số lượng dữ liệu
                number_of_data = my_sheet.cell(row=index, column=5)
                number_of_data.value = id_crawler.get_num_word()

                # Tạo cột internalUrl

                internal_data = my_sheet.cell(row=index, column=6)
                internal_data.value = id_crawler.list_to_string(id_crawler.get_internal_link_list())

                # Tạo cột externalUrl

                external_data = my_sheet.cell(row=index, column=7)
                external_data.value = id_crawler.list_to_string(id_crawler.get_external_link_list())

                # Tạo cột tag
                tag_list_data = my_sheet.cell(row=index, column=8)
                tag_list_data.value = ','.join(str(tagData) for tagData in id_crawler.get_tag_list())

                # Tạo cột xác định index hay noindex
                is_index_data = my_sheet.cell(row=index, column=9)
                is_index_data.value = id_crawler.index_or_no()

                # Tạo cột xác định folow hay noFollow
                is_follow_data = my_sheet.cell(row=index, column=10)
                is_follow_data.value = id_crawler.follow_or_no()

                # Tạo cột hrefLanguage
                href_lang_data = my_sheet.cell(row=index, column=11)
                href_lang_data.value = id_crawler.get_hreflang()

                # Tạo cột meta title
                meta_title_data = my_sheet.cell(row=index, column=12)
                meta_title_data.value = str(id_crawler.get_meta_title())

                # Tạo cột meta description
                meta_description_data = my_sheet.cell(row=index, column=13)
                meta_description_data.value = id_crawler.get_meta_description()

                # Tạo cột canonicalUrl
                meta_canonical_data = my_sheet.cell(row=index, column=15)
                meta_canonical_data.value = id_crawler.get_canonical_link()

                my_wb.save("crawl_data" + i + ".xlsx")
            else:
                print("next")


# main function
if __name__ == '__main__':
    print("start export")
    _thread.start_new_thread(export_excel("idWebsite1.txt", "1"))
    _thread.start_new_thread(export_excel("idWebsite2.txt", "2"))
    _thread.start_new_thread(export_excel("idWebsite1.txt", "3"))
    _thread.start_new_thread(export_excel("idWebsite2.txt", "4"))
    _thread.start_new_thread(export_excel("idWebsite1.txt", "5"))
    _thread.start_new_thread(export_excel("idWebsite2.txt", "6"))
    print("end export")
