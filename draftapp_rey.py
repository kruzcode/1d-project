import streamlit as st
# from attractions_dict import ATTRACTIONS, all_themes

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

# initialize the list of themes and attractions
all_themes = ['nature', 'great views', 'leisure']
ATTRACTIONS = [ 
    { "name"    : "flower dome", 
      "theme": 'nature', "queue_time": 'long',
      "description" : "showcasing flowers from all over the world"
    }, 
        { "name"    : "jizzler's ring", 
      "theme": 'nature', "queue_time": 'short',
      "description" : "showcasing flowers from all over the world"
    }, 
    { "name"    : "skywalk", 
      "theme":'great views', "queue_time": 'short',
      "description" : "get a great view of the garden from here"
    },
      { "name"    : "goon lagoon", 
      "theme":'leisure, nature', "queue_time": 'medium',
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

# st.pills()- similar to a st.selectbox or st.multiselect where the options are displayed as pill-buttons instead of a drop-down list.
selected_themes = st.pills(
    "Filter by Theme",
    options=all_themes,
    selection_mode="multi",
    label_visibility="collapsed",
    key="filter_themes"
)

st.text("Your selected options are: " +  ", ".join(selected_themes) + "")

search_query = st.text_input(
    "Search for an attraction",
    label_visibility="collapsed",
    placeholder="Search for an attraction",
    key="search_attraction"
)


search_query_strippedlower = search_query.strip().lower()

## Commented out the following code for now, using pills instead of multiselect for theme selection.
# st.multiselect(
#     label="Theme Filter"    ,
#     options=all_themes,
#     select_all=False,
#     key="theme_filter",
#     filter_mode="fuzzy"
#     )
# the goal is to have multiple 'st.multiselect'

### Display user's choices as a debugging hint 
### This is stored in a datatype similar to a list
#st.write(st.session_state.user_selection)

st.slider("Queue Preference", min_value=0, max_value=120, value=120, key='queue_slide')
st.write(f"Queue time: {st.session_state.queue_slide}mins")

def queue_cat(t):
    cat = []
    if t >= 0:
        cat.append('short')
    if t > 40:
        cat.append('medium')
    if t > 80:
        cat.append('long')
    return cat

def reset_choices():
    st.session_state.filter_themes = []
    # st.session_state.theme_filter = []
    st.session_state.queue_slide = 120
    st.session_state.search_attraction = ""
## Calculation -------------------------------------------------------------------------
## Shows you the code to 
## 1) declare a button and detect if it is clicked through the if-statement 
## 2) obtain the user's inputs from the respective widgets using st.session_state 
## 3) call the functions in mylibrary.py to get the result
## 4) display the outcome in a streamlit table using a python dictionary 
## 5) How do you declare a button to execute a function when clicked
## ------------------------------------------------------------------------------------ 

# output a table, can i make it so that it gets input for the search bar, theme filter and queue slider? 

# def filter_recommendations(attractions_list, theme_choice, search_query, queue_choice): #edited
#     out = []
#     for search in search_query:
#         for time in queue_choice:
#             for theme in theme_choice:
#                 for attraction in attractions_list:
#                     if (theme in attraction["theme"]) and (time in attraction['queue_time']):
#                         out.append(attraction)
#     return out

# initialize out as a empty list, then for each attraction in the attractions_list, check if the theme_choice is in the attraction's theme and if the queue_choice is in the attraction's queue_time. If both conditions are met, append the attraction to the out list. Finally, return the out list. 
# def find_recommendations(attractions_list, theme_choice, search_query, queue_choice): #edited
#     out = []
#     #for time in queue_choice:
#     for attraction in attractions_list:
#         attr_name = attraction["name"].lower() # convert the attraction name to lowercase for case-insensitive comparison
#         check_attr = sorted(attr_name)

#         if search_query not in attr_name:
#             continue  # Skip this attraction if it doesn't match the search query
#         check_theme = sorted(attraction["theme"])
#         sorted_theme_choice = sorted(", ".join(theme_choice))
#         if (check_theme == sorted_theme_choice):# and (time in attraction['queue_time']):
#             out.append(attraction)
#     return out



def find_recommendations(attractions_list, theme_choice, search_query, queue_choice): # takes in the attracitons dict, options will be the filtered choices,  query from the search and lastly the queue time.
    out = []
    for attractions in attractions_list:
        attr_name = attractions["name"].lower() # convert the attraction name to lowercase for case-insensitive comparison
        attr_theme = attractions["theme"]
        queue_time = attractions["queue_time"]

        # flexible substring search anywhere inside the attraction's name
        if search_query in attr_name and any(theme in attr_theme for theme in theme_choice) and queue_time in queue_choice:
            out.append(attractions)
    return out
        



options = list( st.session_state.filter_themes )  
# options = list( st.session_state.theme_filter )  
queue_time = queue_cat(st.session_state.queue_slide)
if options == []:
    options=all_themes
recs = find_recommendations(ATTRACTIONS, options, search_query_strippedlower, queue_time)
st.table(recs)    

st.button("Reset Selections", on_click=reset_choices)
