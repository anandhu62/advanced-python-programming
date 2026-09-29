import math

partners = [
    ["D101", "Rahul", (12, 11), 1, 8, 5, 10],
    ["D102", "Anu",   (9, 8),   1, 4, 4, 8],
    ["D103", "Kiran", (9, 8),   0, 4, 3, 6],
    ["D104", "John",  (11, 9),  1, 2, 5, 4]
]

restaurant = (6, 7)

best = None

for p in partners:

    partner_id = p[0]
    location = p[2]
    status = p[3]
    deliveries = p[4]
    rating = p[5]
    idle_time = p[6]

 
    if status == 0:
        continue

    x1, y1 = restaurant
    x2, y2 = location

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if best is None:
        best = p
        best_distance = distance

    else:

        best_deliveries = best[4]
        best_rating = best[5]

        # Rule 1: Fewest deliveries
        if deliveries < best_deliveries:
            best = p
            best_distance = distance

        # Rule 2: Highest rating
        elif deliveries == best_deliveries and rating > best_rating:
            best = p
            best_distance = distance

        # Rule 3: Nearest
        elif (deliveries == best_deliveries and
              rating == best_rating and
              distance < best_distance):
            best = p
            best_distance = distance

        # Rule 4: Longest idle time
        elif (deliveries == best_deliveries and
              rating == best_rating and
              distance == best_distance and
              idle_time > best[6]):
            best = p
            best_distance = distance


if best is not None:

    # Update status to Busy
    best[3] = 0

    # Increment deliveries
    best[4] += 1

    print("Delivery Assigned to", best[0])

else:
    print("All delivery partners are busy. Order added to waiting queue.")