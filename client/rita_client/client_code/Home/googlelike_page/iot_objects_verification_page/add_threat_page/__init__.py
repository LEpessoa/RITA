from ._anvil_designer import add_threat_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_threat_page(add_threat_pageTemplate):
  def __init__(self, iot_critical_object_acronym='DVC', threat_type_list=[],**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.iot_critical_object_acronym = iot_critical_object_acronym
    self.threat_type_list = threat_type_list
    self.add_countermeasure_repeating_panel.add_event_handler('x-toggle-add-remove-countermeasure',self.toggle_add_remove_countermeasure)

    # Any code you write here will run before the form opens.
    self.dictionary = {cat['id']:True for cat in threat_type_list}
    # threatTypeDTO: 
    # (IoTCriticalObjects,iot_threat_id,name,description,resilientSolution_IDS)
    threats = anvil.server.call('filterThreatTypes',threatTypeDTO=(self.iot_critical_object_acronym,None,None,None,None))
    objects = [{'id':o[0],
                'iot_threat_id':o[2],
                'name':o[3],
                'description':o[4],
               'quantity':self.check_dictionary(o[0])} for o in threats]
    self.item = objects
    
  def check_dictionary(self, id_):
      if id_ in self.dictionary:
        return 1
      return 0
    
  def toggle_add_remove_countermeasure(self, countermeasure):
    print('printing received countermeasure.')
    print(countermeasure)
    print('FIN')      

  def save_button_click(self, **event_args):
    filtered_list = filter(lambda cat : cat['quantity']==1, self.item)
    self.raise_event('x-close-alert',value=list(filtered_list))

  def cancel_button_click(self, **event_args):
    self.raise_event('x-close-alert',value=None)







