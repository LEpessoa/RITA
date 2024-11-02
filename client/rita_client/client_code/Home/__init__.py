from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .iot_objects_page import iot_objects_page
from .threat_types_page import threat_types_page
from .solutions_page import solutions_page
from .about_page import about_page
from .modelling_process_page import modelling_process_page
from .references_page import references_page
from .googlelike_page import googlelike_page
from ..confirmation_popup_modal import confirmation_popup_modal
from .googlelike_page.iot_objects_verification_page import iot_objects_verification_page

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)    
    self.search_text = ""
    # Any code you write here will run before the form opens.
    # current_page = about_page()
    current_page = googlelike_page()
    self.content_panel.clear()
    self.content_panel.add_component(current_page)
    # confirm = alert(content=confirmation_popup_modal(message='Wanna duck?'),buttons=[])    

  def iot_objects_link_click(self, **event_args):
    current_page = iot_objects_page()        
    self.content_panel.clear()
    self.content_panel.add_component(current_page)

  def threats_link_click(self, **event_args):
    current_page = threat_types_page()     
    self.content_panel.clear()
    self.content_panel.add_component(current_page)

  def solutions_link_click(self, **event_args):
    current_page = solutions_page()        
    self.content_panel.clear()
    self.content_panel.add_component(current_page)

  def about_link_1_click(self, **event_args):
    current_page = about_page()        
    self.content_panel.clear()
    self.content_panel.add_component(current_page)
    
  def set_open_form(self, form):
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(form)
    
  def addm4riota_link_1_click(self, **event_args):
    page = googlelike_page()
    self.set_open_form(page)

  def modelling_process_link_1_click(self, **event_args):
    current_page = modelling_process_page()        
    self.content_panel.clear()
    self.content_panel.add_component(current_page)

  def references_link_1_click(self, **event_args):
    current_page = references_page()        
    self.content_panel.clear()
    self.content_panel.add_component(current_page)

  def button_1_click(self, **event_args):
    anvil.server.call('search',{"tt":"Tampering","ico":"device","rs":None})








