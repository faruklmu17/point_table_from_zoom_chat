def create_points_table(text):
    lines = text.split('\n')
    user_points = {}  # Dictionary to store points for each user
    
    for line in lines:
        # Check if the line contains the expected pattern
        if " From " in line and " to Everyone:" in line:
            # Extract the username
            username = line.split(" From ")[1].split(" to Everyone:")[0]
            
            # Exclude "Faruk Hasan"
            if username != "Faruk Hasan":
                # Increment the points for the username
                user_points[username] = user_points.get(username, 0) + 1
    
    return user_points  # Return the cumulative points dictionary

# Read the chat file
with open('meeting_saved_chat.txt', 'r') as file:
    text_content = file.read()

# Get the cumulative points table
points_table = create_points_table(text_content)

# Display the results
print("Cumulative Points Table:")
print("-" * 30)
for user, points in sorted(points_table.items(), key=lambda x: x[1], reverse=True):
    print(f"{user}: {points}")
