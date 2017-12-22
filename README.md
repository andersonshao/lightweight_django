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

