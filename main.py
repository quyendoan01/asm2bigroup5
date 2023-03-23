import csv
import numpy as np
import pandas as pd
import os
from pathlib import Path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


arr_int = ["transaction_id", "sales_outlet_id", "customer_id", "order", "line_item_id", "product_id",
           "store_postal_code", "manager",
           "quantity", "home_store", "Date_ID", "Week_ID", "Month_ID", "Quarter_ID", "Year_ID", "birth_year",
           "staff_id", "start_of_day", "quantity_sold", "waste", "beans_goal",
           "beverage_goal", "food_goal", "merchandise _goal", "total_goal", "store_square_feet"]
arr_float = ["line_item_amount", "unit_price", "current_wholesale_price", "store_longitude", "store_latitude"]
arr_string = ["instore_yn", "promo_item_yn", "customer_first-name", "customer_email", "loyalty_card_number", "gender",
              "Neighorhood","transaction_time",
              "generation", "first_name", "last_name", "Week_Desc", "Month_Name", "position", "Quarter_Name",
              "%waste", "product_group", "product_category", "product_type", "product", "product_description",
              "unit_of_measure", "current_retail_price", "tax_exempt_yn", "promo_yn", "new_product_yn", "year_month",
              "sales_outlet_type", "store_address", "store_city", "store_state_province", "store_telephone", "location"]
arr_date = ["transaction_date", "customer_since", "birthdate", "birth_year", "start_date"]

print(bcolors.OKBLUE + bcolors.BOLD + "[==============                 ===============]" + bcolors.ENDC)
print(bcolors.OKCYAN + bcolors.BOLD + "[=======                                =======]" + bcolors.ENDC)
print(
    bcolors.BOLD + "\033[96m[===" + bcolors.WARNING + "    WELCOME TO THE PROGRAM OF TEAM 5    " + "\033[96m===]" + bcolors.ENDC)
print(bcolors.OKCYAN + bcolors.BOLD + "[=======                                =======]" + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.BOLD + "[==============                 ===============]" + bcolors.ENDC)
print()
print()

