def main():
    # Configuration
    #URL = "http://site2.local:8000"
    #API_KEY = "your_api_key"
    #API_SECRET = "your_api_secret"
    
    BASE_URL = "http://localhost:8080"
    API_KEY = "2b569a6ac236864"
    API_SECRET = "4a3efd5987ec14c"
 
    manager = FrappeManager(BASE_URL, API_KEY, API_SECRET)
    
    # Initialize manager
    #manager = FrappeManager(URL, API_KEY, API_SECRET)
    
    # CREATE
    customer = manager.create("Customer", {
        "customer_name": "ACME Corporation",
        "customer_type": "Company",
        "customer_group": "Commercial",
        "territory": "All Territories"
    })
    customer_id = customer['name']
    
    # READ
    customer_data = manager.read("Customer", customer_id)
    print(f"Customer: {customer_data['customer_name']}")
    
    # UPDATE
    manager.update("Customer", customer_id, {
        "mobile_no": "+1234567890",
        "email_id": "contact@acme.com"
    })
    
    # LIST
    customers = manager.list_all(
        "Customer",
        fields=["name", "customer_name", "customer_type"],
        filters=[["customer_type", "=", "Company"]],
        limit=10
    )
    print(f"Found {len(customers)} companies")
    
    # SEARCH
    results = manager.search("Customer", "ACME", "customer_name")
    print(f"Search results: {len(results)}")
    
    # COUNT
    total = manager.get_count("Customer")
    print(f"Total customers: {total}")
    
    # BULK CREATE
    bulk_data = [
        {"customer_name": "Company A", "customer_type": "Company", 
         "customer_group": "Commercial", "territory": "All Territories"},
        {"customer_name": "Company B", "customer_type": "Company", 
         "customer_group": "Commercial", "territory": "All Territories"},
    ]
    # results = manager.bulk_create("Customer", bulk_data)
    
    # DELETE (commented for safety)
    # manager.delete("Customer", customer_id)

if __name__ == "__main__":
    main()