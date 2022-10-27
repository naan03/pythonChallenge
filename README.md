
How to run the project?

Task1:
1. Create your virtualenv and activate your virtualenv install all libs from requirements.txt by below command.

pip install -r requirements.txt

2. Switch to the project directory and modify the column_data value in the config.json, follow the format below.

column_name:column_type, column_name:column_type, column_name:column_type
[N.B: Only integer and string are suppored at the moment.]

3. Switch to the task1 directory and execute the command below, and you will get a file at your output_path.

python3 gen.py -o output_path -r rows

4. To run unit tests, switch to the test directory and execute the command python3 task1test.py.
   Or open the task1test.py, right-click and select Execute Unit Test.
   After the test, please manually check if the csv files exist, and the content is correct.


Task2:

Introduction:
This project is based on flask, postgre. 
POST request could split the string into sub-strings of a specified length, and asynchronously write to a CSV file 
through multi-threading. 
GET request could get a mock data. 
db_init.py is for init the db, create tables and insert some rows. db.py defines the database connection, 
models.py maps the table structure to objects.


1. Create your virtualenv and activate your virtualenv install all libs from requirements.txt by below command.

pip install -r requirements.txt 

2. Now create .env file in your root directory and add bellow text or strings.

ALLOWED_HOSTS=*,127.0.0.1,
DATABASE_NAME=<your database name>
DATABASE_USERNAME=<your database username>
DATABASE_PASSWORD=<your datababse password>
DATABASE_HOST=<your database host>
DATABASE_PORT=5432

3. After DB setup you need to run below command for creating tables in your DB. 

python db_init.py

Don't forget to activate your virtualenv and also this command will work in your project root directory.

4. Set the size of chuck string, open config.json, parameter chuck_size is the length of the chuck string.
   The number of threads that asynchronously write file is defined in api.py, line 11, executor = ThreadPoolExecutor(10)
   you can change it. The output file is in outputs folder.

5. Switch to the task1 directory and execute the command python3 api.py

6. Open the browser and enter the address http://127.0.0.1:5000/file, and you will get a sample data.

7. If you want to try POST requests, you need to install Postman, or similar software first. Then sand a POST request 
   with parameter file_data to URL http://127.0.0.1:5000/file.

Improvement
1. I tried to complete all database modules, however, I haven't use prostgre and its related frameworks. Hence, 
retrieving data from the database still has some issue, I've commented out the relevant code for now.
   
2. The unit tests are not complete, I tried mocking the client to make a POST request, but it doesn't works. Hence,
I tested api.py by postman.



