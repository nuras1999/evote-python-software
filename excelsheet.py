import xlsxwriter

workbook = xlsxwriter.Workbook('Result.xlsx')
worksheet = workbook.add_worksheet()

# Create some cell formats with protection properties.
unlocked = workbook.add_format({'locked': False})
locked   = workbook.add_format({'locked': True})

# Format the worksheet to unlock all cells.
worksheet.set_column('A:XDF', None, locked)

# Turn worksheet protection on.
worksheet.protect()

row_format = workbook.add_format({'bold': True, 'font_color': '#8904B1','bg_color':'#F3E2A9','align':'center','shrink':'True','border':1})
merge_format = workbook.add_format({'bold': True, 'font_color': '#8A0829','bg_color':'#A9F5A9','align':'center','valign':'vcenter','shrink':'True','font_size':'15','border':1})
merge_format_1 = workbook.add_format({'bold': True, 'font_color': '#B40404','bg_color':'#FFFF00','align':'center','valign':'vcenter','shrink':'True','font_size':'15'})
result_count_format = workbook.add_format({'bold': True, 'font_color': '#blue','bg_color':'#ffffff','align':'center','valign':'vcenter','shrink':'True','font_size':'15','border':1})
result_individual_count_format = workbook.add_format({'bold': True, 'font_color': 'orange','bg_color':'#ffffff','align':'center','valign':'vcenter','shrink':'True','font_size':'15','border':1})
name_format = workbook.add_format({'bold': True, 'font_color': 'green','bg_color':'#ffffff','align':'center','valign':'vcenter','shrink':'True','font_size':'12','border':1})


# voter_format_last = workbook.add_format()
# voter_format_last.set_bottom()
# voter_format_last.set_left(1)
# voter_format_last.set_right(1)
# voter_format_all = workbook.add_format()
# voter_format_all.set_left(1)
# voter_format_all.set_right(1)

#worksheet.merge_range('A1:C2', 'eVOTE RESULT', merge_format)

worksheet.merge_range('F1:K2', 'Joint Secretary Election ',merge_format)


worksheet.write(2,0, 'VOTED FOR',row_format )  
worksheet.write(3,0, 'Hello')
worksheet.write(4,0, 'This ')
worksheet.write(5,0, 'is')
worksheet.write(6,0, 'Just') # Unlocked by default.


worksheet.write(10,0, 'Arun',name_format ) 
worksheet.write(11,0, 'Akash',name_format ) 
worksheet.write(12,0, 'Keshav',name_format ) 
worksheet.write(13,0, 'Sanjai',name_format ) 

worksheet.write(10,1, '3',result_individual_count_format)
worksheet.write(11,1, '2',result_individual_count_format)
worksheet.write(12,1, '1',result_individual_count_format)
worksheet.write(13,1, '2',result_individual_count_format)



worksheet.merge_range('A16:B16', 'VOTES',merge_format_1)

worksheet.write(15,2, '15',result_count_format)

worksheet.merge_range('A18:B18', 'WINNER',merge_format_1)

worksheet.merge_range('C18:E18', 'Keshavamoorthy',result_count_format)
worksheet.merge_range('F18:H18', 'Akash Sivadas Menon',result_count_format)
#worksheet.write(11,2, 'Keshavamoorthy',result_count_format)

workbook.close()