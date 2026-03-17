def parse_scholarships(soup):
    scholarships = []

    items = soup.find_all("div", class_="quote")

    for item in items:
        title = item.find("span", class_="text").text.strip()
        author = item.find("small", class_="author").text.strip()

        scholarships.append({
            "title": title,
            "country": author,   # using author as dummy column
            "deadline": "N/A",
            "link": "N/A"
        })

    return scholarships