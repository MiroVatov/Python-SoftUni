pencils = 4.75
flumasters = 1.80
drawing_paper = 6.50
notebook = 2.50

pencils_qty = int(input())
flumasters_qty = int(input())
drawing_paper_qty = int(input())
notebooks_qty = int(input())

total_bill = (pencils * pencils_qty) + (flumasters * flumasters_qty) + (drawing_paper * drawing_paper_qty) + (notebook * notebooks_qty)
total_bill = total_bill - ((total_bill * 5) / 100 )

print(f'Your total is {total_bill:.2f}lv')