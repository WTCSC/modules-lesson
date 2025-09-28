#!/usr/bin/env python3
"""
Built-in Modules Demo: Because Who Has Time to Reinvent the Wheel?

This script demonstrates various built-in Python modules through
scenarios that might actually matter to a high school student.
No boring calculator examples here - we're talking real life stuff!

Author: Your Friendly Neighborhood Code Teacher
Target Audience: Students who think they're too cool for school (but still need to pass)
"""

import random
import datetime
import os
import sys
import math
import json
from pathlib import Path


def random_module_demo():
    """
    Random Module: For when you can't make decisions
    (Which, let's be honest, is most of high school)
    """
    print("🎲 RANDOM MODULE: Life's Ultimate Decision Maker 🎲")
    print("=" * 50)
    
    # Choosing what to eat for lunch (the eternal struggle)
    lunch_options = [
        "Pizza (again...)", 
        "Cafeteria Mystery Meat", 
        "That sad sandwich from home",
        "Just skip lunch and eat regret",
        "Vending machine cuisine"
    ]
    
    print("🍕 What should I eat for lunch?")
    print(f"   The universe has decided: {random.choice(lunch_options)}")
    
    # Group project partner selection (may the odds be ever in your favor)
    classmates = ["Alex (does all the work)", "Jordan (disappears mysteriously)", 
                 "Sam (shows up 5 minutes before deadline)", "Casey (actually competent)"]
    
    print("\n👥 Group project partner assignment:")
    partners = random.sample(classmates, 2)  # Pick 2 partners
    print(f"   You're stuck with: {', '.join(partners)}")
    print("   (Good luck with that!)")
    
    # Random excuse generator for late homework
    excuses = [
        "My dog ate my laptop",
        "I was abducted by aliens (they needed help with calculus)",
        "Netflix held me hostage",
        "I forgot I had hands",
        "The assignment was due TODAY?!"
    ]
    
    print(f"\n📝 Random excuse for late homework:")
    print(f"   '{random.choice(excuses)}'")
    
    # Random grade prediction (because anxiety is fun!)
    print(f"\n📊 Your random test score prediction: {random.randint(65, 98)}%")
    print("   (Disclaimer: This is not actually predictive. Study, you magnificent disaster.)")
    
    print("\n" + "=" * 50 + "\n")


