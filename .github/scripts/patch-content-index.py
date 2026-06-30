import sys
f = ".quartz/plugins/content-index/dist/index.js"
c = open(f).read()
o = "delete content2.description;\n        delete content2.date;"
n = "if (!content2.description) delete content2.description;"
if o not in c:
    print("FAIL: pattern not found")
    sys.exit(1)
c = c.replace(o, n)
open(f, "w").write(c)
print("PATCHED: " + f)
