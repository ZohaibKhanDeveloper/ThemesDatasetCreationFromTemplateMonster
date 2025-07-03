from bs4 import BeautifulSoup
import pandas as pd

def scrapeAndSaveData(path,sheet_name,no_pages):
    print(f"---({sheet_name})---")
    products = []
    for page in range(1,no_pages):
        with open(f'{path}_{page}.html','r',encoding='utf-8') as file:
            print(f"Reading file {page}...")
            soup = BeautifulSoup(file,'html.parser')
            products.append(soup.find_all("article",class_="product"))
    products_name = []
    products_price = []
    offered_by = []
    products_description = []
    number_of_sales = []
    ratings = []   
    products_link = []
    for product in products:
        for prod in product:
            products_name.append(prod.find("span",class_="product-name-title-text").text)
            products_price.append(int(((prod.find("div",class_="product-price").text).strip())[1:]))
            offered_by.append(prod.find("span",class_="product-name-vendor-text").text)
            if prod.find("div",class_="product-description"):
                products_description.append(prod.find("div",class_="product-description").text)
            else:
                products_description.append("Description Not Available")    
            sales = prod.find("span",class_="product-sales_amount")
            if sales:
                sales = sales.text.replace(",", "")
                number_of_sales.append(int(sales))
            else:
                number_of_sales.append(0)
            support = prod.find("span",class_="product-support-rating__text") 
            if support:
                ratings.append(float(support.find("strong").text))
            else:
                ratings.append(0.0)  
            products_link.append(prod.find("a",class_="product-name-title-link").get("href"))      
    all_data = pd.DataFrame({
        "Product name":products_name,
        "Product Price":products_price,
        "Offered by":offered_by,
        "Product Description":products_description,
        "Number of Sales":number_of_sales,
        "Ratings/5":ratings,
        "Product Link":products_link,
    })   
    print(all_data)
    print(all_data.describe())  
    all_data.to_csv(f"{sheet_name}.csv",index=False)   

scrapeAndSaveData(path="Html5Templates/HTML5-Themes",sheet_name="Html5TemplatesData",no_pages=161) 
scrapeAndSaveData(path="JoomlaTemplates/JoomlaTemplates",sheet_name="JoomlaTemplatesData",no_pages=37) 
scrapeAndSaveData(path="LandingPagesTemplates/LandingPagesTemplates",sheet_name="LandingPagesTemplatesData",no_pages=50) 
scrapeAndSaveData(path="PrestaShopTemplates/PrestaShopThemes",sheet_name="PrestaShopTemplatesData",no_pages=35)
scrapeAndSaveData(path="ShopifyTemplates/ShopifyThemes",sheet_name="ShopifyThemesTemplatesData",no_pages=69) 
scrapeAndSaveData(path="WooCommerceTemplates/WooCommerceThemes",sheet_name="WooCommerceTemplatesData",no_pages=42) 
scrapeAndSaveData(path="WordpressTemplates/WordpressThemes",sheet_name="WordpressThemesTemplatesData",no_pages=173)  