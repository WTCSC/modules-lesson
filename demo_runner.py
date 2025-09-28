#!/usr/bin/env python3
"""
Demo Runner: The Ultimate Module Comparison Tool

This script helps you compare the monolithic nightmare with the modular masterpiece.
It's like a before/after transformation show, but for code!

Run this to see the difference modules make in your life.
"""

import os
import sys
import subprocess
import time


def print_banner(title, emoji="🎯"):
    """Print a fancy banner for sections."""
    print(f"\n{emoji} {title} {emoji}")
    print("=" * (len(title) + 4))


def print_section_separator():
    """Print a section separator."""
    print("\n" + "-" * 60 + "\n")


def run_demo_section(title, description, commands, wait_time=3):
    """
    Run a demo section with description and commands.
    
    Args:
        title (str): Section title
        description (str): What this section shows
        commands (list): List of commands to run
        wait_time (int): Seconds to wait between sections
    """
    print_banner(title, "🎯")
    print(f"📝 {description}")
    print(f"\n⚡ Running commands:")
    
    for cmd in commands:
        print(f"   $ {cmd}")
    
    print(f"\n⏳ Starting in {wait_time} seconds...")
    
    # Countdown
    for i in range(wait_time, 0, -1):
        print(f"   {i}...", end=" ", flush=True)
        time.sleep(1)
    print("🚀 GO!\n")
    
    # Run the commands
    for cmd in commands:
        try:
            result = subprocess.run(cmd, shell=True, cwd=os.getcwd(), 
                                  capture_output=False, text=True)
            if result.returncode != 0:
                print(f"❌ Command failed: {cmd}")
        except Exception as e:
            print(f"❌ Error running command: {e}")
    
    print_section_separator()


def main():
    """Main demo runner function."""
    print_banner("PYTHON MODULES LESSON DEMO", "🎉")
    print("Welcome to the ultimate before/after coding transformation!")
    print("We'll show you the power of modular programming through")
    print("practical examples that don't completely bore you to death.")
    
    print("\n📚 What you'll see:")
    print("  1. Built-in modules showcase") 
    print("  2. Monolithic nightmare (the 'before')")
    print("  3. Modular masterpiece (the 'after')")
    print("  4. Side-by-side comparison")
    
    input("\n🎯 Press Enter to start the demo...")
    
    # Section 1: Built-in Modules
    run_demo_section(
        "BUILT-IN MODULES SHOWCASE",
        "See how Python's built-in modules solve real problems",
        ["python builtin_modules_demo.py"],
        wait_time=2
    )
    
    input("👀 Press Enter to continue to the nightmare...")
    
    # Section 2: The Nightmare
    print_banner("THE MONOLITHIC NIGHTMARE", "😱")
    print("📝 This is what happens when you put EVERYTHING in one file.")
    print("   It's like putting your entire life in one giant box and")
    print("   hoping you can find your socks when you need them.")
    print("\n🔍 Key problems with monolithic code:")
    print("   ❌ Hard to find specific functions")
    print("   ❌ One bug can break everything")
    print("   ❌ Impossible to reuse code")
    print("   ❌ Nightmare to maintain")
    print("   ❌ Team collaboration is chaos")
    
    print(f"\n📊 Nightmare stats:")
    
    # Get file stats
    nightmare_file = "before_modules/student_management_nightmare.py"
    if os.path.exists(nightmare_file):
        with open(nightmare_file, 'r') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        code_lines = len([line for line in lines if line.strip() and not line.strip().startswith('#')])
        comment_lines = len([line for line in lines if line.strip().startswith('#')])
        
        print(f"   📄 Total lines: {total_lines}")
        print(f"   💾 Code lines: {code_lines}")
        print(f"   💬 Comment lines: {comment_lines}")
        print(f"   😱 Functions: TOO MANY TO COUNT!")
    
    input("\n🎯 Press Enter to see the nightmare in action...")
    
    print("🏃‍♀️ Quick demo of the nightmare system:")
    print("   (We'll load sample data and show statistics)")
    print_section_separator()
    
    # Section 3: The Modular Solution
    input("✨ Press Enter to see the modular solution...")
    
    print_banner("THE MODULAR MASTERPIECE", "✨")
    print("📝 The same functionality, but organized like a responsible adult!")
    print("\n🎯 Modular benefits:")
    print("   ✅ Clear organization and separation of concerns")
    print("   ✅ Easy to find and fix bugs")
    print("   ✅ Code reuse across projects")
    print("   ✅ Team members can work on different modules")
    print("   ✅ Easy to test individual components")
    print("   ✅ Your future self won't hate you")
    
    # Get modular stats
    modular_files = [
        "after_modules/student_utils.py",
        "after_modules/grade_calculator.py", 
        "after_modules/social_media.py",
        "after_modules/student_management_system.py"
    ]
    
    print(f"\n📊 Modular stats:")
    total_modular_lines = 0
    
    for file_path in modular_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                lines = len(f.readlines())
            total_modular_lines += lines
            filename = os.path.basename(file_path)
            print(f"   📄 {filename}: {lines} lines")
    
    print(f"   📊 Total modular lines: {total_modular_lines}")
    print(f"   🎯 Number of modules: {len(modular_files)}")
    print(f"   ✨ Average lines per module: {total_modular_lines // len(modular_files)}")
    
    input("\n🎯 Press Enter to see the modular system in action...")
    
    print("🏃‍♀️ Quick demo of the modular system:")
    print("   (We'll load sample data and show statistics)")
    print_section_separator()
    
    # Section 4: Comparison
    input("📊 Press Enter for the final comparison...")
    
    print_banner("THE VERDICT", "⚖️")
    print("📊 Side-by-side comparison:")
    print("\n🔍 Code Organization:")
    print("   😱 Nightmare: Everything in one 400+ line file")
    print("   ✨ Modular: Organized into 4 focused modules")
    
    print("\n🐛 Bug Fixing:")
    print("   😱 Nightmare: Find the needle in the haystack")
    print("   ✨ Modular: Know exactly which module to check")
    
    print("\n🔄 Code Reuse:")
    print("   😱 Nightmare: Copy and paste chaos")
    print("   ✨ Modular: Import functions anywhere")
    
    print("\n👥 Team Work:")
    print("   😱 Nightmare: Merge conflicts and tears")
    print("   ✨ Modular: Different people, different modules")
    
    print("\n🧪 Testing:")
    print("   😱 Nightmare: Test everything or nothing")
    print("   ✨ Modular: Test individual components")
    
    print("\n🚀 Scalability:")
    print("   😱 Nightmare: Adding features breaks everything")
    print("   ✨ Modular: Add new modules without fear")
    
    print_banner("CONCLUSION", "🎓")
    print("🌟 Modular programming isn't just a best practice—")
    print("   it's a sanity preservation technique!")
    print("\n💡 Key takeaways:")
    print("   • Separate concerns into different modules")
    print("   • Use Python's built-in modules instead of reinventing")
    print("   • Import only what you need")
    print("   • Document your modules well")
    print("   • Your future self will thank you!")
    
    print("\n🎉 Congratulations! You've completed the modules lesson!")
    print("   Now go forth and modularize responsibly! 🚀")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Demo interrupted!")
        print("Thanks for checking out the modules lesson! 👋")
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")
        print("But hey, at least the error is contained! 🎭")