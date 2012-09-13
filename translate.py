#coding:utf-8
import urllib
import json
from optparse import OptionParser
import ConfigParser
import chardet

def youdao_api(type='json'):
    #读配置文件
    cf = ConfigParser.ConfigParser()
    cf.read('youdao.conf')
    key = cf.get('youdao','key')
    keyfrom = cf.get('youdao','key_from')
    if key and keyfrom:
        return 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q='%(keyfrom,key,type)

def translate(key_world):
    base_url = youdao_api()
    key_world.decode(chardet.detect(key_world)['encoding']).encode('utf8')
    json_data =urllib.urlopen(base_url+key_world)
    resault = json.load(json_data)
    return resault

def print_resault(resault):
    print 'keyword:%s'%(resault['query'])
    translation = resault.get('translation',[])
    basic = resault.get('basic',[])
    if translation and basic:
        print '基本解释:'
        print '\n'.join(translation)
        print '\n'.join(basic['explains'])
    else:
        print '在有道词典中没有这个单词的基本解释。'

    web = resault.get('web',[])
    if web:
        print '在有道的搜索中，有与你输入关键字相似或相同的解释。'
        for key_dict in web:
            #codeing
            key =key_dict['key']
            value = ','.join(key_dict['value'])
            print u'keywork:%s\n解释:%s'%(key,value)
    else:
        print '在有道的网络中没有这个单词的解释'


if __name__ == '__main__':
    perser = OptionParser()
    perser.add_option("-k",'--keyword',dest="keyword",help="keywork")
    (options,args) = perser.parse_args()
    if options.keyword:
        resault = translate(options.keyword)
        print_resault(resault)
    else:
        print "没有输入关键字"

