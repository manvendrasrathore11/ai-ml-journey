import smtplib
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/Dovety-Electric-Replaceable-Extension-Adjustable/dp/B0DDXCCXPC/ref=sr_1_3_sspa?_encoding=UTF8&content-id=amzn1.sym.4da186f5-145b-4e27-9ae2-777c48d6d9cd&dib=eyJ2IjoiMSJ9.SIiusJOq0P1CRDJtAomA64Rg6HIMWSmZUL8bNxTKWnBTH3CQPE_hLr0xw4gR4rE9FGXsStk8ogfpkBrGZsY-ZHYiMqzS-OdQ-L5cV-kPCLSW1cA63yWuRHTc3iebHV4f9NfRnfvMG3ueDO05f_m9juPEioBM3Go5v-S2et5erxaqeop6RMaa9QrsKdMDCooIzmF3dsmjSKN8zwMnEVpIV5dkT-sCahAqfoo4zxoRi8ElXxJFPwbBwsSNyZ4nePbrnWjDrs8-LDbJIHZXVJVpTrSd4qeObYrpjou9ugwEISU.GZhsCpGgFAkLzyjIs9Xe4ABs_vRTTXWQ6LrQukMFUPU&dib_tag=se&keywords=cleaning%2Btools&pd_rd_r=0d7b84c4-63d9-49df-b8d5-06ddd1d1f62e&pd_rd_w=0CUPS&pd_rd_wg=O7hIr&qid=1752871810&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
MY_EMAIL =  "man.day.32.python@gmail.com"
PASSWORD = "ctyblzjujnpasswr"

# headers = {
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
# "Accept-Encoding": "gzip, deflate, br, zstd",
# "Accept-Language": "en-US,en;q=0.9",
# "Priority": "u=0, i",
# "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
# "Sec-Ch-Ua-Mobile": "?0",
# "Sec-Ch-Ua-Platform": "\"Windows\"",
# "Sec-Fetch-Dest": "document",
# "Sec-Fetch-Mode": "navigate",
# "Sec-Fetch-Site": "cross-site",
# "Sec-Fetch-User": "?1",
# "Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
# }

headers = {
"Accept-Language": "en-US,en;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}



response = requests.get(url=URL , headers= headers)

amazon_web_page = response.text

SOUP = BeautifulSoup(amazon_web_page,"html.parser")

price = SOUP.find(name = "span",class_ = "a-price-whole").get_text()

print(price)
# Convert to floating point number
price_as_float = float(price)
print(price_as_float)




title = SOUP.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 400


if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
    connection.starttls()
    result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
    connection.sendmail(
        from_addr=os.environ["EMAIL_ADDRESS"],
        to_addrs="manvendrasrathore11@gmail.com",
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
    )

