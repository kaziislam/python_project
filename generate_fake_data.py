import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate fake data
num_records = 50
data = []

# Supplier names to repeat
supplier_names = [
    "Adams PLC",
    "Hill-Hurst",
    "Lane PLC",
    "Sanchez-Thomas",
    "Daniel-Jones",
    "Ball-White",
    "Robertson-Frazier",
    "Flores-Berry",
    "Pope-Conrad",
    "Martin Ltd",
    "Crawford, Nelson and Hood",
    "Griffin-Lopez",
    "Marshall-Rogers",
    "Diaz, Ellis and Smith",
    "Franco, Oliver and Moreno"
]

for _ in range(num_records):
    product_no = fake.random_int(min=1000, max=9999)
    inventory = fake.random_int(min=10, max=100)
    price = round(fake.random.uniform(10, 100), 2)  # Generate a random number between 10 and 100
    supplier_name = fake.random_element(supplier_names)  # Randomly select a supplier name

    data.append([product_no, inventory, price, supplier_name])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Product No', 'Inventory', 'Price', 'Supplier Name'])

# Export to Excel
excel_filename = 'inventory.xlsx'
df.to_excel(excel_filename, index=False)

print(f'Fake data generated and exported to {excel_filename}')
