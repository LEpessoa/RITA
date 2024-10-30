from ._anvil_designer import iot_objects_verification_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..add_iot_critical_objects_page import add_iot_critical_objects_page
from .... import global_services as gs
from ..pdf_page import pdf_page
from ..html_form_report_pdf import html_form_report_pdf

class iot_objects_verification_page(iot_objects_verification_pageTemplate):
  def __init__(self,critical_objects_found_dic={} ,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.critical_objects_found_dic = critical_objects_found_dic
    self.identified_iot_objects_repeating_panel.items = self.critical_objects_found_dic
    # Any code you write here will run before the form opens.
    self.toggle_no_critical_object_found()
    self.input_content_label.text = gs.googleLikePageTextAreaContent
      
  def toggle_no_critical_object_found(self, **event_args):
    # Set the visibility fot the data grid and no critical objects found warning according to the data-grid's list length
    self.identified_iot_objects_data_grid.visible = (len(self.critical_objects_found_dic) != 0)
    self.no_critical_object_found_label_2.visible = (len(self.critical_objects_found_dic) == 0)

  def add_object_button_click(self, **event_args):
    if self.identified_iot_objects_repeating_panel.items == None:
      self.identified_iot_objects_repeating_panel.items = []
    result = alert(content=add_iot_critical_objects_page(critical_object_list=list(self.identified_iot_objects_repeating_panel.items)), dismissible=False,large=True, buttons=[])
    print('Result received is: ')
    print(result)
    if len(result) != 0 :
      self.critical_objects_found_dic = result
      self.identified_iot_objects_repeating_panel.items = result
    self.toggle_no_critical_object_found()

  def debug_button_click(self, **event_args):
    print(self.critical_objects_found_dic)

  def generate_report_button_click(self, **event_args):
    # pdf = anvil.server.call('create_pdf')
    # anvil.media.download(pdf)
    # result = alert(content=html_form_report_pdf(input_dic=self.critical_objects_found_dic),               
    #            large=True,
    #            buttons=[
    #              ("Close", "close"),                 
    #            ])
    report = html_form_report_pdf(input_dic=self.critical_objects_found_dic, lastPage=self)
    open_form(report)




    


