import csv
import pandas as pd
file = './big-mac-full-index.csv'
df = pd.read_csv(file)

def get_big_mac_price_by_year(year,country_code):
    

    country_code = country_code.upper()
    query_str = f"(iso_a3 == '{country_code}' and date >= '{year}-01-01' and date <= '{year}-12-31')"
    price_yr_df = df.query(query_str)
    price_by_country = round(price_yr_df['dollar_price'].mean(), 2)

    return price_by_country 


def get_big_mac_price_by_country(country_code):
    query_str = f"(iso_a3 == '{country_code.upper()}')"
    price_df = df.query(query_str)
    mean_price = round(price_df['dollar_price'].mean(), 2)

    return mean_price


def get_the_cheapest_big_mac_price_by_year(year):
    query_df = f"(iso_a3 == '{year}' and date <= '{year}')"
    cheapest_df = df.query(query_df)
    min_df = cheapest_df['dollar_price'].idxmin()
    min_price = cheapest_df.loc[min_df]
    min_BM = f"{min_price['name']}({min_price['iso_a3']}): ${round(min_price['dollar_price'], 1)}"
    
    return min_BM

    

def get_the_most_expensive_big_mac_price_by_year(year):
    max_year = f"(iso_a3 == '{year}' and date <= '{year}'))"
    max_q = df.query(max_year)
    max_item = max_q['dollar_price'].idxmax()
    max_loc = max_year.loc[max_item]
    max_price = f"{max_loc['name']}({max_loc['iso_a3']}): ${round(max_loc['dollar_price'], 1)}"
    return max_price



if __name__ == "__main__":
    print(get_big_mac_price_by_year(2006, 'usa'))
    print(get_big_mac_price_by_country('usa'))
    x = get_the_cheapest_big_mac_price_by_year (2008)
    print(x)
    