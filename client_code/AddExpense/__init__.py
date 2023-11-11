from ._anvil_designer import AddExpenseTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AddExpense(AddExpenseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def save_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    service = self.service_box.text
    amount = self.amount_box.text
    if service and amount:
      self.raise_event("x-close-alert", value=True)
    else:
      if not service:
        self.service_box.role = "input-error"
      if not amount:
        self.amount_box.role = "input-error"

  def cancel_button_click(self, **event_args):
    self.raise_event("x-close-alert", value=False)

  def service_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.service_box.role == "input-error" and self.service_box.text:
      self.service_box.role = "default"

  def amount_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.amount_box.role == "input-error" and self.amount_box.text:
      self.amount_box.role = "default"



    


  

  

  


