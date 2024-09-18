import random

# Define tables for each region
biomes = {
    "forest": {
        "humanoid": {
            2: "Bandit",
            3: "Druid",
            4: "Elf",
            5: "Goblin",
            6: "Ranger",
            7: "Scout",
            8: "Thief",
            9: "Witch",
            10: "Villager",
            11: "Wizard",
            12: "Woodcutter"
        },
        "creature": {
            2: "Bear",
            3: "Boar",
            4: "Deer",
            5: "Dire Wolf",
            6: "Giant Spider",
            7: "Owlbear",
            8: "Pixie",
            9: "Treant",
            10: "Unicorn",
            11: "Wolf",
            12: "Wyvern"
        },
        "event": {
            2: "Thunderstorm",
            3: "Forest Fire",
            4: "Flooded River",
            5: "Mysterious Fog",
            6: "Earthquake",
            7: "Big Dogs Need Petting",
            8: "Stop to tie your shoe",
            9: "Tummy Ache. Yikes!",
            10: "Sneezing fit",
            11: "Poison Oak in Delicate Places ):",
            12: "Ascend to Olympia Armwrestle Hercules"
        }
    },
    "mountains": {
        "humanoid": {
            2: "Ironsoul Monk",
            3: "Fire Newts",
            4: "Giant",
            5: "Dwarf",
            6: "Lizardfolk",
            7: "Cultist",
            8: "Lizardfolk",
            9: "Shepard",
            10: "Prospector",
            11: "Hobgoblin",
            12: "Sindri Irontooth and Brynhirn"
        },
        "creature": {
            2: "Kluth the Red",
            3: "Bulette",
            4: "Oread",
            5: "Guard Drake",
            6: "Crag Cat",
            7: "Dire Goat",
            8: "Harpy",
            9: "Wyvern",
            10: "Xorn",
            11: "Yeti",
            12: "Behir"
        },
        "event": {
            2: "Minor Eruption",
            3: "Weather Change",
            4: "Crafting Component",
            5: "Shelter",
            6: "Setback",
            7: "Rockslide",
            8: "Stop to tie your shoe",
            9: "Tummy Ache. Yikes!",
            10: "Sneezing fit",
            11: "Poison Oak in Delicate Places ):",
            12: "Ascend to Olympia Armwrestle Hercules"
        }
    },
    "plains": {
        "humanoid": {
            2: "Horse Archer",
            3: "Runaway Cultist",
            4: "Aarokocra",
            5: "Hobgoblin",
            6: "Faithful",
            7: "Gnoll",
            8: "Wind Tribe",
            9: "Bandits",
            10: "Goblins",
            11: "Wights",
            12: "Gnoll Warhost"
        },
        "creature": {
            2: "White Auroch",
            3: "Manticore",
            4: "Grick",
            5: "Ankheg",
            6: "Giant Ants",
            7: "Hyena",
            8: "Giant Eagle",
            9: "Gryphon",
            10: "Carrion Crawler",
            11: "Lightbender",
            12: "Oracle of Storms"
        },
        "event": {
            2: "Floating City Overhead",
            3: "Weather Change",
            4: "Crafting Component",
            5: "Shelter",
            6: "Twister",
            7: "Setback",
            8: "Stop to tie your shoe",
            9: "Tummy Ache. Yikes!",
            10: "Sneezing fit",
            11: "Poison Oak in Delicate Places ):",
            12: "Ascend to Olympia Armwrestle Hercules"
        }
    },
    "hills": {
        "humanoid": {
            2: "Bazerak the Helsmith",
            3: "Treasure Hunters",
            4: "Duergar",
            5: "Gnolls",
            6: "Treasure Hunters",
            7: "Gobbos",
            8: "Bandits",
            9: "Gobbos",
            10: "Silver Knight",
            11: "Bandit",
            12: "The White Prince"
        },
        "creature": {
            2: "Cadaver Collector",
            3: "Iron Golem",
            4: "Multivok Bodyguard",
            5: "Animated Armor",
            6: "Rust Monster",
            7: "Wolf",
            8: "Bronze Scout",
            9: "Owlbear",
            10: "Troll",
            11: "Peryton",
            12: "Steel Predator"
        },
        "event": {
            2: "Earthquake",
            3: "Weather Change",
            4: "Crafting Component",
            5: "Shelter",
            6: "Setback",
            7: "Rockslide",
            8: "Stop to tie your shoe",
            9: "Tummy Ache. Yikes!",
            10: "Sneezing fit",
            11: "Poison Oak in Delicate Places ):",
            12: "Ascend to Olympia Armwrestle Hercules"
        }
    },
    # Define other regions similarly
    # "swamp": {...},
    # "badlands": {...},
}

