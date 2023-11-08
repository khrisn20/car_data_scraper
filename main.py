import requests
from bs4 import BeautifulSoup as bs

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
city = "tampa"
state_initials = "fl"
zip_code = "33602"
first_search_url = f"https://www.autotrader.com/cars-for-sale/all-cars/{city}-{state_initials}?zip={zip_code}"

response = request.get(first_search_url, headers=headers)
soup = bs(response.content, "html.parser")

search_results = soup.find("div", class_ = "padding-bottom-4 text-bold text-size-400 text-size-sm-500").text
search_results = search_results.split()[0]
first_record = 1
number_of_records_per_page = 100
url = f"https://www.autotrader.com/cars-for-sale/all-cars/{city}-{state_initials}?firstRecord={first_record}&isNewSearch=false&numRecords={number_of_records_per_page}&zip={zip_code}"

#while first_record < search_results:
    #Get Car Data (includes first)
    #cars_data = soup.find_all("h3")
    #for cd in cars_data:
    #    print(cd.text.split())

    #Get Car Mileage (skips first)
    #cars_mileage = soup.find_all("div", class_ = "item-card-specifications col-xs-9 margin-top-4 text-subdued-lighter")
    #for cm in cars_mileage:
    #    print(cm.text.split()[0])

    #Get Car Price (includes first)
    #cars_price = soup.find_all("span", class_ = "first-price text-ultra-bold")
    #for cp in cars_price:
    #    print(cp.text)
    
    #first_record += number_of_records_per_page



