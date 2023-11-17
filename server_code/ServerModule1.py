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
def get_sales():  #added by Dumbo, return spending table of the current user
  currUser = anvil.users.get_user()
  if currUser:
    return app_tables.spending.client_writable(owner=currUser)

@anvil.server.callable
def return_table():
  return app_tables.files.search()

@anvil.server.callable
def return_spending_table():
  return app_tables.spending.search()

@anvil.server.callable
def return_data(month): #parametru user?
  #Your code to process and return data goes here
  if month == "November":
    return [
      [342, 673, 684, 933], 
      [331, 887, 520, 21],
      [331, 887, 520, 300]
    ]
  elif month == "October":
    return [
      [695, 704, 201, 554], 
      [332, 633, 400, 843],
      [331, 887, 520, 321]
    ]
  elif month == "September":
    return [
      [680, 743, 202, 600], 
      [832, 945, 432, 49],
      [331, 887, 520, 189]
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
