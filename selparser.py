import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urls

def get_data(url, category):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path=r'D:\VSCodeProjects\Projs\StaffSalesBot_parser\webdvr\chromedriver.exe', options=options)
    driver.get(url=url)
    
    for _ in range(0, 40):
        driver.execute_script('window.scrollBy(0, 100)')
        print('scrolled')
    
    try:
        WebDriverWait(driver, 10).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-card__info--oldprice')))
    except Exception as ex:
        print(ex)
    
    old_prices = driver.find_elements(By.CLASS_NAME, value='product-card__info--oldprice')
    names = driver.find_elements(By.CLASS_NAME, value='product-card__info--title')
    prices = driver.find_elements(By.CLASS_NAME, value='product-card__info--price')
    sizes = driver.find_elements(By.CLASS_NAME, value='product-card__info--sizes')
    discount = driver.find_elements(By.CLASS_NAME, value='product-card__discount')
    item_link = driver.find_elements(By.CLASS_NAME, value='catalog__product-catalog')
    if len(item_link) >= 8:
        try:
            x = item_link[7].find_element(By.CLASS_NAME, value='product-card__discount')
            print(x)
        except:
            item_link.pop(7)
    # x = item_link[0].find_element(By.TAG_NAME, value='a').get_attribute('href')
    # print(x)
    # x = item_link[0].find_element(By.TAG_NAME, value='img').get_attribute('src')
    # print(x)
    
    # //*[@id="__next"]/div/div/div[1]/div/div/div/div/div[4]/div[1]/div[1]/div/a
    
    parsed = []
    
    for i in range(0, len(old_prices)):
        
        
        parsed.append(
            {
                'name': names[i].text,
                'sizes': sizes[i].text,
                'price': prices[i].text,
                'old_price': old_prices[i].text,
                'discount': discount[i].text,
                'href': item_link[i].find_element(By.TAG_NAME, value='a').get_attribute('href'),
                'img_link': item_link[i].find_element(By.TAG_NAME, value='img').get_attribute('src')
            }
    )
        
    with open(f'./.parsed/{category}.json', 'w', encoding='utf-8') as file:
        json.dump(parsed, file, indent=5, ensure_ascii=False)


def update_data():
    for i in urls.all_urls:
        # print(i)
        for k, v in i.items():
            get_data(v, k)

# update_data()

# get_data('https://www.staff-clothes.com/m/verkhnyaya-odezhda/c1038/?orderBy=DESC&sort=discount')
        