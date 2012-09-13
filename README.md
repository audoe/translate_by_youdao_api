#有道翻译

使用有道的翻译api实现一个小型的翻译工具，未来会支持百度的API

###使用方法

在有道的 [API申请页] (http://fanyi.youdao.com/openapi?path=data-mode "申请页面")
,申请一个key，相关的内容写入到 **youdao.conf** 这个文件里。

在你的终端下使用:

```python
python translation.py -k word //work 可以是中文或者英文，有道会判断相应的逻辑
```

###开发计划

- 有道的基本翻译
- 有道的网络翻译
- 百度翻译的支持
- 简单的gtk界面

###创意想法

- redis 缓存支持
- 自学习（队列支持）
- 服务
- 文本文档翻译（保持原有格式）
- 更多API服务的支持



有什么想法？
欢迎与我联系

- twitter: [@audoe] (http://twitter.com/audoe "audoe")
- weibo:  [@audoe] (http://weibo.com/audoe "audoe")
- email: whchen1080@gmail.com


###坑爹的想法


坑爹？加一个语音输入的模块算吗？
如果你有什么坑爹的想法，同样也欢迎联系我


###服务保证

- 每个daily update版本都是可执行的

