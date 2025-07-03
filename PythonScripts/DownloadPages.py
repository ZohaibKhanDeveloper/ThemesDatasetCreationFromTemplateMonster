from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service(r"C:\Users\PMLS\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)
def downloadPages(category_name,link,no_pages,path_of_saving):
    for page_no in range(1, no_pages):
        driver.get(f"{link}/?page={page_no}")
        with open(f"{path_of_saving}/{category_name}_{page_no}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)  # Save page source to HTML file
            time.sleep(1)

    time.sleep(5)
    driver.quit()
# Fucntion call for different Types of themes from the website

# downloadPages(
#     category_name="WordpressThemes",
#     link="https://www.templatemonster.com/wordpress-themes",
#     no_pages=173,
#     path_of_saving="WordpressTemplates"
# )   
     
# downloadPages(
#     category_name="HTML5-Themes",
#     link="https://www.templatemonster.com/html-website-templates",
#     no_pages=161,
#     path_of_saving="Html5Templates"
# ) 

# downloadPages(
#     category_name="WooCommerceThemes",
#     link="https://www.templatemonster.com/woocommerce-themes",
#     no_pages=42,
#     path_of_saving="WooCommerceTemplates"
# )

# downloadPages(
#     category_name="PrestaShopThemes",
#     link="https://www.templatemonster.com/prestashop-themes",
#     no_pages=35,
#     path_of_saving="PrestaShopTemplates"
# )

# downloadPages(
#     category_name="JoomlaTemplates",
#     link="https://www.templatemonster.com/joomla-templates",
#     no_pages=37,
#     path_of_saving="JoomlaTemplates"
# )

# downloadPages(
#     category_name="LandingPagesTemplates",
#     link="https://www.templatemonster.com/landing-page-templates.php",
#     no_pages=50,
#     path_of_saving="LandingPagesTemplates"
# )