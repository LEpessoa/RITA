from ._anvil_designer import resizeableTextAreaTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class resizeableTextArea(resizeableTextAreaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  @property
  def text(self):
      print(f"Getting text: {self._text}")
      return self._text

  @text.setter
  def text(self, value):
      print(f"Setting my_prop: {value}")
      self._text=value

  @property
  def minheight(self):      
      return self._minheight

  @minheight.setter
  def minheight(self, value):      
      self._minheight=value

  def setText(self,**args):
    self.call_js('setText',self._text)
    self.call_js('setMinHeight',self._minheight)
