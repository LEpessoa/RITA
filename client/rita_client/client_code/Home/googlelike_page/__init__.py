from ._anvil_designer import googlelike_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .iot_objects_verification_page import iot_objects_verification_page
from ... import global_services as gs

class googlelike_page(googlelike_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)        
    self.use_cases_text_area.text = gs.googleLikePageTextAreaContent
    # Any code you write here will run before the form opens.
  
  def set_open_form(self, form):
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(form)
    
  def find_button_click(self, **event_args):    
    textToSend = self.use_cases_text_area.text    
    answer = anvil.server.call('findIco', textToSend)
    print(answer)
    page = iot_objects_verification_page(critical_objects_found_dic=answer)
    self.set_open_form(page)

  def use_cases_text_area_change(self, **event_args):
    gs.googleLikePageTextAreaContent = self.use_cases_text_area.text



