from ._anvil_designer import add_countermeasure_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_countermeasure_page(add_countermeasure_pageTemplate):
  def __init__(self, iot_threat_acronym='PLTT1', countermeasure_list=[],**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.iot_threat_acronym = iot_threat_acronym
    self.countermeasure_list = countermeasure_list
    self.add_countermeasure_repeating_panel.add_event_handler('x-toggle-add-remove-countermeasure',self.toggle_add_remove_countermeasure)

    # Any code you write here will run before the form opens.
    self.dictionary = {cat['id']:True for cat in countermeasure_list}    
    countermeasures = anvil.server.call('filterSolutions',
                    solutionDTO=(None,None,None,None,None,None,
                                 self.iot_threat_acronym))
    if len(countermeasures) > 0:
      print('Showing countermeasure found.')
      print(countermeasures)
      objects = [{'id':o['id'],
                  'resilient_solution_id':o['resilient_solution_id'],
                  'name':o['name'],
                  'description':o['description'],                  
                  'quantity':self.check_dictionary(o['id'])} for o in countermeasures]
      self.item = objects
    else:
      self.item = []
    
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







