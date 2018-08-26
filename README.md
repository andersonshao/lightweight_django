# Lightweight-Django
Lightweight Django study notes

### **第五章 使用Backbone.js的客户端Django**
> 这一章多涉及到前端js，稍稍回顾下廖雪峰的js教程。先硬着头皮看吧。程序员越来越全栈化，要学的东西还很多。

> 项目在PyCharm中runserver成功，但在chrome中却没有呈现理想的效果。了解了在chrome中调试js的技巧。

> 两天一直在解决一个问题：Cannot read property 'replace' of undefined. Google了好多方案都没头绪。最后参考 https://github.com/lightweightdjango/examples，发现出错的地方很搞笑，views.js 里面有个 templateName写错了，应该是'header-template'却误写成'head-template'。 chrome把错误定位到backbone.js 和 TemplateView 里，而 'header-template' 来自 继承 TemplateView的 HeaderView ...仔细想想这样的错误提示也没错，只不过有点哭笑不得。

> home-template 无法渲染成功， 参考了github项目上的代码仍然失败。 已经提交了issue，且在Stackoverflow上提出了问题。接下来去完善之前的博客，准备部署上线

