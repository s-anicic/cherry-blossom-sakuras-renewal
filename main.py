# Game title: Cherry Blossom: Sakura’s Renewal

import time

# Functions

# slow_print prints the line slowly (0.05s / 5 milliseconds delay)
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

# emoji_loading_line prints one string of emoji at a time (0.3s / 300 milliseconds delay)
def emoji_loading_line(line, delay=0.3):
    for emoji in line:
        print(emoji, end='', flush=True)
        time.sleep(delay)
    print("\n")

# Introduction scene 
def intro_scene():
    slow_print("You find yourself in a serene Japanese garden, surrounded by soft pink cherry blossoms. 🌸")
    emoji_loading_line("🍃🍃🍃")
    slow_print("The petals float gently in the breeze, and the air smells faintly of sweet tea and earth.")
    slow_print("You walk slowly until you find a large cherry blossom tree and decide to sit beneath it.")
    slow_print("As you relax, the world around you begins to shimmer and change...")
    emoji_loading_line("✨✨✨")
    emoji_loading_line("🌸🌸🌸")
    slow_print("The pink blossoms intensify, the air glows softly, and the garden transforms into a whimsical, cosy realm.")
    slow_print("Before you, a quaint coffee shop appears. But it's run-down and in need of care.")
    slow_print("Your adventure begins here. Your goal: restore the coffee shop.")
    input("Press Enter to continue...")

# Main
def main():
    intro_scene()