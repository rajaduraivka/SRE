import psycopg2

def update_earnings(conn, cursor, user_id, amount):
    # Construct the SELECT query to fetch current earnings
    select_query = """
        SELECT total_earned, redeem_amount
        FROM earnings
        WHERE user_id = %s;
    """

    # Execute the query
    cursor.execute(select_query, (user_id,))
    earnings = cursor.fetchone()

    if earnings is not None:
        total_earned, redeem_amount = earnings
        print(f"Current earnings for user ID {user_id}:")
        print(f"Total earned: {total_earned}")
        print(f"Redeem amount: {redeem_amount}")

        # Construct the UPDATE query
        update_query = """
            UPDATE earnings
            SET total_earned = total_earned - %s, redeem_amount = redeem_amount - %s
            WHERE user_id = %s;
        """

        # Execute the update query
        cursor.execute(update_query, (amount, amount, user_id))

        # Commit the changes
        conn.commit()

        print("Earnings updated successfully!")
    else:
        print(f"No earnings found for user ID {user_id}")

# Connect to the database
try:
    connection = psycopg2.connect(
        dbname="redeem_service_db",
        user="bijakpg_prod",
        password="JDEvnndNXn_PRODDB",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()

    # Get user input
    user_id = input("Enter user ID: ")
    amount = float(input("Enter amount to subtract: "))  # Assuming amount is a float

    # Call the function to update earnings
    update_earnings(connection, cursor, user_id, amount)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
