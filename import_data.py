from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

products = [
    # T-Shirts
    {"name": "White Basic T-Shirt", "category": "T-Shirt"},
    {"name": "Black Graphic T-Shirt", "category": "T-Shirt"},
    {"name": "Blue Striped T-Shirt", "category": "T-Shirt"},
    {"name": "Red Oversized T-Shirt", "category": "T-Shirt"},
    {"name": "Green Vintage T-Shirt", "category": "T-Shirt"},
    {"name": "Yellow Crop T-Shirt", "category": "T-Shirt"},
    {"name": "Pink Printed T-Shirt", "category": "T-Shirt"},
    {"name": "Grey Pocket T-Shirt", "category": "T-Shirt"},
    {"name": "Orange Tie Dye T-Shirt", "category": "T-Shirt"},
    {"name": "Purple Logo T-Shirt", "category": "T-Shirt"},
    {"name": "White V-Neck T-Shirt", "category": "T-Shirt"},
    {"name": "Black Long Sleeve T-Shirt", "category": "T-Shirt"},
    {"name": "Navy Polo T-Shirt", "category": "T-Shirt"},
    {"name": "Brown Henley T-Shirt", "category": "T-Shirt"},
    {"name": "Beige Linen T-Shirt", "category": "T-Shirt"},

    # Jackets
    {"name": "Black Leather Jacket", "category": "Jacket"},
    {"name": "Brown Denim Jacket", "category": "Jacket"},
    {"name": "Navy Bomber Jacket", "category": "Jacket"},
    {"name": "Grey Windbreaker Jacket", "category": "Jacket"},
    {"name": "Green Military Jacket", "category": "Jacket"},
    {"name": "White Puffer Jacket", "category": "Jacket"},
    {"name": "Red Varsity Jacket", "category": "Jacket"},
    {"name": "Camel Trench Coat Jacket", "category": "Jacket"},
    {"name": "Blue Quilted Jacket", "category": "Jacket"},
    {"name": "Black Zip Up Jacket", "category": "Jacket"},
    {"name": "Orange Parka Jacket", "category": "Jacket"},
    {"name": "Grey Fleece Jacket", "category": "Jacket"},
    {"name": "Olive Field Jacket", "category": "Jacket"},
    {"name": "Pink Cropped Jacket", "category": "Jacket"},

    # Pants
    {"name": "Blue Slim Fit Jeans", "category": "Pants"},
    {"name": "Black Skinny Jeans", "category": "Pants"},
    {"name": "Grey Cargo Pants", "category": "Pants"},
    {"name": "Beige Chino Pants", "category": "Pants"},
    {"name": "Navy Dress Pants", "category": "Pants"},
    {"name": "White Wide Leg Pants", "category": "Pants"},
    {"name": "Brown Corduroy Pants", "category": "Pants"},
    {"name": "Black Jogger Pants", "category": "Pants"},
    {"name": "Olive Straight Leg Pants", "category": "Pants"},
    {"name": "Grey Pleated Trousers", "category": "Pants"},
    {"name": "Dark Blue Bootcut Jeans", "category": "Pants"},
    {"name": "Cream Linen Pants", "category": "Pants"},
    {"name": "Red Plaid Pants", "category": "Pants"},
    {"name": "Black Leather Pants", "category": "Pants"},
    {"name": "White Lace Pants", "category": "Pants"},

    # Dresses
    {"name": "Floral Midi Dress", "category": "Dress"},
    {"name": "Black Mini Dress", "category": "Dress"},
    {"name": "White Maxi Dress", "category": "Dress"},
    {"name": "Red Evening Dress", "category": "Dress"},
    {"name": "Blue Wrap Dress", "category": "Dress"},
    {"name": "Pink Summer Dress", "category": "Dress"},
    {"name": "Yellow Sundress", "category": "Dress"},
    {"name": "Green Bodycon Dress", "category": "Dress"},
    {"name": "Purple Slip Dress", "category": "Dress"},
    {"name": "Orange Shirt Dress", "category": "Dress"},
    {"name": "Navy Pleated Dress", "category": "Dress"},
    {"name": "Beige Linen Dress", "category": "Dress"},
    {"name": "Black Off Shoulder Dress", "category": "Dress"},
    {"name": "White Lace Dress", "category": "Dress"},
    {"name": "Red Satin Dress", "category": "Dress"},

    # Shoes
    {"name": "White Leather Sneakers", "category": "Shoes"},
    {"name": "Black Running Shoes", "category": "Shoes"},
    {"name": "Brown Leather Boots", "category": "Shoes"},
    {"name": "Beige Suede Loafers", "category": "Shoes"},
    {"name": "Navy Canvas Sneakers", "category": "Shoes"},
    {"name": "Black High Heel Shoes", "category": "Shoes"},
    {"name": "White Slip On Shoes", "category": "Shoes"},
    {"name": "Grey Sport Shoes", "category": "Shoes"},
    {"name": "Red Platform Shoes", "category": "Shoes"},
    {"name": "Brown Chelsea Boots", "category": "Shoes"},
    {"name": "Black Ankle Boots", "category": "Shoes"},
    {"name": "White Chunky Sneakers", "category": "Shoes"},
    {"name": "Tan Sandals", "category": "Shoes"},
    {"name": "Black Oxford Shoes", "category": "Shoes"},
    {"name": "Navy Boat Shoes", "category": "Shoes"},
    {"name": "Pink Ballet Flats", "category": "Shoes"},
    {"name": "Grey Mule Shoes", "category": "Shoes"},
    {"name": "Brown Hiking Boots", "category": "Shoes"},

    # Accessories
    {"name": "Black Leather Belt", "category": "Accessories"},
    {"name": "Brown Leather Wallet", "category": "Accessories"},
    {"name": "Navy Baseball Cap", "category": "Accessories"},
    {"name": "White Sun Hat", "category": "Accessories"},
    {"name": "Black Wool Scarf", "category": "Accessories"},
    {"name": "Grey Knit Beanie", "category": "Accessories"},
    {"name": "Brown Leather Bag", "category": "Accessories"},
    {"name": "Black Crossbody Bag", "category": "Accessories"},
    {"name": "White Tote Bag", "category": "Accessories"},
    {"name": "Gold Chain Necklace", "category": "Accessories"},
    {"name": "Silver Hoop Earrings", "category": "Accessories"},
    {"name": "Black Sunglasses", "category": "Accessories"},
    {"name": "Brown Leather Gloves", "category": "Accessories"},
    {"name": "Red Knit Scarf", "category": "Accessories"},
    {"name": "Navy Bucket Hat", "category": "Accessories"},
    {"name": "Black Mini Backpack", "category": "Accessories"},
    {"name": "Tan Shoulder Bag", "category": "Accessories"},
    {"name": "Gold Watch", "category": "Accessories"},
    {"name": "Silver Bracelet", "category": "Accessories"},
    {"name": "Black Hair Clip", "category": "Accessories"},

    # Sportswear
    {"name": "Black Yoga Pants", "category": "Sportswear"},
    {"name": "Blue Sport Shorts", "category": "Sportswear"},
    {"name": "Grey Gym Hoodie", "category": "Sportswear"},
    {"name": "White Tennis Skirt", "category": "Sportswear"},
    {"name": "Pink Sports Bra", "category": "Sportswear"},
    {"name": "Black Compression Shorts", "category": "Sportswear"},
    {"name": "Navy Track Pants", "category": "Sportswear"},
    {"name": "Green Running Jacket", "category": "Sportswear"},
    {"name": "White Gym Tank Top", "category": "Sportswear"},
    {"name": "Grey Sweatpants", "category": "Sportswear"},
    {"name": "Blue Cycling Shorts", "category": "Sportswear"},
    {"name": "Orange Workout Hoodie", "category": "Sportswear"},
    {"name": "Black Athletic Leggings", "category": "Sportswear"},
    {"name": "Red Sport Jersey", "category": "Sportswear"},
    {"name": "Purple Zip Up Hoodie", "category": "Sportswear"},

    # Hoodies & Sweaters
    {"name": "Grey Pullover Hoodie", "category": "Hoodie"},
    {"name": "Black Zip Hoodie", "category": "Hoodie"},
    {"name": "Navy Crewneck Sweater", "category": "Hoodie"},
    {"name": "White Knit Sweater", "category": "Hoodie"},
    {"name": "Green Oversized Hoodie", "category": "Hoodie"},
    {"name": "Brown Turtleneck Sweater", "category": "Hoodie"},
    {"name": "Pink Cardigan Sweater", "category": "Hoodie"},
    {"name": "Blue Cable Knit Sweater", "category": "Hoodie"},
    {"name": "Red Christmas Sweater", "category": "Hoodie"},
    {"name": "Beige Wool Sweater", "category": "Hoodie"},
    {"name": "Orange Tie Dye Hoodie", "category": "Hoodie"},
    {"name": "Purple Fleece Hoodie", "category": "Hoodie"},

    # Shorts
    {"name": "Blue Denim Shorts", "category": "Shorts"},
    {"name": "Black Biker Shorts", "category": "Shorts"},
    {"name": "Khaki Chino Shorts", "category": "Shorts"},
    {"name": "White Linen Shorts", "category": "Shorts"},
    {"name": "Navy Swim Shorts", "category": "Shorts"},
    {"name": "Grey Sweat Shorts", "category": "Shorts"},
    {"name": "Green Cargo Shorts", "category": "Shorts"},
    {"name": "Red Board Shorts", "category": "Shorts"},
    {"name": "Pink Floral Shorts", "category": "Shorts"},
    {"name": "Brown Leather Shorts", "category": "Shorts"},
]

try:
    es.indices.delete(index="products")
    print("Deleted old index")
except:
    print("No old index found, creating new...")

es.indices.create(index="products", mappings={
    "properties": {
        "name": {"type": "text"},
        "category": {"type": "keyword"}
    }
})

for i, product in enumerate(products):
    es.index(index="products", id=i, document=product)

print(f"Done! Imported {len(products)} products.")