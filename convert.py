import pdfminer
import pdfminer.high_level
import pdfminer.layout
import pandas as pd

# Define input and output file paths
pdf_path = 'convert.pdf'
csv_path = 'outpu.xlsx'

# Extract text from PDF using pdfminer
text = pdfminer.high_level.extract_text(pdf_path)

# Split text into lines and remove leading/trailing white spaces
lines = [line.strip() for line in text.split('\n')]

# Split each line into columns using tab delimiter
rows = [line.split('\t') for line in lines]

# Create a Pandas DataFrame from the rows
df = pd.DataFrame(rows)

# Write the DataFrame to a CSV file
df.to_excel(csv_path, index=False, header=False)
