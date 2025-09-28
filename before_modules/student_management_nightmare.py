#!/usr/bin/env python3
"""
STUDENT MANAGEMENT NIGHTMARE: The Monolithic Monster

This is what happens when you put EVERYTHING in one file.
It's like putting your entire life in one giant box and 
hoping you can find your socks when you need them.

This program manages student information, calculates grades,
handles social media posts, and generates reports.
All in one beautiful, chaotic mess.

WARNING: This code is intentionally terrible. Don't do this at home.
(Or at school. Or anywhere, really.)
"""

import random
import datetime
import json
import math

# Global variables everywhere! Because organization is overrated!
students = []
social_media_posts = []
grade_weights = {"homework": 0.3, "tests": 0.4, "participation": 0.2, "projects": 0.1}
current_semester = "Fall 2024"

def add_student():
    """Add a student. This function does way too much."""
    print("Adding a new student to our digital prison... I mean, system!")
    
    name = input("Student name (or nickname if they're too cool for real names): ")
    if not name:
        name = "Anonymous Troublemaker"
    
    # Generate random student ID because we're lazy
    student_id = random.randint(10000, 99999)
    
    # Get grade level
    try:
        grade = int(input("Grade level (9-12, or just guess): "))
        if grade < 9 or grade > 12:
            print("That's not a high school grade, but sure, let's go with it.")
    except ValueError:
        grade = random.choice([9, 10, 11, 12])
        print(f"Invalid input. I'll just say they're in grade {grade}.")
    
    # Generate random email because students never remember theirs
    email = f"{name.lower().replace(' ', '.')}@school.edu"
    
    # Create student dictionary
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
        "attendance": random.randint(70, 98),  # Because someone's always missing
        "disciplinary_actions": random.choice([0, 0, 0, 1, 2]),  # Most are angels
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
        "dietary_restrictions": random.choice(["None", "Vegetarian", "Allergic to vegetables", "Only eats pizza"]),
        "transportation": random.choice(["Bus", "Car", "Skateboard", "Pure willpower", "Teleportation"]),
        "clubs": [],
        "career_goals": random.choice([
            "I have no idea",
            "Internet famous",
            "Professional gamer",
            "Something with computers",
            "Anything that pays well"
        ])
    }
    
    students.append(student)
    print(f"Student {name} (ID: {student_id}) has been added to the system!")
    print("Welcome to the educational industrial complex!")
    return student

def find_student_by_id(student_id):
    """Find a student by ID. Simple enough, right?"""
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def find_student_by_name(name):
    """Find a student by name. What could go wrong?"""
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

def add_grade():
    """Add a grade. This function is getting out of hand."""
    print("Time to add some grades! (Insert evil teacher laugh here)")
    
    # Find the student
    student_name = input("Student name: ")
    student = find_student_by_name(student_name)
    
    if not student:
        print("Student not found. Maybe they're in witness protection?")
        return
    
    # Get grade category
    print("Grade categories:")
    for category in grade_weights.keys():
        print(f"  - {category}")
    
    category = input("Category: ").lower()
    if category not in grade_weights:
        print("Invalid category. I'll just put it under 'homework' because why not?")
        category = "homework"
    
    # Get the grade
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
    
    # Add the grade
    student["grades"][category].append(grade)
    
    # Recalculate GPA (this should be its own function but whatever)
    total_points = 0
    total_weight = 0
    
    for cat, weight in grade_weights.items():
        if student["grades"][cat]:
            avg = sum(student["grades"][cat]) / len(student["grades"][cat])
            total_points += avg * weight
            total_weight += weight
    
    if total_weight > 0:
        student["gpa"] = total_points / total_weight
    
    print(f"Grade {grade} added to {student['name']}'s {category}!")
    print(f"New GPA: {student['gpa']:.2f}")
    
    # Generate automatic social media post about grades
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
    
    post = random.choice(posts)
    student["social_media"]["posts_about_school"].append({
        "post": post,
        "timestamp": datetime.datetime.now().isoformat(),
        "likes": random.randint(5, 50),
        "comments": random.randint(0, 15)
    })

def generate_social_media_post():
    """Generate a random social media post because why not?"""
    student_name = input("Student name for social media post: ")
    student = find_student_by_name(student_name)
    
    if not student:
        print("Student not found. Creating anonymous post instead!")
        student_name = "Anonymous Student"
    
    # Random post templates
    posts = [
        "Just survived another day of high school 🏫😴",
        "When the teacher says 'this won't be on the test' but it's definitely on the test 📚😭",
        "Cafeteria food hit different today... in a bad way 🤢",
        "Group project partner just ghosted us 👻 Classic move!",
        "3 hours of homework for 1 class? Make it make sense 📝😵",
        "Friday feeling already and it's only Tuesday 📅😑",
        "That moment when you realize you studied for the wrong test 📖🤡",
        "Teacher: 'Any questions?' Me: *has 47 questions* Also me: *stays silent* 🤐",
        "Why do they call it rush hour when nobody's moving? Oh wait, that's the lunch line 🍕⏰",
        "Successfully avoided eye contact with teacher for entire class 👁️‍🗨️✅"
    ]
    
    post_content = random.choice(posts)
    timestamp = datetime.datetime.now()
    likes = random.randint(10, 200)
    comments = random.randint(0, 50)
    
    post = {
        "student": student_name,
        "content": post_content,
        "timestamp": timestamp.isoformat(),
        "likes": likes,
        "comments": comments,
        "hashtags": random.sample(["#highschoollife", "#studentproblems", "#sendhelp", 
                                 "#almostweekend", "#cafeteriafood", "#homework", 
                                 "#groupprojects", "#teacherproblems"], 
                                random.randint(1, 4))
    }
    
    social_media_posts.append(post)
    
    if student and isinstance(student, dict):
        student["social_media"]["posts"].append(post)
    
    print(f"\n📱 New post by {student_name}:")
    print(f"   {post_content}")
    print(f"   👍 {likes} likes | 💬 {comments} comments")
    print(f"   {' '.join(post['hashtags'])}")

