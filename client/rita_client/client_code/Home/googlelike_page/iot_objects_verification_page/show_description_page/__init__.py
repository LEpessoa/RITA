from ._anvil_designer import show_description_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class show_description_page(show_description_pageTemplate):
  def __init__(self,title='Title Default', description='Description Default', **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.title = title
    self.description = description
    
    # Any code you write here will run before the form opens.
    self.title_label.text=title
    self.description_label.text = description