import requests

url = "https://greenbook.nafdac.gov.ng/"

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

    "start": 0,
    "length": 100,

    "search[value]": "",
    "search[regex]": "false",
    "search_ingredient": "",

    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
}

headers = {
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0",
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=30
)

response.raise_for_status()

data = response.json()

print("recordsTotal:", data["recordsTotal"])
print("recordsFiltered:", data["recordsFiltered"])
print("Records returned:", len(data["data"]))

print("\nCategories found in first 100 records:")

categories = {}

for product in data["data"]:
    category = product.get("product_category")

    if category:
        name = category.get("name")
        categories[name] = categories.get(name, 0) + 1
    else:
        categories["NO CATEGORY"] = categories.get("NO CATEGORY", 0) + 1

for category, count in categories.items():
    print(category, ":", count)