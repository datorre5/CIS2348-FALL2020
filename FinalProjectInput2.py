#Daniel Torres
#PSID:1447167


import pandas as pd
import datetime as dt

# # 2 # #
# # A i # #
# Create a class with some characteristics for the inventory


class FullInventory:
    date_columns = ['service date']


# Specify for the full inventory csv file to read-in
full_inventory = r'/Users/Dani//Processed/FullInventory.csv' #update users to you

# Read in the csv file, specify Date column to ensure Date variable
full_inventory = pd.read_csv(full_inventory, parse_dates=FullInventory.date_columns)

# Create two dictionaries for the two queried columns that can be used later to search keyword hits
# Entries will be stripped from trailing blanks, and stored as lowercase to ensure more hits

branddict = {}
brand_dict = full_inventory['manufacturer name'].str.strip().str.lower().unique()
for brand in brand_dict:
    add = {brand: 'Manufacturer'}
    branddict.update(add)

itemdict = {}
item_dict = full_inventory['item type'].str.strip().str.lower().unique()
for item in item_dict:
    add = {item: 'item type'}
    itemdict.update(add)

# Start the loop for the query which will only be broken when user enters 'q'
while True:
    manufacturerlist = []  # List to append in manufacturer name picked up in search words
    itemlist = []  # List to append in item type picked up in search words

    # Prompted message for the user that requires input
    query = input("""What manufacturer and item type would you like to query, exit with 'q': """)
    # If statement to check breaking from the loop if user enters 'q'
    if query == 'q':
        print('You are leaving . . . Thank you for using this query!')  # Message to confirm user is leaving query
        break
    else:
        query = query.split(' ')  # Split every word keyed in query, this is a list

        # Loop over the list with the keyed in words
        for word in query:
            word = word.lower()  # transform word into lowercase equivalent
            # check if there are matches with the unique entries in inventory
            if word in branddict.keys():
                manufacturerlist.append(word)  # If yes- Append to list that can be used for filtering & printing
            elif word in itemdict.keys():
                itemlist.append(word)  # If yes- Append to list that can be used for filtering & printing
            else:
                pass  # If no hit on this word, then ignore

        # First check: More than one manufacturer name, or item type. If yes- break loop with printing with message
        if len(manufacturerlist) > 1 or len(itemlist) > 1:
            print('No such item in inventory')
            continue
        # Second check: No manufacturer name, or no item type. If yes- break loop with printing with message
        elif len(manufacturerlist) == 0 or len(itemlist) == 0:
            print('No such item in inventory')
            continue

        # Two valid keywords are found, second stage of loop enters
        else:
            # Filter inventory on the keywords. Filter lowercase equivalent, without trailing blanks.
            # Filter method will not impact printing result later.
            query_result = full_inventory[((full_inventory['manufacturer name'].str.strip().str.lower() == manufacturerlist[0]) &
                                          (full_inventory['item type'].str.strip().str.lower() == itemlist[0]))]

            # Exclude damaged items and also check if combination exists
            query_result = query_result[(query_result['is damaged'].isnull())]
            # Check if there are any items left in result, after filtering out damaged items.
            if len(query_result) == 0:
                print('No such item in inventory')
                continue
            # If there are one or more items, then proceed with loop.
            else:
                pass

            # Get most expensive item in final result, else continue to final section loop.
            if len(query_result) > 1:
                expensive = query_result['price'].max()  # Most expensive item
                query_result = query_result[(query_result['price'] == expensive)]  # Filter this item
            else:
                pass

            # Reset the index, this will help with our loc-slicing.
            query_result = query_result.reset_index(drop=True)
            # Final check: Service data is in the past, then break loop with printing message no availability.
            if query_result.loc[0, 'service date'] < dt.date.today():
                print('No such item in inventory')
                continue
            else:
                # Create variables by locating all requirements that need printing. Effectively first row on column name
                itemid = query_result.loc[0, 'item ID']
                manu = query_result.loc[0, 'manufacturer name']
                itype = query_result.loc[0, 'item type']
                price = query_result.loc[0, 'price']
                print(f'Your item is: {itemid}, {manu}, {itype}, {price}')

# Loop will terminate when user breaks by typing 'q'