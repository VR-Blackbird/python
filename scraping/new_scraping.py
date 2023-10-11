import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import requests
import time
import os
from multiprocessing import Pool



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


chrome_driver_path = "/home/blackbird/Desktop/scripts/python/scraping/chromedriver"

service = webdriver.ChromeService(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)



def get_all_images(driver, delay, url, max_images=20):
  
    driver.get(url)

    image_urls = set()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)
    while len(image_urls) <= max_images:
        thumbnails = driver.find_elements(By.CLASS_NAME, "Q4LuWd")
        for image in thumbnails:
            try:
                image.click()
                time.sleep(delay)
            except Exception as e:
                print("Unable to click image")
                continue
            else:
                images = driver.find_elements(By.CLASS_NAME, "sFlh5c")
                time.sleep(delay)
                for i in images:
                    src = i.get_attribute("src")
                    if src and "http" in src:
                        image_urls.add(src)
                        print("Added Image ", src)
                        print(len(image_urls))
                        if len(image_urls) >= max_images:
                            print("All images queried")
                            return image_urls

        


image_url = "https://www.google.com/search?q=messi&sca_esv=572573644&hl=en-US&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjUut6MuO6BAxVz2DgGHWb7CJMQ_AUoAnoECAMQBA&biw=1920&bih=971&dpr=1"


all_images = get_all_images(driver, 1, image_url)

def download_images(image, idx, folder):
    img = requests.get(image).content
    img_byte = io.BytesIO(img)
    prop_image = Image.open(img_byte)

    path = folder + "/" + f"messi-{idx+1}.jpg"
    with open(path, "wb") as f:
        prop_image.save(f, "JPEG")

folder_name = os.path.dirname(os.path.realpath(__file__)) + "/" + "messi"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

with Pool(processes=5) as pool:
    pool.starmap(download_images, [(url, idx, folder_name) for idx, url in  enumerate(all_images)])

# download_images(all_images, folder_name)