"""
Social Media Module

This module handles all social media-related functionality.
Because apparently everything needs to be posted online these days!

Functions:
- generate_social_media_post(): Create a random social media post
- display_recent_posts(): Show recent posts from the feed
- get_trending_hashtags(): Get popular hashtags
- analyze_student_social_activity(): Analyze a student's social media presence
"""

import random
import datetime
from student_utils import find_student_by_name


def generate_social_media_post(students_list, social_media_posts):
    """
    Generate a random social media post from a student.
    
    Args:
        students_list (list): List of all students
        social_media_posts (list): List to add the new post to
    """
    student_name = input("Student name for social media post: ")
    student = find_student_by_name(students_list, student_name)
    
    if not student:
        print("Student not found. Creating anonymous post instead!")
        student_name = "Anonymous Student"
        student = None
    
    # Random post templates that high schoolers might actually post
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
        "Successfully avoided eye contact with teacher for entire class 👁️‍🗨️✅",
        "Coffee is my personality now ☕️💀",
        "When you finish an assignment 5 minutes before it's due 🏃‍♀️💨",
        "Plot twist: I actually understood the math lesson today 🤯📐",
        "Dress code violation for showing my ankles apparently 🙄👟",
        "Fire drill during the only class I actually like 🔥😒",
        "Found a dollar in my locker from last semester 💵✨",
        "Forgot my lunch and now I'm photosynthesizing 🌱☀️",
        "When the WiFi goes down and we all become cavemen 📡❌",
        "Successfully parallel parked on the first try! 🚗🎯",
        "Procrastination level: expert 🏆⏰"
    ]
    
    post_content = random.choice(posts)
    timestamp = datetime.datetime.now()
    likes = random.randint(10, 200)
    comments = random.randint(0, 50)
    
    # Generate relevant hashtags
    hashtags = random.sample([
        "#highschoollife", "#studentproblems", "#sendhelp", 
        "#almostweekend", "#cafeteriafood", "#homework", 
        "#groupprojects", "#teacherproblems", "#schoolvibes",
        "#stressed", "#coffee", "#procrastination", "#mood",
        "#relatable", "#teenageproblems", "#schoolstruggles"
    ], random.randint(2, 5))
    
    # Create the post
    post = {
        "student": student_name,
        "content": post_content,
        "timestamp": timestamp.isoformat(),
        "likes": likes,
        "comments": comments,
        "hashtags": hashtags
    }
    
    social_media_posts.append(post)
    
    # Add to student's personal posts if student exists
    if student:
        student["social_media"]["posts"].append(post)
    
    # Display the new post
    print(f"\n📱 New post by {student_name}:")
    print(f"   {post_content}")
    print(f"   👍 {likes} likes | 💬 {comments} comments")
    print(f"   {' '.join(hashtags)}")


def display_recent_posts(social_media_posts, count=5):
    """
    Display the most recent social media posts.
    
    Args:
        social_media_posts (list): List of all social media posts
        count (int): Number of recent posts to display
    """
    if not social_media_posts:
        print("📱 Social Media Feed: Crickets... 🦗")
        print("   (Nobody's posted anything yet. How un-teen-like!)")
        return
    
    print(f"📱 RECENT SOCIAL MEDIA POSTS (Last {count})")
    print("=" * 45)
    
    # Get the most recent posts
    recent_posts = social_media_posts[-count:] if len(social_media_posts) >= count else social_media_posts
    recent_posts.reverse()  # Show newest first
    
    for i, post in enumerate(recent_posts, 1):
        # Parse timestamp for display
        timestamp = datetime.datetime.fromisoformat(post["timestamp"])
        time_str = timestamp.strftime("%m/%d %H:%M")
        
        print(f"\n{i}. @{post['student']} • {time_str}")
        print(f"   {post['content']}")
        print(f"   👍 {post['likes']} | 💬 {post['comments']}")
        
        if post.get('hashtags'):
            print(f"   {' '.join(post['hashtags'])}")


def get_trending_hashtags(social_media_posts, top_n=5):
    """
    Get the most popular hashtags from recent posts.
    
    Args:
        social_media_posts (list): List of all social media posts
        top_n (int): Number of top hashtags to return
        
    Returns:
        list: List of (hashtag, count) tuples
    """
    hashtag_counts = {}
    
    for post in social_media_posts:
        if post.get('hashtags'):
            for hashtag in post['hashtags']:
                hashtag_counts[hashtag] = hashtag_counts.get(hashtag, 0) + 1
    
    # Sort by count and return top N
    trending = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)
    return trending[:top_n]


