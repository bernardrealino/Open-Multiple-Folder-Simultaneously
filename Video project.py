import os
import subprocess

# Function to get screen resolution
def get_screen_resolution():
    # Use system_profiler to get screen information
    result = subprocess.run(
        ["system_profiler", "SPDisplaysDataType"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    # Parse the output to find the resolution
    for line in result.splitlines():
        if "Resolution:" in line:
            # Extract width and height from the line
            parts = line.split()
            width = int(parts[1])
            height = int(parts[3])
            return width, height

# Get the screen width and height automatically
SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()

# Paths to open
paths = [
    '/Users/bernard/Documents/My Projects/Video Production Project/PROJECTS',
    '/Volumes/Bernard SSD 256/My Projects/Video Production/PROJECTS',
    '/Volumes/Project Files/Video Production/PROJECTS'
]

# Define window positions (x, y, width, height) for each window based on screen size
screen_positions = [
    {'x': 0, 'y': 50, 'width': SCREEN_WIDTH / 4, 'height': SCREEN_HEIGHT},    # First window: 1/4 of the screen
    {'x': SCREEN_WIDTH / 4, 'y': 50, 'width': SCREEN_WIDTH / 2, 'height': SCREEN_HEIGHT},  # Second window: 2/4 (half) of the screen
    {'x': SCREEN_WIDTH * 3 / 4, 'y': 50, 'width': SCREEN_WIDTH / 4, 'height': SCREEN_HEIGHT}  # Third window: 1/4 of the screen
]

# Loop over each path and its corresponding position
for i, path in enumerate(paths):
    # Open the path
    os.system(f'open "{path}"')

    # Get the position for the current path
    pos = screen_positions[i]

    # Use AppleScript to move the window to the corresponding side
    applescript = f'''
    tell application "Finder"
        set theWindow to window 1
        set bounds of theWindow to {{{pos['x']}, {pos['y']}, {pos['x'] + pos['width']}, {pos['y'] + pos['height']}}}
    end tell
    '''

    # Run the AppleScript to move the Finder window
    subprocess.run(['osascript', '-e', applescript])
