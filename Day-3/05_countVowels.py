s = "Ser operations in Py"
v = {'a','e','i','o','u',"A","E","I","O","U"}
c = sum(s.count(ch) for ch in (set(s)& v))
print("Number of vowels",c)


res = 0
for i in s:
  if i in v:
    res+=1
print("Count of Vowels:",res)