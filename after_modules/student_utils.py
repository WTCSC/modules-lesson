"""
Student Utilities Module

This module handles all student-related operations.
Look how clean and organized this is! Your future self will thank you.

Functions:
- add_student(): Add a new student to the system
- find_student_by_id(): Find a student by their ID
- find_student_by_name(): Find a student by their name
- generate_student_report(): Create a detailed student report
"""

import random
import datetime


def add_student(students_list):
    """
    Add a new student to the system.
    
    Args:
        students_list (list): List of existing students
        
    Returns:
        dict: The newly created student dictionary
    """
    print("Adding a new student to our digital prison... I mean, system!")
    
    name = input("Student name (or nickname if they're too cool for real names): ")
    if not name:
        name = "Anonymous Troublemaker"
    
    # Generate random student ID because we're efficient like that
    student_id = random.randint(10000, 99999)
    
    # Get grade level with error handling
    try:
        grade = int(input("Grade level (9-12, or just guess): "))
        if grade < 9 or grade > 12:
            print("That's not a high school grade, but sure, let's go with it.")
    except ValueError:
        grade = random.choice([9, 10, 11, 12])
        print(f"Invalid input. I'll just say they're in grade {grade}.")
    
    # Generate email because students never remember theirs anyway
    email = f"{name.lower().replace(' ', '.')}@school.edu"
    
    # Create the student dictionary with all the important stuff
    student = {
        "id": student_id,
        "name": name,
        "grade": grade,
        "email": email,
        "subjects": [],
        "grades": {
            "homework": [],
            "tests": [],
            "participation": [],
            "projects": []
        },
        "gpa": 0.0,
        "attendance": random.randint(70, 98),
        "disciplinary_actions": random.choice([0, 0, 0, 1, 2]),
        "favorite_excuse": random.choice([
            "My internet was down",
            "I forgot we had school today",
            "My cat deleted my homework",
            "I was abducted by aliens",
            "Time is a social construct"
        ]),
        "social_media": {
            "posts": [],
            "followers": random.randint(50, 500),
            "following": random.randint(100, 800),
            "posts_about_school": []
        },
        "emergency_contact": "Mom (good luck reaching her)",
        "dietary_restrictions": random.choice([
            "None", "Vegetarian", "Allergic to vegetables", "Only eats pizza"
        ]),
        "transportation": random.choice([
            "Bus", "Car", "Skateboard", "Pure willpower", "Teleportation"
        ]),
        "clubs": [],
        "career_goals": random.choice([
            "I have no idea",
            "Internet famous", 
            "Professional gamer",
            "Something with computers",
            "Anything that pays well"
        ])
    }
    
    students_list.append(student)
    print(f"Student {name} (ID: {student_id}) has been added to the system!")
    print("Welcome to the educational industrial complex!")
    return student


def find_student_by_id(students_list, student_id):
    """
    Find a student by their ID number.
    
    Args:
        students_list (list): List of students to search
        student_id (int): The student ID to find
        
    Returns:
        dict or None: Student dictionary if found, None otherwise
    """
    for student in students_list:
        if student["id"] == student_id:
            return student
    return None


def find_student_by_name(students_list, name):
    """
    Find a student by their name (case-insensitive).
    
    Args:
        students_list (list): List of students to search
        name (str): The student name to find
        
    Returns:
        dict or None: Student dictionary if found, None otherwise
    """
    for student in students_list:
        if student["name"].lower() == name.lower():
            return student
    return None


def generate_student_report(student):
    """
    Generate a comprehensive report for a specific student.
    
    Args:
        student (dict): The student dictionary to report on
    """
    if not student:
        print("Student not found. Maybe they transferred to a better school?")
        return
    
    print(f"\n📋 STUDENT REPORT: {student['name']}")
    print("=" * 50)
    
    # Basic information
    print(f"Student ID: {student['id']}")
    print(f"Grade Level: {student['grade']}")
    print(f"Email: {student['email']}")
    print(f"GPA: {student['gpa']:.2f}")
    print(f"Attendance: {student['attendance']}%")
    
    # Grades breakdown
    print(f"\nGRADES BREAKDOWN:")
    for category, grades in student["grades"].items():
        if grades:
            avg = sum(grades) / len(grades)
            print(f"  {category.title()}: {avg:.1f}% (from {len(grades)} assignments)")
        else:
            print(f"  {category.title()}: No grades yet")
    
    # Personal information
    print(f"\nPERSONAL INFO:")
    print(f"  Favorite excuse: '{student['favorite_excuse']}'")
    print(f"  Career goals: {student['career_goals']}")
    print(f"  Transportation: {student['transportation']}")
    print(f"  Dietary restrictions: {student['dietary_restrictions']}")
    
    # Social media presence
    print(f"\nSOCIAL MEDIA PRESENCE:")
    print(f"  Followers: {student['social_media']['followers']}")
    print(f"  Following: {student['social_media']['following']}")
    print(f"  School-related posts: {len(student['social_media']['posts_about_school'])}")
    
    if student['social_media']['posts_about_school']:
        print("  Recent school posts:")
        for post in student['social_media']['posts_about_school'][-3:]:
            print(f"    - {post['post']} ({post['likes']} likes)")
    
    # Disciplinary record
    if student['disciplinary_actions'] > 0:
        print(f"\nDISCIPLINARY RECORD:")
        print(f"  Total actions: {student['disciplinary_actions']}")
        print("  (Details confidential, but probably involved talking in class)")
    else:
        print(f"\nDISCIPLINARY RECORD: Clean! ✨")


def load_sample_students():
    """
    Create and return sample student data for testing.
    
    Returns:
        list: List of sample student dictionaries
    """
    sample_students = [
        {
            "id": 12345,
            "name": "Alex Procrastinator",
            "grade": 11,
            "email": "alex.procrastinator@school.edu",
            "subjects": ["Computer Science", "Math", "English"],
            "grades": {
                "homework": [85, 78, 92, 88],
                "tests": [82, 95, 76],
                "participation": [90, 85, 95, 88],
                "projects": [94, 87]
            },
            "gpa": 87.3,
            "attendance": 89,
            "disciplinary_actions": 1,
            "favorite_excuse": "My internet was down",
            "social_media": {
                "posts": [],
                "followers": 234,
                "following": 456,
                "posts_about_school": []
            },
            "emergency_contact": "Mom (good luck reaching her)",
            "dietary_restrictions": "Allergic to vegetables",
            "transportation": "Skateboard",
            "clubs": ["Coding Club", "Procrastinators Anonymous"],
            "career_goals": "Something with computers"
        },
        {
            "id": 54321,
            "name": "Jordan Overachiever",
            "grade": 12,
            "email": "jordan.overachiever@school.edu",
            "subjects": ["AP Everything"],
            "grades": {
                "homework": [98, 97, 99, 96],
                "tests": [97, 98, 95],
                "participation": [100, 98, 99],
                "projects": [99, 98]
            },
            "gpa": 97.8,
            "attendance": 99,
            "disciplinary_actions": 0,
            "favorite_excuse": "I don't make excuses",
            "social_media": {
                "posts": [],
                "followers": 89,
                "following": 23,
                "posts_about_school": []
            },
            "emergency_contact": "Mom (she answers immediately)",
            "dietary_restrictions": "Perfect nutrition only",
            "transportation": "Arrives by lightning bolt",
            "clubs": ["Everything Club", "President of Student Council"],
            "career_goals": "Rule the world (benevolently)"
        }
    ]
    
    return sample_students