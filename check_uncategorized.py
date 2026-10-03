import json

with open("data/all_products.json", encoding="utf-8") as file:
    products = json.load(file)

uncategorized = []

for product in products:
    category = product.get("product_category")

    if not category:
        uncategorized.append(product)

print("Total products:", len(products))
print("Without category:", len(uncategorized))

for product in uncategorized:
    print(
        product.get("product_id"),
        "|",
        product.get("product_name"),
        "|",
        product.get("NAFDAC"),
        "|",
        product.get("status")
    )