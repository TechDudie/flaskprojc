import sys
file = open(sys.argv[1]).read()
array = file.split('\n')
global x
global q
global stdout
x = -1
q = 1
stdout = ""
def out(text):
  global stdout
  stdout += text
def remove(text):
  try:
    return text.split(": ")[1]
  except:
    return text
def cycle():
  global x
  global q
  if x == 0:
    out("q" + str(q) + " = {\n  'question': '" + i + "',")
  if x == 1:
    out("  'a': '" + i + "',")
  if x == 2:
    out("  'b': '" + i + "',")
  if x == 3:
    out("  'c': '" + i + "',")
  if x == 4:
    out("  'd': '" + i + "',")
  if x == 5:
    out("  'answer': '" + i + "',\n}")
out("# Autogenerated file by 'build.py'\n# (c) 2022 TechDudie\n\n")
for i in array:
  x += 1
  i = remove(i)
  cycle()
  if x > 5:
    x = -1
    q += 1
out("q = [")
for i in range(1, q + 1):
  out("q{}, ".format(i))
stdout = stdout[:-2]
out("]")
outputfile = open(sys.argv[2], "w")
outputfile.write(stdout)
