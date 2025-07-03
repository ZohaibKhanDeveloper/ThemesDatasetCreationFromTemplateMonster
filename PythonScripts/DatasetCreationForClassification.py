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
for i in range(0,1100):
    category.append("html5")
for i in range(0,1100):
    category.append("Joomla")
for i in range(0,1100):
    category.append("Landing Pages")
for i in range(0,1100):
    category.append("PrestaShop")
for i in range(0,1100):
    category.append("Shopify")
for i in range(0,1100):
    category.append("WooCommerce")
for i in range(0,1100):
    category.append("Wordpress")    
print(len(category))                        
for file in all_files:
    data = pd.read_csv(file)
    print(f"Reading and merging {file}")
    for d in data["Product name"].tolist()[0:1100]:
        product_name.append(d)
    for d in data["Product Price"].tolist()[0:1100]:
        product_price.append(d)
    for d in data["Offered by"].tolist()[0:1100]:
        vendor.append(d)        
    for d in data["Product Description"].tolist()[0:1100]:
        product_description.append(d)    
    for d in data["Number of Sales"].tolist()[0:1100]:
        no_of_sales.append(d)
    for d in data["Ratings/5"].tolist()[0:1100]:
        ratings.append(d)
    for d in data["Product Link"].tolist()[0:1100]:
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
dataset.to_csv("ThemeClassificationDataset.csv",index=False)
dataset.to_json("ThemeClassificationDataset.json",index=False)        