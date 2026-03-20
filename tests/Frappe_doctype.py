from frappeclient import FrappeClient

client = FrappeClient("http://localhost:8080")
client.authenticate("2b569a6ac236864", "125c762ad812b07")

# Specific doctypes to retrieve
target_doctypes = ["Item", "Customer", "Supplier", "UOM", "Price List"]

print(f"Retrieving {len(target_doctypes)} DocTypes:\n")
for doctype_name in target_doctypes:
    print(f"- {doctype_name}")


