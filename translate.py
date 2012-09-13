#coding:utf-8
import urllib
import json
from optparse import OptionParser
import chardet
#有道的key，要从http://fanyi.youdao.com/openapi?path=data-mode上申请
youdao_key = '1222489799'
youdao_key_from = 'myblogaudoe1'

def youdao_api(key,keyfrom,type='json'):
    if key and keyfrom:
        return 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q='%(keyfrom,key,type)

def translate(key_world):
    base_url = youdao_api(youdao_key,youdao_key_from)
    key_world.decode(chardet.detect(key_world)['encoding']).encode('utf8')
    json_data =urllib.urlopen(base_url+key_world)
    resault = json.load(json_data)
    return resault
def print_resault(resault):
    print 'keyword:%s'%(resault['query'])
    if resault.get('basic',''):
        basic = resault.get('basic')
        print ','.join(basic['explains'])
    else:
        print "没有这个单词的解释。请检查你的输入。"
if __name__ == '__main__':
    perser = OptionParser()
    perser.add_option("-k",'--keyword',dest="keyword",help="keywork")
    (options,args) = perser.parse_args()
    if options.keyword:
        resault = translate(options.keyword)
        print_resault(resault)
    else:
        print "没有输入关键字"

