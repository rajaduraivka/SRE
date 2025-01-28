import psycopg2

def update_record(conn, cursor, record_id, new_value1):
    # Assuming you have a table named 'your_table' with columns 'column1', and 'id'
    # Replace these with your actual table and column names

    # Construct the UPDATE query
    update_query = """
        UPDATE orders_bankdetail
        SET redeem_eligible = %s
        WHERE id = %s;
    """

    # Execute the query
    cursor.execute(update_query, (new_value1, record_id))

    # Commit the changes
    conn.commit()

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="bijak",
    user="bijak_db_user",
    password="f}DF8Au~bh",
    host="localhost",
    port="5427"
)

# Create a cursor object
cursor = conn.cursor()

try:
    # Get the ID of the record you want to update
    record_id = int(input("Enter the ID of the record you want to update: "))

    # Get the new values from the user
    new_value1 = input("Enter here as t if you want to update this ID to be redeem_eligible: ")

    # Display the proposed changes
    print(f"Proposed changes:\nID: {record_id}\nredeem_eligible: {new_value1}")

    # Ask for confirmation
    confirmation = input("Do you want to proceed with the update? (y/n): ")

    if confirmation.lower() == 'y':
        update_record(conn, cursor, record_id, new_value1)
        print("Record updated successfully.")
    else:
        print("Update operation cancelled.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()

