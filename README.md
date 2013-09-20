<h3>Simple match tool</h3>
<h4>usage:</h4>

<p>Let's say we are interested to get few parameters from fixed file name sceme
we build a pattern:<br>
pattern = ("OSD", Unicode/2, Number/2, "OBJECTS.xml")<br>
where Unicode/2 = 2 characters of Unicode, Number/2 = 3 digit number</p>
<br>
<p>(Res, Matches) = match (pattern, u"OSDРУ99OBJECTS.xml")<br>
Where Res = Boolean success/fail<br>
if success<br>
&nbsp;&nbsp;[Lang, Clip] = Matches<br>
<br>
in this case<br>
&nbsp;&nbsp;Lang = "PY"<br>
&nbsp;&nbsp;Clip = 99</p>



