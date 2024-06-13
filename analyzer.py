import csv

# File paths
csv_file = 'Info for Webpage .csv'  # Updated CSV file name
output_file = 'names.txt'

def process_csv(csv_file, output_file):
    # Read data from CSV and sort by roll numbers
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        sorted_rows = sorted(reader, key=lambda row: int(row['Roll']))

    # Write sorted data to names.txt with padded roll numbers
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for row in sorted_rows:
            roll = row['Roll']
            full_name = row['Full name']
            facebook_url = row['Facebook ID url '].strip()

            # Pad roll number with leading zero if necessary
            padded_roll = roll.zfill(2)
            
            # Write to names.txt in the desired format
            outfile.write(f"{padded_roll} {full_name} [{facebook_url}]\n")

if __name__ == "__main__":
    # Process the CSV file and write to names.txt
    process_csv(csv_file, output_file)
    
    print("Processing complete.")