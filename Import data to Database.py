import psycopg2
import csv

# PostgreSQL connection parameters
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='DSE',
    user='postgres',
    password='amimobin0000'
)

# CSV file paths
company_data = r'C:\Users\DELL\Desktop\Practices\company_data.csv'
other_info_data = r'C:\Users\DELL\Desktop\Practices\other_info_data.csv'

try:
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Create table
    cur.execute("""
        CREATE TABLE company_data (
            Company_ID VARCHAR,
            Company_Name VARCHAR,
            Sectors VARCHAR,
            Trading_Codes VARCHAR,
            Scrip_Codes VARCHAR,
            Websites VARCHAR,
            Urls VARCHAR
        )
    """)

    # Open the CSV file
    with open(company_data, 'r') as file:
        # Create a CSV reader object
        csv_data_1 = csv.reader(file)

        # Skip the header row if necessary
        next(csv_data_1)

        # Import each row from the CSV file
        for row in csv_data_1:
            cur.execute(
                "INSERT INTO company_data (Company_ID, Company_Name, Sectors, Trading_Codes, Scrip_Codes, Websites, Urls) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            )

    # Commit the changes to the database
    conn.commit()

    cur.execute("""
        CREATE TABLE other_info_data (
            Company_ID VARCHAR,
            Date DATE,
            Sponsor NUMERIC,
            Govt NUMERIC,
            Institute NUMERIC,
            Foreign NUMERIC,
            Public NUMERIC
        )
    """)

    # Open the CSV file
    with open(other_info_data, 'r') as file:
        # Create a CSV reader object
        csv_data_2 = csv.reader(file)

        # Skip the header row if necessary
        next(csv_data_2)

        # Import each row from the CSV file
        for row in csv_data_2:
            cur.execute(
                "INSERT INTO other_info_data (Company_ID, Date, Sponsor, Govt, Institute, Foreign, Public) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            )


    # Commit the changes to the database
    conn.commit()

    # Print a success message
    print("CSV files imported into PostgreSQL successfully!")

except (Exception, psycopg2.Error) as error:
    # Print an error message if the import fails
    print("Error while importing CSV files into PostgreSQL:", error)

finally:
    # Close the cursor and connection
    cur.close()
    conn.close()
