badges = {}

def unlock_badge(name):
    """Unlocks a badge."""
    global badges
    if name not in badges or not badges[name]:
        badges[name] = True
        print(f"Badge '{name}' unlocked!")
    else:
        print(f"Badge '{name}' already unlocked.")

def get_badges():
    """Returns the currently unlocked badges."""
    return badges

# Example usage
unlock_badge("God Mode")
unlock_badge("Unlimited Resources")
unlock_badge("God Mode")
print("\nCurrently unlocked badges:")
print(get_badges())