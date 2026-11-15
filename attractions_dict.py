all_themes = ['User Interests', 'Queue Time']
ATTRACTIONS = [ 
    { "name"    : "Bamboo Coaster", 
      "theme": 'thrill', "queue_time": 'short',
      "description" : "Coast through the bamboo forest of China!"
    }, 
        { "name"    : "Po's Plunge", 
      "theme": 'thrill', "queue_time": 'medium',
      "description" : "Dive with the Dragon Warrior!"
    }, 
    { "name"    : "Jade Palace Rush", 
      "theme":'thrill', "queue_time": 'long',
      "description" : "Feel the rush as you explore the Palace of Jaded"
    },
      { "name"    : "Luke 'Skywalk'er", 
      "theme":'sightseeing', "queue_time": 'medium',
      "description" : "Walk the skies with luke!"
    }
    { "name"    : "Appst in island", 
      "theme":'sightseeing', "queue_time": 'long',
      "description" : "You already know..."
    }
    { "name"    : "Black n White world", 
      "theme":'immersive', "queue_time": 'short',
      "description" : "Go back in time and live in the world of B&W"
    }
    { "name"    : "Diddy doit", 
      "theme":'immersive', "queue_time": 'medium',
      "description" : "Just do it!"
    }
    { "name"    : "Dragon Warrier Adventure", 
      "theme":'immersive', "queue_time": 'long',
      "description" : "Venture into the the realm of the Warriors!"
    }
    { "name"    : "Goon Lagoon", 
      "theme":'relaxation', "queue_time": 'short',
      "description" : "Pause...?"
    }
    { "name"    : "Bamboo Forest", 
      "theme":'relaxation', "queue_time": 'medium',
      "description" : "Chill with the pandas"
    }
    { "name"    : "Shifu's Pond", 
      "theme":'relaxation', "queue_time": 'long',
      "description" : "Reach flow state with Shifu"
    }
  
]

if not in attrations:
  return 'No options available.' # display or wtv nonsense
