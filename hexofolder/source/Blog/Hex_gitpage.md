---
url: hexo
---

# 如何优雅的白嫖博客服务

Date: 2020/6/14
[Main Tutorial](https://blog.csdn.net/muzilanlan/article/details/81542917)

原博客已经写的很清楚了， 这里我只记录一下我遇到的问题。


# 1. npm error
```bash
npm install -g hexo-cli
```
```bash
npm ERR! code EINTEGRITY
npm ERR! sha512-XlPzRtnsdrUfTSkLJPACQgWByybB56E79H8xIjGWj0GL+J/VqENsgc+GER0ytFwrP/6YKCerXdaUWOYMcv6aiA== integrity checksum failed when using sha512: wanted sha512-XlPzRtnsdrUfTSkLJPACQgWByybB56E79H8xIjGWj0GL+J/VqENsgc+GER0ytFwrP/6YKCerXdaUWOYMcv6aiA== but got sha512-BdyVintFFu5qQX0AtuwgmXxphBU1V+VL9+8GPemcM9Q86MPG+MCTA26bCyEyzUqDPVBm7xF3gjACaOwMBEmAZQ==. (653 bytes)

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/ken/.npm/_logs/2020-06-14T05_36_46_129Z-debug.log
```

**Solution:**
```bash
npm cache verify
npm install -g hexo-cli
```
reference: [天魂_TH](https://www.jianshu.com/p/2899bd2a0a20)

## 2. npm Download

```bash
npm config set registry https://registry.npm.taobao.org
```
reference: [慢读慢写](https://blog.csdn.net/ibmall/article/details/81390639)

## 3. Start the Service:
[![tztLw9.jpg](https://s1.ax1x.com/2020/06/14/tztLw9.jpg)](https://imgchr.com/i/tztLw9)

# 4 Director Structure

```bash
.
├── 1
├── _config.yml
├── db.json
├── node_modules
├── package.json
├── package-lock.json
├── public
├── scaffolds
├── source
└── themes
```

After you run `hexo g`, all `.md` files in `source` directory would be turned to `html` files and stored at `publish` directory which you can upload to GitHub.

the home page `public/index.html` is stored at `source/_posts/hello-world.md`.

# New Category:

```bash
hexo new page categories
```
A new directory `categories` would be create in `source`


# Customize your theme
reference: [dxs雪松](https://www.cnblogs.com/d-xs/p/6891647.html)


```bash
~/hexofolder$ tree -L 1 themes/landscape/
```
```
themes/landscape/
├── _config.yml
├── Gruntfile.js
├── languages
├── layout
├── LICENSE
├── package.json
├── README.md
├── scripts
└── source
```

# Adding head index

reference: [锦瑟华年](http://kuangqi.me/tricks/enable-table-of-contents-on-hexo/)

Insert the codes below after `<%- post.content %>` in the file `themes/landscape/layout/_partial/article.ejs`
```html
<!-- Table of Contents -->
<% if (!index){ %>
  <div id="toc" class="toc-article">
    <strong class="toc-title">文章目录</strong>
    <%- toc(post.content) %>
  </div>
<% } %>
```

Adding codes below at `themes/landscape/source/css/_partial/article.styl`
```css
/*toc*/
.toc-article
  background: #eee;
  border: 1px solid #bbb;
  border-radius: 10px;
  margin: 1.5em 0 0.3em 1.5em;
  padding: 0em 1em 0 1em;
  max-width: 100%
.toc-title
  font-size: 120%
#toc
  line-height: 1em;
  font-size: 0.9em;
  float: right
.toc
  padding: 0;
  margin: 1em;
  line-height: 1.8em;
.toc-child
  margin-left: 1em
```

# final style.css file
```css
/* -2.5 Scroll To Up */
.back-to-top {
  position: fixed;
  bottom: 10px;
  right: 10px;
  border-radius:1000px
}

.back-to-top i {
  display: block;
  width: 36px;
  height: 36px;
  line-height: 36px;
  color: #fff;
  font-size: 14px;
  text-align: center;
  border-radius: 30px;
  background-color: #F97794;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

.title_index {
  position: fixed;
  bottom: 40px;
  right: -9px;
}

/*toc*/
.toc-article {
  background: #eee;
  border: 1px solid #bbb;
  border-radius: 10px;
  margin: 1.5em 0 0.3em 1.5em;
  padding: 0em 1em 0 1em;
  max-width: 100%
}
.toc-title {
  font-size: 120%
}

#toc {
  line-height: 1em;
  font-size: 0.9em;
  float: right
}
.toc{
  padding: 0;
  margin: 1em;
  line-height: 1.8em;
}
.toc-child {
  margin-left: 1em
}
li {
    list-style-type:none;
}

#nav {
  display:block;
  z-index: 10;
  background: salmon;
  border: 1px solid #bbb;
  border-radius: 100px;
  max-width: 100%;
}
#nav li a {
    display: block;
    max-width: 100%;
}
#nav li ul {
    position: fixed;
    right: 0;
    bottom:5%;
    display:none;
    width:80%;
}
#nav li:hover ul {
    display:block;
}
```

## Title Index

http://kuangqi.me/tricks/enable-table-of-contents-on-hexo/
