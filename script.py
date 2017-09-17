from .internal.writer import Writer
from .builders import Literal

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