# Instagram Hashtag Finder
# Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan

import re
from itertools import combinations

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════╗
    ║       Instagram Hashtag Finder v1.0                ║
    ║   Coded by Pakistani Ethical Hacker                 ║
    ║          Mr Sabaz Ali Khan                         ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """
    print(banner)

def clean_keyword(keyword):
    """Clean and normalize the input keyword."""
    keyword = re.sub(r'[^a-zA-Z0-9\s]', '', keyword.lower()).strip()
    return keyword.replace(' ', '')

def generate_hashtags(keyword):
    """Generate related hashtags based on the keyword."""
    cleaned_keyword = clean_keyword(keyword)
    if not cleaned_keyword:
        return []
    
    # Base hashtag
    hashtags = [f"#{cleaned_keyword}"]
    
    # Split keyword into words if it contains spaces in original input
    words = keyword.lower().split()
    
    # Generate variations
    for word in words:
        cleaned_word = clean_keyword(word)
        if cleaned_word:
            hashtags.append(f"#{cleaned_word}")
    
    # Generate combinations of words
    if len(words) > 1:
        for i in range(2, len(words) + 1):
            for combo in combinations(words, i):
                combo_keyword = ''.join(combo)
                cleaned_combo = clean_keyword(combo_keyword)
                if cleaned_combo:
                    hashtags.append(f"#{cleaned_combo}")
    
    # Add popular suffixes
    suffixes = ['love', 'style', 'life', 'trending', 'vibes', 'daily', 'insta']
    for suffix in suffixes:
        hashtags.append(f"#{cleaned_keyword}{suffix}")
    
    # Remove duplicates and limit to 30 hashtags (Instagram's limit)
    hashtags = list(dict.fromkeys(hashtags))[:30]
    return hashtags

def main():
    print_banner()
    print("Welcome to Instagram Hashtag Finder!")
    print("Enter a keyword to generate related hashtags.")
    print("Type 'exit' to quit.\n")
    
    while True:
        keyword = input("Enter keyword (e.g., 'digital marketing'): ")
        if keyword.lower() == 'exit':
            print("Thank you for using Instagram Hashtag Finder!")
            break
        
        hashtags = generate_hashtags(keyword)
        if not hashtags:
            print("Invalid input. Please enter a valid keyword.\n")
            continue
        
        print("\nGenerated Hashtags:")
        print("==================")
        for i, hashtag in enumerate(hashtags, 1):
            print(f"{i}. {hashtag}")
        print(f"\nTotal: {len(hashtags)} hashtags")
        print("Copy and paste these hashtags to your Instagram post!\n")

if __name__ == "__main__":
    main()