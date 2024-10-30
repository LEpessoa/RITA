from ._anvil_designer import RowTemplate11Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...show_description_page import show_description_page

class RowTemplate11(RowTemplate11Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.plus_button.visible = self.item['quantity']==0
    self.minus_button.visible = self.item['quantity']==1
    
  def check_description_button_click(self,**event_args):
    alert(content=show_description_page(title=self.item['name'], description=self.item['description']),large=True)
  
  def plus_button_click(self, **event_args):    
    self.item['quantity'] = 1
    self.refresh_data_bindings()
    print('Printing item stored')
    print(self.item)
    print('fin')
    self.plus_button.visible=False
    self.minus_button.visible=True
    self.raise_event('x-toggle-add-remove-countermeasure',countermeasure=self.item)
  
  def minus_button_click(self, **event_args):
    self.item['quantity'] = 0
    self.refresh_data_bindings()
    print('Printing item stored')
    print(self.item)
    print('fin')
    self.minus_button.visible=False
    self.plus_button.visible=True
    self.raise_event('x-toggle-add-remove-countermeasure',countermeasure=self.item)



