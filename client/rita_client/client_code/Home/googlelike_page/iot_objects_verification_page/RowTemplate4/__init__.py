from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..add_threat_page import add_threat_page
from ..show_description_page import show_description_page

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.threats_repeating_panel.add_event_handler('x-delete-threat',self.delete_threat)
    self.threats_repeating_panel.items = self.item['threats']
    # Any code you write here will run before the form opens.
  
  def delete_threat(self, threat, **event_args):  
    filtered_list = list(filter(lambda t : t['id']!=threat['id'],self.item['threats']))
    self.item['threats']=filtered_list
    self.refresh_data_bindings()
    
  def add_threat_button_click(self, **event_args):
    # iot_critical_object_acronym='DVC', threat_type_list=[]
    result = alert(content=add_threat_page(
      iot_critical_object_acronym=self.item['acronym'],
       threat_type_list=self.item['threats']
    ),large=True,buttons=[],dismissible=True)
    if result != None:
      self.item['threats'] = result
      self.threats_repeating_panel.items = result
      self.refresh_data_bindings()      
      print('Result bore fruits:')
      print(result)
      print('FIN')
    
  def iot_critical_obj_description_button_click(self, **event_args):
    alert(content=show_description_page(self.item['name'],self.item['description']))

  def button_1_click(self, **event_args):
    print('showing threats')
    print(self.threats_repeating_panel.items)

  def ico_definition_button_click(self, **event_args):
    print("ico_definition_button_click called")
    print(self.item)
    print(self.item['name'])
    print(self.item['description'])
   #alert(content=show_description_page(self.item['name'],self.item['description']))



