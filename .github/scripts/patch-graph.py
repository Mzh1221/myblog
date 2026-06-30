import sys
for f in [".quartz/plugins/graph/dist/index.js", ".quartz/plugins/graph/dist/components/index.js"]:
    c = open(f).read()
    n = c.replace(
        'a.startsWith("/")&&(a=a.slice(1))),a}',
        'a.startsWith("/")&&(a=a.slice(1))),decodeURIComponent(a)}',
    )
    if c == n:
        print("FAIL: no match in " + f)
        sys.exit(1)
    open(f, "w").write(n)
    print("PATCHED: " + f)
