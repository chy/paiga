from .internal.writer import Writer
from pyga import Literal

class Script(object):
  def __init__(self):
    self._children = []
    self._writer = Writer()

  def add(self, child):
    # we special-case strings so that people don't need to write "Literal" everywhere.
    if isinstance(child, str):
      child = Literal(child)
    self._children.append(child)
    return child

  # Converts everything in the script to a string
  # and returns it.
  def compile(self):
    for thing in self._children[:-1]:
      self._writer.Write(thing.build())
      self._writer.newline(1)
    self._writer.Write(self._children[-1].build())
    return self._writer.Done()
    
  # def write(path):
  #   Writer()
  #
  # def function(self, name):
  #   return Function(name)
  #
  # def rule(self, name):
  #   return Rule(name)
  #
  # def cond(self):
  #   return Condition()

  # def cond(self, condition_literal, successor_literal, else_literal):
  #   condition = Condition().case(Literal(condition_literal), Literal(successor_literal))
  #   condition.then(Literal(else_literal))
  #   return condition

  # def literal(self, literal_expression):
  #   return Literal(literal_expression)

  # def cond(self):
  #   return self.add(Condition())