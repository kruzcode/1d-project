import streamlit as st

all_themes = ['immersive', 'thrill', 'sightseeing', 'relaxation']
all_height = ['No height restrictions', 'Over 81 cm OK', 'Over 90 cm OK', 'Over 102 cm OK']
ATTRACTIONS = [
    {
        "name": "Mickey & Minnie's Runaway Railway",
        "theme": "thrill, immersive, sightseeing", "queue_time": "short",
        "height_restriction": "0-250 cm",
        "description": "A trackless dark ride that takes guests straight into a chaotic, colorful Mickey Mouse cartoon short."
    },
    {
        "name": "Sorcerer's Apprentice: Broomstick Brigade",
        "theme": "thrill, immersive", "queue_time": "medium",
        "height_restriction": "102-250 cm",
        "description": "A swinging suspended coaster where riders dodge overflowing water buckets and enchanted brooms inside Yen Sid's tower."
    },
    {
        "name": "Furious Five: Valley of Peace Coaster",
        "theme": "thrill, sightseeing", "queue_time": "long",
        "height_restriction": "102-250 cm",
        "description": "A high-flying launched coaster featuring near-miss elements and inversions themed around the acrobatic fighting styles of Tigress, Crane, Viper, Monkey, and Mantis."
    },
    {
        "name": "Kung Fu Panda: Journey of the Dragon Warrior",
        "theme": "sightseeing, relaxation, immersive", "queue_time": "medium",
        "height_restriction": "0-250 cm",
        "description": "A scenic indoor boat ride through the Jade Palace and the Spirit Realm as Po battles Kai."
    },
    {
        "name": "Buzz Lightyear's Star Command Drop",
        "theme": "thrill", "queue_time": "long",
        "height_restriction": "102-250 cm",
        "description": "A thrilling drop-tower ride where riders help Buzz launch into hyperspace to defend the Gamma Quadrant from Emperor Zurg."
    },
    {
        "name": "Mickey's PhilharMagic",
        "theme": "relaxation", "queue_time": "short",
        "height_restriction": "0-250 cm",
        "description": "A 3D musical film experience where Donald Duck steals Mickey's sorcerer hat, sending the audience tumbling through classic animated worlds."
    },
    {
        "name": "Slinky Dog Dash",
        "theme": "thrill, immersive, sightseeing", "queue_time": "medium",
        "height_restriction": "90-250 cm",
        "description": "A family coaster set in Andy's backyard where riders launch across tracks built from his Mega Coaster Play Kit."
    },
    {
        "name": "Toy Story Mania!",
        "theme": "immersive", "queue_time": "long",
        "height_restriction": "0-250 cm",
        "description": "An interactive 4D carnival-game attraction where riders wear 3D glasses and launch virtual darts, rings, and pies at targets."
    },
    {
        "name": "Steamboat Willie's River Race",
        "theme": "relaxation, sightseeing, thrill", "queue_time": "short",
        "height_restriction": "90-250 cm",
        "description": "A family-friendly water flume ride styled in classic 1928 black-and-white animation, complete with whistling steamboats and slapstick gags."
    },
    {
        "name": "Po's Noodle Bowl Spin",
        "theme": "relaxation, immersive", "queue_time": "medium",
        "height_restriction": "81-250 cm",
        "description": "A chill teacup-style flat ride set inside Mr. Ping's noodle shop, where oversized soup bowls spin and tilt to a lively kung fu soundtrack."
    },
]


st.title("Welcome to Panda Theme Park! Please enjoy our attractions!") # 'st' stands for streamlit (st.title -> same function as a print)
# streamlit is to access specific UXs
st.image(
    "po.jpg")

init = {
    "theme_filter": [],
    "queue_slide": 120,
    "height_range": (0, 250),
    "toggle": False,
}

for key, default_val in init.items():
    if key not in st.session_state:
        st.session_state[key] = default_val

def reset_choices():
    st.session_state.theme_filter = []
    st.session_state.queue_slide = 120
    st.session_state.height_range = (0,250)
    st.session_state.toggle = False

@st.dialog("Filters")
def filter_dialog():
    st.pills(
        "Themes",
        options=all_themes, 
        selection_mode="multi",
        label_visibility="collapsed",
        key="theme_filter"
        )
    queue_slide = st.slider("Your Queue Preference (min)", min_value=0, max_value=120, value=120, key='queue_slide')
    height_range = st.slider("Your Group's Height Range (cm)", min_value=0, max_value=250, value=(0,250), key='height_range')
    toggle = st.toggle("Sort by queue time", key="toggle")
    if st.button("Apply", type="primary"):
        st.rerun()

if st.button("⚙️ Filters", key="open_filters"):
    filter_dialog()

queue_slide = st.session_state.queue_slide
height_range = st.session_state.height_range
toggle = st.session_state.toggle


def attraction_height(r):
    str = r["height_restriction"].replace("cm", "").strip()
    low, high = str.split("-")
    return (int(low), int(high))

def height_restriction(height_ran, height_res):
    x1, x2 = height_res
    y1, y2 = height_ran
    if (x1 <= y1) and (x2 >= y2):
        return True
    else:
        return False
    
def queue_cat(t):
    cat = []
    if t >= 0:
        cat.append('short')
    if t > 40:
        cat.append('medium')
    if t > 80:
        cat.append('long')
    return cat

def filter_recommendations_queue(attractions_list, theme_choice, queue_choice, top_rec):
    out = []
    for time in queue_choice:                      
        for theme in theme_choice:                
            for attraction in attractions_list:    
                if (theme in attraction["theme"]) and height_restriction(height_range, attraction_height(attraction)) and (time in attraction['queue_time']) and (attraction not in out) and ( attraction not in top_rec):
                    out.append(attraction)       
    return out

def filter_recommendations_theme(attractions_list, theme_choice, queue_choice, top_rec):
    out = []
    for theme in theme_choice:                      
        for time in queue_choice:                
            for attraction in attractions_list:    
                if (theme in attraction["theme"]) and height_restriction(height_range, attraction_height(attraction)) and (time in attraction['queue_time']) and (attraction not in out) and ( attraction not in top_rec):
                    out.append(attraction)       
    return out
    
def find_recommendations(attractions_list, theme_choice, queue_choice): #edited
    out = []
    for time in queue_choice:
        for attraction in attractions_list:
            check_theme = sorted(attraction["theme"])
            sorted_theme_choice = sorted(", ".join(theme_choice))
            if (check_theme == sorted_theme_choice) and (time in attraction['queue_time']) and height_restriction(height_range, attraction_height(attraction)):
                out.append(attraction)
    return out

options = list( st.session_state.theme_filter )  
queue_time = queue_cat(st.session_state.queue_slide)
if options == []:
    options=all_themes
    table_2 = 'Our Attractions'
    top_recs = []
else:
    st.write("Your Top Recommendations")
    top_recs = find_recommendations(ATTRACTIONS, options, queue_time)
    st.table(top_recs)
    table_2 = 'You might also like...'

st.write(table_2)
if toggle:
    second_recs = filter_recommendations_queue(ATTRACTIONS, options, queue_time, top_recs)
else:
    second_recs = filter_recommendations_theme(ATTRACTIONS, options, queue_time, top_recs)
st.table(second_recs)    

st.button("Reset Selections", on_click=reset_choices)
