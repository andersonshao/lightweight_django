# Lightweight-Django
Lightweight Django study notes

## 2017-12-18
### **第一章 世界上最小的Django项目**

## 2017-12-19
### **第二章 无状态的web应用**
> 占位图片的覆盖文字显示有问题，不清楚是跟chrome浏览器有关，还是缓存有bug。
> 
> 注意tuple的单元素写法，TEMPLATES里的dict元素后面少写了个','导致runserver失败。以后用到iterable对象尽量用list。

## 2017-12-20
### **第三章 创建静态站点生成器**
> pip install django-compressor require Microsoft VC++ 14.0 从一个日本网站找到解决方案<br>Google确实能解决问题，百度重复的垃圾信息太多

## 2017-12-21
### **第四章 构建REST API**

> djangorestframework 从3.6起移除了 DjangoFilterBackend

因此使用3.5版本
	
	pip install djangorestframework==3.5.0

## 2017-12-22
### **第五章 使用Backbone.js的客户端Django**
> 这一章多涉及到前端js，稍稍回顾下廖雪峰的js教程。先硬着头皮看吧。程序员越来越全栈化，要学的东西还很多。

## 2017-12-23
> 项目在PyCharm中runserver成功，但在chrome中却没有呈现理想的效果。了解了在chrome中调试js的技巧。

## 2017-12-24
> 两天一直在解决一个问题：Cannot read property 'replace' of undefined. Google了好多方案都没头绪。最后参考 https://github.com/lightweightdjango/examples，发现出错的地方很搞笑，views.js 里面有个 templateName写错了，应该是'header-template'却误写成'head-template'。 chrome把错误定位到backbone.js 和 TemplateView 里，而 'header-template' 来自 继承 TemplateView的 HeaderView ...仔细想想这样的错误提示也没错，只不过有点哭笑不得。

## 2017-12-25
> home-template 无法渲染成功， 参考了github项目上的代码仍然失败。 已经提交了issue，且在Stackoverflow上提出了问题。接下来去完善之前的博客，准备部署上线