while True:

    print(bcolors.OKCYAN + "1. Choose a csv file")
    print("2. Exit" + bcolors.ENDC)
    choosen_first = int(input(bcolors.OKBLUE + "Choose your function: " + bcolors.ENDC))
    if choosen_first == 1:
        file_name = Path(input(bcolors.OKBLUE + "Please enter the file name (.csv): " + bcolors.ENDC))
        if not (file_name.is_file()):
            print(bcolors.FAIL + "File has name [" + str(file_name) + "] is not found" + bcolors.ENDC)
        else:
            file_data = pd.read_csv(file_name)
            arr_header = list(file_data.columns)

            arr_int_n = []
            arr_float_n = []
            arr_string_n = []
            arr_date_n = []
            arr_unknown = []
            for i in arr_header:
                if i in arr_int:
                    arr_int_n.append(i)
                elif i in arr_float:
                    arr_float_n.append(i)
                elif i in arr_string:
                    arr_string_n.append(i)
                elif i in arr_date:
                    arr_date_n.append(i)
                else:
                    arr_unknown.append(i)

            print("The columns included in the file are:")
            for i in arr_header:
                print(i, end=" | ")

            print()
            while True:
                if arr_unknown != []:
                    while True:
                        print(bcolors.WARNING + "Some columns is undefined", arr_unknown)
                        print(bcolors.OKCYAN + "1. Show data of columns")
                        print("2. Delete column")
                        print("3. Skip (this data will convert to string!)" + bcolors.ENDC)
                        choosen_unknown = int(input(bcolors.OKBLUE + "Choose your function: " + bcolors.ENDC))
                        if choosen_unknown == 1:
                            print(file_data[arr_unknown])
                        elif choosen_unknown == 2:
                            file_data.drop(arr_unknown,
                                           axis='columns', inplace=True)
                            break
                        else:
                            arr_string_n += arr_unknown
                            arr_unknown = []
                            break
                file_row = len(file_data.index)
                file_row_missing = file_data.shape[0] - file_data.dropna().shape[0]
                # print("...Formatting data...")
                # file_data[arr_int_n] = file_data[arr_int_n].astype(int)
                # print("Columns have been formatted data")
                print(bcolors.OKCYAN + "Perform data manipulation:")
                print("1. Reformat data")
                print("2. Check null data")
                print("3. View data by row number/column name")
                print("4. View summary")
                print("5. Save as new file")
                print("6. Back" + bcolors.ENDC)
                choosen_config = int(input(bcolors.OKBLUE + "Choose your function: " + bcolors.ENDC))
                if choosen_config == 1:
                    col_err = 0
                    row_err = 0
                    err_column_int = []
                    err_row_int = []
                    err_column_float = []
                    err_row_float = []
                    err_column_date = []
                    err_row_date = []
                    #print(file_data_int.applymap(lambda x: isinstance(x, (int, float))))
                    for i in arr_int_n:
                        try:
                            file_data[i] = file_data[i].astype(int)
                        except ValueError:
                            if i not in err_column_int:
                                err_column_int.append(i)
                                col_err += 1
                            s1 = pd.DataFrame(pd.to_numeric(file_data[i], errors='coerce'))
                            s2 = s1[s1[i].isnull()].index
                            err_row_int.append(s2)
                            row_err += s1.shape[0] - s1.dropna().shape[0]
                    for i in arr_float_n:
                        try:
                            file_data[i] = file_data[i].astype(float)
                        except ValueError:
                            if i not in err_column_float:
                                err_column_float.append(i)
                                col_err += 1
                            s3 = pd.DataFrame(pd.to_numeric(file_data[i], errors='coerce'))
                            s4 = s3[s3[i].isnull()].index
                            err_row_float.append(s4)
                            row_err += s3.shape[0] - s3.dropna().shape[0]
                    for i in arr_date_n:
                        try:
                            file_data[i] = pd.to_datetime(file_data[i], format='%d/%m/%Y')
                        except ValueError:
                            if i not in err_column_date:
                                err_column_date.append(i)
                                col_err += 1
                            s5 = pd.DataFrame(pd.to_datetime(file_data[i], format='%d/%m/%Y', errors='coerce'))
                            s6 = s5[s5[i].isnull()].index
                            err_row_date.append(s6)
                            row_err += s5.shape[0] - s5.dropna().shape[0]
                    if col_err > 0:
                        col_arr_err = err_column_int + err_column_float + err_column_date
                        row_arr_err = err_row_int + err_row_float + err_row_date
                        print("Have", col_err, "column has error value: ")
                        print(col_arr_err)
                        print(bcolors.WARNING + "We have unknown value in cell of ", row_err, "/", file_row, "data rows",
                              "(",
                              round(row_err / file_row * 100, 3), "%)" + bcolors.ENDC)
                        print(bcolors.OKCYAN + "1. Manual editing")
                        print("2. Delete rows" + bcolors.ENDC)
                        choosen_err = input(bcolors.OKBLUE + "Choose your function: " + bcolors.ENDC)
                        if choosen_err == "1":
                            while True:
                                count = 1
                                for i in col_arr_err:
                                    print(bcolors.OKCYAN + str(count) + ".", i)
                                    count += 1
                                print(str(count) + ". Back" + bcolors.ENDC)
                                choosen_fix_err = int(input(bcolors.OKBLUE + "Choose your function: " + bcolors.ENDC))
                                try:
                                    column_fix = col_arr_err[choosen_fix_err-1]
                                    print(column_fix)
                                    print(file_data.loc[row_arr_err[choosen_fix_err-1]][column_fix])
                                    row_num = 1
                                    for i in row_arr_err[choosen_fix_err-1]:
                                        fix_value = input(bcolors.OKBLUE + "Change value for row " + str(row_num) + ": " + bcolors.ENDC)
                                        file_data.loc[i, column_fix] = fix_value
                                        row_num += 1
                                    col_arr_err.remove(column_fix)
                                    row_arr_err.pop(choosen_fix_err-1)
                                except IndexError:
                                    break

                        else:
                            for i in range(len(err_column_int)):
                                file_data.loc[err_row_int[i], err_column_int[i]] = np.nan
                            for i in range(len(err_column_float)):
                                file_data.loc[err_row_float[i], err_column_float[i]] = np.nan
                            for i in range(len(err_column_date)):
                                file_data.loc[err_row_date[i], err_column_date[i]] = np.nan
                            file_data.dropna(subset=arr_header, inplace=True)
                            file_row = len(file_data.index)
                    else:
                        print(bcolors.HEADER + "Data has been formatted" + bcolors.ENDC)

                elif choosen_config == 2:
                    file_row = len(file_data.index)
                    file_row_missing = file_data.shape[0] - file_data.dropna().shape[0]
                    if file_row_missing <= 0:
                        print(bcolors.HEADER + "No value in data is null" + bcolors.ENDC)
                    else:
                        print(bcolors.WARNING + "We have missing value in cell of ", file_row_missing, "/", file_row, "data rows", "(",
                              round(file_row_missing / file_row * 100, 3), "%)" + bcolors.ENDC)
                        if file_row_missing > 0:
                            print(bcolors.OKCYAN + "1. Manual editing")
                            print("2. Delete rows" + bcolors.ENDC)
                            choosen_missing = input(bcolors.OKBLUE + "Choose your function: " + bcolors.ENDC)
                            if choosen_missing == "1":

                                col_null = np.where(pd.isnull(file_data))[1]
                                try:
                                    # data_null = pd.DataFrame(file_data.loc[row_null][col_null])
                                    for i in col_null:
                                        row_null = file_data[file_data[arr_header[i]].isnull()].index
                                        print(file_data.loc[row_null][arr_header[i]])
                                        data_null_fix = input(bcolors.OKBLUE + "Replace this data: " + bcolors.ENDC)
                                        file_data.loc[row_null, arr_header[i]] = data_null_fix
                                except IndexError:
                                    break
                            else:
                                file_data.dropna(subset=arr_header, inplace=True)
                                file_row = len(file_data.index)
                elif choosen_config == 3:
                    while True:
                        print(bcolors.OKCYAN + "1. Show data by 1 row number")
                        print("2. Show data by 1 column name")
                        print("3. Show data by many row and many column number")
                        print("4. Back" + bcolors.ENDC)
                        show_data = int(input(bcolors.OKBLUE + "Choose your function: " + bcolors.ENDC))
                        if show_data == 1:
                            print("This data have", file_row, "row")
                            row_data = int(input(bcolors.OKBLUE + "Enter the number of row: " + bcolors.ENDC))
                            try:
                                print(file_data.loc[row_data])
                            except KeyError:
                                print(bcolors.FAIL + "Seems like this data does not have that row" + bcolors.ENDC)

                        elif show_data == 2:
                            print("This data have", len(arr_header), "column")
                            print(arr_header)
                            column_data = input(bcolors.OKBLUE + "Enter the column name: " + bcolors.ENDC).split(" ")

                            try:
                                print(file_data[column_data])
                            except KeyError:
                                print(bcolors.FAIL + "Seems like this data does not have that column" + bcolors.ENDC)

                        elif show_data == 3:
                            row_start = int(input(bcolors.OKBLUE + "Index of start row : "))
                            row_end = int(input("Index of end row: ")) + 1
                            column_start = int(input("Index of start column: "))
                            column_end = int(input("Index of end column: " + bcolors.ENDC)) + 1
                            row_middle = 0
                            column_middle = 0
                            if row_start > row_end:
                                row_middle = row_start
                                row_start = row_end
                                row_end = row_middle
                            if column_start > column_end:
                                column_middle = column_start
                                column_start = column_end
                                column_end = column_middle
                            try:
                                print(file_data.iloc[row_start:row_end, column_start:column_end])
                            except ValueError:
                                print(bcolors.FAIL + "Seems like this data does not have that index of row/column" + bcolors.ENDC)
                        else:
                            break
                elif choosen_config == 4:
                    print(file_data)
                elif choosen_config == 5:
                    new_file_name = input(bcolors.OKBLUE + "Enter new file name (.csv): " + bcolors.ENDC)
                    file_data.to_csv(new_file_name, index=False)
                    print(bcolors.HEADER + "Save data successful !!" + bcolors.ENDC)
                else:
                    break
    else:
        break

print(bcolors.HEADER + "Program is ended !!" + bcolors.ENDC)