def calculate_class_statistics():
    """Calculate class statistics. This is getting ridiculous."""
    if not students:
        print("No students in the system. Ghost class!")
        return
    
    print(f"\n📊 CLASS STATISTICS FOR {current_semester}")
    print("=" * 50)
    
    # Basic stats
    total_students = len(students)
    print(f"Total students: {total_students}")
    
    # Grade distribution
    grade_levels = {}
    for student in students:
        grade = student["grade"]
        grade_levels[grade] = grade_levels.get(grade, 0) + 1
    
    print("\nGrade level distribution:")
    for grade in sorted(grade_levels.keys()):
        count = grade_levels[grade]
        percentage = (count / total_students) * 100
        print(f"  Grade {grade}: {count} students ({percentage:.1f}%)")
    
    # GPA statistics
    gpas = [student["gpa"] for student in students if student["gpa"] > 0]
    if gpas:
        avg_gpa = sum(gpas) / len(gpas)
        min_gpa = min(gpas)
        max_gpa = max(gpas)
        
        print(f"\nGPA Statistics:")
        print(f"  Average GPA: {avg_gpa:.2f}")
        print(f"  Highest GPA: {max_gpa:.2f}")
        print(f"  Lowest GPA: {min_gpa:.2f}")
        
        # GPA ranges
        excellent = len([gpa for gpa in gpas if gpa >= 90])
        good = len([gpa for gpa in gpas if 80 <= gpa < 90])
        average = len([gpa for gpa in gpas if 70 <= gpa < 80])
        struggling = len([gpa for gpa in gpas if gpa < 70])
        
        print(f"\nGPA Distribution:")
        print(f"  Excellent (90+): {excellent} students")
        print(f"  Good (80-89): {good} students")
        print(f"  Average (70-79): {average} students")
        print(f"  Needs Help (<70): {struggling} students")
    
    # Attendance
    attendance_rates = [student["attendance"] for student in students]
    avg_attendance = sum(attendance_rates) / len(attendance_rates)
    print(f"\nAverage attendance: {avg_attendance:.1f}%")
    
    # Disciplinary actions
    total_actions = sum(student["disciplinary_actions"] for student in students)
    print(f"Total disciplinary actions: {total_actions}")
    
    # Social media stats
    total_posts = len(social_media_posts)
    total_likes = sum(post["likes"] for post in social_media_posts)
    print(f"\nSocial Media Activity:")
    print(f"  Total posts: {total_posts}")
    print(f"  Total likes: {total_likes}")
    if total_posts > 0:
        avg_likes = total_likes / total_posts
        print(f"  Average likes per post: {avg_likes:.1f}")

def generate_student_report():
    """Generate a report for a specific student. So much code..."""
    student_name = input("Student name for report: ")
    student = find_student_by_name(student_name)
    
    if not student:
        print("Student not found. Maybe they transferred to a better school?")
        return
    
    print(f"\n📋 STUDENT REPORT: {student['name']}")
    print("=" * 50)
    
    # Basic info
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
    
    # Personal info
    print(f"\nPERSONAL INFO:")
    print(f"  Favorite excuse: '{student['favorite_excuse']}'")
    print(f"  Career goals: {student['career_goals']}")
    print(f"  Transportation: {student['transportation']}")
    print(f"  Dietary restrictions: {student['dietary_restrictions']}")
    
    # Social media
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

def save_data():
    """Save all data to files because we're pretending to be organized"""
    # Save students
    with open('/tmp/students_data.json', 'w') as f:
        json.dump(students, f, indent=2, default=str)
    
    # Save social media posts
    with open('/tmp/social_media_posts.json', 'w') as f:
        json.dump(social_media_posts, f, indent=2, default=str)
    
    print("Data saved to /tmp/ folder!")
    print("(Because that's definitely where important data belongs)")

def load_sample_data():
    """Load some sample data so we're not starting from scratch"""
    global students, social_media_posts
    
    # Sample students
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
    
    students.extend(sample_students)
    print("Sample data loaded! Now we have some students to work with.")

def main_menu():
    """The main menu. This function is the boss of all other functions."""
    print("\n🎓 STUDENT MANAGEMENT NIGHTMARE 🎓")
    print("Where organization goes to die!")
    print("\nMenu Options:")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Generate Social Media Post")
    print("4. Calculate Class Statistics")
    print("5. Generate Student Report")
    print("6. Save Data")
    print("7. Load Sample Data")
    print("8. Exit (Escape while you can)")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-8): ")
            
            if choice == "1":
                add_student()
            elif choice == "2":
                add_grade()
            elif choice == "3":
                generate_social_media_post()
            elif choice == "4":
                calculate_class_statistics()
            elif choice == "5":
                generate_student_report()
            elif choice == "6":
                save_data()
            elif choice == "7":
                load_sample_data()
            elif choice == "8":
                print("Goodbye! Thanks for using the nightmare system!")
                print("May your code be forever modular! ✨")
                break
            else:
                print("Invalid choice. Try again, or don't. I'm not your boss.")
                
        except KeyboardInterrupt:
            print("\n\nForce quit detected! Goodbye!")
            break
        except Exception as e:
            print(f"Something went wrong: {e}")
            print("This is what happens when you put everything in one file!")

if __name__ == "__main__":
    print("Welcome to the Student Management Nightmare!")
    print("This is what happens when you don't use modules.")
    print("Brace yourself for the chaos... 🌪️\n")
    main_menu()