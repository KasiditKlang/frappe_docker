from frappeclient import FrappeClient

client = FrappeClient("http://localhost:8080")
client.authenticate("2b569a6ac236864", "125c762ad812b07")

# Get Item DocType structure
doctype_meta = client.get_doc("DocType", "Item")

# Print all fields
for field in doctype_meta.get("fields", []):
    print(f"{field['fieldname']:30} | {field['fieldtype']:15} | Required: {field.get('reqd', 0)}")