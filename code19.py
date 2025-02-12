import csv


input_file = 'code19.txt'
output_file = 'code19.csv'

with open(input_file, 'r') as txt_file, open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    for i in txt_file:
        row = i.strip().split(',')
        csv_writer.writerow(row)
        

print(f'Converted {input_file} to {output_file}.')