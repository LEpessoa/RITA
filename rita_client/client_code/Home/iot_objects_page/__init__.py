from ._anvil_designer import iot_objects_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class iot_objects_page(iot_objects_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.header_headline.scroll_into_view()
    # Any code you write here will run before the form opens.
    def buildObject(obj):
      return {'id':obj[0],'name':obj[1],'acronym':obj[2]}
    
    iot_critical_objects_list = map(buildObject,anvil.server.call('getDevices_resource'))    
    self.iot_critical_objects_RP.items = iot_critical_objects_list
    
  def scrollTop(self, **kwargs):
    self.header_headline.scroll_into_view()