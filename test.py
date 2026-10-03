import requests

url = "https://greenbook.nafdac.gov.ng/"

params = {
    "draw": 1,

    "columns[0][data]": "product_name",
    "columns[0][name]": "product_name",
    "columns[0][searchable]": "true",
    "columns[0][orderable]": "true",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",

    "columns[1][data]": "ingredient.ingredient_name",
    "columns[1][name]": "ingredient.ingredient_name",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",

    "columns[2][data]": "product_category.name",
    "columns[2][name]": "product_category.name",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "false",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",

    "columns[3][data]": "product_category_id",
    "columns[3][name]": "product_category_id",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",

    "columns[5][data]": "NAFDAC",
    "columns[5][name]": "NAFDAC",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",

    "columns[9][data]": "applicant.name",
    "columns[9][name]": "applicant.name",
    "columns[9][searchable]": "true",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",

    "columns[10][data]": "approval_date",
    "columns[10][name]": "approval_date",
    "columns[10][searchable]": "true",
    "columns[10][orderable]": "true",
    "columns[10][search][value]": "",
    "columns[10][search][regex]": "false",

    "columns[11][data]": "status",
    "columns[11][name]": "status",
    "columns[11][searchable]": "true",
    "columns[11][orderable]": "true",
    "columns[11][search][value]": "",
    "columns[11][search][regex]": "false",

    "order[0][column]": "0",
    "order[0][dir]": "asc",

    "start": 100,
    "length": 100,

    "search[value]": "",
    "search[regex]": "false",
    "search_ingredient": "",
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0",
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=30
)

print("Status:", response.status_code)
print("URL:", response.url)

# print(response.text[:2000])
data = response.json()

categories = {}

for product in data["data"]:
    category = product.get("product_category")

    if category:
        category_id = category.get("id")
        category_name = category.get("name")

        categories[category_id] = category_name

print("\nCategories found:")
for category_id, category_name in categories.items():
    print(category_id, "=", category_name)

print("Total:", data["recordsTotal"])
print("Filtered:", data["recordsFiltered"])
print("Returned:", len(data["data"]))

for product in data["data"]:
    print(
        product["product_id"],
        product["product_name"],
        product["NAFDAC"],
        product["status"]
    )
    data = response.json()

print("Total:", data["recordsTotal"])
print("Filtered:", data["recordsFiltered"])
print("Returned:", len(data["data"]))

for product in data["data"]:
    print(
        product["product_id"],
        "|",
        product["product_name"],
        "|",
        product["NAFDAC"],
        "|",
        product["status"]
    )

    response = requests.get(url, params=params, headers=headers)

print("Status:", response.status_code)

data = response.json()

print("Total:", data["recordsTotal"])
print("Filtered:", data["recordsFiltered"])
print("Returned:", len(data["data"]))

for product in data["data"][:10]:
    print(
        product["product_id"],
        "|",
        product["product_name"],
        "|",
        product.get("NAFDAC"),
        "|",
        product.get("product_category", {}).get("name")
    )