import random

def generate_random_words(word_list, num_words):
    return random.sample(word_list, min(num_words, len(word_list)))

def main():
    words = [
    "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon",
    "Mango", "Nectarine", "Orange", "Pear", "Quince", "Raspberry", "Strawberry", "Tangerine", "Ugli", "Vanilla",
    "Watermelon", "Xigua", "Yam", "Zucchini", "Abandon", "Ability", "Absence", "Academy", "Accept", "Accuse",
    "Achieve", "Acquire", "Address", "Advance", "Afraid", "Agency", "Airport", "Allege", "Amazing", "Ancient",
    "Animal", "Balance", "Benefit", "Beyond", "Bottle", "Branch", "Brought", "Calculate", "Capture", "Celebrate",
    "Channel", "Command", "Complain", "Concept", "Conduct", "Create", "Damage", "Decent", "Decrease", "Demand",
    "Detailed", "Difficult", "Discuss", "Driver", "Economy", "Element", "Emerge", "Enough", "Ensure", "Excited",
    "Expect", "Familiar", "Fashion", "Feature", "Fellow", "Finish", "Foreign", "Fragile", "Freedom", "Garden",
    "Genuine", "Gravity", "Growth", "Happen", "History", "Impact", "Improve", "Increase", "Inspire", "Invest",
    "Journey", "Justify", "Kitchen", "Knowledge", "Label", "Library", "Listen", "Manage", "Market", "Modern",
    "Notice", "Obtain", "Option", "Organize", "Package", "Parent", "Pattern", "Perform", "Possible", "Project",
    "Protect", "Purpose", "Quality", "Rebuild", "Reason", "Refresh", "Regret", "Remain", "Result", "Safety",
    "Science", "Secure", "Social", "Society", "Spirit", "Sponsor", "Spread", "Symbol", "System", "Teacher",
    "Trouble", "Unique", "Value", "Various", "Vision", "Volume", "Wonder", "Achieve", "Advice", "Adjust",
    "Alcohol", "Answer", "Appeal", "Aspect", "Attempt", "Author", "Backward", "Bargain", "Benefit", "Biological",
    "Bizarre", "Breakfast", "Capture", "Courage", "Decision", "Disease", "Doubt", "Eclipse", "Effort", "Enigma",
    "Example", "Famous", "Further", "Gesture", "Hero", "Improve", "Invention", "Jealous", "Journey", "Justify",
    "Knowledge", "Leisure", "Library", "Meaning", "Mislead", "Natural", "Obvious", "Original", "Poverty", "Present",
    "Quality", "Random", "Rely", "Search", "Sensitive", "Shortage", "Support", "Technique", "Understand", "Validate",
    "Vivid", "Wisdom", "Xenon", "Youth", "Zodiac", "Access", "Agriculture", "Appetite", "Aspire", "Attract",
    "Balance", "Behavior", "Breathe", "Briefly", "Climate", "Clothing", "Compact", "Conflict", "Consider", "Contract",
    "Contrast", "Creative", "Decide", "Define", "Demand", "Dynamic", "Embrace", "Ensure", "Enrich", "Example",
    "Exercise", "Frequent", "Horizon", "Include", "Inspire", "Intent", "Locate", "Maintain", "Natural", "Observe",
    "Option", "Partner", "Project", "Quality", "Recycle", "Revisit", "Succeed", "Support", "Suspend", "Transfer",
    "Trust", "Uncover", "Validate", "Venture", "Wander", "Write", "Abnormal", "Atmosphere", "Barrier", "Bravery",
    "Broadcast", "Capture", "Courage", "Delegate", "Diameter", "Diploma", "Engineer", "Facility", "Finance",
    "Friendship", "Genuine", "History", "Innovate", "Journal", "Kingdom", "Latitude", "Lifestyle", "Manipulate",
    "Maturity", "Navigate", "Neutron", "Obstacle", "Paradigm", "Popular", "Priority", "Relevant", "Serenity",
    "Sophisticate", "Strategy", "Technology", "Translate", "Universal", "Vocabulary", "Weigh", "Wellness", "Workshop",
    "Yesterday", "Zeal", "Agency", "Apology", "Attach", "Balance", "Beyond", "Card", "Courage", "Decent", "Effort",
    "Embrace", "Famous", "Fragile", "Growth", "Honor", "Impact", "Index", "Library", "Motive", "Noble", "Offer",
    "Principle", "Return", "Succeed", "Trust", "Value", "Warmth", "Youth", "Account", "Adventure", "Assess", "Bargain",
    "Capital", "Certain", "Complete", "Concept", "Conflict", "Constant", "Creative", "Cultural", "Decade", "Define",
    "Deliver", "Digital", "Eclipse", "Enjoy", "Evaluate", "Feature", "Finance", "Forgive", "Frequent", "Generate",
    "Global", "Ground", "Impact", "Industry", "Inspire", "Integrate", "Maintain", "Major", "Moment", "Network",
    "Obvious", "Outcome", "Pattern", "Personal", "Produce", "Process", "Project", "Purpose", "Quality", "Realize",
    "Response", "Sensitive", "Significant", "Strategy", "Structure", "Succeed", "Support", "Technology", "Understand",
    "Value", "Vivid", "Witness", "Wonder", "Annual", "Approach", "Beauty", "Bless", "Briefly", "Captive", "Classify",
    "Concept", "Contrast", "Detailed", "Develop", "Direct", "Dynamic", "Evaluate", "Exception", "Exchange", "Explore",
    "Express", "Fashion", "Favorable", "Frequent", "Handle", "Involve", "Journey", "Maintain", "Natural", "Normal",
    "Package", "Revisit", "Succeed", "System", "Transmit", "Unique", "Vacation", "Volunteer", "Accept", "Apparent",
    "Benefit", "Capacity", "Challenge", "Confirm", "Defense", "Detailed", "Duration", "Elevate", "Engage", "Exact",
    "Failure", "Feature", "Focus", "Generate", "Inform", "Interest", "Legend", "Manage", "Minimum", "Network", "Option",
    "Platform", "Present", "Revisit", "Science", "Service", "Similar", "Support", "Suspend", "Theory", "Update",
    "Virtue", "Vivid", "Witness"
    ]
    
    print("=====================")
    print("Random Word Generator")
    print("=====================")
    
    while True:
        user_input = input("How many words would you like to generate: ")
        
        if user_input.isdigit():
            num_words = int(user_input)
            if num_words > 0:
                break 
            else:
                print("Please enter a positive number.")
        else:
            print("Invalid input. Please enter a number.")
    
    random_words = generate_random_words(words, num_words)
    print(f"Generated words: {', '.join(random_words)}")

if __name__ == "__main__":
    main()
    