#!/usr/bin/env python3

# command line args
import argparse
import os
import zipfile
import datetime
import json
from collections import Counter

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--output_folder', default='outputs')
args = parser.parse_args()

# Load keywords
hashtags = [
    '#blm',
    '#black_lives_matter',
    '#george_floyd',
    '#racism',
    '#justice',
    '#police_brutality',
]

# Initialize counters
counter_lang = {hashtag: Counter() for hashtag in hashtags}
counter_country = {hashtag: Counter() for hashtag in hashtags}
counter_state = Counter()

# Add initialization for '_all' key
counter_lang['_all'] = Counter()
counter_country['_all'] = Counter()

# Open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # Loop over every file within the zip file
    for i, filename in enumerate(archive.namelist()):
        print(datetime.datetime.now(), args.input_path, filename)

        # Open the inner file
        with archive.open(filename) as f:

            # Loop over each line in the inner file
            for line in f:

                # Load the tweet as a Python dictionary
                tweet = json.loads(line)
                if tweet['place']['country_code'] == 'US':

                    # Convert text to lowercase
                    text = tweet['text'].lower()

                    # Search hashtags
                    for hashtag in hashtags:
                        lang = tweet['lang']
                        place = tweet['place']
                        if hashtag in text:
                            counter_lang[hashtag][lang] += 1
                            if place is not None:
                                country_code = place['country_code']
                                counter_country[hashtag][country_code] += 1
                            else:
                                counter_country[hashtag]['other'] += 1
                        counter_lang['_all'][lang] += 1
                        if place is not None:
                            counter_country['_all'][place['country_code']] += 1
                            state = place["full_name"].split(", ")[-1]  # Corrected index to get the state
                            counter_state[state] += 1
                        else:
                            counter_country['_all']['other'] += 1

# Open the output file
try:
    os.makedirs(args.output_folder)
except FileExistsError:
    pass

output_path_base = os.path.join(args.output_folder, os.path.basename(args.input_path))
output_path_lang = output_path_base + '.lang'
output_path_country = output_path_base + '.country'
output_path_state = output_path_base + '.state'  # Added state output file

print('saving', output_path_lang)
print('saving', output_path_country)
print('saving', output_path_state)

with open(output_path_lang, 'w') as f:
    f.write(json.dumps(counter_lang))

with open(output_path_country, 'w') as f:
    f.write(json.dumps(counter_country))

with open(output_path_state, 'w') as f:
    f.write(json.dumps(counter_state))
