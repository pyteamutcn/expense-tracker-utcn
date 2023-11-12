import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
import plotly.graph_objects as go
from anvil.tables import app_tables
import anvil.server
import anvil.plotly_templates

anvil.plotly_templates.set_default("rally")

#Return the contents of the Files data table. If this table included secure data, 
#we would only want to return the data that can be user visible
@anvil.server.callable
def return_table():
  return app_tables.files.search()

@anvil.server.callable
def return_spending_table():
  return app_tables.spending.search()

@anvil.server.callable
def return_data(month):
  #Your code to process and return data goes here
  if month == "November":
    return [
      [11342, 11673, 12684, 12933], 
      [14331, 14887, 13520, 13021],
      [4331, 4887, 3520, 3021]
    ]
  elif month == "October":
    return [
      [8695, 8704, 9201, 9554], 
      [12332, 12633, 13000, 13843],
      [4331, 4887, 3520, 3021]
    ]
  elif month == "September":
    return [
      [5680, 5743, 5802, 6003], 
      [7832, 7945, 8432, 8049],
      [4331, 4887, 3520, 3021]
    ]

@anvil.server.callable
def return_bar_charts():
  #You can use any Python plotting library on the server including Plotly Express, MatplotLib, Seaborn, Bokeh
  fig = go.Figure(
    [
      go.Bar(
        y=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
        x=[13, 21, 64, 119, 94],
        orientation='h',
        name="New Users"
        ),
      go.Bar(
        y=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
        x=[24, 35, 80, 250, 274],
        orientation='h',
        name="Existing Users"
      ),
    ]
  )
  
  fig.update_layout(
    barmode="stack",
  )
  return fig
