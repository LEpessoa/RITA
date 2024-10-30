from ._anvil_designer import solutions_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class solutions_page(solutions_pageTemplate):
  def __init__(self, solution_type=None,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.solution_type = solution_type
    
    # Any code you write here will run before the form opens.
    
    # Populate Solutions Dropdown       
    self.solution_drop_down_1.items = anvil.server.call('getAllSolutionTypesDropdown')
    
    #Populate IoT Threats Dropdown
    self.threats_drop_down.items = anvil.server.call('getAllThreatTypesDropdown')
    
    #Pre-select a value for the solution dropdown base on solution_type property
    if self.solution_type != None:
      self.solution_drop_down_1.selected_value = self.solution_type
      print('Selected solution: ' + self.solution_type)
    
    #Populate Solutions RepeatingPanel / table
    self.threats_drop_down_change()

  def form_show(self, **event_args):
    self.headline_1.scroll_into_view()

  def threats_drop_down_change(self, **event_args):
    # solutionDTO has the format below, the values between quotes should be replaced by the wanted values, or None.
    # ("id", "resilient_solution_id", 'name', 'description', 'references', 'resilient_solution_enum', TT_id)    
    solutionDTO = (None, self.solution_drop_down_1.selected_value, None, None, None, None, self.threats_drop_down.selected_value)
    self.solutions_repeating_panel_1.items = anvil.server.call('filterSolutions',solutionDTO)
     


