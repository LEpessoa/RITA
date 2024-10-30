from ._anvil_designer import RowTemplate10Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....show_description_page import show_description_page

class RowTemplate10(RowTemplate10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def show_rcm_button_click(self, **event_args):
    alert(content=show_description_page(self.item['name'],self.item['description']),large=True)

  def delete_rcm_button_click(self, **event_args):
    print('Deleting RCM: '+ self.item['name'])
    self.parent.raise_event('x-delete-rcm',rcm=self.item)
    self.refresh_data_bindings()





