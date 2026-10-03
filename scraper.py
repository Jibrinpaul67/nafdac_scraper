import requests
import json
import time
from pathlib import Path


URL = "https://greenbook.nafdac.gov.ng/"

CATEGORIES = {
    1: "Drugs",
    2: "Vaccines and Biologics",
    5: "Medical devices",
    6: "Veterinary",
    7: "Herbals and Nutraceuticals",
}

PAGE_SIZE = 100

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0",
}


def get_products(category_id, start):

    params = {
        "draw": 1,

        "columns[0][data]": "product_name",
        "columns[1][data]": "ingredient.ingredient_name",
        "columns[2][data]": "product_category.name",
        "columns[3][data]": "product_category_id",
        "columns[4][data]": "ingredient.synonym",
        "columns[5][data]": "NAFDAC",
        "columns[6][data]": "form.name",
        "columns[7][data]": "route.name",
        "columns[8][data]": "strength",
        "columns[9][data]": "applicant.name",
        "columns[10][data]": "approval_date",
        "columns[11][data]": "status",

        "start": start,
        "length": PAGE_SIZE,

        "search[value]": "",
        "search[regex]": "false",
        "search_ingredient": "",

        # Category filter
        "columns[3][search][value]": str(category_id),
    }

    response = requests.get(
        URL,
        params=params,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def scrape_category(category_id, category_name):

    print()
    print("=" * 60)
    print(f"SCRAPING: {category_name}")
    print("=" * 60)

    start = 0
    all_products = []

    while True:

        print(f"Fetching records {start} - {start + PAGE_SIZE}...")

        data = get_products(category_id, start)

        products = data.get("data", [])

        if not products:
            break

        all_products.extend(products)

        total = data["recordsFiltered"]

        print(
            f"Received {len(products)} records "
            f"({len(all_products)} / {total})"
        )

        if len(all_products) >= total:
            break

        start += PAGE_SIZE

        # Be polite to the server
        time.sleep(0.5)

    print(f"Finished {category_name}: {len(all_products)} records")

    return all_products


def main():

    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)

    all_products = []

    for category_id, category_name in CATEGORIES.items():

        products = scrape_category(
            category_id,
            category_name
        )

        all_products.extend(products)

        filename = (
            output_dir /
            f"{category_id}_{category_name.lower().replace(' ', '_')}.json"
        )

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                products,
                file,
                ensure_ascii=False,
                indent=2
            )

        print(f"Saved: {filename}")


    with open(
        output_dir / "all_products.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_products,
            file,
            ensure_ascii=False,
            indent=2
        )

    print()
    print("=" * 60)
    print("SCRAPING COMPLETE")
    print("=" * 60)
    print(f"Total products collected: {len(all_products)}")


if __name__ == "__main__":
    main()