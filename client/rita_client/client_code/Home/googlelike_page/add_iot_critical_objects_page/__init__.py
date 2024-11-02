from ._anvil_designer import add_iot_critical_objects_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_iot_critical_objects_page(add_iot_critical_objects_pageTemplate):
  def __init__(self,critical_object_list=[], **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.critical_object_list = critical_object_list
    self.add_iot_objects_repeating_panel.add_event_handler('x-add_critical_object', self.add_critical_object)
    self.add_iot_objects_repeating_panel.add_event_handler('x-remove_critical_object',self.remove_critical_object)

    # Any code you write here will run before the form opens.
    critical_objects_list_dictionary = {cat['id']:cat for cat in critical_object_list}
    def buildObject(obj):
      key = obj[0]
      quantity = 0
      if key in critical_objects_list_dictionary.keys():
        quantity = critical_objects_list_dictionary[key]['quantity']
      return {'id':obj[0],'name':obj[1],'acronym':obj[2],'quantity':quantity,'threats':[], 'reference':''}
    self.iot_critical_objects_list = map(buildObject,anvil.server.call('getDevices_resource'))    
    self.add_iot_objects_repeating_panel.items = self.iot_critical_objects_list
  
  def cancel_button_click(self, **event_args):    
    self.raise_event("x-close-alert", value=self.critical_object_list)

  def save_button_click(self, **event_args):    
    self.raise_event("x-close-alert", value=list(self.critical_object_list))
    
  def remove_critical_object(self, critical_object,**event_args):    
    new_critical_object_list = [cat for car in self.add_iot_objects_repeating_panel.items if cat['id'] != critical_object['id'] or (cat['id'] == critical_object['id'] and critical_object['quantity'] > 0)]
    self.critical_object_list = new_critical_object_list
    print('remove critical object called.')
    print(new_critical_object_list)     
  
  def add_critical_object(self, critical_object,**event_args):
    print('Showing Critical Object')
    print(list(critical_object))
    if len(list(self.critical_object_list)) == 0:      
      new_list = list(self.critical_object_list)
      new_list.append(critical_object)
      self.critical_object_list = new_list
      return
    new_critical_object_list = list(self.critical_object_list)
    new_critical_object_list = list(filter(lambda obj : obj['id'] != critical_object['id'],new_critical_object_list))
    new_critical_object_list.append(critical_object)
    self.critical_object_list = new_critical_object_list
    
    
    
  


