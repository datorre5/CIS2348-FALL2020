#Daniel Torres
#PSID: 1447167


import pandas as pd
import os
import datetime as dt

# Specify the input folder
inputs = r'/Users/Dani/Assignments' #Update to your self to whoever is grading
outputs = r'/Users/Dani/Processed'  #Update to yourself to whoever is grading

# Create classes with some characteristics for the inventory processing


class FullInventory:
    col_names = ['item ID', 'manufacturer name', 'item type', 'price', 'service date', 'is damaged']
    file_output = os.path.join(outputs, 'FullInventory.csv')


class ManufacturerList:
    col_names = ['item ID', 'manufacturer name', 'item type', 'is damaged']
    file_path = os.path.join(inputs, 'ManufacturerList.csv')


class PriceList:
    col_names = ['item ID', 'price']
    file_path = os.path.join(inputs, 'PriceList.csv')


class ServiceList:
    date_col = ['service date']
    col_names = ['item ID', 'service date']
    file_path = os.path.join(inputs, 'ServiceDatesList.csv')


# Read in the Manufacturer list csv file
manu_list = pd.read_csv(ManufacturerList.file_path, header=None, names=ManufacturerList.col_names)

# Read in the Price list csv file
price_list = pd.read_csv(PriceList.file_path, header=None, names=PriceList.col_names)

# Read in the Service list csv file, specify date column
service_list = pd.read_csv(ServiceList.file_path, header=None,
                           names=ServiceList.col_names, parse_dates=ServiceList.date_col)

# # 1 # #
# # A # #
# Create the full inventory, this by merging the dataframes together, starting with manufacturer list & Price, left join
full_inventory = pd.merge(manu_list, price_list, on=['item ID'], how='left')  # Merge on item ID

# Finalize the full inventory, merging with Service list, left join
full_inventory = pd.merge(full_inventory, service_list, on=['item ID'], how='left')  # Merge on item ID

# Rearrange columns as specified, by reverting to how we mapped the class
full_inventory = full_inventory[FullInventory.col_names]

# Sort by manufacturer, ascending
full_inventory = full_inventory.sort_values(['manufacturer name'], ascending=True)

# Create OS correct path for output
FullInventory_destination = os.path.join(outputs, 'FullInventory.csv')

# Output / save the processed file into the destination folder, without index
full_inventory.to_csv(FullInventory_destination, index=False)
print(full_inventory)

# # B # #
# Create the different item inventories by means of a loop
# First a list is created with all the unique item types
item_type = full_inventory['item type'].unique()
# Then the loop processes the list
for item in item_type:
    # Item is filtered
    item_inv = full_inventory[(full_inventory['item type'] == item)]
    # Selection is sorted for Item ID, index dropped in case of printing
    item_inv = item_inv.sort_values(['item ID'], ascending=True).reset_index(drop=True)
    # Creating OS-correct path for destination
    item_destination = os.path.join(outputs, f'{item}inventory.csv')
    # Replicate the columns and order listed in assignment, by means of slicing
    item_inv = item_inv[['item ID', 'manufacturer name', 'price', 'service date', 'is damaged']]
    # Specific item inventory is saved in processed folder, without index
    item_inv.to_csv(item_destination, index=False)


# # C # #
# Creating the past services file
# Create an object that holds today's date
today = dt.date.today()
# Copy a sliced version of the original inventory file, by comparing with the date object today
past_serviced = full_inventory[(full_inventory['service date'].dt.date < today)].copy()
# Sort from oldest to newest. Reset index in case of printing.
past_serviced = past_serviced.sort_values(['service date'], ascending=True).reset_index(drop=True)
# Save the processed dataframe into dedicated csv on OS correct path
past_destination = os.path.join(outputs, 'pastservicedinventory.csv')
# Save the dataframe, without index
past_serviced.to_csv(past_destination, index=False)


# # D # #
# Creating damaged items csv
# Slice on our full inventory dataframe, by filtering damaged items. Create a copy to transform.
dmg = full_inventory[(full_inventory['is damaged'] == 'damaged')].copy()
# Sort values oldest to most recent
dmg = dmg.sort_values(['price'], ascending=False).reset_index(drop=True)
# Create OS correct path for saving
dmg_destination = os.path.join(outputs, 'damagedinventory.csv')
# Save the processed dataframe, without index
dmg.to_csv(dmg_destination, index=False)



class FullInventory:
    date_columns = ['service date']


# Specify for the full inventory csv file to read-in
full_inventory = r'/Users/Dani//Processed/FullInventory.csv'

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



import pandas as pd
import datetime as dt

# # 2 # #
# # A i # #
# Create a class with some characteristics for the inventory


class FullInventory:
    date_columns = ['service date']


# Specify for the full inventory csv file to read-in
full_inventory = r'/Users/Dani//Processed/FullInventory.csv'

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
