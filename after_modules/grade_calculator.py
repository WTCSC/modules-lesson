"""
Grade Calculator Module

This module handles all grade-related calculations and operations.
Because math is hard, but organizing math is harder!

Functions:
- add_grade(): Add a grade to a student's record
- calculate_gpa(): Calculate a student's GPA
- calculate_class_statistics(): Generate statistics for the entire class
- get_grade_weights(): Return the grading weight system
"""

import random
import datetime
from student_utils import find_student_by_name

# Grade weight configuration - adjust as needed for your grading system
GRADE_WEIGHTS = {
    "homework": 0.3,
    "tests": 0.4, 
    "participation": 0.2,
    "projects": 0.1
}


def get_grade_weights():
    """
    Return the current grade weighting system.
    
    Returns:
        dict: Grade category weights
    """
    return GRADE_WEIGHTS.copy()


def calculate_gpa(student):
    """
    Calculate and update a student's GPA based on their grades.
    
    Args:
        student (dict): Student dictionary to calculate GPA for
        
    Returns:
        float: The calculated GPA
    """
    total_points = 0
    total_weight = 0
    
    for category, weight in GRADE_WEIGHTS.items():
        if student["grades"][category]:  # If there are grades in this category
            # Calculate average for this category
            category_avg = sum(student["grades"][category]) / len(student["grades"][category])
            total_points += category_avg * weight
            total_weight += weight
    
    if total_weight > 0:
        gpa = total_points / total_weight
        student["gpa"] = gpa
        return gpa
    else:
        student["gpa"] = 0.0
        return 0.0


def add_grade(students_list, social_media_posts):
    """
    Add a grade to a student's record and update their GPA.
    Also generates a social media post because teens post about everything!
    
    Args:
        students_list (list): List of all students
        social_media_posts (list): List to add social media posts to
    """
    print("Time to add some grades! (Insert evil teacher laugh here)")
    
    # Find the student
    student_name = input("Student name: ")
    student = find_student_by_name(students_list, student_name)
    
    if not student:
        print("Student not found. Maybe they're in witness protection?")
        return
    
    # Display grade categories
    print("Grade categories:")
    for category in GRADE_WEIGHTS.keys():
        print(f"  - {category}")
    
    category = input("Category: ").lower()
    if category not in GRADE_WEIGHTS:
        print("Invalid category. I'll just put it under 'homework' because why not?")
        category = "homework"
    
    # Get the grade with validation
    try:
        grade = float(input("Grade (0-100): "))
        if grade < 0:
            grade = 0
            print("Negative grades aren't a thing. Set to 0.")
        elif grade > 100:
            print("Over 100? Someone's an overachiever!")
    except ValueError:
        grade = random.randint(60, 95)
        print(f"Invalid grade. I'll give them a {grade} because I'm feeling generous.")
    
    # Add the grade to the student's record
    student["grades"][category].append(grade)
    
    # Recalculate GPA
    new_gpa = calculate_gpa(student)
    
    print(f"Grade {grade} added to {student['name']}'s {category}!")
    print(f"New GPA: {new_gpa:.2f}")
    
    # Generate automatic social media post about the grade
    _generate_grade_social_media_post(student, grade, social_media_posts)


def _generate_grade_social_media_post(student, grade, social_media_posts):
    """
    Generate a social media post about a grade (private helper function).
    
    Args:
        student (dict): The student who got the grade
        grade (float): The grade they received
        social_media_posts (list): List to add the post to
    """
    # Choose post based on grade range
    if grade >= 90:
        posts = [
            f"Just got a {grade}! 🎉 #blessed #smartcookie",
            f"When you actually study and it pays off... {grade}! 📚✨",
            f"Mom's gonna be so proud! {grade} on that assignment! 👏"
        ]
    elif grade >= 70:
        posts = [
            f"Could be worse... got a {grade} 🤷‍♀️",
            f"Passed with a {grade}! That's what matters, right? 😅", 
            f"Not my best work but {grade} will do 📝"
        ]
    else:
        posts = [
            f"We don't talk about that {grade}... 😭",
            f"Time to have a serious talk with my study habits... {grade} 📉",
            f"At least I showed up? Got a {grade} 🤦‍♀️"
        ]
    
    post_content = random.choice(posts)
    
    # Create the social media post
    post = {
        "post": post_content,
        "timestamp": datetime.datetime.now().isoformat(),
        "likes": random.randint(5, 50),
        "comments": random.randint(0, 15)
    }
    
    # Add to student's school posts
    student["social_media"]["posts_about_school"].append(post)
    
    # Add to general social media feed with student name
    full_post = {
        "student": student["name"],
        "content": post_content,
        "timestamp": post["timestamp"],
        "likes": post["likes"],
        "comments": post["comments"],
        "hashtags": ["#grades", "#schoollife", "#student"]
    }
    social_media_posts.append(full_post)


