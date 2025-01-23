    lines = text.split('\n')
    
    for line in lines:
        if " From " in line and " to Everyone:" in line:
            username = line.split(" From ")[1].split(" to Everyone:")[0]
            
            # Exclude Faruk Hasan
            if username != "Faruk Hasan":
                user_points[username] = user_points.get(username, 0) + 1
                
                current_points = user_points.copy()
                points_history.append((line, current_points))
    
    return points_history

with open('paste.txt', 'r') as file:
    text_content = file.read()

points_table = create_points_table(text_content)

print("Cumulative Points Table:")
print("-" * 50)
for entry in points_table:
    message, points = entry
    sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
    points_str = " | ".join([f"{user}: {count}" for user, count in sorted_points])
    print(f"{message} | {points_str}")
