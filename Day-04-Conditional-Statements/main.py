# AI Tool Recommendation System

print("Choose your task:")
print("1. Coding\n2. Research\n3. Image Generation\n4. Presentation")

choice = int(input("Enter your Choice: "))

if choice == 1:
    print("Claude")
elif choice == 2:
    print("Perplexity")
elif choice == 3:
    print("Midjourney")
elif choice == 4:
    print("Gamma")
else:
    print("Invalid choice")
