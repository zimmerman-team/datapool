import spidermonkey
rt = spidermonkey.Runtime()
cx = rt.new_context()
func = cx.execute('function(val) {return "whoosh: " + val;}')
func('text')
func = cx.execute('function(val) { arr = {}; arr["lat"] = val;arr["long"] = 123443; return arr}')
test_val = func(12243232)
print test_val['lat']
