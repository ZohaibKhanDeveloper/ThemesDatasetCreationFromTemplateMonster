import pandas as pd
all_files = [
    "Html5TemplatesData.csv",
    "JoomlaTemplatesData.csv",
    "LandingPagesTemplatesData.csv",
    "PrestaShopTemplatesData.csv",
    "ShopifyThemesTemplatesData.csv",
    "WooCommerceTemplatesData.csv",
    "WordpressThemesTemplatesData.csv",
    ]

product_name = []
product_price = []
vendor = []
product_description = []
no_of_sales = []
ratings = []
category = []
product_link = []

for i in range(0,5733):
    category.append("html5")
for i in range(0,1272):
    category.append("Joomla")    
for i in range(0,1719):
    category.append("LandingPage")    
for i in range(0,1198):
    category.append("PrestaShop")
for i in range(0,2438):
    category.append("Shopify")
for i in range(0,1441):
    category.append("WooCommerce")            
for i in range(0,6150):
    category.append("html5")    

for file in all_files:
    data = pd.read_csv(file)
    print(f"Reading and merging {file}")
    for d in data["Product name"].tolist():
        product_name.append(d)
    for d in data["Product Price"].tolist():
        product_price.append(d)
    for d in data["Offered by"].tolist():
        vendor.append(d)        
    for d in data["Product Description"].tolist():
        product_description.append(d)    
    for d in data["Number of Sales"].tolist():
        no_of_sales.append(d)
    for d in data["Ratings/5"].tolist():
        ratings.append(d)
    for d in data["Product Link"].tolist():
        product_link.append(d)

dataset = pd.DataFrame({
    "Product name":product_name,
    "Product description":product_description,
    "Product Price":product_price,
    "Vendor":vendor,
    "No.of Sales":no_of_sales,
    "Ratings/5":ratings,
    "Category":category,
    "Product link":product_link,
})          
print(dataset)
print(dataset.describe())            
dataset.to_csv("RecomendationSystemDataset.csv",index=False)