
from inparse import Inparse

import requests
parser_json='''
{
"cr_by": "kkyon",
"cr_dt": "Thu, 11 Oct 2018 22:05:08 GMT",
"no": "8eed5dc5",
"selectors": [
{
"name": "article_body",
"parent_sid": null,
"selector": "div#endText",
"sid": 11,
"type": "article_body"
},
{
"name": "publish_date",
"parent_sid": null,
"selector": "div.post_time_source",
"sid": 12,
"type": "publish_date"
},
{
"name": "title",
"parent_sid": null,
"selector": "h1",
"sid": 13,
"type": "title"
},
{
"name": "author",
"parent_sid": null,
"selector": "li[data-module-name='n_topnavapplist_t_0']",
"sid": 14,
"type": "author"
},
{
"name": "top_image",
"parent_sid": null,
"selector": "div.post_next_post.clearfix",
"sid": 15,
"type": "top_image"
}
],
"status": "ok",
"type": "Ariticle",
"website": "news.163.com"
}


'''


def test_parser():


    from inparse import Inparse
    import requests
    p=Inparse(None,None,parser_json=parser_json)
    res=requests.get('https://news.163.com/18/1002/16/DT4HPVNL000187VE.html')
    d=p.parse(res.text)
    Inparse.pretty_print(d)



def test_parser2():
    Inparse.TEST_MODE=True
    p=Inparse('b45beddc','d50cb533f69b6a78892afbd093f95fc1')
    d=p.parse_url('https://qz.com/india/1413291/trulymadly-ceo-on-how-dating-apps-like-bumble-india-must-localise/')
    Inparse.pretty_print(d)

if __name__ == '__main__':
    test_parser()
    test_parser2()
