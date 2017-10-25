from abc import ABCMeta, abstractmethod
from internal.entity import *

# Users create and manipulate these builders, then pass them to Script
# in the order they'd like them to turn up in the output CGA.

class Builder(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def build(self):
    pass


class Literal(Builder):
  def __init__(self, literal=""):
    self._literal = LiteralEntity(literal)

  def literal(self, literal_expression):
    self._literal.literal = literal_expression

  def build(self):
    return self._literal


class false(Literal):
  def __init__(self):
    super(false, self).__init__("false")


class true(Literal):
  def __init__(self):
    super(true, self).__init__("true")


# This decorator converts incoming strings to our internal
# representation (LiteralEntity) for ease of use.
# def convert_strings_to_literals(function):
#   def wrapper(*args):
#     return function([Literal(x) if isinstance(x, str) else x for x in args])
#
#   return wrapper

def convert_strings_to_literals(*args):
  return [Literal(x) if isinstance(x, str) else x for x in args[0]]

class Condition(Builder):
  def __init__(self):
    self._condition = ConditionEntity()

  def case(self, condition, successor):
    condition = Literal(condition) if isinstance(condition, str) else condition
    successor = Literal(successor) if isinstance(successor, str) else successor

    self._condition.children[condition.build()] = successor.build()
    return self

  # 'else' is reserved in python, so we add an underscore.
  def else_(self, successor):
    successor = Literal(successor) if isinstance(successor, str) else successor
    self._condition.else_ = successor.build()
    return self

  def build(self):
    return self._condition


class Stochastic(Condition):
  def _init__(self):
    super(Stochastic, self).__init__()
    self._condition = StochasticEntity()

class Rule(Builder):
  def __init__(self, rule_name):
    super(Rule, self).__init__()
    self._rule = RuleEntity()
    self._rule.name = rule_name

  def param(self, *parameters):
    parameters = convert_strings_to_literals(parameters)
    self._rule.parameters.extend([x.build() for x in parameters])
    return self

  def add(self, *successors):
    """Adds the input successors to the rule's internal list of successors.

    This can be called multiple times in succession, or multiple things can
    be passed to it:
     lot = Rule("Lot")
     lot.add("extrude(height)", "Envelope(landuse)"
    or
     lot = Rule("Lot")
     lot.add("extrude(height)").add("Envelope(landuse)")
    """
    successors = convert_strings_to_literals(successors)
    self._rule.children.extend([x.build() for x in successors])
    return self

  def parameters(self):
    return [x.literal for x in self._rule.parameters]

  def build(self):
    return self._rule


class Function(Builder):
  def __init__(self, name, parameters=[]):
    self._function = FunctionEntity()
    self._function.name = name
    for parameter in parameters:
      self.param(parameter)

  def parameters(self):
    return [x.literal for x in self._function.parameters]

  def param(self, *parameters):
    parameters = convert_strings_to_literals(parameters)
    self._function.parameters.extend([x.build() for x in parameters])
    return self

  def add(self, *expressions):
    expressions = convert_strings_to_literals(expressions)
    self._function.children.extend([x.build() for x in expressions])
    return self

  def parameters(self):
    return [x.literal for x in self._function.parameters]

  def build(self):
    return self._function