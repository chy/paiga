from __future__ import print_function
from abc import ABCMeta, abstractmethod

'''
  Interface that uses the Builder design pattern.
'''
class EntityBuilder(object):
  __metaclass__ = ABCMeta
  
  @abstractmethod
  def buildPart(self):
    pass
    
class BuildRule(EntityBuilder):
  pass
  
class BuildFunction(EntityBuilder):
  pass
  
class BuildOperation(EntityBuilder):
  pass
  
