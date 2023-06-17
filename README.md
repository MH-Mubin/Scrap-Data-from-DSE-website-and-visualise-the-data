**Task list:** <br>
Scrape data from DSE website using beautiful soup:<br>
Scrape CODE from https://dsebd.org/company_listing.php <br>
Company list page: https://dsebd.org/displayCompany.php?name={CODE}<br>
Information required to scrape and clean:<br>
			Company name, Trading code, Scrip code, Other Information of the
Company [Month wise]<br>
Run the script daily at 5PM to get updated information<br>
Save data in PostgreSQL database<br>
Build API<br>
Create BI dashboard with POWER BI or Streamlit<br>
Create a github repo and share with your instructor<br>


There are two different codes for the task. First code scrap the data from DSE website and save the data to csv file, and second code import the data to PostgreSQL Database.

**First part of the Documentation for scrap the data from DSE website and save the data to csv file**

**Description:** This function scrapes data from the DSE (Dhaka Stock Exchange) website, processes the data, and saves it to CSV files. It utilizes the BeautifulSoup library for web scraping and the pandas library for data manipulation.

**Step 1:** Scraping data from the DSE website: The function sends an HTTP request to the DSE website and retrieves the HTML content of the page. It uses BeautifulSoup to parse the HTML and extract relevant information from the web page.

**Step 2:** Processing and extracting relevant information: The function performs various operations on the scraped data to extract the required information. It finds trading codes, generates unique IDs, extracts scrip codes, URLs, sectors, websites, and other information of the companies listed on the DSE website.

**Step 3:** Converting data into pandas DataFrames: The extracted data is organized into a dictionary format, which is then converted into pandas DataFrames using the pd.DataFrame.from_dict() method. Multiple DataFrames are created for different sets of data.

**Step 4:** Saving the DataFrames to CSV files: The pandas DataFrames are saved as CSV files using the to_csv() method. The CSV files, namely company_data.csv and other_info_data.csv, are generated in the current working directory.

**Calling the datasets function:** The last line of code calls the datasets() function to execute the code and perform the data scraping, processing, and CSV file generation.

**Second part of the Documentation for import those csv files to PostgreSQL database**

**Description:** This code snippet demonstrates how to import data from a CSV file into a PostgreSQL database table using the psycopg2 library.

**PostgreSQL Connection:** The code establishes a connection to a PostgreSQL database using the specified connection parameters (host, port, database, user, password).

**CSV File:** The csv_file variable contains the file path of the CSV file to be imported. Make sure to provide the correct file path.

**Table Creation:** The code creates two tables named company_data and other_info_data in the PostgreSQL database. Both tables has seven columns matching the structure of the CSV file.

**CSV Import:** The code reads the CSV files using the csv.reader object. It skips the header row and imports each row of data into the company_data table and other_info_data using the INSERT statement.

**Commit and Close:** After importing the data, the code commits the changes to the database and closes the cursor.

**Error Handling:** If an exception occurs during the import process, an error message is printed.
