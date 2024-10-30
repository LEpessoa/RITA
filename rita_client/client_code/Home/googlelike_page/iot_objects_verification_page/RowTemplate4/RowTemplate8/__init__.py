from ._anvil_designer import RowTemplate8Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...show_description_page import show_description_page
from ...add_countermeasure_page import add_countermeasure_page

class RowTemplate8(RowTemplate8Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.add_event_handler('x-refresh-data-bindings',self.refresh_my_bindings)
    self.rcmas_repeating_panel.add_event_handler('x-delete-rcm',self.delete_rcm)
    
    # Any code you write here will run before the form opens.
    if 'rcms' not in self.item.keys():
      self.item['rcms']=[]
  
  def refresh_my_bindings(self,**event_args):
    self.refresh_data_bindings()
    
  def add_countermeasure_button_click(self, **event_args):
    result = alert(content=add_countermeasure_page(
      iot_threat_acronym=self.item['iot_threat_id'],
      countermeasure_list=self.item['rcms']
      ),large=True,buttons=[],dismissible=True)
    if result != None:
      self.item['rcms'] = result
      self.rcmas_repeating_panel.items = result
      self.refresh_data_bindings()      

  def threat_description_button_click(self, **event_args):
    alert(content=show_description_page(self.item['name'],self.item['description']),large=True)

  def delete_threat_button_click(self, **event_args):
    print('Deleting threat: '+ self.item['name'])
    self.parent.raise_event('x-delete-threat',threat=self.item)
    self.refresh_data_bindings()
  
  def delete_rcm(self, rcm, **event_args):  
    filtered_list = list(filter(lambda t : t['id']!=rcm['id'],self.item['rcms']))
    self.item['rcms']=filtered_list
    self.refresh_data_bindings()




