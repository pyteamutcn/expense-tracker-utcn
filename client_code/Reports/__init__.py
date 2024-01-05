from ._anvil_designer import ReportsTemplate
from anvil import *
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
    self.plot_1.data = [
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[510, 620, 687, 745, 881],
        name="Europe"
    ),
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[733, 880, 964, 980, 1058],
        name="Americas"
    ),
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[662, 728, 794, 814, 906],
        name="Asia"
    )
    ]

    #Return the figure from the server to populate plot_2
    self.plot_2.figure = anvil.server.call('return_bar_charts')

    self.plot_3.data = [
      go.Pie(
        labels=["Mobile", "Tablet", "Desktop"],
        values=[2650, 755, 9525]
      )
    ]
    
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
    

