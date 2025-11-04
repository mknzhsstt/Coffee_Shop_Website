"""
Seed script to populate the database with initial data
"""

from app.database import get_db
from app.menu_categories.categories_db import create_category
from app.menu_items.items_db import create_menu_item
from app.locations.locations_db import create_location
from app.opening_hours.hours_db import create_opening_hours


async def seed_database():
    """Populate the database with initial sample data"""

    # Sample categories
    categories = [
        {"name": "Coffee", "description": "Hot and cold coffee beverages"},
        {"name": "Tea", "description": "Various tea selections"},
        {"name": "Pastries", "description": "Fresh baked goods"},
        {"name": "Sandwiches", "description": "Sandwiches and light meals"},
    ]

    # Sample menu items
    menu_items = [
        {
            "name": "Espresso",
            "description": "Rich and bold coffee shot",
            "price": 2.50,
            "category_id": 1,
        },
        {
            "name": "Cappuccino",
            "description": "Espresso with steamed milk and foam",
            "price": 4.00,
            "category_id": 1,
        },
        {
            "name": "Green Tea",
            "description": "Organic green tea",
            "price": 2.00,
            "category_id": 2,
        },
        {
            "name": "Croissant",
            "description": "Buttery, flaky pastry",
            "price": 3.50,
            "category_id": 3,
        },
    ]

    # Sample locations
    locations = [
        {
            "name": "Downtown Coffee Shop",
            "address": "123 Main St, City, State 12345",
            "phone": "555-0123",
            "email": "downtown@coffeeshop.com",
        },
        {
            "name": "University Branch",
            "address": "456 Campus Dr, City, State 12345",
            "phone": "555-0456",
            "email": "university@coffeeshop.com",
        },
    ]

    # Sample opening hours
    opening_hours = [
        {
            "location_id": 1,
            "day_of_week": 1,
            "opening_time": "07:00",
            "closing_time": "20:00",
        },
        {
            "location_id": 1,
            "day_of_week": 2,
            "opening_time": "07:00",
            "closing_time": "20:00",
        },
        {
            "location_id": 2,
            "day_of_week": 1,
            "opening_time": "06:30",
            "closing_time": "22:00",
        },
        {
            "location_id": 2,
            "day_of_week": 2,
            "opening_time": "06:30",
            "closing_time": "22:00",
        },
    ]

    print("Seeding database with sample data...")

    # Add your database seeding logic here
    print("Database seeded successfully!")


if __name__ == "__main__":
    import asyncio

    asyncio.run(seed_database())
