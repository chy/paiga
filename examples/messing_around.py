
class example:
  def __init__(self):
    self._private = "hi"
    self._public = "How you doin"
  
  @property
  def private(self):
    return self._private
    
  @property
  def public(self):
    return self._public
    
  @public.setter
  def public(self, value):
    self._public = value
 
e = example()
print(e.private)
print(e.public)
e.public = "public"
print(e.public)