def calculate_class_statistics(students_list, social_media_posts, current_semester="Fall 2024"):
    """
    Calculate and display comprehensive class statistics.
    
    Args:
        students_list (list): List of all students
        social_media_posts (list): List of social media posts
        current_semester (str): Current semester name
    """
    if not students_list:
        print("No students in the system. Ghost class!")
        return
    
    print(f"\n📊 CLASS STATISTICS FOR {current_semester}")
    print("=" * 50)
    
    # Basic statistics
    total_students = len(students_list)
    print(f"Total students: {total_students}")
    
    # Grade level distribution
    grade_levels = {}
    for student in students_list:
        grade = student["grade"]
        grade_levels[grade] = grade_levels.get(grade, 0) + 1
    
    print("\nGrade level distribution:")
    for grade in sorted(grade_levels.keys()):
        count = grade_levels[grade]
        percentage = (count / total_students) * 100
        print(f"  Grade {grade}: {count} students ({percentage:.1f}%)")
    
    # GPA statistics
    gpas = [student["gpa"] for student in students_list if student["gpa"] > 0]
    if gpas:
        avg_gpa = sum(gpas) / len(gpas)
        min_gpa = min(gpas)
        max_gpa = max(gpas)
        
        print(f"\nGPA Statistics:")
        print(f"  Average GPA: {avg_gpa:.2f}")
        print(f"  Highest GPA: {max_gpa:.2f}")
        print(f"  Lowest GPA: {min_gpa:.2f}")
        
        # GPA distribution ranges
        excellent = len([gpa for gpa in gpas if gpa >= 90])
        good = len([gpa for gpa in gpas if 80 <= gpa < 90])
        average = len([gpa for gpa in gpas if 70 <= gpa < 80])
        struggling = len([gpa for gpa in gpas if gpa < 70])
        
        print(f"\nGPA Distribution:")
        print(f"  Excellent (90+): {excellent} students")
        print(f"  Good (80-89): {good} students")
        print(f"  Average (70-79): {average} students")
        print(f"  Needs Help (<70): {struggling} students")
    
    # Attendance statistics
    attendance_rates = [student["attendance"] for student in students_list]
    avg_attendance = sum(attendance_rates) / len(attendance_rates)
    print(f"\nAverage attendance: {avg_attendance:.1f}%")
    
    # Disciplinary actions
    total_actions = sum(student["disciplinary_actions"] for student in students_list)
    print(f"Total disciplinary actions: {total_actions}")
    
    # Social media activity statistics
    total_posts = len(social_media_posts)
    if social_media_posts:
        total_likes = sum(post["likes"] for post in social_media_posts)
        avg_likes = total_likes / total_posts
        print(f"\nSocial Media Activity:")
        print(f"  Total posts: {total_posts}")
        print(f"  Total likes: {total_likes}")
        print(f"  Average likes per post: {avg_likes:.1f}")
    else:
        print(f"\nSocial Media Activity:")
        print(f"  Total posts: 0")
        print(f"  (Everyone's actually studying for once!)")


def get_student_grade_summary(student):
    """
    Get a summary of a student's grades in all categories.
    
    Args:
        student (dict): Student to get grade summary for
        
    Returns:
        dict: Summary of grades by category
    """
    summary = {}
    
    for category, grades in student["grades"].items():
        if grades:
            summary[category] = {
                "average": sum(grades) / len(grades),
                "count": len(grades),
                "grades": grades.copy()
            }
        else:
            summary[category] = {
                "average": 0,
                "count": 0,
                "grades": []
            }
    
    return summary