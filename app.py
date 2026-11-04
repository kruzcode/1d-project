import streamlit as st

## The logic for the calculation is stored in functions in mylibrary.py 


## User Interface ---------------------------------------------------------------------
## This file shows you streamlit code for three parts.
## Business Data - how to specify the data for the attractions in the theme park.
## Data Entry - how to make widgets to get the user inputs. 
## Calculation - how to get the result from the user inputs. 
## ------------------------------------------------------------------------------------


## Business Data ---------------------------------------------------------------------
## Attractions belong to one or more of three categories, "nature", "great views", "shows"
## ALL_CATEGORIES  is a list of strings containing all the categories
## ATTRACTIONS is a list of dictionaries. 
## each dictionary represents one attraction and has three key-value pairs 
## the "category" key stores a list, which means one attraction can have more than one category
## ------------------------------------------------------------------------------------

NATURE = "nature"
GREAT_VIEWS = "great views"
SHOWS = "shows" 

ALL_CATEGORIES = [NATURE, GREAT_VIEWS, SHOWS]

ATTRACTIONS = [ 
    { "name"    : "flower dome", 
      "category": [ NATURE ], 
      "description" : "showcasing flowers from all over the world"
    }, 
    { "name"    : "skywalk", 
      "category": [ GREAT_VIEWS], 
      "description" : "get a great view of the garden from here"
    }, 
    { "name"    : "light show at supertree grove", 
      "category": [ GREAT_VIEWS, SHOWS], 
      "description" : "daily free light shows at 7.30 pm and 8.30 pm"
    }, 
    { "name"    : "the meadow", 
      "category": [ NATURE, SHOWS], 
      "description" : "enjoy free movie screening among the native trees at 6 pm"
    } 
]


## Data Entry -------------------------------------------------------------------------
## Shows you the code to 
## 1) write a title on the screen
## 2) how do you write a multiselect widget to allow the user to select more than one choice
## 3) how do you write text on the screen 
## The key attribute enables you to retrieve the data entered for that widget from st.session_state 
## ------------------------------------------------------------------------------------

st.title("What kind of attraction do you wish to visit at GBTB?") # 'st' stands for streamlit (st.title -> same function as a print)
# streamlit is to access specific UXs

st.multiselect(
    label="Select your category",
    options=ALL_CATEGORIES,
    key="user_selection" 
    )
# the goal is to have multiple 'st.multiselect'

### Display user's choices as a debugging hint 
### This is stored in a datatype similar to a list
st.write(st.session_state.user_selection)

### Define a function to clear the user's choices
def reset_choices():
    st.session_state.user_selection = []

## Calculation -------------------------------------------------------------------------
## Shows you the code to 
## 1) declare a button and detect if it is clicked through the if-statement 
## 2) obtain the user's inputs from the respective widgets using st.session_state 
## 3) call the functions in mylibrary.py to get the result
## 4) display the outcome in a streamlit table using a python dictionary 
## 5) How do you declare a button to execute a function when clicked
## ------------------------------------------------------------------------------------ 
def get_recommendations(attractions_list, choices): #edited
    out = []
    for choice in choices:
        for cat in attractions_list:
            if choice in cat["category"]:
                out.append(cat)
    return out
        
if st.button("Get me recommendations"):
    options = list( st.session_state.user_selection )  
    recs = get_recommendations(ATTRACTIONS, options)
    st.table(recs)

st.button("Reset Selections", on_click=reset_choices)
