import datetime
import json
import time
import random
import os
from bs4 import BeautifulSoup
from curl_cffi import requests

AFFILIATE_TAG = "1097fa-20"

input_catalog = {
    "Nursery & Furniture": {
        "Crib or Bassinet": {
            "Budget": "https://www.amazon.com/dp/B002MZMDX8/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B010S7VZ6W/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0148KHE7O/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B0F23LPQSV/?tag=1097fa-20"
        },
        "Nursery Glider": {
            "Budget": "https://www.amazon.com/dp/B00I5ELBA6/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B072VGKCFZ/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0192SZGNQ/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B0CZ6M96RR/?tag=1097fa-20"
        },
        "Mattress & Sheets": {
            "Budget": "https://www.amazon.com/dp/B004044LD4/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B004EWG4ZA/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B00WR958TA/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B07NQN9XBT/?tag=1097fa-20"
        },
        "Baby Monitor": {
            "Budget": "https://www.amazon.com/dp/B00JEV5UI8/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B09GM8JZM9/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B08FF4GV5C/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B0B5283WSZ/?tag=1097fa-20"
        },
        "Sound Machine": {
            "Budget": "https://www.amazon.com/dp/B01D50RYSC/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B0C5S8VB2K/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0D6SX8VLQ/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B06XMRCC94/?tag=1097fa-20"
        }
    },
    "Travel & Gear": {
        "Infant Car Seat": {
            "Budget": "https://www.amazon.com/dp/B07Y5S4VWT/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B09LKZFKGD/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0DHLQL58Y/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B0987YSHNY/?tag=1097fa-20"
        },
        "Travel Stroller": {
            "Budget": "https://www.amazon.com/dp/B07P1YSC18/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B019DHBCXE/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0BYTKYGZ3/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B0D9XS9VXL/?tag=1097fa-20"
        },
        "Baby Carrier": {
            "Budget": "https://www.amazon.com/dp/B00M0DWQYI/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B079TFMCHY/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B07B41952V/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B092FM5KJ7/?tag=1097fa-20"
        },
        "Diaper Bag": {
            "Budget": "https://www.amazon.com/dp/B0FSLB42V3/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B07C3SWZXK/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0BSKZFV8Z/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B0DNWZ1KV8/?tag=1097fa-20"
        }
    },
    "Feeding & Nursing": {
        "Bottle Starter Set": {
            "Budget": "https://www.amazon.com/dp/B00RVIOQLI/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B0964CHD65/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0F54RHSM7/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B0FPGB6D2G/?tag=1097fa-20"
        },
        "Nursing Pillow": {
            "Budget": "https://www.amazon.com/dp/B0F8LDHL26/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B0F6T5VNRX/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B08J54C2Y8/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B08SMT92PK/?tag=1097fa-20"
        },
        "High Chair": {
            "Budget": "https://www.amazon.com/dp/B01JRY07BQ/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B00PTL13LA/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0D5KLGSYS/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B006T6CKG6/?tag=1097fa-20"
        },
        "Burp Cloths": {
            "Budget": "https://www.amazon.com/dp/B0757FF5Z9/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B08CBJ2SSQ/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B079MFDF4M/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B00N4PNYRY/?tag=1097fa-20"
        },
        "Breast Pump": {
            "Budget": "https://www.amazon.com/dp/B0006HBS1M/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B00BLBLR1I/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B00DBKFFJM/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B07G375DHR/?tag=1097fa-20"
        }
    },
    "Diapering Needs": {
        "Diapers (Starter Supply)": {
            "Budget": "https://www.amazon.com/dp/B00FF79658/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B0178B04JK/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0CKV2ZL1Y/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B0B5YCSGDD/?tag=1097fa-20"
        },
        "Baby Wipes": {
            "Budget": "https://www.amazon.com/dp/B07H53W5WP/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B07SCL613T/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B008KJEYLO/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B01LXNICJF/?tag=1097fa-20"
        },
        "Diaper Pail": {
            "Budget": "https://www.amazon.com/dp/B0D37YXJBF/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B01BDQDIGM/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0CK2K6JXD/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B09RCPTWB4/?tag=1097fa-20"
        },
        "Changing Pad": {
            "Budget": "https://www.amazon.com/dp/B009EDSWJA/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B00O64QJOC/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B075X8TPMN/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B004FTTV5W/?tag=1097fa-20"
        },
        "Diaper Cream": {
            "Budget": "https://www.amazon.com/dp/B07H7GBJC4/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B0107QP1VE/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B01LZF07GU/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B0825WHHGJ/?tag=1097fa-20"
        }
    },
    "Clothing & Basics": {
        "Sleep & Plays": {
            "Budget": "https://www.amazon.com/dp/B07NSNHX12/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B08BV38H37/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0CN3CHM3T/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B0G232YTND/?tag=1097fa-20"
        },
        "Bodysuits": {
            "Budget": "https://www.amazon.com/dp/B007CRR7Z0/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B083X7MVK8/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B08X8JG5G7/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B08G5WTTLZ/?tag=1097fa-20"
        },
        "Swaddle Blankets": {
            "Budget": "https://www.amazon.com/dp/B077G8FMBY/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B07C8L4CTZ/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0B75QS1RF/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B09Y8SNJ15/?tag=1097fa-20"
        },
        "Socks": {
            "Budget": "https://www.amazon.com/dp/B00X21MRHI/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B0733N7PLQ/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B07SH3H9WV/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B07D49GDQK/?tag=1097fa-20"
        }
    },
    "Bath & Health": {
        "Baby Bathtub": {
            "Budget": "https://www.amazon.com/dp/B000067EH7/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B099FM4W4H/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0DVLQN538/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B07RJ3C7DX/?tag=1097fa-20"
        },
        "Healthcare Kit": {
            "Budget": "https://www.amazon.com/dp/B00VXMXN30/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B01J8C1VVC/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0DP4TXLP9/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B075G6XMSF/?tag=1097fa-20"
        },
        "Towels & Washcloths": {
            "Budget": "https://www.amazon.com/dp/B07ZSCJB4K/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B00X22L0AC/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0992BFRRF/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B081SFS6SW/?tag=1097fa-20"
        },
        "Baby Wash": {
            "Budget": "https://www.amazon.com/dp/B07D2JMJPS/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B004L5JCZ4/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0FY3YPZCG/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B000P7M26I/?tag=1097fa-20"
        },
        "Nasal Aspirator": {
            "Budget": "https://www.amazon.com/dp/B001OTK6JG/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B00171WXII/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B07N28G62S/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B08G6SZ2LT/?tag=1097fa-20"
        }
    },
    "Play & Soothing": {
        "Bouncer or Swing": {
            "Budget": "https://www.amazon.com/dp/B00KHR7TPK/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B0GD8VN5WX/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B0D5DL7RWZ/?tag=1097fa-20",
            "Luxury": "https://www.amazon.com/dp/B0B3F93NYT/?tag=1097fa-20"
        },
        "Play Mat": {
            "Budget": "https://www.amazon.com/dp/B0D7P22KPN/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B076HYSWB9/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B075R8BXXC/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B0CD2WMW6Y/?tag=1097fa-20"
        },
        "Pacifier Pack": {
            "Budget": "https://www.amazon.com/dp/B0D82PQKPC/?tag=1097fa-20",
            "Standard": "https://www.amazon.com/dp/B0DPN9YJSW/?tag=1097fa-20",
            "Premium": "https://www.amazon.com/dp/B08L9HV8JC/?tag=1097fa-20",
            "Organic": "https://www.amazon.com/dp/B09X1YTHWS/?tag=1097fa-20"
        }
    }
}

