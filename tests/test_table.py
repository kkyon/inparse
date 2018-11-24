
from inparse import Inparse

import requests
parser_json='''
{
"cr_by": "kkyon",
"cr_dt": "Thu, 11 Oct 2018 22:05:08 GMT",
"no": "11111",
"selectors": [

{
"name": "table",
"parent_sid": null,
"parent_name": null,
"selector": "inparse.table",
"sid": 1,
"type": "table"
},

{
"name": "table_body",
"parent_sid": 1,
"parent_name": "table",
"selector": "inparse.table_body",
"sid": 2,
"type": "table_body"
},

{
"name": "table_header",
"parent_sid": 1,
"parent_name": "table",
"selector": "inparse.table_header",
"sid": 3,
"type": "table_header"
}

],
"status": "ok",
"type": "Table",
"website": "https://www.yeastar.com/webinars/"
}


'''


def test_table():


    from inparse import Inparse
    import requests
    p=Inparse(None,None,parser_json=parser_json)
    for url in ['https://www.yeastar.com/academy/onsite-training-schedule/','http://cs.sports.163.com/tables/','https://www.imdb.com/chart/top']:
        #,'https://www.yeastar.com/academy/onsite-training-schedule/', 'https://www.imdb.com/chart/top'

        res=requests.get(url)
        d=p.parse(res.text)
        Inparse.pretty_print(d)





