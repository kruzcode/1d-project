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


all_themes = ['nature', 'great views', 'leisure']
ATTRACTIONS = [ 
    { "name"    : "flower dome", 
      "theme": 'nature', "queue_time": 'long',
      "description" : "showcasing flowers from all over the world"
    }, 
    { "name"    : "skywalk", 
      "theme":'great views', "queue_time": 'short',
      "description" : "get a great view of the garden from here"
    },
      { "name"    : "goon lagoon", 
      "theme":'leisure', "queue_time": 'medium',
      "description" : "get a great view of the garden from here"
    }
]


## Data Entry -------------------------------------------------------------------------
## Shows you the code to 
## 1) write a title on the screen
## 2) how do you write a multiselect widget to allow the user to select more than one choice
## 3) how do you write text on the screen 
## The key attribute enables you to retrieve the data entered for that widget from st.session_state 
## ------------------------------------------------------------------------------------

st.title("Welcome to Panda Theme Park! Please enjoy our attractions!") # 'st' stands for streamlit (st.title -> same function as a print)
# streamlit is to access specific UXs

st.multiselect(
    label="Theme Filter",
    options=all_themes,
    key="theme_filter" 
    )
# the goal is to have multiple 'st.multiselect'

### Display user's choices as a debugging hint 
### This is stored in a datatype similar to a list
#st.write(st.session_state.user_selection)

queue_slide = st.slider("Queue Preference", min_value=0, max_value=120, value=30)
st.write(f"Queue time:{queue_slide}")

def queue_cat(t):
    if t < 80:
        cat = 'long'
    elif t < 40:
        cat = 'medium'
    else:
        cat = 'short'
    return cat

def reset_choices():
    st.session_state.theme_filter = []
    queue_slide = 30
## Calculation -------------------------------------------------------------------------
## Shows you the code to 
## 1) declare a button and detect if it is clicked through the if-statement 
## 2) obtain the user's inputs from the respective widgets using st.session_state 
## 3) call the functions in mylibrary.py to get the result
## 4) display the outcome in a streamlit table using a python dictionary 
## 5) How do you declare a button to execute a function when clicked
## ------------------------------------------------------------------------------------ 
def get_recommendations(attractions_list, theme_choice, queue_choice): #edited
    out = []
    for theme in theme_choices:
        for attraction in attractions_list:
            if (theme in attraction["theme"]) and (queue_choice in attraction['queue_time']):
                out.append(attraction)
            elif (theme in attraction["theme"]) ^ (queue_choice in attraction['queue_time']):
                out.append(attraction)
    return out
        
if st.button("Get me recommendations"):
    options = list( st.session_state.theme_filter )  
    queue_time = queue_cat(queue_slide)
    recs = get_recommendations(ATTRACTIONS, options, queue_time)
    st.table(recs)

st.button("Reset Selections", on_click=reset_choices)
