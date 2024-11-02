import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

googleLikePageTextAreaContent = ""

def setGoogleLikePageTextAreaContent(stringVal):
  global google_like_page_text_area_content
  print("setGoogleLikePageTextAreaContent called with input: "+stringVal)
  google_like_page_text_area_content = stringVal

def getGoogleLikePageTextAreaContent():
  global googleLikePageTextAreaContent
  print("Getting saved text area value!")
  print(googleLikePageTextAreaContent)
  return googleLikePageTextAreaContent
