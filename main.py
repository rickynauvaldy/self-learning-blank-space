import pandas as pd
import json
from os import walk, stat


# Functions

def concat_name(df_col):
    """Concat list values"""
    result = ""
    for item in df_col:
        result += "," + item['name']

    # remove comma in the front, and put back to df
    return result[1:]


def check_stat(process_name, current_data, all_data, counter, note=''):
    if len(current_data) % counter == 0:
        print(process_name + ' ' + str(len(current_data)) + '/' + str(len(all_data)) + ' file processed ' + note)


def self_learn_blank_space():
    # change this
    data_path = 'D:/Projects/codes/Academi/self-learning-1/resources/'
    counter = 1000

    _, _, filenames = next(walk(data_path))
    all_data = []

    filenames = filenames[:1]
    print('File count:' + str(len(filenames)))
    empty_count = 0

    # Gather only filled JSON
    for filename in filenames:
        full_path = data_path + filename

        # check if file is empty
        if stat(full_path).st_size != 0:

            # Append data
            process_name = 'append_data'

            # set encoding for unhandled char
            with open(full_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                all_data.append(data)
                check_stat(process_name, all_data, filenames, counter)
        else:
            empty_count = empty_count + 1

    check_stat('Done! ', all_data, filenames, len(all_data), 'with ' + str(empty_count) + ' empty files')

    # Create a dataframe
    df = pd.json_normalize(all_data)

    # Change nested json to text
    df['genres'] = df['genres'].apply(concat_name)
    df['spoken_languages'] = df['spoken_languages'].apply(concat_name)

    # Define needed columns and convert df to json
    columns = ['original_title', 'budget', 'genres', 'popularity', 'release_date', 'revenue', 'runtime', 'vote_average',
               'vote_count', 'spoken_languages']
    df_for_json = df[columns]
    data_for_json = df_for_json.to_json(orient='records')

    # Dump to file
    with open('output.json', 'w') as outfile:
        # use "loads" to remove "\" from output
        json.dump(json.loads(data_for_json), outfile)


if __name__ == '__main__':
    self_learn_blank_space()
