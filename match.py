# code-encoding: utf8

import exceptions

DEBUG = 0

def debug(message):
  if DEBUG:
    print "\t>\t%s" % message
    
class __Placeholder__(object):  
    
  def __init__(self, Type, length=None):
    self.type = Type
    self.length = length    
    
  def __div__(self, len):
    return __Placeholder__(self.type, len)
    
  def __repr__(self):
    return "<Placeholder for %s, length: %d>" % (self.type, self.length)
    
Number = __Placeholder__(int )
String = __Placeholder__(str)
Unicode = __Placeholder__(unicode)


def match( pattern, String):
  currentPosition = 0
  result = []
  for entry in pattern:
    if isinstance(entry, __Placeholder__):
      if entry.length:
        part = String[currentPosition: currentPosition+entry.length]
        try:
          convertedPart = entry.type(part)
          result.append(convertedPart)
          currentPosition+=entry.length
          debug("entry match: '%s' is %s" % (convertedPart,  entry.type ) )
        except Exception,e :
          debug( "%s is not %s" % (part ,  entry.type ) )
          return (False, "%s is not %s" % (part ,  entry.type ))
      else:                
        Rest = String[currentPosition: ]
        Try = ""        
        for ptest in range(1,len(Rest)):
          try:            
            Try = entry.type(Rest[:ptest])
          except exceptions.ValueError, e:            
            break
        STry = unicode(Try)
        length=len(STry)
        if length:
          result.append(Try)
          currentPosition+=length
          debug("entry match: '%s' is %s" % (Try,  entry.type ) )
        else:
          debug("Can't handle the case")
          return (False, "%s is not %s" % (part ,  entry.type ))
        
        
    elif isinstance(entry, basestring):
      part = String[currentPosition: currentPosition+len(entry)]
      if part != entry:
        return (False, "String '%s' do not match expected '%s'" % (part, entry)  )
      else:
        debug("String '%s' match" % entry)
        
      #result.append(entry)
      currentPosition+=len(entry)
      
    else:
      raise Exception("Wrong pattern received: %s" % str(pattern)  )
      
  return (True, result)

# -----------------
if __name__ == "__main__" :     
  pattern = ("OSD", String/2, Number/2, "OBJECTS.xml")  
  print "pattern received: %s" % str(pattern)
  print match (pattern, "OSDEN01OBJECTS.xml")
  
  # --------
  
  pattern = ("OSD", Unicode/2, Number/2, "OBJECTS.xml")  
  print "pattern received: %s" % str(pattern)
  (Res, Matches) = match (pattern, u"OSDРУ99OBJECTS.xml") 
  if Res:
    [Lang, Clip] = Matches
    print "Clip is %s and %d" % ( Lang , Clip)
  else:
    print "Failed to parse:", Matches
    
    
  
    
  