def datetime_module_demo():
    """
    Datetime Module: Time is an illusion, but deadlines are not
    """
    print("⏰ DATETIME MODULE: Master of Time and Procrastination ⏰")
    print("=" * 55)
    
    now = datetime.datetime.now()
    print(f"🕐 Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("   (Time keeps moving whether you're ready or not)")
    
    # Calculate how much time until graduation
    graduation_date = datetime.date(2025, 6, 15)  # Adjust as needed
    today = datetime.date.today()
    days_until_graduation = (graduation_date - today).days
    
    print(f"\n🎓 Days until graduation: {days_until_graduation}")
    if days_until_graduation > 100:
        print("   (That's like... forever. You have time to procrastinate more!)")
    elif days_until_graduation > 30:
        print("   (Getting close! Maybe start thinking about the future?)")
    else:
        print("   (PANIC MODE ACTIVATED! 🚨)")
    
    # Weekend countdown (the most important calculation)
    days_until_weekend = (4 - today.weekday()) % 7  # Friday is day 4
    if days_until_weekend == 0:
        print(f"\n🎉 IT'S FRIDAY! Weekend vibes activated!")
    else:
        print(f"\n📅 Days until weekend: {days_until_weekend}")
        print("   (Counting down like it's New Year's Eve)")
    
    # Check if it's a reasonable time to be awake
    if now.hour < 6:
        print(f"\n🌙 It's {now.hour}:00 AM - Go to sleep, you night owl!")
    elif now.hour > 23:
        print(f"\n🌙 It's {now.hour}:00 - Your future self will thank you for sleeping now")
    else:
        print(f"\n☀️ It's {now.hour}:00 - Socially acceptable time to be conscious")
    
    print("\n" + "=" * 55 + "\n")


def os_module_demo():
    """
    OS Module: Interact with your computer like a hacker (but legally)
    """
    print("💻 OS MODULE: Your Computer's Personal Assistant 💻")
    print("=" * 48)
    
    # Current working directory (where am I in this digital wasteland?)
    print(f"📁 Current directory: {os.getcwd()}")
    print("   (This is where you are in the file system maze)")
    
    # Environment variables (your computer's secret diary)
    user = os.environ.get('USER', 'Mystery Person')
    home = os.environ.get('HOME', 'Nowhere')
    print(f"\n👤 Computer thinks you are: {user}")
    print(f"🏠 Your home directory: {home}")
    
    # List files in current directory
    files = os.listdir('.')
    print(f"\n📋 Files in current directory ({len(files)} items):")
    for file in files[:5]:  # Show only first 5 to avoid spam
        print(f"   📄 {file}")
    if len(files) > 5:
        print(f"   ... and {len(files) - 5} more files")
    
    # Check if important directories exist
    important_dirs = ['Downloads', 'Documents', 'Desktop']
    print(f"\n🔍 Checking for important directories in {home}:")
    for dir_name in important_dirs:
        dir_path = os.path.join(home, dir_name)
        if os.path.exists(dir_path):
            print(f"   ✅ {dir_name} exists (as it should)")
        else:
            print(f"   ❌ {dir_name} missing (your computer is weird)")
    
    print("\n" + "=" * 48 + "\n")


def sys_module_demo():
    """
    Sys Module: The existential crisis module
    """
    print("🐍 SYS MODULE: Python's Identity Crisis Helper 🐍")
    print("=" * 47)
    
    print(f"🐍 Python version: {sys.version}")
    print("   (If it's not 3.x, we need to have a serious talk)")
    
    print(f"\n💾 Platform: {sys.platform}")
    print("   (Your computer's personality)")
    
    print(f"\n📊 Python path (where Python looks for modules):")
    for i, path in enumerate(sys.path[:3]):  # Show first 3 paths
        print(f"   {i+1}. {path}")
    print(f"   ... and {len(sys.path) - 3} more locations")
    
    # Command line arguments (what did you tell this program?)
    print(f"\n💬 Command line arguments: {sys.argv}")
    if len(sys.argv) == 1:
        print("   (You ran this script without any arguments - basic level activated)")
    else:
        print("   (Look at you, passing arguments like a pro!)")
    
    print("\n" + "=" * 47 + "\n")


def math_module_demo():
    """
    Math Module: For when your calculator is just not dramatic enough
    """
    print("🧮 MATH MODULE: Making Numbers Less Boring 🧮")
    print("=" * 44)
    
    # Pizza sharing calculations (the most important math)
    pizza_slices = 8
    friends = 3
    slices_per_person = math.floor(pizza_slices / friends)
    leftover_slices = pizza_slices % friends
    
    print(f"🍕 Pizza Math Crisis:")
    print(f"   {pizza_slices} slices ÷ {friends} friends = {slices_per_person} slices each")
    print(f"   Leftover slices: {leftover_slices}")
    if leftover_slices > 0:
        print("   (Fight to the death for the remaining slices!)")
    else:
        print("   (Perfect distribution - world peace achieved!)")
    
    # GPA calculations (the eternal source of stress)
    grades = [87, 92, 78, 95, 88]
    average = sum(grades) / len(grades)
    print(f"\n📊 GPA Calculations:")
    print(f"   Grades: {grades}")
    print(f"   Average: {average:.2f}")
    print(f"   Square root of average: {math.sqrt(average):.2f}")
    print("   (Don't ask why we need the square root - it's advanced math)")
    
    # Trigonometry (because apparently it matters in real life?)
    angle = 45  # degrees
    angle_rad = math.radians(angle)
    print(f"\n📐 Trig Functions for {angle}°:")
    print(f"   sin({angle}°) = {math.sin(angle_rad):.3f}")
    print(f"   cos({angle}°) = {math.cos(angle_rad):.3f}")
    print(f"   tan({angle}°) = {math.tan(angle_rad):.3f}")
    print("   (Your geometry teacher is somewhere smiling)")
    
    # Power calculations
    phone_battery = 15  # percent
    hours_to_charge = math.log(100/phone_battery) / math.log(2)  # Rough estimate
    print(f"\n🔋 Phone Battery Math:")
    print(f"   Current battery: {phone_battery}%")
    print(f"   Estimated hours to full charge: {hours_to_charge:.1f}")
    print("   (This is completely made up math, but sounds scientific!)")
    
    print("\n" + "=" * 44 + "\n")


def json_module_demo():
    """
    JSON Module: For storing data like a civilized human being
    """
    print("📄 JSON MODULE: Data Storage for the Modern Age 📄")
    print("=" * 50)
    
    # Student profile data
    student_profile = {
        "name": "Alex Procrastinator",
        "grade": 11,
        "favorite_subjects": ["Computer Science", "Lunch", "Study Hall"],
        "least_favorite_subjects": ["Early Morning Math", "PE After Lunch"],
        "hobbies": ["Gaming", "Netflix", "Avoiding Homework", "Snacking"],
        "life_goals": ["Graduate", "Get into college", "Become internet famous"],
        "current_mood": "Slightly panicked but optimistic",
        "coffee_dependency_level": "Dangerous",
        "study_efficiency": {
            "morning": "Terrible",
            "afternoon": "Questionable", 
            "evening": "Decent",
            "night": "Surprisingly good",
            "3am": "Transcendent"
        }
    }
    
    # Convert to JSON string
    json_string = json.dumps(student_profile, indent=2)
    print("📝 Student Profile as JSON:")
    print(json_string)
    
    # Parse JSON back to Python object
    parsed_data = json.loads(json_string)
    print(f"\n🔍 Parsing JSON back to Python:")
    print(f"   Student name: {parsed_data['name']}")
    print(f"   Favorite subjects: {', '.join(parsed_data['favorite_subjects'])}")
    print(f"   Current mood: {parsed_data['current_mood']}")
    print(f"   3 AM study efficiency: {parsed_data['study_efficiency']['3am']}")
    
    # Save to file (so we can pretend to be organized)
    filename = "/tmp/student_profile.json"
    with open(filename, 'w') as file:
        json.dump(student_profile, file, indent=2)
    
    print(f"\n💾 Data saved to: {filename}")
    print("   (Look at you, being all organized and stuff!)")
    
    print("\n" + "=" * 50 + "\n")


def main():
    """
    Main function: Where the magic happens (and by magic, we mean organized chaos)
    """
    print("🎉 WELCOME TO PYTHON BUILT-IN MODULES BOOTCAMP! 🎉")
    print("Where we learn to use the tools Python gives us for free")
    print("(Because free stuff is the best stuff)")
    print("\n" + "=" * 60 + "\n")
    
    # Run all demonstrations
    random_module_demo()
    datetime_module_demo()
    os_module_demo()
    sys_module_demo()
    math_module_demo()
    json_module_demo()
    
    print("🎊 CONGRATULATIONS! 🎊")
    print("You've survived the built-in modules tour!")
    print("You're now officially 37% cooler and 73% more employable*")
    print("(*Statistics may be completely fabricated)")
    print("\n💡 Pro tip: These modules are your friends. Use them.")
    print("Don't reinvent the wheel - Python already did that for you!")


if __name__ == "__main__":
    main()