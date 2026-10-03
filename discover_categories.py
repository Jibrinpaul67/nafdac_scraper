import requests

url = "https://greenbook.nafdac.gov.ng/"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0",
}


def get_category(category_id):

    params = {
        "draw": 1,

        "columns[0][data]": "product_name",
        "columns[1][data]": "ingredient.ingredient_name",
        "columns[2][data]": "product_category.name",

        "columns[3][data]": "product_category_id",
        "columns[3][search][value]": str(category_id),

        "columns[5][data]": "NAFDAC",
        "columns[9][data]": "applicant.name",
        "columns[10][data]": "approval_date",
        "columns[11][data]": "status",

        "start": 0,
        "length": 1,

        "search[value]": "",
        "search_ingredient": "",
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


print("Searching for NAFDAC product categories...\n")

for category_id in range(1, 15):

    try:

        data = get_category(category_id)

        filtered = data["recordsFiltered"]

        if filtered > 0 and data["data"]:

            product = data["data"][0]

            category = product.get("product_category", {})

            print(
                f"ID {category_id}: "
                f"{category.get('name')} "
                f"({filtered} products)"
            )

    except Exception as e:

        print(f"Error checking category {category_id}: {e}")