old_data = {}
if os.path.exists('products.json'):
    try:
        with open('products.json', 'r') as f:
            old_db = json.load(f)
            for cat_name, cat_items in old_db.items():
                if cat_name == "_metadata": continue
                for item in cat_items:
                    for tier in item.get('tiers', []):
                        if "link" in tier:
                            old_data[tier["link"]] = tier
        print("[+] Successfully loaded previous products.json for backup data.")
    except Exception as e:
        print(f"[!] Could not load backup data: {e}")

def get_amazon_data(url, max_retries=3):
    if url == "#" or "EXAMPLE_ASIN" in url: 
        return "Placeholder Item", 0.00, "https://dummyimage.com/400x300/1e293b/f8fafc.png&text=No+Link", 0.0, 0

    browsers = ["chrome110", "chrome120", "safari15_3", "edge101"]

    for attempt in range(max_retries):
        try:
            browser = random.choice(browsers)
            response = requests.get(url, impersonate=browser, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")

            title = "Amazon Product"
            price = 0.00
            img = "https://dummyimage.com/400x300/1e293b/f8fafc.png&text=Image+Error"
            rating = 0.0
            reviews = 0

            title_tag = soup.find(id="productTitle")
            if title_tag: title = title_tag.text.strip()

            buy_box = soup.find(id="corePriceDisplay_desktop_feature_div") or \
                      soup.find(id="corePrice_feature_div") or \
                      soup.find(id="centerCol")

            search_area = buy_box if buy_box else soup

            price_whole = search_area.find("span", class_="a-price-whole")
            price_fraction = search_area.find("span", class_="a-price-fraction")
            
            if price_whole and price_fraction:
                clean_price = price_whole.text.replace(',', '').replace('.', '').strip() + '.' + price_fraction.text.strip()
                try:
                    price = float(clean_price)
                except ValueError:
                    price = 0.00

            rating_tag = soup.find("span", class_="a-icon-alt")
            if rating_tag:
                try: rating = float(rating_tag.text.split()[0])
                except: pass

            review_tag = soup.find("span", id="acrCustomerReviewText") or soup.find("span", {"data-hook": "total-review-count"})
            if review_tag:
                try:
                    review_text = review_tag.text.replace(',', '')
                    reviews = int(''.join(filter(str.isdigit, review_text)))
                except: pass

            img_tag = soup.find("img", id="landingImage") or soup.find("img", id="imgBlkFront")
            if img_tag:
                temp_img = None
                
                if img_tag.has_attr("data-a-dynamic-image"):
                    try:
                        dynamic_images = json.loads(img_tag["data-a-dynamic-image"])
                        urls = list(dynamic_images.keys())
                        if urls: temp_img = urls[0]
                    except: pass
                
                if not temp_img and img_tag.has_attr("data-old-hires") and img_tag["data-old-hires"]:
                    temp_img = img_tag["data-old-hires"]

                if not temp_img and img_tag.has_attr("src"):
                    src = img_tag["src"]
                    if not src.endswith('.gif') and not src.startswith('data:image'):
                        temp_img = src

                if temp_img and temp_img.startswith("http") and not temp_img.endswith(".gif"):
                    img = temp_img

            return title, price, img, rating, reviews

        except Exception as e:
            print(f"  [!] Error connecting. Retrying {attempt + 1}/{max_retries}...")
            time.sleep(random.randint(5, 10))

    return "Failed to Load", 0.00, "https://dummyimage.com/400x300/1e293b/f8fafc.png&text=Error", 0.0, 0

final_database = {}

for category, items in input_catalog.items():
    print(f"\nBuilding Category: {category}")
    final_database[category] = []
    
    for item_name, tiers in items.items():
        item_block = {
            "name": item_name,
            "tiers": []
        }
        
        for tier_name, link in tiers.items():
            print(f"  Scraping {item_name} ({tier_name})...")
            
            clean_url = link.split('?')[0]
            
            title, price, img, rating, reviews = get_amazon_data(clean_url)
            
            if price == 0.0 or title == "Amazon Product" or title == "Failed to Load":
                if link in old_data and old_data[link].get("price", 0) > 0.0:
                    print(f"    [!] Scrape failed. Rescuing previous valid data for {tier_name}.")
                    title = old_data[link].get("title", title)
                    price = old_data[link].get("price", price)
                    img = old_data[link].get("img", img)
                    rating = old_data[link].get("rating", rating)
                    reviews = old_data[link].get("reviews", reviews)
                else:
                    print(f"    [!] Scrape failed and no valid backup found for {tier_name}.")

            tier_data = {
                "tier": tier_name,
                "title": title,
                "price": price,
                "rating": rating,
                "reviews": reviews,
                "link": link,
                "img": img
            }
            
            if category == "Travel & Gear" and item_name == "Infant Car Seat":
                if tier_name == "Budget": tier_data["crashTest"] = "ProtectPlus Engineered"
                elif tier_name == "Standard": tier_data["crashTest"] = "EPS Energy-Absorbing Foam"
                elif tier_name == "Premium": tier_data["crashTest"] = "Meets US FMVSS 213 Standards"
                elif tier_name.lower() == "luxury": tier_data["crashTest"] = "Advanced Side Impact Protection"

            item_block["tiers"].append(tier_data)
            
            time.sleep(random.uniform(4, 9))
            
        final_database[category].append(item_block)

final_database["_metadata"] = {
    "last_updated": datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")
}

with open('products.json', 'w') as f:
    json.dump(final_database, f, indent=4)

print("\nUpdate complete. Dynamically built products.json.")
