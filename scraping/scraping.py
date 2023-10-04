
import os
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
import time

# Set ChromeDriver options (headless mode)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Provide the path to the ChromeDriver executable
chromedriver_path = "/home/blackbird/Desktop/scripts/python/scraping/chromedriver"

# Initialize the WebDriver
service = webdriver.ChromeService(executable_path=chromedriver_path)
wd = webdriver.Chrome(service=service, options=chrome_options)

def get_all_images(driver, url, delay, max_images):
    def scroll_down(web_driver):
        web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    driver.get(url)

    image_urls = set()

    while len(image_urls) < max_images:
        scroll_down(driver)
        time.sleep(delay)
        thumbnails = driver.find_elements(By.CLASS_NAME, "Q4LuWd")
        for image in thumbnails[len(image_urls):]:
            if len(image_urls) == max_images:
                break
            print("Length - ", len(image_urls))
            try:
                image.click()
                time.sleep(1)
            except Exception as e:
                print(f"Error clicking image: {str(e)}")
                continue
            else:
                images = driver.find_elements(By.CLASS_NAME, "r48jcc")
                for i in images:
                    src = i.get_attribute("src")
                    if src and "http" in src:
                        image_urls.add(src)
                        if len(image_urls) >= max_images:
                            break

    return image_urls

def download_images(download_folder, image_urls):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for idx, src in enumerate(image_urls):
        file_name = f"image_{idx+1}.jpg"
        try:
            download_image(download_folder, src, file_name)
        except Exception as e:
            print(f"Error downloading image {idx+1}: {str(e)}")

def download_image(download_folder, src, file_name):
    image = requests.get(src).content
    image_bin = io.BytesIO(image)
    image_inside = Image.open(image_bin)
    path = os.path.join(download_folder, file_name)
    with open(path, "wb") as f:
        image_inside.save(f, "JPEG")

puppies = "https://www.google.com/search?q=puppies+desktop+wallpaper+hd&tbm=isch&ved=2ahUKEwjeh8Pc-tyBAxWH5TgGHQmBAAcQ2-cCegQIABAA&oq=puppies+desktop+wall&gs_lcp=CgNpbWcQARgBMgUIABCABDIFCAAQgAQyBggAEAUQHjIGCAAQBRAeMgYIABAFEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeOgcIABCKBRBDOgsIABCABBCxAxCDAToICAAQgAQQsQM6CggAEIoFELEDEENQjwtYpCtglDRoAHAAeACAAWCIAdAMkgECMjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAMABAQ&sclient=img&ei=WaYdZZ73NIfL4-EPiYKCOA&bih=939&biw=1920"
max_images_to_download = 20
download_folder = os.getcwd() + "/" + "puppies"

image_urls = get_all_images(wd, puppies, 1, max_images_to_download)
download_images(download_folder, image_urls)
