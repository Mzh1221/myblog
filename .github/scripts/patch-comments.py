import sys
f = ".quartz/plugins/comments/dist/components/index.js"
c = open(f).read()
o = 'if(!e)return;let t=document.createElement("script");t.src="https://giscus.app/client.js"'
n = 'if(!e)return;e.innerHTML="";let t=document.createElement("script");t.src="https://giscus.app/client.js"'
if o not in c:
    print("FAIL: pattern not found")
    sys.exit(1)
c = c.replace(o, n)
open(f, "w").write(c)
print("PATCHED: " + f)
