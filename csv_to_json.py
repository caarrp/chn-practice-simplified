import csv
import json
import unicodedata

def csv_to_json(csv_file_path, json_file_path):
    try:
        # Read the CSV and convert to a dictionary
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = []

            # Process each row, ensuring proper handling of unicode and nested structures
            for row in csv_reader:
                processed_row = {}
                for key, value in row.items():
                    try:
                        # Attempt to parse nested structures (e.g., lists, dictionaries)
                        processed_row[key] = json.loads(value)
                    except (json.JSONDecodeError, TypeError):
                        # If parsing fails, keep the value as a string
                        processed_row[key] = value
                data.append(processed_row)

        # Write the dictionary to a JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Successfully converted {csv_file_path} to {json_file_path}")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_file_path = 'learnword.csv'  # Replace with your CSV file name
json_file_path = 'example.json'  # Replace with your desired JSON file name
csv_to_json(csv_file_path, json_file_path)