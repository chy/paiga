from abc import ABCMeta, abstractmethod
from internal.entity import *

class EntityVisitor(object):
  """Our visitor base class.

  Each visitor implementation defines an operation for
  our CGA entities (conditions, rules, etc).
  The main one here is serialization (see writer.py).

  The various _visit_x methods define the operation implemented by
  this visitor for each Entity subclass.
  Add a new EntityVisitor subclass to define a new operation over
  a tree of entities.
  Example operations:
    - Custom serialization.
    - Validate an entity tree to make sure it would serialize to
      valid CGA.
  """
  __metaclass__ = ABCMeta

  # These methods define this visitor's operation for the various
  # Entity subclasses. There should be a method in the base class
  # here for each Entity subclass. If you add a new Entity subclass,
  # add a method here and call it from visit() above.

  @abstractmethod
  def visit_rule(self, rule, depth=0):
    pass

  @abstractmethod
  def visit_literal(self, literal, depth=0):
    pass

  @abstractmethod
  def visit_function(self, function, depth=0):
    pass

  @abstractmethod
  def visit_condition(self, condition, depth=0):
    pass
