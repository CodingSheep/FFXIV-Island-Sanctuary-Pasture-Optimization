rares = ['Alligator', 'Apkallu of Paradise', 'Beachcomb', 'Black Chocobo', 'Dodo of Paradise',
         'Glyptodon', 'Goobue', 'Gold Back', 'Grand Buffalo', 'Island Billy', 'Island Stag',
         'Lemur', 'Ornery Karakul', 'Paissa', 'Star Marmot', 'Twinklefleece', 'Yellow Coblyn',
         'Griffin', 'Tiger', 'Morbol', 'Amethyst Spriggan', 'Rare Boar', 'Weird Spriggan',
         'Funguar', 'Alkonost', 'Adamantoise', 'Pteranodon', 'Morbol', 'Grand Doblyn']

replace = {
    # Carapace/Claw
    'Beachcomb': 'Beachcomb/Glyptodon Pup/Adamantoise',
    'Glyptodon Pup': 'Beachcomb/Glyptodon Pup/Adamantoise',
    'Adamantoise': 'Beachcomb/Glyptodon Pup/Adamantoise',
    
    # Fur/Claw
    'Lemur' : 'Lemur/Star Marmot',
    'Star Marmot': 'Lemur/Star Marmot',
    
    # Claw/Fur
    'Ground Squirrel': 'Ground Squirrel/Opo-Opo',
    'Opo-Opo': 'Ground Squirrel/Opo-Opo',
    
    # Milk/Horn
    'Aurochs': 'Aurochs/Island Nanny',
    'Island Nanny': 'Aurochs/Island Nanny',
    
    # Feather/Egg
    'Dodo of Paradise': 'Dodo of Paradise/Gold Back/Alkonost',
    'Gold Back': 'Dodo of Paradise/Gold Back/Alkonost',
    'Alkonost': 'Dodo of Paradise/Gold Back/Alkonost',
    
    # Egg/Feather
    'Blue Back': 'Blue Back/Dodo',
    'Dodo': 'Blue Back/Dodo',
    
    # Carapace/Fang
    'Yellow Coblyn': 'Yellow Coblyn/Morbol Seedling',
    'Morbol Seedling': 'Yellow Coblyn/Morbol Seedling',
    
    # Fang/Carapace
    'Coblyn': 'Coblyn/Morbol/Grand Doblyn',
    'Morbol': 'Coblyn/Morbol/Grand Doblyn',
    'Grand Doblyn': 'Coblyn/Morbol/Grand Doblyn',
    
    # Fang/Fur
    'Tiger': 'Tiger/Quartz Spriggan/Weird Spriggan',
    'Quartz Spriggan': 'Tiger/Quartz Spriggan/Weird Spriggan',
    'Weird Spriggan': 'Tiger/Quartz Spriggan/Weird Spriggan',
    
    # Fleece/Fur
    'Twinklefleece': 'Twinklefleece/Funguar',
    'Funguar': 'Twinklefleece/Funguar'
}