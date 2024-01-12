from ._anvil_designer import ReportsTemplate
from anvil import *
from datetime import datetime
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Reports(ReportsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

    #Populate plot_1 with dummy data. All three Bar charts will be added to the same figure
    self.clothesHandler("January", 2024)
    
    self.plot_1.data = [
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[510, 620, 687, 745, 881],
        name="Clothes"
    ),
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[733, 880, 964, 980, 1058],
        name="Food"
    ),
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[662, 728, 794, 814, 906],
        name="Entertainment"
    ),
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[662, 728, 794, 814, 906],
        name="Bills"
    )
    ]

    #Return the figure from the server to populate plot_2
    self.plot_2.figure = anvil.server.call('return_bar_charts')

    self.plot_3.data = [
      go.Pie(
        labels=["Hygene", "Junk Food", "Bills"],
        values=[2650, 755, 9525]
      )
    ]

  def costCategoriePerLuna(self, month, year, category):
    currUser = anvil.users.get_user()
    data_category_month = [
      row for row in app_tables.spending.search()
        if (row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == category)    
    ]

    price = 0
    for row in data_category_month:
      price += row['Price']
    print(price)
    return price
    
  
  def clothesHandler(self, currMonth, currYear):
    rez = [[], [], []]
    
    string_to_int = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
  }
    
    rezMonth = []
    rezYear = []
    
    for i in range(0, 5):  # Exclude the current month
            # Calculate the month and year for each of the 3 months before the current month
            past_month = (string_to_int[currMonth] - i) % 12 or 12
            rezMonth.append(past_month)
            if string_to_int[currMonth] > 5 :
              past_year = currYear
            else:
              past_year = currYear - 1 if past_month in (8, 9, 10, 11, 12) else currYear
            rezYear.append(past_year)

    ## past_month = (current_month - i) % 12 or 12
    for i in range(0, 5):
      rez[0].append(rezMonth[i])

    for i in range(0, 5):
      rez[1].append(self.costCategoriePerLuna(rezMonth[i], rezYear[i], "Clothes"))
    print(rez[1])

    
    
  
  def label_7_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    monthly_spendings = self.update_current_month_spendings()
    self.label_7.text = f"${monthly_spendings:.2f}"

  def update_current_month_spendings(self):
      # Dynamically get the current month and year
      current_month = datetime.now().month
      current_year = datetime.now().year
        

      # Fetch current month's spendings
      current_month_spendings = anvil.server.call('return_month_spend', current_month, current_year)

      # Calculate the total spendings for the current month
      total_spendings = 0
      for row in current_month_spendings:
        total_spendings = total_spendings + row['Price']

      # Update the label text
      return total_spendings


  def label_8_show(self, **event_args):
      """This method is called when the Label is shown on the screen"""
      # Calculate the average spendings for the past 3 months
      average_spendings = self.calculate_average_spendings()
        
      # Update the label text
      self.label_8.text = f"${average_spendings:.2f}"
    
  def calculate_average_spendings(self):
      # Get the current month and year
      current_month = datetime.now().month
      current_year = datetime.now().year

      # Calculate the average spendings for the 3 months before the current month
      total_spendings = 0
      for i in range(1, 4):  # Exclude the current month
          # Calculate the month and year for each of the 3 months before the current month
          past_month = (current_month - i) % 12 or 12
          if current_month > 3 :
            past_year = current_year
          else:
            past_year = current_year - 1 if past_month in (10, 11, 12) else current_year

          # Fetch spendings for each of the 3 months before the current month
          past_month_spendings = anvil.server.call('return_month_spend', past_month, past_year)

          # Calculate total spendings for each of the 3 months before the current month
          for row in past_month_spendings:
              total_spendings += row['Price']

      # Calculate the average spendings
      average_spendings = total_spendings / 3 if total_spendings > 0 else 0
      return average_spendings
    

