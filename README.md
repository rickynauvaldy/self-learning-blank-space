# self-learning-blank-space

# Description
This code compile JSON files of movie data into one JSON output.

It illustrate a data engineering task that need to store the data gathered by software engineering team in JSON format in a data warehouse, but the JSON files are not clean enough as it contains some nested JSON that needed to be processed first. The data is extracted and cleaned from JSON files into a huge JSON file.

# Prerequisites
- List of requirements are available in the `requirements.txt` and can be installed by running `pip install -r requirements.txt`

# Data
Examples of 100 JSON files that need to be compiled are available in the resources folder.

One of it sample data looks like the following:

```
{
  "adult": false,
  "backdrop_path": "/kpuTCMw3v2AuKjqGS7383uWbc8V.jpg",
  "belongs_to_collection": null,
  "budget": 0,
  "genres": [
    {
      "id": 18,
      "name": "Drama"
    },
    {
      "id": 80,
      "name": "Crime"
    },
    {
      "id": 35,
      "name": "Comedy"
    }
  ],
  "homepage": "",
  "id": 2,
  "imdb_id": "tt0094675",
  "original_language": "fi",
  "original_title": "Ariel",
  "overview": "Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don't go as planned...",
  "popularity": 10.764,
  "poster_path": "/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg",
  "production_companies": [
    {
      "id": 2303,
      "logo_path": null,
      "name": "Villealfa Filmproductions",
      "origin_country": "FI"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "FI",
      "name": "Finland"
    }
  ],
  "release_date": "1988-10-21",
  "revenue": 0,
  "runtime": 73,
  "spoken_languages": [
    {
      "iso_639_1": "fi",
      "name": "suomi"
    },
    {
      "iso_639_1": "de",
      "name": "Deutsch"
    }
  ],
  "status": "Released",
  "tagline": "",
  "title": "Ariel",
  "video": false,
  "vote_average": 6.8,
  "vote_count": 105
}
```
The desired output looks like the following:

```
[
  {
    "original_title": "Lock, Stock and Two Smoking Barrels",
    "budget": 1350000,
    "genres": "Comedy, Crime",
    "popularity": 7119,
    "release_date": "1998-03-05",
    "revenue": 28356188,
    "runtime": 105,
    "vote_average": 8.2,
    "vote_count": 4048,
    "spoken_languages": "English"
  },
  {
    "original_title": "Verfolgt",
    "budget": 0,
    "genres": "Drama",
    "popularity": 5331,
    "release_date": "2006-08-06",
    "revenue": 0,
    "runtime": 87,
    "vote_average": 4.9,
    "vote_count": 11,
    "spoken_languages": "Deutsch"
  }
]
```

# Flow
- Import required modules
- define `concat_name` function for further use in transforming nested JSON to a comma seperated value
- Set data_path to match your resources folder
- get all filenames
- for each filename, check whether the file is empty (skipped if it is), `json.load()` the row and append to a list
- Progress print is available per `counter` rows
- `genres` and `spoken_languages` column is transformed using the `concat_name` function
- Transform the dataframe into json
- Dump the data into a file

# Running the Program
- Make sure that all the prerequisites are satisfied
- Configure the `data_path` to match your resources folder, i.e. the folder of the JSON files
- Run the program by running this script `python main.py`

# Output
Output of this file is to large to be pushed to GitHub. You can find it in this link https://drive.google.com/file/d/1-xYN0chqzeZ9YfVYQDDmUrNLy7QHHcr3/view?usp=sharing

# Notes
- Compiled data is not cleaned enough as the author notices some empty values in "spoken_languages" key
- As the JSON files that need to be processed consist of 500,000+ files, it took a long time to finish
- Unicode character is stored as the unicode (e.g. Espa\u00f1ol in Espanol)
- This code is made as a Self-Learning Module Part 1 to Academi by blank-space Data Engineering Track (https://www.blank-space.io/program)

# Contact
For further information, you might want to reach me to ricky.nauvaldy@gmail.com