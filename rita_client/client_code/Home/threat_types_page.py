from ._anvil_designer import threat_types_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class threat_types_page(threat_types_pageTemplate):
  def __init__(self, threat_type_filter=(None,None,None,None,None), **properties):
    # threat_filter_format = (IoTCriticalObject, iot_threat_id,name,description,ResilientSolutionIds)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.threat_type_filter = threat_type_filter    
    # Any code you write here will run before the form opens.
    
    # Populate Filter By Threat Types Dropdown       
    self.filter_by_threat_type_drop_down.items = anvil.server.call('getAllThreatTypesDropdown')
    
    # Populate Filter By Solution Types Dropdown       
    self.filter_by_iot_obj_drop_down.items = anvil.server.call('getAllIoTObjectsDropdown')
    
    # Load a filtered list on the repeating panel
    self.applyLoadedFilter()

    
  def filterThreats(self, threatTypeDTO=None,**event_args):
    search_text = self.search_text_box.text
    # selectedThreatType = self.filter_by_threat_type_drop_down.selected_value
    # selectedICOType = self.filter_by_iot_obj_drop_down.selected_value
    # threat_filter_format = (IoTCriticalObject, iot_threat_id,name,description,ResilientSolutionIds)
    selected_iot = self.filter_by_iot_obj_drop_down.selected_value
    # print(f'Selected IoT value: {selected_iot}')
    selected_threat = self.filter_by_threat_type_drop_down.selected_value
    # print(f'Selected threat type value is: {selected_threat}')
    if threatTypeDTO==None:
      threatTypeDTO = (selected_iot,selected_threat,search_text,search_text,search_text)
    print('threateTypeDTO is:')
    print(threatTypeDTO)
    filtered_results = anvil.server.call('filterThreatTypes', threatTypeDTO)
    self.threats_repeating_panel_1.items = map(lambda obj : {'id':obj[0],'iot_objects':obj[1],'threat_id':obj[2],'name':obj[3],'description':obj[4],'reference':obj[4],'resilient_solution_ids':obj[5]}, filtered_results)

  def scroll_top(self, **event_args):    
    self.headline_1.scroll_into_view()
  
  def applyLoadedFilter(self, **event_args):
    if self.threat_type_filter != None:
       # threat_filter_format = (IoTCriticalObject, iot_threat_id,name,description,ResilientSolutionIds)
      if (self.threat_type_filter[0] != None):
        self.filter_by_iot_obj_drop_down.selected_value = self.threat_type_filter[0]
      if (self.threat_type_filter[1] != None):
        self.filter_by_threat_type_drop_down.selected_value = self.threat_type_filter[1]    
    self.filterThreats(self.threat_type_filter)





