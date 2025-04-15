# main.py
import importlib

def run_extractor(module_name):
    try:
        extractor = importlib.import_module(module_name)
        video_url = input("Enter the YouTube video URL: ")
        
        # Run the correct function based on module
        if module_name == "extract_views":
            extractor.extract_views(video_url)
        elif module_name == "extract_likes":
            extractor.extract_likes(video_url)
        elif module_name == "extract_comments":
            extractor.extract_comments(video_url)
        else:
            print("Unknown extractor.")
    except ImportError:
        print(f"❌ Could not load module: {module_name}")

if __name__ == "__main__":
    print("Select what you want to track:")
    print("1. Views")
    print("2. Likes")
    print("3. Comments")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        run_extractor("extract_views")
    elif choice == "2":
        run_extractor("extract_likes")
    elif choice == "3":
        run_extractor("extract_comments")
    else:
        print("❌ Invalid choice.")
