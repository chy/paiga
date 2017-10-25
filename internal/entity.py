from abc import ABCMeta, abstractmethod
import time

class Entity(object):
  """A description of a CGA entity, such as a rule, condition, or attribute.

  Each Entity is a collection of data necessary to describe the thing in CGA
  it represents. Entity follows the Composite design pattern: each Entity
  may really be a tree of entities (if so, it's a CompositeEntity, see below).
  Otherwise, it is a LeafEntity. This is useful to represent nested conditions,
  rule definitions, and so on.
  Operations over a tree of entities should be defined with a new EntityVisitor
  rather than as methods on the entity classes.

  The Entity subclasses are very similar to each other. We have distinct classes
  for them mostly just for the types.
  The entities don't validate their contents. If you nest a rule definition
  inside of a function or something the FunctionEntity and RuleEntity will not
  complain about it.

  These are internal structures operated on by Script.
  Generally, use the builders + Script instead of an Entity unless you're
  adding new functionality to the library.

  Attributes:
    name: The name of the class instance. This should be unique.
  """
  __metaclass__ = ABCMeta

  def __init__(self):
    self.name = ""

  @abstractmethod
  def has_children(self):
    """Returns whether or not this Entity has child entities"""
    raise NotImplementedError("Implement this.")

  @abstractmethod
  def accept(self, visitor, depth=0):
    """Executes the input visitor on itself and its children, if any.

    In other words, this method calls the visitor on the entire tree
    defined by this Entity. Each Entity subclass should implement this
    to call the correct method on the visitor.

    Args:
      visitor: an EntityVisitor.
    """
    raise NotImplementedError("Implement this.")


class LeafEntity(Entity):
  __metaclass__ = ABCMeta

  def has_children(self):
    return False

  def children(self):
    return []


class CompositeEntity(Entity):
  def __init__(self):
    super(CompositeEntity, self).__init__()
    # These should be Entities, though we don't check.
    self.children = []

  def has_children(self):
    return True if (len(self.children) > 0) else False

  def add(self, child):
    self.children.append(child)

  def children(self):
    return self.children

class LiteralEntity(LeafEntity):
  """Represents an arbitrary CGA expression.

  A LiteralEntity is something that should be inserted as given
  into the output CGA. That is: it's a string. Use this for
  anything that doesn't have a defined Entity.

  Attributes:
    name: The name of the literal. We define a default. This shouldn't get printed
    in the output CGA, but is useful for debugging purposes.
    literal: the expression represented, as a string.
  """
  def __init__(self, literal_expression=""):
    self.name = "literal_" + str(time.clock())
    self.literal = literal_expression

  def accept(self, visitor, depth=0):
    visitor.visit_literal(self, depth)

class ConditionEntity(CompositeEntity):
  """Represents a CGA condition definition.

  Attributes:
    name: The name of the condition. We define a default. This shouldn't get printed
    in the output CGA, but is useful for debugging purposes.
    parameters: ordered list of entities representing the function's parameters.
      These may be empty.
    _children: ordered list of entities representing the function's constituent expressions.
  """
  def __init__(self):
    super(ConditionEntity, self).__init__()
    self.name = "cond_" + str(time.clock())
    # dictionary of case : successor entities
    self.children = {}
    # 'else' is reserved in Python (of course), so we have an underscore.
    self.else_ = {}

  def accept(self, visitor, depth=0):
    visitor.visit_condition(self, depth)

class StochasticEntity(ConditionEntity):
  def __init__(self):
    super(StochasticEntity, self).__init__()
    self.name = "stochastic_" + str(time.clock())

  def accept(self, visitor, depth=0):
    visitor.visit_condition(self, depth)

class RuleEntity(CompositeEntity):
  """Represents a CGA rule definition.

  This doesn't represent a rule -call-.

  Attributes:
    name: The name of the rule. This is what the rule will be called in the output
      CGA. We define a default.
    parameters: ordered list of entities representing the rule's parameters.
      These may be empty.
    _children: ordered list of entities representing this rule's successors.
  """

  def __init__(self):
    super(RuleEntity, self).__init__()
    self.name = "rule_" + str(time.clock())
    # A list of literals.
    self.parameters = []

  def accept(self, visitor, depth=0):
    visitor.visit_rule(self, depth)

class FunctionEntity(CompositeEntity):
  """Represents a CGA function definition.

  This doesn't represent a function -call-.

  Attributes:
    name: The name of the function. This is what the function will be called in the output
      CGA. We define a default.
    parameters: ordered list of entities representing the function's parameters.
      These may be empty.
    _children: ordered list of entities representing the function's constituent expressions.
  """
  def __init__(self):
    super(FunctionEntity, self).__init__()
    self.name = "fn_" + str(time.clock())
    self.parameters = []

  def accept(self, visitor, depth=0):
    visitor.visit_function(self, depth)
