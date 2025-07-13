def unlock_badge(name):
#     """Unlocks a badge."""
#     global badges
#     if name not in badges or not badges[name]:
#         badges[name] = True
#         print(f"Badge '{name}' unlocked!")
#     else:
#         print(f"Badge '{name}' already unlocked.")
# def get_badges():
#     """Returns the currently unlocked badges."""
#     return badges
# # Example usage
# unlock_badge("God Mode")
# unlock_badge("Unlimited Resources")
# unlock_badge("God Mode")
# print("\nCurrently unlocked badges:")
# print(get_badges())

import json
import os
from datetime import datetime

# Define a file path for persistent storage
BADGE_FILE = "badges.json"

# Define badge metadata (description, potential tiers)
BADGE_METADATA = {
    "God Mode": {"description": "Become invincible.", "tier": 3},
    "Unlimited Resources": {"description": "Never run out of anything.", "tier": 3},
    "First Step": {"description": "Complete your first task.", "tier": 1},
    "Master Collector": {"description": "Unlock all tier 1 badges.", "tier": 2}
}

def load_badges():
    """Loads badges from the persistent storage file."""
    if os.path.exists(BADGE_FILE):
        with open(BADGE_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # Handle empty or corrupted file
                return {}
    else:
        return {}

def save_badges(badges_data):
    """Saves current badges to the persistent storage file."""
    with open(BADGE_FILE, 'w') as f:
        json.dump(badges_data, f, indent=2)

# Load existing badges when the notebook starts
badges = load_badges()

def unlock_badge(name):
    """
    Unlocks a badge, records timestamp, and saves to persistent storage.
    Checks for meta-badges (e.g., 'Master Collector').
    """
    global badges
    now = datetime.now().isoformat() # Use ISO format for easy comparison and storage

    if name not in badges:
        badges[name] = {
            "unlocked": True,
            "timestamp": now,
            "metadata": BADGE_METADATA.get(name, {"description": "No description available", "tier": 0})
        }
        print(f"Badge '{name}' unlocked at {now}!")
        save_badges(badges) # Save after unlocking

        # Check for meta-badges after unlocking
        check_meta_badges()

    elif not badges[name]["unlocked"]:
        # This case is less likely with the current structure, but good for robustness
        badges[name]["unlocked"] = True
        badges[name]["timestamp"] = now
        print(f"Badge '{name}' unlocked at {now}!")
        save_badges(badges)
        check_meta_badges()

    else:
        print(f"Badge '{name}' already unlocked on {badges[name]['timestamp']}.")

def get_badges(unlocked_only=True):
    """
    Returns the currently unlocked badges, optionally with full details.
    """
    if unlocked_only:
        return {name: data for name, data in badges.items() if data["unlocked"]}
    else:
        return badges

def check_meta_badges():
    """
    Checks for conditions to unlock meta-badges based on currently unlocked badges.
    This is a simple example; more complex dependencies would require a graph or similar structure.
    """
    unlocked = get_badges(unlocked_only=True)

    # Example meta-badge: Master Collector (unlock all Tier 1 badges)
    tier1_badges = {name for name, meta in BADGE_METADATA.items() if meta.get("tier") == 1}
    unlocked_tier1 = {name for name in unlocked if unlocked[name]["metadata"].get("tier") == 1}

    if tier1_badges and unlocked_tier1 == tier1_badges and "Master Collector" not in unlocked:
         unlock_badge("Master Collector")


# --- Enhanced Example Usage ---

# Simulate some actions that could unlock badges
unlock_badge("First Step")
unlock_badge("God Mode")
unlock_badge("Unlimited Resources")

# Try unlocking an existing badge again
unlock_badge("God Mode")

# Simulate unlocking another Tier 1 badge (assuming "Another Tier 1 Badge" is defined in METADATA)
# If you define "Another Tier 1 Badge" and call this, it will unlock Master Collector
# For demonstration, let's manually add a placeholder badge and trigger the check
# BADGE_METADATA["Another Tier 1 Badge"] = {"description": "Another simple step.", "tier": 1}
# unlock_badge("Another Tier 1 Badge")


print("\nCurrently unlocked badges (summary):")
print(get_badges(unlocked_only=True))

print("\nAll badge data:")
print(json.dumps(get_badges(unlocked_only=False), indent=2))

