from pyga.internal.entity import *

# Public PYGA Api.
# Users create and manipulate these builders, then pass them to Script
# in the order they'd like them to turn up in the output CGA.

# TODO(wimberley): before launch. Determine final builder object
# hierarchy and methods. Difficult to change later.

# The RuleBuilder class.
# class Rule(object):
#
#   def __init__(self, rule_name):
#     self._rule = RuleEntity()
#     self._rule.name = rule_name
#     self._parameters = self._rule.parameters
#
#   @property
#   def parameters(self):
#     return [x.literal for x in self._parameters]
#
#   def param(self, parameter_literal):
#     self._function.parameters.append(Literal(parameter_literal).build())
#     return self
#
#   def literal(self, successor_literal_string):
#     self._rule.children.append(Literal(successor_literal_string).build())
#     return self
#
#   '''
#     successor: a CGA Entity.
#   '''
#   def add(self, successor):
#     if isinstance(successor, str):
#       self._rule.add(Literal(successor).build())
#     else:
#       self._rule.add(successor.build())
#     return self
#
#   def build(self):
#     return self._rule
#
# The LiteralBuilder class.
class Literal(object):
  def __init__(self, literal=""):
    self._literal = LiteralEntity(literal)

  def literal(self, literal_expression):
    self._literal.literal = literal_expression

  def build(self):
    return self._literal

class false(Literal):
  def __init__(self):
    Literal("false")

class true(Literal):
  def __init__(self):
    Literal("true")
#
# # The FunctionBuilder class.
# class Function(object):
#   def __init__(self, fn_name, params):
#     self._function = FunctionEntity()
#     self._function.name = fn_name
#     self._parameters = self._function.parameters
#     for p in params:
#       self.param(p)
#
#   @property
#   def parameters(self):
#     return [x.literal for x in self._parameters]
#
#   #params are a list of param literals.
#   # def __init__(self, function_name, parameters):
#   #   self(function_name, parameters)
#   #   self._function.parameters = parameters
#
#   def param(self, parameter_literal):
#     self._function.parameters.append(Literal(parameter_literal).build())
#     return self
#
#   def literal(self, successor_literal_string):
#     self._function.expressions.append(Literal(successor_literal_string).build())
#     return self
#
#   def add(self, successor):
#     if isinstance(successor, str):
#       self._function.add(Literal(successor).build())
#     else:
#       self._function.add(successor.build())
#     return self
#
#   def build(self):
#     return self._function

# The ConditionBuilder class.
# class Condition(Entity):
#   def __init__(self):
#     self.name = time.time() + "condition"
#     self.conditions = {}
#     self.final = {}
class Condition(object):
  def __init__(self):
    self._condition = ConditionEntity()

  """
    condition: a CGA entity
    successor: a CGA entity
  """
  def case(self, condition, successor):
    if isinstance(condition, str):
      condition = Literal(condition)
    if isinstance(successor, str):
      successor = Literal(successor)
    self._condition.conditions[condition.build()] = successor.build()
    return self

  # 'else' is reserved in python.
  def then(self, successor):
    if isinstance(successor, str):
      successor = Literal(successor)
    self._condition.final = successor.build()
    return self


  def build(self):
    return self._condition

# class Attribute(object):
#   def __init__(self):
#     self._attribute = AttributeEntity()
#
#   # annotation: an
#   def annotate(self, annotation):
#     self._attribute.annotations.append(annotation)
#
#   def build(self):
#     return self._attribute