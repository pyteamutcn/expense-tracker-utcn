import anvil.email
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

def return_month_spend_category(month,year,category): 
  currUser = anvil.users.get_user()
  data_for_month_cat = [
        row for row in app_tables.spending.search()
        if (row['Date'].month == month and row['Date'].year == year and row['owner'] == currUser and row['category_dd']['Name'] == category)
    ]
  total_price = 0
  for row in data_for_month_cat:
    total_price += row['Price']
  return total_price

@anvil.server.callable
def return_week1_spend(month,year): #adauga categorie daca ne hotaram sa facem si cu categorii custom and category
  currUser = anvil.users.get_user()
  data_food_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 1 and row['Date'].day <=7 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Food")    
    ]
  data_entertainment_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 1 and row['Date'].day <=7 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Entertainment")    
    ]
  data_bills_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 1 and row['Date'].day <=7 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Bills")    
    ]
  week1 = [0,0,0]
  for row in data_food_month:
    week1[0] += row['Price']
  for row in data_entertainment_month:
    week1[1] += row['Price']
  for row in data_bills_month:
    week1[2] += row['Price']

  return week1
  
@anvil.server.callable
def return_week2_spend(month,year): #adauga categorie daca ne hotaram sa facem si cu categorii custom and category
  currUser = anvil.users.get_user()
  data_food_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 8 and row['Date'].day <= 14 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Food")    
    ]
  data_entertainment_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 8 and row['Date'].day <= 14 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Entertainment")    
    ]
  data_bills_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 8 and row['Date'].day <= 14 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Bills")    
    ]
  week2 = [0, 0, 0]
  for row in data_food_month:
    week2[0] += row['Price']
  for row in data_entertainment_month:
    week2[1] += row['Price']
  for row in data_bills_month:
    week2[2] += row['Price']

  return week2

@anvil.server.callable
def return_week3_spend(month,year): #adauga categorie daca ne hotaram sa facem si cu categorii custom and category
  currUser = anvil.users.get_user()
  data_food_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 15 and row['Date'].day <= 21 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Food")    
    ]
  data_entertainment_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 15 and row['Date'].day <= 21 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Entertainment")    
    ]
  data_bills_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 15 and row['Date'].day <= 21 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Bills")    
    ]
  week3 = [0, 0, 0]
  for row in data_food_month:
    week3[0] += row['Price']
  for row in data_entertainment_month:
    week3[1] += row['Price']
  for row in data_bills_month:
    week3[2] += row['Price']

  return week3

@anvil.server.callable
def return_week4_spend(month,year): #adauga categorie daca ne hotaram sa facem si cu categorii custom and category
  currUser = anvil.users.get_user()
  data_food_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 22 and row['Date'].day <= 31 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Food")    
    ]
  data_entertainment_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 22 and row['Date'].day <= 31 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Entertainment")    
    ]
  data_bills_month = [
        row for row in app_tables.spending.search()
        if (row['Date'].day >= 22 and row['Date'].day <= 31 and row['Date'].month == month and row['Date'].year == year
            and row['owner'] == currUser and row['category_dd']['Name'] == "Bills")    
    ]
  week4 = [0, 0, 0]
  for row in data_food_month:
    week4[0] += row['Price']
  for row in data_entertainment_month:
    week4[1] += row['Price']
  for row in data_bills_month:
    week4[2] += row['Price']

  return week4

@anvil.server.callable
def return_data(month, year):
  #Your code to process and return data goes here
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
  
  week1 = anvil.server.call('return_week1_spend', string_to_int[month], year)
  week2 = anvil.server.call('return_week2_spend', string_to_int[month], year)
  week3 = anvil.server.call('return_week3_spend', string_to_int[month], year)
  week4 = anvil.server.call('return_week4_spend', string_to_int[month], year)
  return [
    [week1[0], week2[0], week3[0], week4[0]], #week1 week2 week3 week4
    [week1[1], week2[1], week3[1], week4[1]],
    [week1[2], week2[2], week3[2], week4[2]]
    ]
  

@anvil.server.callable
def return_bar_charts(month, year):
  #You can use any Python plotting library on the server including Plotly Express, MatplotLib, Seaborn, Bokeh
  if(month - 1 == 0):
    foodLM = return_month_spend_category(12,year-1,"Food")
    enLM = return_month_spend_category(12,year-1,"Entertainment")
    clLM = return_month_spend_category(12,year-1,"Clothes")
    hyLM = return_month_spend_category(12,year-1,"Hygene")
    billsLM = return_month_spend_category(12,year-1,"Bills")
  else:
    foodLM = return_month_spend_category(month-1,year,"Food")
    enLM = return_month_spend_category(month-1,year,"Entertainment")
    clLM = return_month_spend_category(month-1,year,"Clothes")
    hyLM = return_month_spend_category(month-1,year,"Hygene")
    billsLM = return_month_spend_category(month-1,year,"Bills")
  food = return_month_spend_category(month,year,"Food")
  en = return_month_spend_category(month,year,"Entertainment")
  cl = return_month_spend_category(month,year,"Clothes")
  hy = return_month_spend_category(month,year,"Hygene")
  bills = return_month_spend_category(month,year,"Bills")
    
  fig = go.Figure(
    [
      go.Bar(
        y=["Food", "Entertainment", "Clothes", "Hygene", "Bills"],
        x=[foodLM, enLM, clLM, hyLM, billsLM],
        orientation='h',
        name="Last Month"
        ),
      go.Bar(
        y=["Food", "Entertainment", "Clothes", "Hygene", "Bills"],
        x=[food, en, cl, hy, bills],
        orientation='h',
        name="This Month"
      ),
    ]
  )
  
  fig.update_layout(
    barmode="stack",
  )
  return fig

@anvil.server.callable
def sendMail():
  anvil.email.send(from_name = "My App Support", 
                 to = "prowhite91@gmail.com",
                 subject = "Welcome",
                 text = "Welcome to My App!")
