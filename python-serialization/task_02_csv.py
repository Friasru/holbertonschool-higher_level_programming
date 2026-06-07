#!/usr/bin/python3
"""Module for converting CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """convert csv data to json and save data.json"""
    try:
        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except (IOError, OSError, json.JSONDecodeError):
        return False
    except Exception:
        return False
