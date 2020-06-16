---
url: Build_index
---

# How to build index in one line codes

```bash
ls | awk '{print "["$1"]("$i")"}'| sed 's/\.md]/]/;s/\.md)/\.html)/;/yuque.yml/d;/(summary.html)/d'  > Blog_index.md
```
