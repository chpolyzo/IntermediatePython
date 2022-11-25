"""Write a stream of close approaches to CSV or to JSON.
This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.
These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.
You'll edit this file in Part 4.
"""

import json
import csv

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.
    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    with open(filename, "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames) # insert header fieldnames
        for row in results: #append results row per row
            writer.writerow([row.time,\
                             row.distance,\
                             row.velocity,\
                             row.neo.designation,\
                             row.neo.name,\
                             row.neo.diameter,\
                             row.neo.hazardous])
            
def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.
    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # dictionary comprehension to save results in a json like way
    results_dict = {"datetime_utc": helpers.datetime_to_str(row.time),
            "distance_au": row.distance,
            "velocity_km_s": row.velocity,
            "neo": {"designation": row.neo.designation,
                    "name": row.neo.name,
                    "diameter_km": row.neo.diameter,
                    "potentially_hazardous": row.neo.hazardous}} for row in results


    # save the list of approach dictionaries in json format
    with open(filename, "w") as outfile:
        json.dump(results_dict, outfile, indent=2)