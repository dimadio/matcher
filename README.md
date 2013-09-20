Simple match tool
 usage:

Let's say we are interested to get few parameters from fixed file name sceme
we build a pattern:
pattern = ("OSD", Unicode/2, Number/2, "OBJECTS.xml")  
where Unicode/2 = 2 characters of Unicode, Number/2 = 3 digit number


(Res, Matches) = match (pattern, u"OSDРУ99OBJECTS.xml") 
Where Res = Boolean success/fail
if success
[Lang, Clip] = Matches

in this case 
  Lang = "PY"
  Clip = 99



