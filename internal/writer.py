from internal.entity import *
from internal.visitor import EntityVisitor

class Writer(EntityVisitor):
  def __init__(self):
    self._string_code = []

  def done(self):
    return "".join(self._string_code)

  def newline(self, num_newlines=1):
    for x in range(0, num_newlines):
      self._string_code.append("\n")

  def _indent(self, num=1):
    self._string_code.append("\t"*num)

  '''
    parameters: a list of LiteralExpressions
  '''
  def _write_parameters(self, parameters):
    if parameters:
      self._write("(")
      for param in parameters[:-1]:
        param.accept(self)
        self._string_code.append(", ")
      parameters[-1].accept(self)
      self._write(")")

  def _write(self, thing, depth=0):
    self._indent(depth)
    self._string_code.append(thing)

  def visit_literal(self, literal, depth=0):
    self._string_code.append(depth*"\t" + literal.literal)

  def visit_condition(self, condition, depth=0):
    for entry in condition.children:
      self._write("case ", depth)
      entry.accept(self)
      if isinstance(condition, StochasticEntity):
        self._write("%")
      self._write(": ")
      self.newline()
      condition.children[entry].accept(self, depth+1)
      self.newline()
    self._write("else: ", depth)
    self.newline()
    if condition.else_:
      condition.else_.accept(self, depth+1)
    else:
      self._write('"You need an else statement."', depth+1)

  def _write_children(self, children, depth=0):
    for child in children[:-1]:
      child.accept(self, depth + 1)
      self.newline()
    children[-1].accept(self, depth + 1)

  def visit_rule(self, rule, depth=0):
    self._write(rule.name, depth)
    self._write_parameters(rule.parameters)
    self._write(" --> ")
    self.newline()
    if rule.has_children():
      self._write_children(rule.children, depth)
    else:
      self._write("This rule has no successors!")

  def visit_function(self, function, depth=0):
    self._write(function.name, depth)
    self._write_parameters(function.parameters)
    self._write(" =")
    self.newline()
    if function.has_children():
      self._write_children(function.children, depth)
    else:
      self._write("This function has no expressions!")