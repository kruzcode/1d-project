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


all_themes = ['immersive', 'thrill', 'sightseeing', 'relaxation']
ATTRACTIONS = [ 
    { "name"    : "Mickey & Minnie's Runaway Railway", 
      "theme": 'thrill, immersive', "queue_time": 'short',
      "description" : "A trackless dark ride that takes guests straight into a chaotic, colorful Mickey Mouse cartoon short."
    }, 
        { "name"    : "Sorcerer’s Apprentice: Broomstick Brigade", 
      "theme": 'thrill', "queue_time": 'medium',
      "description" : "A swinging suspended coaster where riders dodge overflowing water buckets and enchanted brooms inside Yen Sid’s tower."
    }, 
    { "name"    : "Furious Five: Valley of Peace Coaster", 
      "theme":'thrill', "queue_time": 'long',
      "description" : "A high-flying launched coaster featuring near-miss elements and inversions themed around the acrobatic fighting styles of Tigress, Crane, Viper, Monkey, and Mantis."
    },
      { "name"    : "Kung Fu Panda: Journey of the Dragon Warrior", 
      "theme":'sightseeing', "queue_time": 'medium',
      "description" : "A scenic indoor boat ride through the Jade Palace and the Spirit Realm as Po battles Kai."
    },
    { "name"    : "Buzz Lightyear’s Star Command Drop", 
      "theme":'sightseeing', "queue_time": 'long',
      "description" : "A thrilling drop-tower ride where riders help Buzz launch into hyperspace to defend the Gamma Quadrant from Emperor Zurg."
    },
    { "name"    : "Mickey’s PhilharMagic", 
      "theme":'immersive', "queue_time": 'short',
      "description" : "A 3D musical film experience where Donald Duck steals Mickey's sorcerer hat, sending the audience tumbling through classic animated worlds."
    },
    { "name"    : "Slinky Dog Dash", 
      "theme":'immersive', "queue_time": 'medium',
      "description" : "A family coaster set in Andy's backyard where riders launch across tracks built from his Mega Coaster Play Kit."
    },
    { "name"    : "Toy Story Mania!", 
      "theme":'immersive', "queue_time": 'long',
      "description" : "An interactive 4D carnival-game attraction where riders wear 3D glasses and launch virtual darts, rings, and pies at targets."
    },
    { "name"    : "Steamboat Willie’s River Race", 
      "theme":'relaxation, sightseeing', "queue_time": 'short',
      "description" : "A family-friendly water flume ride styled in classic 1928 black-and-white animation, complete with whistling steamboats and slapstick gags."
    },
    { "name"    : "Po’s Noodle Bowl Spin", 
      "theme":'relaxation', "queue_time": 'medium',
      "description" : "A shill teacup-style flat ride set inside Mr. Ping’s noodle shop, where oversized soup bowls spin and tilt to a lively kung fu soundtrack."
    },
    { "name"    : "Kung Fu Panda: Journey of the Dragon Warrior", 
      "theme":'relaxation', "queue_time": 'long',
      "description" : "A scenic indoor boat ride through the Jade Palace and the Spirit Realm as Po battles Kai."
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
    select_all=False,
    key="theme_filter" 
    )
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
    st.session_state.theme_filter = []
    st.session_state.queue_slide = 120
## Calculation -------------------------------------------------------------------------
## Shows you the code to 
## 1) declare a button and detect if it is clicked through the if-statement 
## 2) obtain the user's inputs from the respective widgets using st.session_state 
## 3) call the functions in mylibrary.py to get the result
## 4) display the outcome in a streamlit table using a python dictionary 
## 5) How do you declare a button to execute a function when clicked
## ------------------------------------------------------------------------------------ 
def filter_recommendations(attractions_list, theme_choice, queue_choice):
    out = []
    for time in queue_choice:                      
        for theme in theme_choice:                
            for attraction in attractions_list:    
                if (theme in attraction["theme"]) and (time in attraction['queue_time']) and (attraction not in out):
                    out.append(attraction)       
    return out

def find_recommendations(attractions_list, theme_choice, queue_choice): #edited
    out = []
    #for time in queue_choice:
    for attraction in attractions_list:
        check_theme = sorted(attraction["theme"])
        sorted_theme_choice = sorted(", ".join(theme_choice))
        if (check_theme == sorted_theme_choice) and (time in attraction['queue_time']):
            out.append(attraction)
    return out

toggle = st.toggle("Find/Filter")

options = list( st.session_state.theme_filter )  
queue_time = queue_cat(st.session_state.queue_slide)
if options == []:
    options=all_themes
if toggle:
    recs = filter_recommendations(ATTRACTIONS, options, queue_time)
else: 
    recs = find_recommendations(ATTRACTIONS, options, queue_time)
st.table(recs)    

st.button("Reset Selections", on_click=reset_choices)
