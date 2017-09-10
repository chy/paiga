#from visitor import EntityVisitor
from abc import ABCMeta, abstractmethod
#from interface import Interface
from .entity import *

#TODO(wimberley): this is not a correct visitor; fix.
# do we need an actual visitor? May have more patterns than
# necessary here.
class Writer():#EntityVisitor):
  def __init__(self):
    self._string_code = []

  def Write(self, entity, depth=0):
    if isinstance(entity, RuleEntity):
      self.WriteRule(entity, depth)
    if isinstance(entity, FunctionEntity):
      self.WriteFunction(entity, depth)
    if isinstance(entity, LiteralEntity):
      self.WriteLiteral(entity, depth)
    if isinstance(entity, ConditionEntity):
      self.WriteCondition(entity, depth)

  def Done(self):
    return "".join(self._string_code)

  def newline(self, num_newlines=1):
    for x in range(0, num_newlines):
      self._string_code.append("\n")

  def indent(self, num=1):
    self._string_code.append("\t"*num)

  '''
    parameters: a list of LiteralExpressions
  '''
  def _write_parameters(self, parameters):
    for x in parameters[:-1]:
      self._write(x)
      self._string_code.append(", ")
    self._write(parameters[-1])

  # def _write(self, things, depth=1):
  #   for thing in things[:-1]:
  #     self.indent(depth)
  #     self._string_code.append(thing)
  #     self.newline()
  #   self.indent(depth)
  #   self._string_code.append(things[-1])

  def _write(self, thing, depth=0):
    self.indent(depth)
    self._string_code.append(thing)

  # '''
  #   entities: a list of CGA Entitites.
  # '''
  # def _write_with_indents(self, entities, depth=1):
  #   for x in entities[:-1]:
  #     self.indent(depth+1)
  #     self.Write(x, depth)
  #     self.newline()
  #   self.Write(entities[-1], depth)
  def WriteChildren(self, children, depth=0):
    for child in children[:-1]:
      self.Write(child, depth+1)
      self.newline()
    self.Write(children[-1], depth+1)

  def WriteRule(self, rule, depth=0):
    self._write((rule.name + " --> "), depth)
    self.newline()
    if rule.has_children():
      self.WriteChildren(rule.children(), depth)

  def WriteLiteral(self, literal, depth=0):
    #self._write(literal.literal)
    self._string_code.append(depth*"\t" + literal.literal)

  def WriteFunction(self, function, depth=0):
    self._write(function.name + "(", depth)
    # self._string_code.append(function.name)
    # self._string_code.append("(")
    self._write_parameters(function.parameters)
    self._write(") =")
    self.newline()
    if function.has_children():
      self.WriteChildren(function.children(), depth)

  def WriteCondition(self, condition, depth=0):
    for c in condition.conditions:
      self._write("case ", depth)
      self.Write(c)
      self._write(" : ")
      self.newline()
      self.Write(condition.conditions[c], depth+1)
      self.newline()
    self._write("else: ", depth)
    self.newline()
    if (condition.final == {}):
      self._write('"You need an else statement."', depth+1)
    self.Write(condition.final, depth+1)

    # self._string_code.append("else : ")
    # if (condition.final == {}):
    #   self._string_code.append("NIL")
    # self.Write(condition.final)
  #
  # @abstractmethod
  # def WriteComment(self, entity):
  #   self.Visit(entity)
  #
  # @abstractmethod
  # def WriteAttribute(self, entity):
  #   self.Visit(entity)
  #
# class Writer(object):
  # __metaclass__ = ABCMeta
  
  # @abstractmethod
  # def serialize(self):
    # pass

# # NOTE: This will probably be the most complicated of the classes
# # Something something visitor pattern + composite pattern
# # Visitor to keep the tree structure and make it easy to visit & serialize parts
# # Composite possibly for builder to interact with rule (it's one or many cgaobjs)
# # something something linter
# class RuleWriter(Writer):
  # '''
    # initial_shape and successor_shape must be Writers.
  # '''
  # def __init__(self, lhs, rhs):
    # self.initial_shape = lhs
    # self.successor_shape = rhs
    # self.children = []
  
  # def _add_child(self, child):
    # pass

  # def serialize(self):
    # return self.initial_shape.serialize() + " -->\n  " + self.successor_shape.serialize()

# class ShapeWriter(Writer):
  # '''
    # name: a string representing this shape's shape symbol.
  # '''
  # def __init__(self, name):
    # self.shape_symbol = name

  # def serialize(self):
    # return str(self.shape_symbol)
	
# class OperationWriter(Writer):
  # def serialize(self):
    # pass

# # Can write abitrary CGA Function
# class FunctionWriter(Writer):
  # def serialize(self):
    # pass

# # Handles CityEngine builtin functions
# class BuiltinWriter(FunctionWriter):
  # def serialize(self):
    # pass

# # Handles CityEngine builtin utils
# class UtilWriter(FunctionWriter):
  # def serialize(self):
    # pass
    
# a = ShapeWriter("A")
# b = ShapeWriter("B")
# r = RuleWriter(a, b)
# print(r.serialize())