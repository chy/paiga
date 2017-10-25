from builders import Literal
from internal.writer import Writer

class Script(object):
  def __init__(self):
    self._children = []
    self._writer = Writer()

  def add(self, child):
    # We special-case strings so that people don't need to write "Literal" everywhere.
    if isinstance(child, str):
      child = Literal(child)
    self._children.append(child)
    return self

  # Converts everything in the script to a string
  # and returns it.
  def serialize(self):
    for child in self._children[:-1]:
      child.build().accept(self._writer)
      self._writer.newline(1)
    # We don't want a newline after the last line, so we add it separately.
    self._children[-1].build().accept(self._writer)
    return self._writer.done()