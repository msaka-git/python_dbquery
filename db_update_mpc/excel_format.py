import pandas as pd
import xlrd
import xlsxwriter


#encoding_override='cp1252'

workbook = xlrd.open_workbook('MPW_inventaire.xlsx', encoding_override='latin1', on_demand=True)
worksheet = workbook.sheet_by_index(0)

#print(worksheet.cell(0,0).value)
serverlar_hostname=worksheet.col_values(0,1,None)
serverlar_os = worksheet.col_values(5, 1, None)
serverlar_scope = worksheet.col_values(1,1,None)
serverlar_type = worksheet.col_values(2,1,None)
serverlar_ip = worksheet.col_values(14,1,None)
serverlar_nat = worksheet.col_values(16,1,None)
serverlar_location = worksheet.col_values(27,1,None)
serverlar_appli = worksheet.col_values(18,1,None)

#print(serverlar)


workbook = xlsxwriter.Workbook('servers.xlsx')
worksheet1 = workbook.add_worksheet('Inventaire')



def extract():
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 1
    column = 0
    content = serverlar_hostname
    worksheet1.write('A1', 'hostname')
    # iterating through content list
    for item in content:
        # write operation perform
        worksheet1.write(row, column, item)

        # incrementing the value of row by one
        # with each iteratons.
        row += 1


    row=1
    column=1
    content=serverlar_os
    worksheet1.write('B1', 'os')

    for item in content:
        # write operation perform
        worksheet1.write(row, column, item)

        # incrementing the value of row by one
        # with each iteratons.
        row += 1

    row=1
    column=2
    content=serverlar_scope
    worksheet1.write('C1', 'scope')

    for item in content:
        worksheet1.write(row,column,item)
        row += 1

    row=1
    column=3
    content=serverlar_type
    worksheet1.write('D1', 'type')

    for item in content:
        worksheet1.write(row,column,item)
        row += 1

    row = 1
    column = 4
    content = serverlar_ip
    worksheet1.write('E1', 'ip')

    for item in content:
        worksheet1.write(row, column, item)
        row += 1

    row = 1
    column = 5
    content = serverlar_nat
    worksheet1.write('F1', 'nat')

    for item in content:
        if item == 42:
            worksheet1.write(row, column, "")
        elif item == "=#N/A":
            worksheet1.write(row, column, "")
        else:
            worksheet1.write(row, column, item)

        row += 1

    row = 1
    column = 6
    content = serverlar_location
    worksheet1.write('G1', 'datastore')

    for item in content:
        worksheet1.write(row, column, item)
        row += 1

    row = 1
    column = 7
    content = serverlar_appli
    worksheet1.write('H1', 'application')

    for item in content:
        worksheet1.write(row, column, item)
        row += 1



    workbook.close()





def to_csv():
    data_xls = pd.read_excel('servers.xlsx', 'Inventaire', index_col=None)
    data_xls.to_csv('servers.csv', encoding='utf-8-sig',index=None)



