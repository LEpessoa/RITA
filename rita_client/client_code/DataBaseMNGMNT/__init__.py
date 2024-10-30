from ._anvil_designer import DataBaseMNGMNTTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class DataBaseMNGMNT(DataBaseMNGMNTTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    list = anvil.server.call('getDevices_resource')
    print(list)

  def clean_devices_click(self, **event_args):
    anvil.server.call('cleanDevices_resource')

  def get_threats_click(self, **event_args):
    anvil.server.call('getThreats_resource')

  def get_solutions_click(self, **event_args):
    anvil.server.call('getSolutions_resource')
    

  def clean_solutions_click(self, **event_args):
    anvil.server.call('cleanSolutions_resource')

  def link_objects_and_threats_button_click(self, **event_args):
    result = anvil.server.call('link_threats_to_objects')
    print(result)

  def clear_link_threats_objects_button_click(self, **event_args):
    anvil.server.call('clear_link_threats_to_objects')









