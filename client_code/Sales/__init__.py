from ._anvil_designer import SalesTemplate
from anvil import *
from anvil import HtmlTemplate
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

class Sales(SalesTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        # The x-axis of plot_1 will be the months of the year. The y-axis will be dummy data returned from the server
        self.x_weeks = ["Week1", "Week2", "Week3", "Week4"]
        
        # Get the y-values from the server
        self.y_values = anvil.server.call('return_data', "November")
        #self.display_table(app_tables.spending)
        self.create_line_graph()

        # Set the contents of the data grid to the contents of the Files table.
        # This is done on the secure server where you might only want to return user-visible data
        self.repeating_panel_1.items = anvil.server.call('return_spending_table')
  
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
                name="Car Expense"
            ),
            go.Scatter(
                x=self.x_weeks,
                y=self.y_values[2],
                #fill="tozeroy",
                line_color = 'blue',
                name="Personal Expense"
            )
        ]

    # Update the values in the line graph based on the selected value of the drop-down menu
    def drop_down_1_change(self, **event_args):
        """This method is called when an item is selected"""
        self.y_values = anvil.server.call('return_data', self.drop_down_1.selected_value)
        self.create_line_graph()
