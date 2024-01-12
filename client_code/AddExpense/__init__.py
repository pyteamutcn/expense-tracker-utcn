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
    currUser = anvil.users.get_user() #added by Dumbo
    self.drop_down_1.items = [(row["Name"], row) for row in (app_tables.categories.search(Owner=None))] + [(row["Name"], row) for row in (app_tables.categories.search(Owner=currUser))]#added by DUmbo, updated dropdown values

  def text_nameAddExpense_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_nameAddExpense.role == "input_error" and self.text_nameAddExpense.text:
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
    #category = self.text_categoryAddExpense.text
    date = self.date_AddExpense.date
    currUser = anvil.users.get_user() #added user specific sales records, so that the sever filters only current user specific data "Dumbo"
    #added new record on spending table so that rows can be identified by user "Dumbo"
    categori = self.drop_down_1.selected_value #addded by Dumbo, matches the sale to the category in the DB

    # Decomment only for terminal test
    # print(name, price, category, date)
    
    if name and price and date and currUser and categori:
      app_tables.spending.add_row(Name = name, Price = float(price), Date = date, owner= currUser, category_dd= categori)
    else:
      if not name:
        self.text_nameAddExpense.role = "input_error"
      if not price:
        self.text_priceAddExpense.role = "input_error"
      if not category:
        self.text_categoryAddExpense.role = "input_error"
      if not date:
        self.date_AddExpense.role = "input_error"
      #if not currUser: ??
 

  def cancelAddExpense_click(self, **event_args):
    self.raise_event("x-close-alert", value=False)

  def text_priceAddExpense_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_categoryAddExpense_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def addCategory_click(self, **event_args):
    """This method is called when the button is clicked"""
    category = self.text_categoryAddExpense.text #added by Dumbo, you can add custom categories by writing in the textbox, updates the textbox
    if category:
      currUser = anvil.users.get_user()
      app_tables.categories.add_row(Name= category, Owner=currUser) #added by Dumbo, matches the custom category to the current user
      self.drop_down_1.items = [(row["Name"], row) for row in (app_tables.categories.search(Owner=None))] + [(row["Name"], row) for row in (app_tables.categories.search(Owner=currUser))]#added by All, updated dropdown values



    


  

  

  


