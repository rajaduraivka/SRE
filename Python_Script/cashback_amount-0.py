import psycopg2

def print_current_cashback(conn, cursor, record_id):
    # Construct the SELECT query
    select_query = """
        SELECT cashback_amount
        FROM cashback_record
        WHERE payment_id = %s;
    """

    # Execute the query
    cursor.execute(select_query, (record_id,))

    # Fetch the result
    cashback_amount = cursor.fetchone()

    # Check if a result was returned
    if cashback_amount is not None:
        # Print the current cashback amount
        print(f"Current cashback amount for PAYMENT ID {record_id}: {cashback_amount[0]}")
    else:
        print(f"No record found for PAYMENT ID {record_id}")

def print_current_cashback(conn, cursor, record_id):
    # Construct the SELECT query
    select_query = """
        SELECT user_id
        FROM cashback_record
        WHERE payment_id = %s;
    """

    # Execute the query
    cursor.execute(select_query, (record_id,))

    # Fetch the result
    user_id = cursor.fetchone()

    # Check if a result was returned
    if user_id is not None:
        # Print the current user ID
        print(f"User ID for PAYMENT ID {record_id}: {user_id[0]}")
    else:
        print(f"No record found for PAYMENT ID {record_id}")

def update_record(conn, cursor, record_id):
    # Construct the UPDATE query
    update_query = """
        UPDATE cashback_record
        SET cashback_amount = '0', reason = 'cashback made 0 to avoid double cashback' 
        WHERE payment_id = %s AND status = 'approved';
    """

    # Execute the query
    cursor.execute(update_query, (record_id,))

    # Commit the changes
    conn.commit()

try:
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="cashback",
        user="bijakpg_prod",
        password="JDEvnndNXn_PRODDB",
        host="localhost",
        port="5432"
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Get the payment id of the record you want to update
    record_id = input("Enter the Payment ID of the record you want to update: ")

    # Call the function to print the current cashback amount
    print_current_cashback(conn, cursor, record_id)

    # Display the proposed changes using f-strings
    print(f"Proposed changes:\nPAYMENT ID: {record_id}\ncashback_amount: 0\nreason: cashback made 0 to avoid double cashback")

    # Ask for confirmation
    confirmation = input("Do you want to proceed with the update? (y/n): ")

    if confirmation.lower() == 'y':
        update_record(conn, cursor, record_id)
        print("Record updated successfully.")
    else:
        print("Update operation cancelled.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
