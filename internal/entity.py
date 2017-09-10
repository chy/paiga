# Definitions for CGA base objects.
# TODO(wimberley): split into one class per file. ... do we need to ? lots of classes.
# TODO(wimberley): add tests
# TODO(wimberley): set up some nice file naming
from abc import ABCMeta, abstractmethod
import time

class Entity(object):
  __metaclass__ = ABCMeta

  def __init__(self):
    self.name = ""

  @abstractmethod
  def has_children(self):
    pass

  # @abstractmethod
  # def accept(visitor):
  #   pass

  # @abstractmethod
  # def serialize(self):
  #   pass

  def name(self):
    return self.name

class LeafEntity(Entity):
  __metaclass__ = ABCMeta

  def has_children(self):
    return False

  @abstractmethod
  def children(self):
    pass

class CompositeEntity(Entity):

  def __init__(self):
    super(Entity, self).__init__()
    self._children = []

  def has_children(self):
    return True if (len(self.children()) > 0) else False

  def add(self, child):
    # if isinstance(child, str):
    #   self._children.append(LiteralEntity(literal_expression=child))
    # else:
    self._children.append(child)

  def children(self):
    return self._children

'''
'''
class RuleEntity(CompositeEntity):
  def __init__(self):
    super(CompositeEntity, self).__init__()
    self.name = "rule_" + str(time.clock())
    self.parameters = []
    # An ordered list of this rule's successors.
    # Each add must be:
    #   - an Entity
    #   - either a literal or able to produce a Shape (optional)
  #   self.successors = []
  #
  # def children(self):
  #   return self.successors

'''
'''
class FunctionEntity(CompositeEntity):
  def __init__(self):
    super(CompositeEntity, self).__init__()
    self.name = "fn_" + str(time.clock())
    self.parameters = []
    # An ordered list of this function's constituent expressions.
  #   # Each expression must be an entity.
  #   self.expressions = []
  #
  # def children(self):
  #   return self.expressions


'''
Conditions can produce either Shapes or Values
'''
class ConditionEntity(Entity):
  def __init__(self):
    self.name = "cond_" + str(time.clock())
    self.name = str(time.time()) + "condition"
    # dictionary of condition : add
    self.conditions = {}
    self.final = {}

  def children(self):
    return self.conditions


class LiteralEntity(Entity):
  def __init__(self, literal_expression=""):
    self.name = "literal_" + str(time.clock())
    self.literal = literal_expression

# '''
# '''
# class AttributeEntity(Entity):
#   def __init__(self):
#     self.expression = Expression()

# '''
# '''
# class AnnotationEntity(Entity):
#   def __init__(self):
#     self.expression = Expression()

# '''
# '''
# class ConstEntity(Entity):
#   def __init__(self):
#     self.expression = Expression()



# '''
# '''
# class Shape(Entity):
#   def __init__(self):
#     pass
#

#
#
# '''
# '''
# class Operation(Entity):
#   def __init__(self):
#     pass
#
#
# '''
# '''
# class Stochastic(Condition):
#   def __init__(self):
#     self.name = time.time() + "stochastic"
#

# '''
# '''
# class Style(Entity):
#   def __init__(self):
#     self.attributes = []
#
#
# '''
# '''
# class Import(Entity):
#   def __init__(self):
#     self.filename = ""
#
#
# '''
# '''
# class Comment(Entity):
#   def __init__(self):
#     self.contents = ""
#     self.block = false