# Backend_Developer_Assignment
The rest API is a Django-based application designed to find the occurrence of words in various paragraphs stored in a PostgreSQL database. This API allows users to input text, and it outputs the paragraphs in which the input text has been found.

 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sachitrao2002/Backend_Developer_Assignment.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

Usage
To use the Arrest API, send HTTP requests to the specified endpoints (see [API Endpoints](#api-endpoints)) with the required parameters. 


API Endpoints

1.GET /search/: Search for the input text in paragraphs and gives a list of paragraphs as output where the input text occurence was found.

Example:
{
   "text":"Maecenas"
}

2.POST/insert/: inserts single/multiple paragraphs given by the user into the PostgreSQL database

Example:
{
    "paragraph":" Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat inegestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eutincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id enenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consecteturlorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id."
}

(if you want to enter multiple paragraphs make sure to leave two blank spaces seperating the two paragraphs)

{

"paragraph":"he is one the most fearless person i have ever seen ,i need to develop confidence like him  he is also a good human by nature"
}

(here we can see that paragraph 1 ie "he is one the most fearless person i have ever seen ,i need to develop confidence like him" and paragraph 2 ie "he is also a good human by nature are sepearated by two blank spaces".)

Database Setup
The project uses PostgreSQL as its database. Make sure to update the database configuration in the settings.py file. You can use the following commands to set up your PostgreSQL database:

# Create a new database
createdb user_data

# Run database migrations
python manage.py migrate

# To run the server
python manage.py runserver




