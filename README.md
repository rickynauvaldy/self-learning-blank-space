# self-learning-blank-space

# Description
This code compile JSON files of movie data into one JSON output.

It illustrate a data engineering task that need to store the data gathered by software engineering team in JSON format in a data warehouse, but the JSON files are not clean enough as it contains some nested JSON that needed to be processed first. The data is extracted and cleaned from JSON files into a huge JSON file.

# Prerequisites
- List of requirements are available in the `requirements.txt` and can be installed by running `pip install -r requirements.txt`

# Data
Examples of 100 JSON files that need to be compiled are available in the resources folder.

One of it sample data looks like the following:

{
<br>  "adult": false,
<br>  "backdrop_path": "/kpuTCMw3v2AuKjqGS7383uWbc8V.jpg",
<br>  "belongs_to_collection": null,
<br>  "budget": 0,
<br>  "genres": [
<br>    {
<br>      "id": 18,
<br>      "name": "Drama"
<br>    },
<br>    {
<br>      "id": 80,
<br>      "name": "Crime"
<br>    },
<br>    {
<br>      "id": 35,
<br>      "name": "Comedy"
<br>    }
<br>  ],
<br>  "homepage": "",
<br>  "id": 2,
<br>  "imdb_id": "tt0094675",
<br>  "original_language": "fi",
<br>  "original_title": "Ariel",
<br>  "overview": "Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don't go as planned...",
<br>  "popularity": 10.764,
<br>  "poster_path": "/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg",
<br>  "production_companies": [
<br>    {
<br>      "id": 2303,
<br>      "logo_path": null,
<br>      "name": "Villealfa Filmproductions",
<br>      "origin_country": "FI"
<br>    }
<br>  ],
<br>  "production_countries": [
<br>    {
<br>      "iso_3166_1": "FI",
<br>      "name": "Finland"
<br>    }
<br>  ],
<br>  "release_date": "1988-10-21",
<br>  "revenue": 0,
<br>  "runtime": 73,
<br>  "spoken_languages": [
<br>    {
<br>      "iso_639_1": "fi",
<br>      "name": "suomi"
<br>    },
<br>    {
<br>      "iso_639_1": "de",
<br>      "name": "Deutsch"
<br>    }
<br>  ],
<br>  "status": "Released",
<br>  "tagline": "",
<br>  "title": "Ariel",
<br>  "video": false,
<br>  "vote_average": 6.8,
<br>  "vote_count": 105
<br>}

The desired output looks like the following:

{
<br>"original_title": "Lock, Stock and Two Smoking Barrels",
<br>"budget": 1350000,
<br>"genres": "Comedy, Crime",
<br>"popularity": 7119,
<br>"release_date": "1998-03-05",
<br>"revenue": 28356188,
<br>"runtime": 105,
<br>"vote_average": 8.2,
<br>"vote_count": 4048,
<br>"spoken_languages": "English"
<br>},
{
<br>"original_title": "Verfolgt",
<br>"budget": 0,
<br>"genres": "Drama",
<br>"popularity": 5331,
<br>"release_date": "2006-08-06",
<br>"revenue": 0,
<br>"runtime": 87,
<br>"vote_average": 4.9,
<br>"vote_count": 11,
<br>"spoken_languages": "Deutsch"
<br>}

# Flow
- Import required modules
- define `concat_name` function for further use in transforming nested JSON to a comma seperated value
- Set data_path to match your resources folder
- get all filenames
- for each filename, `json.load()` the row and append to a list
- Progress print is available per `counter` rows
- `genres` and `spoken_languages` column is transformed using the `concat_name` function
- Transform the dataframe into json
- Dump the data into a file

# Running the Program
- Make sure that all the prerequisites are satisfied
- Configure the `data_path` to match your resources folder, i.e. the folder of the JSON files
- Run the program by running this script `python main.py`

# Notes
- Compiled data is not cleaned enough as the author notices some empty value in "spoken_languages" key
- As the JSON files that need to be processed consist of 500,000+ files, it took a long time to finish
- Unicode character is stored as the unicode (e.g. Espa\u00f1ol in Espanol)
- This code is made as a Self-Learning Module Part 1 to Academi by blank-space Data Engineering Track (https://www.blank-space.io/program)

# Contact
For further information, you might want to reach me to ricky.nauvaldy@gmail.com