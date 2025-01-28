import psycopg2

def update_database():
    # Database connection parameters
    conn_params = {
        'dbname': 'bijak',
        'user': 'bijak_db_user',
        'password': 'f}DF8Au~bh',
        'host': 'localhost',
        'port' : "5427"
    }
    
    # Create a connection to the database
    conn = psycopg2.connect(**conn_params)
    
    try:
        # Cursor to perform database operations
        with conn.cursor() as cursor:
            # SQL Update Query
            sql_update_query = """
                UPDATE public.account_user
                SET auto_cashback = 'f', 
                    auto_cashback_eligible = '{"online": false, "advance": false}'
                WHERE auto_cashback = 't';
            """
            # Execute the SQL UPDATE statement
            cursor.execute(sql_update_query)
            # Commit changes
            conn.commit()
            
            # Print the number of rows updated
            print(f"Update successful. Rows affected: {cursor.rowcount}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback on error
    
    finally:
        if conn is not None:
            conn.close()  # Close the database connection

if __name__ == '__main__':
    update_database()