def roll_dice(sides=6):
    """Rolls a dice with the given number of sides (default 6)."""
    dice_roll = random.randint(1, sides)
    return dice_roll

def generate_weighted_roll():
    """Generates a weighted roll by summing two d6 rolls."""
    return roll_dice() + roll_dice()

def get_random_encounter(region, table):
    """Gets a random encounter from the specified table in the given region."""
    encounter_table = biomes[region][table]
    roll_result = generate_weighted_roll()
    return encounter_table[roll_result]

def get_creature_properties():
    """Generates the number of creatures and their disposition."""
    number = roll_dice()
    dispositions = {
        1: "Moving",
        2: "Stationary",
        3: "Hunting",
        4: "Injured",
        5: "Dead",
        6: "Tracks"
    }
    disposition = dispositions[number]
    return number, disposition

def get_event_type():
    """Generates a random event type."""
    event_types = {
        1: "Natural",
        2: "Supernatural",
        3: "Environmental",
        4: "Man-made",
        5: "Mystical",
        6: "Mundane"
    }
    return event_types[roll_dice()]

def format_time(hour):
    #creates a 12-hour clock output to go with generated encounters
    period = "AM" if hour < 12 else "PM"
    hour = hour % 12
    hour = 12 if hour == 0 else hour
    return f"{hour}:00 {period}"

start_hour = 6

def generate_encounter(debug=False):
    """Main function to generate a random encounter."""
    region = input("Enter a region (forest, plains, hills, mountains): ").strip().lower()
    try:
        watches = int(input("How many watches would you like to check encounters for?: "))
    except ValueError:
        print("Please enter a valid number for watches.")
        return
    
    if watches < 0:
        print(f"{watches} is a negative value. Please enter a valid positive value for number of watches.")

    elif region not in biomes:
        print(f"Region '{region}' not recognized. Please try again.")
        return  
    for i in range(watches):
        #Roll a d4 and generate an encounter on a 1 result
        dice_roll = roll_dice(4)
        if debug:
            print(f"Dice roll result for watch {i+1}: {dice_roll}")
        if dice_roll == 1:
            # Determine the type of encounter (1: Humanoid, 2: Creature, 3: Event)
            encounter_type_roll = roll_dice(3)
            if encounter_type_roll == 1:
                encounter_type = "humanoid"
            elif encounter_type_roll == 2:
                encounter_type = "creature"
            elif encounter_type_roll == 3:
                encounter_type = "event"
            else:
                print(f"Not a valid encounter type.")

            encounter = get_random_encounter(region, encounter_type)

            # Determine properties based on encounter type
            if encounter_type in ["humanoid", "creature"]:
                number, disposition = get_creature_properties()
                print(f"Encounter: {number} {encounter}(s), Disposition: {disposition} ")
            else:
                event_type = get_event_type()
                print(f"Encounter: {encounter}, Type: {event_type}")       
        else:
            print("No encounter this watch.")
        e = round(1 + i/6)
        #print the time of day
        current_time = (start_hour + i * 4) % 24
        print(f"Watch {i+1} Time: {format_time(current_time)}, Day {e}") 
        print()

if __name__ == "__main__":
    while True:
        generate_encounter(debug=True)
        print()  # Just for spacing between encounters
