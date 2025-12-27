#!/usr/bin/env python3
"""
API Docs BS Generator - Because real documentation is just too mainstream.
When the API docs are written by someone who's never actually used the API.
"""

import random
import json
from datetime import datetime

# The sacred texts of API documentation
ENDPOINTS = [
    "/api/v1/{resource}/magic",
    "/api/v2/{id}/transform",
    "/internal/{secret}/endpoint",
    "/legacy/{deprecated}/still_works"
]

PARAMETERS = [
    "offset", "limit", "sort", "filter", "q", "api_key",
    "callback", "format", "version", "timestamp", "signature"
]

ERRORS = [
    "400: Invalid parameter 'foo' (but we won't tell you which one)",
    "401: Authentication failed (try adding ?auth=true)",
    "403: Forbidden (but the real reason is a typo in our code)",
    "404: Endpoint not found (it was deprecated 3 years ago)",
    "429: Rate limited (limit: 1 request per hour)",
    "500: Internal server error (it's always our fault)"
]

RESPONSES = [
    {"status": "success", "data": {"id": 123}},
    {"error": "Something went wrong", "code": 42},
    {"result": "pending", "estimated_completion": "soon"},
    {"items": [], "total": 0, "page": 1}
]


def generate_docs(api_name="MyAwesomeAPI"):
    """Generate documentation that looks legit but is utterly useless."""
    
    docs = {
        "api_name": api_name,
        "version": f"{random.randint(1, 3)}.{random.randint(0, 9)}",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "base_url": f"https://api.{api_name.lower()}.com",
        "endpoints": [],
        "common_parameters": random.sample(PARAMETERS, random.randint(3, 6)),
        "authentication": "API key required (or maybe OAuth? We're not sure)",
        "rate_limiting": f"{random.randint(10, 1000)} requests per {random.choice(['minute', 'hour', 'day'])}",
        "important_notes": [
            "All dates are in UTC (or maybe local time?)",
            "Responses are JSON (except when they're XML)",
            "This API is in beta (since 2018)"
        ]
    }
    
    # Generate some "helpful" endpoints
    for i in range(random.randint(2, 4)):
        endpoint = random.choice(ENDPOINTS)
        docs["endpoints"].append({
            "method": random.choice(["GET", "POST", "PUT", "DELETE"]),
            "path": endpoint.replace("{resource}", random.choice(["users", "items", "widgets"])),
            "description": f"{random.choice(['Retrieves', 'Creates', 'Updates', 'Deletes'])} {random.choice(['data', 'resources', 'entities'])}",
            "parameters": random.sample(PARAMETERS, random.randint(2, 4)),
            "example_response": random.choice(RESPONSES),
            "errors": random.sample(ERRORS, random.randint(1, 3))
        })
    
    return docs


def main():
    """Because reading real docs is for suckers."""
    print("\n=== API Documentation BS Generator ===\n")
    print("Generating documentation that looks official but provides zero actual help...\n")
    
    api_name = input("Enter API name (or press Enter for random): ").strip()
    if not api_name:
        api_name = random.choice(["CloudService", "DataPlatform", "MicroAPI"])
    
    docs = generate_docs(api_name)
    
    print(f"\n=== {docs['api_name']} API Documentation ===")
    print(f"Version: {docs['version']}")
    print(f"Base URL: {docs['base_url']}\n")
    
    print("Endpoints:")
    for endpoint in docs["endpoints"]:
        print(f"  {endpoint['method']} {endpoint['path']}")
        print(f"    Desc: {endpoint['description']}")
        print(f"    Params: {', '.join(endpoint['parameters'])}")
        
    print(f"\nCommon Parameters: {', '.join(docs['common_parameters'])}")
    print(f"\nAuthentication: {docs['authentication']}")
    print(f"Rate Limiting: {docs['rate_limiting']}")
    
    print("\nImportant Notes:")
    for note in docs["important_notes"]:
        print(f"  • {note}")
    
    print("\n\n(For actual working examples, please consult Stack Overflow)\n")
    
    # Save to file because why not
    with open(f"{api_name.lower()}_docs.json", "w") as f:
        json.dump(docs, f, indent=2)
    print(f"Documentation saved to {api_name.lower()}_docs.json")
    print("(File contains the same amount of useful information as the console output)\n")


if __name__ == "__main__":
    main()
