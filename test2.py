__author__ = 'Administrator'
import os
import xlrd
import HttpBase
import xlsxwriter
LISR_EXCEL = []
def sample_request(base_url="", http_api="", method="", http_port="", http_params="",list_index=0):
        h = HttpBase.http_request(base_url=base_url, http_api=http_api, method=method, http_port=int(http_port), http_params=http_params)
        res = h.request()
        app = {}
        app["result"] = res[0]
        app["json"] = res[1]
        LISR_EXCEL[list_index]["app"] = app

def read_excel(file= 'd:\httpapi.xlsx'):
    data = xlrd.open_workbook(file)
    table = data.sheet_by_index(0)
    nrows = table.nrows #行数
    colnames = table.row_values(0) #某一行数据
    for rownum in range(1, nrows):
         row = table.row_values(rownum)
         if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            LISR_EXCEL.append(app)
    return LISR_EXCEL

def write_excel(file='d:/result1.xlsx'):
    if not os.path.isfile(file):
            f = open(file, "w")
            f.close()
            print(u"结果文件不存在，创建文件成功")
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "id")
    worksheet.write(0, 1, "接口描述")
    worksheet.write(0, 2, "主机域名")
    worksheet.write(0, 3, "端口号")
    worksheet.write(0, 4, "Url")
    worksheet.write(0, 5, "请求方法")
    worksheet.write(0, 6, "Post参数")
    worksheet.write(0, 7, "预期值")
    worksheet.write(0, 8, "实际返回结果")
    temp = 0
    for i in range(0, len(LISR_EXCEL)):
        for j in LISR_EXCEL[i]:
            worksheet.write(i+1, temp, LISR_EXCEL[i]["id"])
            worksheet.write(i+1, temp+1, LISR_EXCEL[i]["api descirtip"])
            worksheet.write(i+1, temp+2, LISR_EXCEL[i]["Host"])
            worksheet.write(i+1, temp+3, LISR_EXCEL[i]["Port"])
            worksheet.write(i+1, temp+4, LISR_EXCEL[i]["Url"])
            worksheet.write(i+1, temp+5, LISR_EXCEL[i]["Method"])
            worksheet.write(i+1, temp+6, LISR_EXCEL[i]["Params"])
            worksheet.write(i+1, +7, LISR_EXCEL[i]["check point"])
            worksheet.write(i+1, +8, str(LISR_EXCEL[i]["app"]))
            break
    print(u"测试结果在d:/result.xlsx文件中")
    workbook.close()

def http_requests(list_excel):
    for i in range(len(list_excel)):
        for j in list_excel[i]:
            sample_request(base_url=list_excel[i]["Host"], http_api=list_excel[i]["Url"], method=list_excel[i]["Method"],
                         http_params=list_excel[i]["Params"], http_port=list_excel[i]["Port"],list_index=i)
            break
l = read_excel()
http_requests(l)
write_excel()
print(LISR_EXCEL)

