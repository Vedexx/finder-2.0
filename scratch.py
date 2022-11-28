import requests
from bs4 import BeautifulSoup
import lxml

def parsesite(site_addr: str):
    result=[]
    # итерация по страницам
    page = 0

    while(True):
        site_addr = site_addr + f'&pageNum_Recordset1={str(page)}'
        req = requests.get(site_addr)
        soup = BeautifulSoup(req.text, 'lxml')
        rows = soup.find('table', id ='tablcont').select('tr')
        for i in range(1, len(rows)):
            tds = rows[i].select('td')
            if tds[1].text.strip() =='':
                return result
            result.append(rows[i])
        page+=1



arr1 = parsesite('http://192.168.94.254:8030/result.php?delo_table=adm_case&delo_id=1500001&adm_case__CASE_NUMBERSS=712&ADM_CASE__JUDGE=&adm_case__RESULT_DATE1D=&adm_case__RESULT_DATE2D=&ADM_CASE__RESULT=&ADM_PARTS__PARTS_TYPE=&adm_parts__NAMESS=%C8%E2%E0%ED%EE%E2&ADM_PARTS__LAW_ARTICLE=&ADM_PARTS__BREAKING_LAW_TYPE=&Submit=%CD%E0%E9%F2%E8')
arr2 = parsesite('http://192.168.94.254:8030/result.php?delo_table=adm_case&delo_id=1500001&ADM_CASE__JUDGE=&adm_case__RESULT_DATE1D=&adm_case__RESULT_DATE2D=&ADM_CASE__RESULT=&ADM_PARTS__PARTS_TYPE=&adm_parts__NAMESS=%C8%E2%E0%ED%EE%E2&ADM_PARTS__LAW_ARTICLE=&ADM_PARTS__BREAKING_LAW_TYPE=&Submit=%CD%E0%E9%F2%E8')
arr3 =parsesite('http://192.168.94.254:8030/result.php?pageNum_Recordset1=10&totalRows_Recordset1=191&delo_table=adm_case&delo_id=1500001&ADM_CASE__JUDGE=&adm_case__RESULT_DATE1D=&adm_case__RESULT_DATE2D=&ADM_CASE__RESULT=&ADM_PARTS__PARTS_TYPE=&adm_parts__NAMESS=%C8%E2%E0%ED%EE%E2&ADM_PARTS__LAW_ARTICLE=&ADM_PARTS__BREAKING_LAW_TYPE=&Submit=%CD%E0%E9%F2%E8')
print(len(arr1))
print(len(arr2))
print(len(arr3))