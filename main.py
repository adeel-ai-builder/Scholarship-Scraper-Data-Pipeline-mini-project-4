import pandas as pd
from scraper import scrape_all_pages
from database import save_to_database

def main():
    print("Starting Scholarship Scraper...\n")
    data=scrape_all_pages(total_pages=5)

    if not data:
        print("No Data found ...")
        return

    df=pd.DataFrame(data)
    df.drop_duplicates(inplace=True) 
    df["deadline"] = pd.to_datetime(df["deadline"], errors="coerce")
    
    df.to_csv("data/scholarships.csv", index=False)  
    print("CSV file saved successfully!")

    save_to_database(df)
    print("\nScraping Completed Successfully!")
if __name__ == "__main__":
    main()