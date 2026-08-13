import math


# ---------------------------------------------------------
# Calculate distance between restaurant and delivery partner
# ---------------------------------------------------------

def calculate_distance(partner_x, partner_y, restaurant_x, restaurant_y):

    distance = math.sqrt(
        (partner_x - restaurant_x) ** 2 +
        (partner_y - restaurant_y) ** 2
    )

    return distance


# ---------------------------------------------------------
# Find the best delivery partner
# ---------------------------------------------------------

def find_best_partner(partners, restaurant_x, restaurant_y):

    best_partner = None
    best_distance = float("inf")

    for partner in partners:

        # Rule 1: Only available partners are eligible
        if partner["status"] != 1:
            continue

        distance = calculate_distance(
            partner["x"],
            partner["y"],
            restaurant_x,
            restaurant_y
        )

        # If this is the first available partner
        if best_partner is None:

            best_partner = partner
            best_distance = distance

        else:

            # Current best partner information
            best_deliveries = best_partner["deliveries"]
            best_rating = best_partner["rating"]
            best_idle = best_partner["idle"]

            current_deliveries = partner["deliveries"]
            current_rating = partner["rating"]
            current_idle = partner["idle"]

            # ------------------------------------------------
            # Rule 2: Fewest deliveries
            # ------------------------------------------------

            if current_deliveries < best_deliveries:

                best_partner = partner
                best_distance = distance

            # ------------------------------------------------
            # Rule 3: Highest rating
            # ------------------------------------------------

            elif current_deliveries == best_deliveries:

                if current_rating > best_rating:

                    best_partner = partner
                    best_distance = distance

                # --------------------------------------------
                # Rule 4: Nearest partner
                # --------------------------------------------

                elif current_rating == best_rating:

                    if distance < best_distance:

                        best_partner = partner
                        best_distance = distance

                    # ----------------------------------------
                    # Rule 5: Longest idle time
                    # ----------------------------------------

                    elif distance == best_distance:

                        if current_idle > best_idle:

                            best_partner = partner
                            best_distance = distance

    return best_partner, best_distance


# =========================================================
# MAIN PROGRAM
# =========================================================

print("=" * 55)
print("       ONLINE FOOD DELIVERY SYSTEM")
print("=" * 55)


# ---------------------------------------------------------
# Restaurant location
# ---------------------------------------------------------

print("\nEnter Restaurant Location")

restaurant_x = float(input("Restaurant X: "))
restaurant_y = float(input("Restaurant Y: "))


# ---------------------------------------------------------
# Number of delivery partners
# ---------------------------------------------------------

n = int(input("\nEnter number of delivery partners: "))

partners = []


# ---------------------------------------------------------
# Get delivery partner details
# ---------------------------------------------------------

for i in range(n):

    print("\n" + "-" * 40)
    print("Delivery Partner", i + 1)
    print("-" * 40)

    partner_id = input("Partner ID: ")
    name = input("Name: ")

    x = float(input("Location X: "))
    y = float(input("Location Y: "))

    print("\nStatus:")
    print("1 - Available")
    print("0 - Busy")

    status = int(input("Enter status: "))

    deliveries = int(
        input("Deliveries completed today: ")
    )

    rating = float(
        input("Customer rating: ")
    )

    idle = int(
        input("Idle time (minutes): ")
    )

    partner = {
        "id": partner_id,
        "name": name,
        "x": x,
        "y": y,
        "status": status,
        "deliveries": deliveries,
        "rating": rating,
        "idle": idle
    }

    partners.append(partner)


# ---------------------------------------------------------
# Find best partner
# ---------------------------------------------------------

best_partner, best_distance = find_best_partner(
    partners,
    restaurant_x,
    restaurant_y
)


# ---------------------------------------------------------
# Display result
# ---------------------------------------------------------

print("\n" + "=" * 55)
print("                 RESULT")
print("=" * 55)


if best_partner is None:

    print("\n❌ All delivery partners are busy.")
    print("The order has been added to the waiting queue.")

else:

    print(
        "\n✅ Delivery Assigned to:",
        best_partner["id"]
    )

    print(
        "Name:",
        best_partner["name"]
    )

    print(
        "Distance:",
        round(best_distance, 2)
    )

    print(
        "Deliveries before assignment:",
        best_partner["deliveries"]
    )

    print(
        "Rating:",
        best_partner["rating"]
    )

    # -----------------------------------------------------
    # Update partner after assignment
    # -----------------------------------------------------

    best_partner["status"] = 0

    best_partner["deliveries"] += 1

    best_partner["idle"] = 0

    print("\nUpdated Partner Information")
    print("--------------------------------")
    print("Status: Busy")
    print(
        "Deliveries completed today:",
        best_partner["deliveries"]
    )