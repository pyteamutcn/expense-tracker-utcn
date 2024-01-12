from ._anvil_designer import SalesTemplate
from anvil import *
from anvil import HtmlTemplate
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
from datetime import datetime 


class Sales(SalesTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        

        # Any code you write here will run before the form opens.
        # The x-axis of plot_1 will be the months of the year. The y-axis will be dummy data returned from the server
        self.x_weeks = ["Week1", "Week2", "Week3", "Week4"]
      
        # Get the y-values from the server
        current_year = datetime.now().year
        self.y_values = anvil.server.call('return_data', self.drop_down_1.selected_value, current_year)
        #self.display_table(app_tables.spending)
        self.create_line_graph()

        # Set the contents of the data grid to the contents of the Files table.
        # This is done on the secure server where you might only want to return user-visible data
        current_month = datetime.now().month
        self.user_sales = anvil.server.call('get_sales')
        self.repeating_panel_1.items = [row for row in self.user_sales.search() if (row['Date'].month == current_month)] #arata doar cheltuielile din luna curenta

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
      

  
    def create_line_graph(self):
        self.plot_1.data = [
            go.Scatter(
                x=self.x_weeks,
                y=self.y_values[0],
                #fill="tozeroy",
                line_color = 'red',
                name="Food"
            ),
            go.Scatter(
                x=self.x_weeks,
                y=self.y_values[1],
                #fill="tonexty",
                line_color = 'green',
                name="Entertainment"
            ),
            go.Scatter(
                x=self.x_weeks,
                y=self.y_values[2],
                #fill="tozeroy",
                line_color = 'blue',
                name="Bills"
            )
        ]

    # Update the values in the line graph based on the selected value of the drop-down menu
    def drop_down_1_change(self, **event_args):
        """This method is called when an item is selected"""
        current_year = datetime.now().year
        self.y_values = anvil.server.call('return_data', self.drop_down_1.selected_value, current_year) #aici trebe sa fac filtrare dupa user, doar la afisare
        self.create_line_graph()

    def label_7_show(self, **event_args):
      """This method is called when the Label is shown on the screen"""
      monthly_spendings = self.update_current_month_spendings()
      self.label_7.text = f"${monthly_spendings:.2f}"


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

