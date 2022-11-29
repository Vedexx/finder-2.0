import urllib.parse
import requests as requests
from bs4 import BeautifulSoup
import lxml


class Parser:

    def __init__(self) -> None:
        super().__init__()

    def parse(self, numcase: str, year: str, person: str, proceedings_type: str, courts: str, progressBar):

        result = []
        courtslist = self.parse_courts(courts)
        begin_date = '01.01.' + year
        end_date = '31.12.' + year
        convert_name = urllib.parse.quote_plus(person,encoding='cp1251')
        if proceedings_type == 'admin':
            count = 0
            step = 100/len(courtslist)-1
            for court in courtslist:
                count += step
                progressBar.setValue(count)
                court = f'{court:02}'
                string_quest = f'http://192.168.94.254:80{court}/result.php?delo_table=adm_case&delo_id=1500001&adm_case__CASE_NUMBERSS={numcase}&ADM_CASE__JUDGE=&adm_case__RESULT_DATE1D={begin_date}&adm_case__RESULT_DATE2D={end_date}&ADM_CASE__RESULT=&ADM_PARTS__PARTS_TYPE=&adm_parts__NAMESS={convert_name}&ADM_PARTS__LAW_ARTICLE=&ADM_PARTS__BREAKING_LAW_TYPE=&Submit=%CD%E0%E9%F2%E8'
                result.extend(self.parsesite(string_quest, court))

        if proceedings_type == 'civil':
            count = 0
            step = 100 / len(courtslist) - 1
            for court in courtslist:
                count += step
                progressBar.setValue(count)
                court = f'{court:02}'
                string_quest = f'http://192.168.94.254:80{court}/result.php?delo_table=g1_case&delo_id=1540005&g1_case__CASE_NUMBERSS={numcase}&G1_CASE__CATEGORY=&G1_CASE__JUDGE=&g1_case__RESULT_DATE1D={begin_date}&g1_case__RESULT_DATE2D={end_date}&G1_CASE__RESULT=&G1_PARTS__PARTS_TYPE=&G1_PARTS__NAMESS={convert_name}&Submit=%CD%E0%E9%F2%E8'
                result.extend(self.parsesite(string_quest, court))
        if proceedings_type == 'crime':
            count = 0
            step = 100 / len(courtslist) - 1
            for court in courtslist:
                count += step
                progressBar.setValue(count)
                court = f'{court:02}'
                string_quest = f'http://192.168.94.254:80{court}/result.php?delo_table=u1_case&delo_id=1540006&u1_case__CASE_NUMBERSS={numcase}&U1_CASE__JUDGE=&u1_case__RESULT_DATE1D={begin_date}&u1_case__RESULT_DATE2D={end_date}&U1_CASE__RESULT=&U1_DEFENDANT__NAMESS={convert_name}&U1_DEFENDANT__LAW_ARTICLE=&U1_DEFENDANT__VERDICT_DATE1D=&U1_DEFENDANT__VERDICT_DATE2D=&U1_DEFENDANT__RESULT=&U1_PARTS__PARTS_TYPE=&U1_PARTS__NAMESS=&Submit=%CD%E0%E9%F2%E8'
                result.extend(self.parsesite(string_quest, court))
        return result

    def parse_courts(self, string):
        arr = []
        elements = string.split(',')
        for element in elements:
            if '-' in element:
                predels = element.split('-')
                arr.extend(range(int(predels[0].strip()), int(predels[1].strip()) + 1))
            else:
                arr.append(int(element.strip()))
        return arr

    def parsesite(self, site_addr: str, court_num):
        result = []
        # итерация по страницам
        page = 0

        while (True):
            site_addr = site_addr + f'&pageNum_Recordset1={str(page)}'
            print(site_addr)
            req = requests.get(site_addr)
            soup = BeautifulSoup(req.text, 'lxml')
            try:
                rows = soup.find('table', id='tablcont').select('tr')
            except Exception as e:
                return result
            for i in range(1, len(rows)):
                tds = rows[i].select('td')
                if tds[1].text.strip() == '':
                    return result
                # разбираем строку на части, изменяем ссылку у номера
                num = tds[0]
                num_href = 'http://192.168.94.254:80'+court_num+'/'+num.select_one('a')['href']
                num_text = num.text
                num_result = f'<td><a href="{num_href}">{num_text}</a>    </td>'
                result_string = num_result+ str(tds[1])+ str(tds[2]) + '<td>'+tds[3].text.strip()+'</td>' + str(tds[4])
                result.append(result_string)
            page += 1
        return result
