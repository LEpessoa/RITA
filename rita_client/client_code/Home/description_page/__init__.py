from ._anvil_designer import description_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..complete_addm4riota_page import complete_addm4riota_page
from ..modelling_process_page import modelling_process_page
from .definition_resilient_iot_page import definition_resilient_iot_page
class description_page(description_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    current_page = definition_resilient_iot_page()        
    self.content_panel.clear()
    self.content_panel.add_component(current_page)

  def complete_addm4riota_link_1_click(self, **event_args):
    current_page = complete_addm4riota_page()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(current_page)

  def modelling_process_link_2_click(self, **event_args):
    current_page = modelling_process_page()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(current_page)




