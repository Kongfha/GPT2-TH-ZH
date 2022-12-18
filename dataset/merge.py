# Open the two input files in read mode
with open('valid.out', 'r') as file1:
  # Open the output file in write mode
  with open('valid.txt', 'w') as out_file:
    # Iterate through the lines in both files
    for line1 in file1:
      # Concatenate the lines and write them to the output file
      out_file.write(line1.strip() + " <|endoftext|>" +'\n')

# Open the two input files in read mode
with open('test.out', 'r') as file1:
  # Open the output file in write mode
  with open('test.txt', 'w') as out_file:
    # Iterate through the lines in both files
    for line1 in file1:
      # Concatenate the lines and write them to the output file
      out_file.write(line1.strip() + " <|endoftext|>" +'\n')

# Open the two input files in read mode
with open('train.out', 'r') as file1:
  # Open the output file in write mode
  with open('train.txt', 'w') as out_file:
    # Iterate through the lines in both files
    for line1 in file1:
      # Concatenate the lines and write them to the output file
      out_file.write(line1.strip() + " <|endoftext|>" +'\n')
