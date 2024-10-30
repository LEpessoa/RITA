from ._anvil_designer import about_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..description_page import description_page
from ..modelling_process_page import modelling_process_page
from ..references_page import references_page
from ..threat_types_page import threat_types_page
from ..iot_objects_page import iot_objects_page
from ..solutions_page import solutions_page

class about_page(about_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def set_open_form(self, form):
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(form)
    
  def description_button_1_click(self, **event_args):
    page = description_page()
    self.set_open_form(page)

  def references_button_17_click(self, **event_args):
    page = references_page()
    self.set_open_form(page)
    
  def PLTT_link_click(self, **event_args):
    page = threat_types_page(threat_type_filter='PLTT')
    self.set_open_form(page)

  def NTT_link_2_click(self, **event_args):
    page = threat_types_page(threat_type_filter='NTT')
    self.set_open_form(page)

  def HTT_link_3_click(self, **event_args):
    page = threat_types_page(threat_type_filter='HTT')
    self.set_open_form(page)

  def NLTT_link_4_click(self, **event_args):
    page = threat_types_page(threat_type_filter='NLTT')
    self.set_open_form(page)

  def ALTT_link_5_click(self, **event_args):
    page = threat_types_page(threat_type_filter='ALTT')
    self.set_open_form(page)

  def modelling_process_link_1_click(self, **event_args):
    page = modelling_process_page()
    self.set_open_form(page)

  def iot_objects_button_1_click(self, **event_args):
    page = iot_objects_page()
    self.set_open_form(page)    

  def PLTT_button_2_click(self, **event_args):
    self.PLTT_link_click()

  def NTT_button_3_click(self, **event_args):
    self.NTT_link_2_click()

  def HTT_button_4_click(self, **event_args):
    self.HTT_link_3_click()

  def NLTT_button_5_click(self, **event_args):
    self.NLTT_link_4_click()

  def altt_button_6_click(self, **event_args):
    self.ALTT_link_5_click()

  def eetk_button_7_click(self, **event_args):
    page = solutions_page(solution_type='EETK')
    self.set_open_form(page)

  def rtk_button_8_click(self, **event_args):
    page = solutions_page(solution_type='RTK')
    self.set_open_form(page)

  def sptk_button_9_click(self, **event_args):
    page = solutions_page(solution_type='SPTK')
    self.set_open_form(page)

  def drtk_button_10_click(self, **event_args):
    page = solutions_page(solution_type='DRTK')
    self.set_open_form(page)

  def sctk_button_11_click(self, **event_args):
    page = solutions_page(solution_type='SCTK')
    self.set_open_form(page)

  def shtk_button_12_click(self, **event_args):
    page = solutions_page(solution_type='SHTK')
    self.set_open_form(page)

  def frtk_button_13_click(self, **event_args):
    page = solutions_page(solution_type='FRTK')
    self.set_open_form(page)

  def sotk_button_14_click(self, **event_args):
    page = solutions_page(solution_type='SOTK')
    self.set_open_form(page)

  def dtk_button_15_click(self, **event_args):
    page = solutions_page(solution_type='DTK')
    self.set_open_form(page)

  def aak_button_16_click(self, **event_args):
    page = solutions_page(solution_type='AAK')
    self.set_open_form(page)

























