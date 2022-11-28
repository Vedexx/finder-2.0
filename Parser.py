class Parser:

    def __init__(self) -> None:
        super().__init__()

    def parse(self, numcase: str, year: str, person: str, proceedings_type: str, courts: str):
        result = []
        courtslist = self.parse_courts(courts)
        begin_date = '01.01.' + year
        end_date = '31.12.' + year
        # todo Преобразовать имя в интернет код
        convert_name =person
        if proceedings_type == 'admin':
            for court in courtslist:
                # todo преобразовать в число, добавить лидирующие нули
                #todo проерить где НОМЕР в запросе
                string_quest = f'http://192.168.94.254:80{court}/result.php?delo_table=adm_case&delo_id=1500001&ADM_CASE__JUDGE=&adm_case__RESULT_DATE1D={begin_date}&adm_case__RESULT_DATE2D={end_date}&ADM_CASE__RESULT=&ADM_PARTS__PARTS_TYPE=&adm_parts__NAMESS={convert_name}&ADM_PARTS__LAW_ARTICLE=&ADM_PARTS__BREAKING_LAW_TYPE=&Submit=%CD%E0%E9%F2%E8'
        #       todo кидаем запрос и парсим страничку
        if proceedings_type == 'civil':
            for court in courtslist:
                string_quest = f'http://192.168.94.254:80{court}/result.php?delo_table=g1_case&delo_id=1540005&g1_case__CASE_NUMBERSS={numcase}&G1_CASE__CATEGORY=&G1_CASE__JUDGE=&g1_case__RESULT_DATE1D={begin_date}&g1_case__RESULT_DATE2D={end_date}&G1_CASE__RESULT=&G1_PARTS__PARTS_TYPE=&G1_PARTS__NAMESS={convert_name}&Submit=%CD%E0%E9%F2%E8'
        if proceedings_type=='crime':
            for court in courtslist

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


parser = Parser()
print(parser.parse_courts('29-36,72,37, 74-87'))
