from abc import ABCMeta, abstractmethod

'''
  Interface that uses the Visitor design pattern.
  Every 'WriteX' method:
    - corresponds to a CGA entity defined in objects.py
    - returns a string: a CGA snippet corresponding to the entity
  Users of this library can write concrete Writers using this interface
  to customize the serialization behavior. Think putting spaces around
  arithmetic operators is too stuffy? Make your own writer that omits them.
  
  A new method must be added here (and in the concrete visitors) whenever a 
  new CGA entity is added. If new entities are added 
'''
class EntityVisitor(object):
  __metaclass__ = ABCMeta
  
  def Visit(self, entity):
    pass
  
  @abstractmethod
  def VisitRule(self, entity):
    pass

  @abstractmethod  
  def VisitFunction(self, entity):
    pass
  
  @abstractmethod
  def VisitComment(self, entity):
    pass
 
  @abstractmethod
  def VisitAttribute(self, entity):
    pass
    