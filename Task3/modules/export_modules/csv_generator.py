def create_csv(filename="data"):
    with open('database.csv', "rb") as data:
        with open(f"export/{filename}.csv", "wb") as new_file:
            new_file.writelines(data.readlines())