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
def return_month_spend(month,year): 
  currUser = anvil.users.get_user()
  data_for_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].month == month and row['Date'].year == year and row['owner'] == currUser)
    ]
  return data_for_month

@anvil.server.callable
def return_week1_spend(month,year): #adauga categorie daca ne hotaram sa facem si cu categorii custom
  currUser = anvil.users.get_user()
  data_for_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 1 and row['Date'].day <=7 and row['Date'].month == month and row['Date'].year == year and row['owner'] == currUser)    
    ]
  week1_total = 0
  for row in data_for_month:
    week1_total += row['Price']
    print(week1_total)
  return data_for_month


@anvil.server.callable
def return_data(month):
  #Your code to process and return data goes here
  week1 = anvil.server.call('return_week1_spend', 1, 2024)
  print(week1)
  if month == "January":
    return [
      [51, 673, 684, 933], #week1 week2 week3 week4
      [331, 887, 520, 21],
      [331, 887, 520, 300]
    ]
  elif month == "October":
    return [
      [695, 704, 201, 554], 
      [332, 633, 400, 843],
      [331, 887, 520, 321]
    ]
  

@anvil.server.callable
def return_bar_charts():
  #You can use any Python plotting library on the server including Plotly Express, MatplotLib, Seaborn, Bokeh
  fig = go.Figure(
    [
      go.Bar(
        y=["Food", "Entertainment", "Clothes", "Hygene", "Junk Food"],
        x=[13, 21, 64, 119, 94],
        orientation='h',
        name="Last Month"
        ),
      go.Bar(
        y=["Food", "Entertainment", "Clothes", "Hygene", "Junk Food"],
        x=[24, 35, 80, 250, 274],
        orientation='h',
        name="This Month"
      ),
    ]
  )
  
  fig.update_layout(
    barmode="stack",
  )
  return fig
