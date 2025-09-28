#!/usr/bin/env python3
"""
Student Management System - The Modular Masterpiece

This is what happens when you organize your code properly!
Clean, readable, maintainable, and your future self won't hate you.

This program demonstrates proper modular programming by separating
different functionalities into their own modules:
- student_utils: Student CRUD operations
- grade_calculator: Grade and GPA calculations  
- social_media: Social media functionality

Look how much cleaner this is compared to the nightmare version!
"""

import json
import sys
import os

# Import our custom modules
from student_utils import (
    add_student, 
    find_student_by_name, 
    find_student_by_id,
    generate_student_report,
    load_sample_students
)
from grade_calculator import (
    add_grade,
    calculate_class_statistics,
    get_grade_weights
)
from social_media import (
    generate_social_media_post,
    display_recent_posts,
    handle_social_media_menu
)

# Global application state (kept minimal!)
students = []
social_media_posts = []
current_semester = "Fall 2024"


def save_data():
    """
    Save all application data to JSON files.
    Clean and simple!
    """
    try:
        # Save students data
        with open('/tmp/students_data.json', 'w') as f:
            json.dump(students, f, indent=2, default=str)
        
        # Save social media posts
        with open('/tmp/social_media_posts.json', 'w') as f:
            json.dump(social_media_posts, f, indent=2, default=str)
        
        print("✅ Data saved successfully to /tmp/ folder!")
        print("   (Look at that organized data storage!)")
        
    except Exception as e:
        print(f"❌ Error saving data: {e}")
        print("   (Even modular code can't fix file system issues!)")


def load_data():
    """
    Load application data from JSON files if they exist.
    """
    global students, social_media_posts
    
    try:
        # Load students data
        if os.path.exists('/tmp/students_data.json'):
            with open('/tmp/students_data.json', 'r') as f:
                students = json.load(f)
            print("📚 Student data loaded from file!")
        
        # Load social media posts
        if os.path.exists('/tmp/social_media_posts.json'):
            with open('/tmp/social_media_posts.json', 'r') as f:
                social_media_posts = json.load(f)
            print("📱 Social media data loaded from file!")
            
        if students or social_media_posts:
            print("✅ Data loaded successfully!")
        else:
            print("📂 No saved data found. Starting fresh!")
            
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        print("   Starting with empty data...")
        students = []
        social_media_posts = []


def load_sample_data():
    """
    Load sample data for demonstration purposes.
    """
    global students
    
    sample_students = load_sample_students()
    students.extend(sample_students)
    
    print("🎭 Sample data loaded!")
    print(f"   Added {len(sample_students)} sample students to the system.")
    print("   Now you have some data to play with!")


def display_main_menu():
    """
    Display the main menu options.
    Look how clean and organized this is!
    """
    print(f"\n🎓 STUDENT MANAGEMENT SYSTEM - {current_semester}")
    print("The modular masterpiece! ✨")
    print("\n📋 MAIN MENU:")
    print("1. 👤 Student Management")
    print("2. 📊 Grade Management") 
    print("3. 📱 Social Media")
    print("4. 📈 View Statistics")
    print("5. 💾 Save Data")
    print("6. 📂 Load Sample Data")
    print("7. ❌ Exit")


def handle_student_management():
    """
    Handle the student management submenu.
    """
    while True:
        print(f"\n👤 STUDENT MANAGEMENT")
        print("1. Add New Student")
        print("2. Find Student by Name")
        print("3. Generate Student Report")
        print("4. List All Students")
        print("5. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            add_student(students)
            
        elif choice == "2":
            name = input("Enter student name: ")
            student = find_student_by_name(students, name)
            if student:
                print(f"✅ Found: {student['name']} (ID: {student['id']}, Grade: {student['grade']})")
                print(f"   GPA: {student['gpa']:.2f} | Attendance: {student['attendance']}%")
            else:
                print("❌ Student not found. Check the spelling or try a different name.")
                
        elif choice == "3":
            name = input("Enter student name for report: ")
            student = find_student_by_name(students, name)
            generate_student_report(student)
            
        elif choice == "4":
            if students:
                print(f"\n📋 ALL STUDENTS ({len(students)} total):")
                print("-" * 60)
                for student in students:
                    print(f"  {student['name']} (Grade {student['grade']}) - GPA: {student['gpa']:.2f}")
            else:
                print("\n📋 No students in the system yet!")
                print("   Add some students to get started!")
                
        elif choice == "5":
            break
            
        else:
            print("❌ Invalid choice. Try again!")


def handle_grade_management():
    """
    Handle the grade management submenu.
    """
    while True:
        print(f"\n📊 GRADE MANAGEMENT")
        print("1. Add Grade")
        print("2. View Grade Weights")
        print("3. Calculate Class Statistics")
        print("4. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            add_grade(students, social_media_posts)
            
        elif choice == "2":
            weights = get_grade_weights()
            print(f"\n⚖️ CURRENT GRADE WEIGHTS:")
            total_weight = 0
            for category, weight in weights.items():
                percentage = weight * 100
                print(f"  {category.title()}: {percentage}%")
                total_weight += weight
            print(f"  Total: {total_weight * 100}%")
            
        elif choice == "3":
            calculate_class_statistics(students, social_media_posts, current_semester)
            
        elif choice == "4":
            break
            
        else:
            print("❌ Invalid choice. Try again!")


def main():
    """
    Main application loop.
    Clean, simple, and modular!
    """
    print("🎉 WELCOME TO THE STUDENT MANAGEMENT SYSTEM! 🎉")
    print("The modular version - where code organization meets sanity!")
    print("\n✨ Features:")
    print("  • Clean, separated modules")
    print("  • Easy to maintain and extend")
    print("  • Your future self will thank you")
    
    # Try to load existing data
    load_data()
    
    while True:
        try:
            display_main_menu()
            choice = input("\nEnter your choice (1-7): ")
            
            if choice == "1":
                handle_student_management()
                
            elif choice == "2":
                handle_grade_management()
                
            elif choice == "3":
                handle_social_media_menu(students, social_media_posts)
                
            elif choice == "4":
                calculate_class_statistics(students, social_media_posts, current_semester)
                
            elif choice == "5":
                save_data()
                
            elif choice == "6":
                load_sample_data()
                
            elif choice == "7":
                print("\n👋 Thanks for using the Student Management System!")
                print("Remember: Modular code is happy code! ✨")
                
                # Ask if they want to save before exiting
                save_choice = input("Save data before exiting? (y/n): ").lower()
                if save_choice in ['y', 'yes']:
                    save_data()
                
                print("Goodbye! 🎓")
                break
                
            else:
                print("❌ Invalid choice. Please enter a number 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n🛑 Force quit detected!")
            save_choice = input("Save data before exiting? (y/n): ").lower()
            if save_choice in ['y', 'yes']:
                save_data()
            print("Goodbye! 👋")
            break
            
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("But hey, at least the error is contained in a module! 🎭")


if __name__ == "__main__":
    main()