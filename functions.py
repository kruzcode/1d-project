import streamlit as st
from attractions_dict import ATTRACTIONS, all_themes

@st.dialog("Filter Attractions")
def filter():
    st.write("Filter attractions")
    st.pills(
            "Filter by Theme",
            options=all_themes, 
            selection_mode="multi",
            label_visibility="collapsed",
            key="filter_themes"
            )
    st.write("Your selected options are: " +  ", ".join(st.session_state.filter_themes) + "")
    if st.button("Apply Filter"):
        st.session_state.filter = list(st.session_state.filter_themes) # storing the selected filter themes in session state
        
        st.rerun()  # rerun the app to apply the filter
        

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