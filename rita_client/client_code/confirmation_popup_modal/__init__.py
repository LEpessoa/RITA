from ._anvil_designer import confirmation_popup_modalTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class confirmation_popup_modal(confirmation_popup_modalTemplate):
  def __init__(self, message=None, confirmation_button_text='yes', cancel_button_text='no',**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.message = message
    self.confirmation_button_text = confirmation_button_text
    self.cancel_button_text = cancel_button_text
    
    
    # Any code you write here will run before the form opens.
    self.confirmation_button.text = confirmation_button_text
    self.cancel_button.text = cancel_button_text
    self.message_label.text = message

  def confirmation_button_click(self, **event_args):
    self.raise_event('x-close-alert',value=True)

  def cancel_button_click(self, **event_args):
    self.raise_event('x-close-alert',value=False)