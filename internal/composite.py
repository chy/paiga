from abc import ABCMeta, abstractmethod

'''
  Interface that uses the Composite design pattern.
'''
class Component(object):
  __metaclass__ = ABCMeta
  # whatever operations are common to components

class LeafComponent(Component):
  __metaclass__ = ABCMeta
  # whatever operations are common to components
  
class Composite(Component):
  __metaclass__ = ABCMeta
  
  @abstractmethod
  def add(self, child):
    pass
  @abstractmethod
  def remove(self, child):
    pass
    
  @abstractmethod
  def get(self, name_of_child):
    pass
    
  # whatever operations are common to composites