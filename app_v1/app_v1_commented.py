import streamlit as st
 
all_themes = ['immersive', 'thrill', 'sightseeing', 'relaxation']

ATTRACTIONS = [
     {
        "name": "Emperror's Quest",
        "theme": "immersive", "queue_time": "short",
        "height_restriction": "0-250 cm",
        "description": "Join Po on a trek through rapids, river pirates, magic and kung fu."
    }, 
    {
        "name": "Land of Awesomeness",
        "theme": "sightseeing", "queue_time": "short",
        "height_restriction": "0-250 cm",
        "description": "The Journey of the Dragon Warrior is a flume ride where guests fight Tian Sha."
    },
    {
        "name": "Alien Swirling Saucer",
        "theme": "relaxation", "queue_time": "short",
        "height_restriction": "0-250 cm",
        "description": "A carnival spinner ride!"
    },
    {
        "name": "Toy's Mania",
        "theme": "relaxation", "queue_time": "short",
        "height_restriction": "0-250 cm",
        "description": "A carnival spinner ride!"
    },
    {
        "name": "Mickey & Minnie's Runaway Railway",
        "theme": "immersive, sightseeing", "queue_time": "short",
        "height_restriction": "0-250 cm",
        "description": "A trackless dark ride that takes guests straight into a chaotic, colorful Mickey Mouse cartoon short."
    },
    {
        "name": "Mickey's Toontown",
        "theme": "sightseeing, relaxation", "queue_time": "short",
        "height_restriction": "0-250 cm",
        "description": "Stroll around Mickey's hometown."
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
    {
        "name": "Minnie's Moonlight Swing",
        "theme": "thrill, relaxation", "queue_time": "short",
        "height_restriction": "90-250 cm",
        "description": "A suspended swing ride that soars high above Toontown, then drifts gently back down under a canopy of twinkling stars."
    },
    {
        "name": "Woody's Roundup Rapids",
        "theme": "thrill, immersive, relaxation", "queue_time": "medium",
        "height_restriction": "102-250 cm",
        "description": "A lazy river winding through Andy's toy-filled bedroom that suddenly turns into splashy rapids when Woody and the gang round up the runaway toys."
    },
    {
        "name": "Dragon Warrior's Grand Adventure",
        "theme": "thrill, immersive, sightseeing, relaxation", "queue_time": "long",
        "height_restriction": "102-250 cm",
        "description": "A grand finale ride where Po, Woody and Mickey team up, gliding past Valley of Peace and Toontown sights before a thrilling final plunge and a calm cruise home."
    }
]
 
st.title("Welcome to Panda Theme Park! Please enjoy our attractions!")
st.image("po.jpg")
 
# Dictionary of the default value for each setting stored in session state
DEFAULTS = {
    "theme_filter": [],
    "queue_slide": 120,
    "height_enable": False,
    "height_range": (0, 250),
    "toggle": False,
}

# Loop over every setting name in DEFAULTS
for key in DEFAULTS:
    # Only if this setting hasn't been saved in session state yet (e.g. on the first page load)...
    if key not in st.session_state:
        # ...store its default value so it persists across reruns
        st.session_state[key] = DEFAULTS[key]
 
# Define a function that resets all filters back to their defaults (used by the "Clear Selections" button)
def init_dialogue():      
    # Reset all saved to empty
    # Reset the saved theme selection to empty
    st.session_state.theme_filter = []
    st.session_state.queue_slide = 120
    st.session_state.height_range = (0,250)
    st.session_state.toggle = False

    # Reset all current to empty
    st.session_state.d_height = (0, 250)
    st.session_state.d_theme = [] 
    st.session_state.d_queue = 120
    st.session_state.d_h_enable = False
    st.session_state.d_tog = False
 
# Decorator: turns the function below into a pop-up dialog titled "Filters" that can't be dismissed by clicking outside it
@st.dialog("Filters", dismissible=False)

# Define the function that builds the contents of the filter pop-up
def filter_dialog():
    # Show multi-select pill buttons for themes and save the chosen themes to session state
    st.session_state.theme_filter = st.pills(
        # The label of the pills widget (hidden below)
        "Themes",
        options=all_themes, 
        # Allow selecting more than one pill at once
        selection_mode="multi",
        # Pre-select whatever themes were previously chosen
        default=st.session_state.theme_filter,
        # Hide the label text so only the pills are visible
        label_visibility="collapsed",
        # Unique key called 'd_theme' that identifies this widget in session state
        key='d_theme')
 
    # Show a slider for queue preference, which starts at the saved value, and saves the result to session state
    st.session_state.queue_slide = st.slider("Your Queue Preference (min)", min_value=0, max_value=120, value=st.session_state.queue_slide, key='d_queue')
 
    # Show a toggle switch to enable the height filter and save its on/off state to session state; outputs as a boolean (T/F)
    st.session_state.height_enable = st.toggle("Enable Height Restriction", value=st.session_state.height_enable, key='d_h_enable')
 
    # Only if the height toggle is on
    if st.session_state.height_enable == True:
        # Show a range slider (0-250 cm) for the group's heights and save the chosen range to session state
        st.session_state.height_range = st.slider("Your Group's Height Range (cm)", min_value=0, max_value=250, value=st.session_state.height_range, key='d_height')
    else:
       pass
     
    # Show a toggle for sorting results by queue time and save its on/off state to session state; outputs as boolean (T/F)
    st.session_state.toggle = st.toggle("Sort by queue time", value=st.session_state.toggle, key='d_tog')
      
    # Create two side-by-side columns for the two buttons
    c1, c2 = st.columns(2)
    with c1:
        # Add a "Clear Selections" button that resets all filters when clicked
        clear_button = st.button("Clear Selections", type="primary", width="stretch", on_click=init_dialogue)    

    with c2:
        # Add a full-width primary "Save & Close" button
        close_button = st.button("Save & Close", type="primary", width="stretch")
     
    # If  "Save & Close" button was clicked
    if close_button:
        # re-run the app and apply the saved filters
        st.rerun()
      
# Show a "⚙️ Filters" button on the page; if it is clicked
if st.button("⚙️ Filters", key="open_filters"):
    # open the filter pop-up dialog as seen in line 155
    filter_dialog()
 
# Define a function that filters by height requirement
def check_height(attraction):
    # If the height restriction filter is toggled on
    if st.session_state.height_enable == True:
        # check if height range fits the attraction's allowed range; outputs boolean
        # 'attraction_height' is later defined in line 220
        # 'height_restriction() is defined later on in line 231
        check_height = height_restriction(st.session_state.height_range, attraction_height(attraction))
    else:
        # every attraction passes, so the result is True
        check_height = True
    # do this rather than just return True' because check_height will be used in steps further down, so helps with labelling
    return check_height
 
# Define a function that converts an attraction's height text (e.g. "102-250 cm") into a (low, high) pair of numbers - as a text
def attraction_height(r):
    # Take the height text, removes "cm", and trim spaces
    # Consider changing the variable named "str" as it shadows Python's built-in str function (?)
    str = r["height_restriction"].replace("cm", "").strip()
    low, high = str.split("-")
    # Return both values converted to whole numbers, now as a tuple
    return (int(low), int(high))
 
# Define a function that checks whether the group's height range fits inside the attraction's allowed range
# height_res is height restriction & height_ran is height range
def height_restriction(height_ran, height_res):
    # Unpack the ATTRACTION'S ALLOWED RANGE into its minimum (x1) and maximum (x2)
    x1, x2 = height_res
    # Unpack the USER'S CHOSEN RANGE into its minimum (y1) and maximum (y2)
    y1, y2 = height_ran
    if (x1 <= y1) and (x2 >= y2):
        return True
    else:
        return False
    
# Define a function that turns a queue time in minutes into a list of acceptable queue categories
def queue_cat(t):
    # initialise (define) cat as an empty list
    cat = []
    if t >= 0:
        cat.append('short')
    if t > 40:
        cat.append('medium')
    if t > 80:
        cat.append('long')
    return cat
 
# Define a function that finds extra recommendations, ordered with QUEUE TIME as the outermost loop
# Used when sorting by queue time
def filter_recommendations_queue(attractions_list, theme_choice, queue_choice, top_rec):
    # Initialise out as an empty list
    out = []
    # Loop over each acceptable queue category
    # Outermost loop, so results are grouped by QUEUE TIME
    # time is set as the for loop index
    for time in queue_choice:                      
        # theme is set as the for loop index
        for theme in theme_choice:                
            # attraction is set as the for loop index
            for attraction in attractions_list:    
                # If:
                # - theme matches,
                # - height passes,
                # - queue category matches, and
                # - attraction isn't already in the results/top_recs
                if (theme in attraction["theme"]) and check_height(attraction) and (time in attraction['queue_time']) and (attraction not in out) and (attraction not in top_rec):
                    # Add the attraction to the results
                    out.append(attraction)       
    return out
 
# Define a function that finds extra recommendations, ordered with THEME as the outermost loop
# Used when NOT sorting by queue time
def filter_recommendations_theme(attractions_list, theme_choice, queue_choice, top_rec):
    # Initialise out as an empty list (again)
    out = []
    # Loop over each chosen theme
    # Outermost loop, so results are grouped by THEME
    for theme in theme_choice:                      
        # time set as the for loop index
        for time in queue_choice:                
            # attraction set as the for loop index
            for attraction in attractions_list:    
                # If:
                # - theme matches,
                # - height passes,
                # - queue category matches, and
                # - attraction isn't already in the results/top_recs
                if (theme in attraction["theme"]) and check_height(attraction) and (time in attraction['queue_time']) and (attraction not in out) and (attraction not in top_rec):
                    # ...add the attraction to the results
                    out.append(attraction)       
    return out
    
# Define a function that finds the top recommendations
# Attractions matching the chosen themes EXACTLY
def find_recommendations(attractions_list, theme_choice, queue_choice): #edited
    out = []
    # time as the for loop index
    for time in queue_choice:
        # attraction as the for loop index
        for attraction in attractions_list:
            # Sort the characters of the attraction's theme string
            # 'sorted()' on a string returns a sorted list of its INDIVIDUAL CHARACTERS
            check_theme = sorted(attraction["theme"])
            # Join the chosen themes into one comma-separated string; i.e (x1, x2, x3, ...)
            # Then sort its INDIVIDUAL CHARACTERS
            sorted_theme_choice = sorted(", ".join(theme_choice))
            # If:
            # - the two sorted character lists are identical,
            # - queue category matches, and
            # - the height passes
            # vvv i.e 'if True and True and True:'
            if (sorted_theme_choice == check_theme) and (time in attraction['queue_time']) and check_height(attraction):
                # Add the attraction to the results
                out.append(attraction)
    return out
 
# Make a list copy of all the themes the user selected in the filter dialog which we obtain previously
options = list( st.session_state.theme_filter )  

# Convert the queue slider value into the list of acceptable queue categories using the pre-defined function 'queue_cat()'
queue_time = queue_cat(st.session_state.queue_slide)

# If the user has not selected any themes
if options == []:
    # Treat it as "all themes" selected
    options=all_themes
    # Set the heading for the list below to "Our Attractions"
    table_2 = 'Our Attractions'
    # Set top_recs as empty if options chosen is none
    top_recs = []
else:
    # Find the top recommendations that match the selected themes, queue categories and height
    top_recs = find_recommendations(ATTRACTIONS, options, queue_time)
    # If any top recommendations were found
    if top_recs:
        st.write("Your Top Recommendations")
        # attraction becomes the for loop index
        for attraction in top_recs:
            # Create a nice visual panel/box/card for this attraction
            with st.container(border=True):
                # Show the attraction's name as a SUBheading
                st.subheader(attraction["name"])
                # Show the attraction's description
                st.write(attraction["description"])
            
                # Create three side-by-side columns for the details
                col1, col2, col3 = st.columns(3)
                # In column 1
                with col1:
                    # Show the theme(s) as small caption text
                    st.caption(f"🎯 **Theme:** {attraction['theme']}")
                # In column 2
                with col2:
                    # Show the queue category as small caption text
                    st.caption(f"⏱️ **Queue:** {attraction['queue_time']}")
                # In column 3
                with col3:
                    # Show the height restriction as small caption text
                    st.caption(f"📏 **Height:** {attraction['height_restriction']}")
    
    # Set the heading for the list below to "You might also like..."
    # NOTE that this is still WITHIN the else statement block
    table_2 = 'You might also like...'
 
# Display the heading text chosen above ("Our Attractions" or "You might also like...")
st.write(table_2)
# If the "Sort by queue time" toggle is on
if st.session_state.toggle:
    # Build the second list sorted/grouped by QUEUE TIME
    second_recs = filter_recommendations_queue(ATTRACTIONS, options, queue_time, top_recs)
else:
    # Build the second list sorted/grouped by THEME
    second_recs = filter_recommendations_theme(ATTRACTIONS, options, queue_time, top_recs)

# attration is the for loop index in the second table
for attraction in second_recs:
    # Create a bordered box/card for this attraction
    with st.container(border=True):
        # Show the attraction's name as a SUBheading
        st.subheader(attraction["name"])
        # Show the attraction's description
        st.write(attraction["description"])
        
        # Create three side-by-side columns for the details
        col1, col2, col3 = st.columns(3)
        # In column 1
        with col1:
            # Show the theme(s) as small caption text
            st.caption(f"🎯 **Theme:** {attraction['theme']}")
        # In column 2
        with col2:
            # Show the queue category as small caption text
            st.caption(f"⏱️ **Queue:** {attraction['queue_time']}")
        # In column 3
        with col3:
            # Show the height restriction as small caption text
            st.caption(f"📏 **Height:** {attraction['height_restriction']}")