def analyze_student_social_activity(student):
    """
    Analyze and display a student's social media activity.
    
    Args:
        student (dict): Student to analyze
    """
    if not student:
        print("Student not found. Can't analyze ghost activity!")
        return
    
    print(f"\n📊 SOCIAL MEDIA ANALYSIS: {student['name']}")
    print("=" * 45)
    
    social_data = student["social_media"]
    
    # Basic stats
    print(f"👥 Followers: {social_data['followers']}")
    print(f"👥 Following: {social_data['following']}")
    
    # Calculate follow ratio
    if social_data['following'] > 0:
        follow_ratio = social_data['followers'] / social_data['following']
        print(f"📈 Follow Ratio: {follow_ratio:.2f}")
        
        if follow_ratio > 1.5:
            print("   (Popular kid detected! 🌟)")
        elif follow_ratio > 0.8:
            print("   (Solid social presence 👍)")
        else:
            print("   (More of a follower than followed 🤷‍♀️)")
    
    # Post activity
    total_posts = len(social_data['posts'])
    school_posts = len(social_data['posts_about_school'])
    
    print(f"\n📝 Total Posts: {total_posts}")
    print(f"🏫 School-related Posts: {school_posts}")
    
    if total_posts > 0:
        school_percentage = (school_posts / total_posts) * 100
        print(f"📊 School Content: {school_percentage:.1f}%")
        
        if school_percentage > 50:
            print("   (School is life! 📚)")
        elif school_percentage > 20:
            print("   (Balanced social media presence)")
        else:
            print("   (Keeping school life private 🤫)")
    
    # Recent school posts
    if social_data['posts_about_school']:
        print(f"\n📱 Recent School Posts:")
        for post in social_data['posts_about_school'][-3:]:
            timestamp = datetime.datetime.fromisoformat(post['timestamp'])
            time_str = timestamp.strftime("%m/%d")
            print(f"   • {time_str}: {post['post']} ({post['likes']} likes)")
    else:
        print(f"\n📱 No school-related posts yet!")
        print("   (Keeping academics and social media separate - wise choice!)")


def generate_random_student_post(student, social_media_posts):
    """
    Generate a random post for a specific student (not grade-related).
    
    Args:
        student (dict): Student to generate post for
        social_media_posts (list): List to add post to
        
    Returns:
        dict: The created post
    """
    # Non-academic post templates
    casual_posts = [
        "Just had the most random dream 😴💭",
        "Found the perfect song for this mood 🎵✨",
        "Weekend plans: absolutely nothing and loving it 🛋️",
        "When did adulting become so complicated? 😅",
        "Random thought: why do we park in driveways and drive on parkways? 🤔",
        "Current status: motivated for exactly 3 minutes ⏰",
        "Life update: still figuring it out 🤷‍♀️",
        "Grateful for small things today 🙏💕",
        "Plot twist: I actually cleaned my room 🧹✨",
        "Me vs. my responsibilities: ongoing battle ⚔️"
    ]
    
    post_content = random.choice(casual_posts)
    timestamp = datetime.datetime.now()
    likes = random.randint(15, 100)
    comments = random.randint(2, 25)
    
    hashtags = random.sample([
        "#mood", "#random", "#life", "#thoughts", "#vibes",
        "#weekend", "#blessed", "#grateful", "#real", "#honest"
    ], random.randint(1, 3))
    
    post = {
        "student": student["name"],
        "content": post_content,
        "timestamp": timestamp.isoformat(),
        "likes": likes,
        "comments": comments,
        "hashtags": hashtags
    }
    
    social_media_posts.append(post)
    student["social_media"]["posts"].append(post)
    
    return post


def display_social_media_menu():
    """Display the social media submenu options."""
    print("\n📱 SOCIAL MEDIA OPTIONS:")
    print("1. Generate Random Post")
    print("2. View Recent Posts")
    print("3. View Trending Hashtags") 
    print("4. Analyze Student Activity")
    print("5. Back to Main Menu")


def handle_social_media_menu(students_list, social_media_posts):
    """
    Handle the social media submenu.
    
    Args:
        students_list (list): List of all students
        social_media_posts (list): List of all social media posts
    """
    while True:
        display_social_media_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            generate_social_media_post(students_list, social_media_posts)
        elif choice == "2":
            display_recent_posts(social_media_posts)
        elif choice == "3":
            trending = get_trending_hashtags(social_media_posts)
            if trending:
                print(f"\n🔥 TRENDING HASHTAGS:")
                for i, (hashtag, count) in enumerate(trending, 1):
                    print(f"   {i}. {hashtag} ({count} posts)")
            else:
                print("\n🔥 No trending hashtags yet!")
                print("   (Create some posts to see what's popular!)")
        elif choice == "4":
            student_name = input("Student name to analyze: ")
            student = find_student_by_name(students_list, student_name)
            analyze_student_social_activity(student)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again, social media guru!")