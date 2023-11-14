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

  def text_nameAddExpense_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_nameAddExpense.role == "input-error" and self.text_nameAddExpense.text:
      self.text_nameAddExpense.role = "default"

  def text_priceAddExpense_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_priceAddExpense.role == "input_error" and self.text_priceAddExpense.text:
      self.text_priceAddExpense.role = "default"

  def text_categoryAddExpense_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_categoryAddExpense.role == "input_error" and self.text_categoryAddExpense.text:
      self.text_categoryAddExpense.role = "default"

  def date_AddExpense_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.date_AddExpense.role == "input_error" and self.date_AddExpense.date:
      self.date_AddExpense.role = "default"

  def saveAddExpense_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_nameAddExpense.text
    price = self.text_priceAddExpense.text
    category = self.text_categoryAddExpense.text
    date = self.date_AddExpense.date
    if name and price and category and date:
      self.raise_event("x-close-alert", value=True)
    else:
      if not name:
        self.text_nameAddExpense.role = "input_error"
      if not price:
        self.text_priceAddExpense.role = "input_error"
      if not category:
        self.text_categoryAddExpense.role = "input_error"
      if not date:
        self.date_AddExpense.role = "input_error"

  def cancelAddExpense_click(self, **event_args):
    self.raise_event("x-close-alert", value=False)



    


  

  

  


