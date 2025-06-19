import pandas as pd

produketet=["Apples", "Bannanas","Oranges","Grapes", "Pinapples"]
sales = [150,200,180,90,60]

sales_perProdcuts=pd.Series(sales, index=produketet)
print(sales_perProdcuts)

#shitja e rrushit
print(sales_perProdcuts["Grapes"])

best_selling_product=sales_perProdcuts.idxmax()
print(best_selling_product)

