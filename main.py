import requests
from bs4 import BeautifulSoup as bs

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }               

city = "tampa"
state_initials = "fl"
zip_code = "33602"

first_search_url = f"https://www.autotrader.com/cars-for-sale/all-cars/{city}-{state_initials}?zip={zip_code}"

response = requests.get(first_search_url, headers=headers)
soup = bs(response.content, "html.parser")

#Get Total Search Results
search_results = soup.find("div", class_ = "padding-bottom-4 text-bold text-size-400 text-size-sm-500").text
search_results = int(search_results.split()[0].replace(",", ""))


first_record = 1
number_of_records_per_page = 100
url_base = f"https://www.autotrader.com/cars-for-sale/all-cars/{city}-{state_initials}?isNewSearch=false&zip={zip_code}"

cars_data = []
while first_record < search_results:
    #Get Random Proxy


    #Build URL
    url = f"{url_base}&firstRecord={first_record}&numRecords={number_of_records_per_page}"
    
    #Make GET Request
    response = requests.get(url, headers=headers)
    soup = bs(response.content, "html.parser")
    
    #Get Car Data From Soup
    cars_description = soup.find_all("h3")
    del cars_description[0]

    cars_price = soup.find_all("span", class_ = "first-price text-ultra-bold")
    del cars_price[0]

    cars_mileage = soup.find_all("div", class_ = "item-card-specifications col-xs-9 margin-top-4 text-subdued-lighter")

    for i in range(len(cars_description)):
        car = cars_description[i].text.split()
        price = cars_price[i].text
        mileage = cars_mileage[i].text.split()[0]
    
        car.append(price)
        car.append(mileage)
        cars_data.append(car)

    #Increment Counter    
    first_record += number_of_records_per_page



