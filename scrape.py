import datetime
import json
import time
import random
from bs4 import BeautifulSoup
from curl_cffi import requests

AFFILIATE_TAG = "1097fa-20"

product_db = {
newborn_essentials = {
    "Nursery & Furniture": [
        {
            "name": "Crib or Bassinet",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Delta Children Canton Mini Crib",
                    "price": 126.32,
                    "rating": 4.6,
                    "reviews": 4218,
                    "link": "https://www.amazon.com/dp/B002MZMDX8/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/710KV1N+JCL._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Graco Benton 5-in-1 Convertible Crib",
                    "price": 199.99,
                    "rating": 4.8,
                    "reviews": 12543,
                    "link": "https://www.amazon.com/dp/B010S7VZ6W/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71CtqIsSfrL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Babyletto Hudson 3-in-1 Convertible Crib",
                    "price": 499.0,
                    "rating": 4.7,
                    "reviews": 2312,
                    "link": "https://www.amazon.com/dp/B0148KHE7O/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71HpSqsYFBL._AC_SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Babyletto Moab 3-in-1 Convertible Crib",
                    "price": 999.0,
                    "rating": 4.5,
                    "reviews": 3125,
                    "link": "https://www.amazon.com/dp/B0F23LPQSV/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61H+V-QhE8L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Nursery Glider",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Storkcraft Premium Hoop Glider",
                    "price": 189.99,
                    "rating": 4.4,
                    "reviews": 18274,
                    "link": "https://www.amazon.com/dp/B00I5ELBA6/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/717el9ToXJL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Delta Children Blair Slim Glider",
                    "price": 232.09,
                    "rating": 4.4,
                    "reviews": 3188,
                    "link": "https://www.amazon.com/dp/B072VGKCFZ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81eDz68ypSL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "DaVinci Olive Upholstered Swivel Glider",
                    "price": 296.65,
                    "rating": 4.8,
                    "reviews": 5491,
                    "link": "https://www.amazon.com/dp/B0192SZGNQ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/91IoSpx8FRL._SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Babyletto Kiwi Glider Recliner Nursery Chair",
                    "price": 1099.0,
                    "rating": 4.8,
                    "reviews": 1280,
                    "link": "https://www.amazon.com/dp/B0CZ6M96RR/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81B-8oJd3gL._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Mattress & Sheets",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Safety 1st Heavenly Dreams Mattress",
                    "price": 62.99,
                    "rating": 4.6,
                    "reviews": 22045,
                    "link": "https://www.amazon.com/dp/B004044LD4/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71krXFLbGtL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Sealy Baby Firm Rest Mattress",
                    "price": 89.99,
                    "rating": 4.8,
                    "reviews": 9532,
                    "link": "https://www.amazon.com/dp/B004EWG4ZA/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81-wl0BzfCL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Newton Baby Wovenaire Crib Mattress",
                    "price": 299.99,
                    "rating": 4.9,
                    "reviews": 6821,
                    "link": "https://www.amazon.com/dp/B00WR958TA/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71VeejrijDL._AC_SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Naturepedic Organic Breathable Baby Crib Mattress",
                    "price": 299.0,
                    "rating": 4.8,
                    "reviews": 1543,
                    "link": "https://www.amazon.com/dp/B07NQN9XBT/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61N9eYJ30xL._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Baby Monitor",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "VTech Upgraded Audio Baby Monitor",
                    "price": 23.95,
                    "rating": 4.5,
                    "reviews": 15482,
                    "link": "https://www.amazon.com/dp/B00JEV5UI8/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61PzyDeMA-L._AC_SX342_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "HelloBaby Video Monitor",
                    "price": 63.16,
                    "rating": 4.6,
                    "reviews": 31056,
                    "link": "https://www.amazon.com/dp/B09GM8JZM9/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61qMfoVil5L._AC_SX355_PIbundle-2,TopRight,0,0_SH20_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Infant Optics DXR-8 PRO Video Monitor",
                    "price": 199.99,
                    "rating": 4.8,
                    "reviews": 45129,
                    "link": "https://www.amazon.com/dp/B08FF4GV5C/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71G9W+hypCL._AC_SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Nanit Pro Smart Baby Monitor & Wall Mount",
                    "price": 299.0,
                    "rating": 4.7,
                    "reviews": 5621,
                    "link": "https://www.amazon.com/dp/B08QMWP5V8/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61lXGz6r5pL._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Sound Machine",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Yogasleep Hushh Portable White Noise Machine",
                    "price": 29.99,
                    "rating": 4.7,
                    "reviews": 42018,
                    "link": "https://www.amazon.com/dp/B01D50RYSC/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61WvB77hXjL._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Hatch Rest Portable Baby Sound Machine",
                    "price": 39.99,
                    "rating": 4.8,
                    "reviews": 38102,
                    "link": "https://www.amazon.com/dp/B06XMRCC94/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/51wXwXw6qCL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Hatch Baby Sound Machine, Night Light",
                    "price": 99.99,
                    "rating": 4.8,
                    "reviews": 12450,
                    "link": "https://www.amazon.com/dp/B0F7C6XJ3P/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61H0H1K9V9L._AC_SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Amazon Echo Dot Max",
                    "price": 99.99,
                    "rating": 4.6,
                    "reviews": 1102,
                    "link": "https://www.amazon.com/dp/B0D6SX8VLQ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71R1sRz81fL._AC_SY355_.jpg"
                }
            ]
        }
    ],
    "Travel & Gear": [
        {
            "name": "Infant Car Seat",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Graco SnugRide 35 Lite LX",
                    "price": 139.99,
                    "rating": 4.8,
                    "reviews": 28104,
                    "link": "https://www.amazon.com/dp/B07Y5S4VWT/?tag=1097fa-20",
                    "crashTest": "ProtectPlus Engineered",
                    "img": "https://m.media-amazon.com/images/I/711Rix6pr9L._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Chicco KeyFit 30 Infant Car Seat",
                    "price": 229.99,
                    "rating": 4.9,
                    "reviews": 35492,
                    "link": "https://www.amazon.com/dp/B09LKZFKGD/?tag=1097fa-20",
                    "crashTest": "EPS Energy-Absorbing Foam",
                    "img": "https://m.media-amazon.com/images/I/71CalcfjvSL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Evenflo Gold Revolve360 Extend All-in-One Rotational Car Seat",
                    "price": 499.99,
                    "rating": 4.9,
                    "reviews": 13,
                    "link": "https://www.amazon.com/dp/B0DTYGNBR3/?tag=1097fa-20",
                    "crashTest": "Meets US FMVSS 213 Standards",
                    "img": "https://m.media-amazon.com/images/I/71TBrQZh2hL._SY355_.jpg"
                },
                {
                    "tier": "luxury",
                    "title": "Baby Jogger City Turn Rotating Convertible Car Seat",
                    "price": 579.99,
                    "rating": 4.8,
                    "reviews": 920,
                    "link": "https://www.amazon.com/dp/B0987YSHNY/?tag=1097fa-20",
                    "crashTest": "Advanced Side Impact Protection",
                    "img": "https://m.media-amazon.com/images/I/61k1Tz4hV0L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Travel Stroller",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Kolcraft Cloud Plus Stroller",
                    "price": 89.99,
                    "rating": 4.5,
                    "reviews": 14588,
                    "link": "https://www.amazon.com/dp/B019DHBCXE/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71RLZKHo-YL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Baby Jogger City Mini GT2 Stroller",
                    "price": 399.99,
                    "rating": 4.8,
                    "reviews": 4219,
                    "link": "https://www.amazon.com/dp/B08ZJTNY7Y/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81er4BpnLhL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Doona Infant Car Seat & Latch Base",
                    "price": 650.0,
                    "rating": 4.9,
                    "reviews": 15682,
                    "link": "https://www.amazon.com/dp/B08VWWQ96T/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71D9O7K0MFL._AC_SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "UPPAbaby Vista V2 Stroller",
                    "price": 999.99,
                    "rating": 4.9,
                    "reviews": 2845,
                    "link": "https://www.amazon.com/dp/B0D9XS9VXL/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61CXZQdFSVL._SY355_.jpg"
                }
            ]
        },
        {
            "name": "Baby Carrier",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Infantino Flip Advanced Carrier",
                    "price": 24.49,
                    "rating": 4.6,
                    "reviews": 45032,
                    "link": "https://www.amazon.com/dp/B00M0DWQYI/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71Ysf6HGZ1L._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Moby Wrap Classic Baby Carrier",
                    "price": 44.99,
                    "rating": 4.5,
                    "reviews": 12084,
                    "link": "https://www.amazon.com/dp/B079TFMCHY/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71j54Z8kalL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Ergobaby Omni 360 Carrier",
                    "price": 179.99,
                    "rating": 4.8,
                    "reviews": 8911,
                    "link": "https://www.amazon.com/dp/B07B41952V/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/710zAgteHvL._SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Ergobaby All Carry Positions Breathable Mesh Baby Carrier",
                    "price": 219.0,
                    "rating": 4.8,
                    "reviews": 820,
                    "link": "https://www.amazon.com/dp/B092FM5KJ7/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71k4vX0vY8L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Diaper Bag",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "LOVEVOOK Laptop Backpack for Women",
                    "price": 28.99,
                    "rating": 4.8,
                    "reviews": 45210,
                    "link": "https://www.amazon.com/dp/B0FSLB42V3/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71X8kM5uH8L._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Ruvalino Multifunction Diaper Bag Backpack",
                    "price": 39.99,
                    "rating": 4.8,
                    "reviews": 45210,
                    "link": "https://www.amazon.com/dp/B07C3SWZ1C/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71X8kM5uH8L._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Skip Hop Forma Backpack Diaper Bag",
                    "price": 75.0,
                    "rating": 4.8,
                    "reviews": 9214,
                    "link": "https://www.amazon.com/dp/B00J4N04EA/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81Uv5BfQGjL._AC_SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Freshly Picked Classic Diaper Bag Backpack",
                    "price": 199.0,
                    "rating": 4.7,
                    "reviews": 1102,
                    "link": "https://www.amazon.com/dp/B01MT2G6D8/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71t2b2uV7gL._AC_SY355_.jpg"
                }
            ]
        }
    ],
    "Feeding & Nursing": [
        {
            "name": "Bottle Starter Set",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Evenflo Feeding Classic Glass 6-Pack",
                    "price": 16.99,
                    "rating": 4.4,
                    "reviews": 1243,
                    "link": "https://www.amazon.com/dp/B00RVIOQLI/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71sgXVcoHRL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Philips Avent Natural Response 4-Pack",
                    "price": 29.95,
                    "rating": 4.7,
                    "reviews": 15682,
                    "link": "https://www.amazon.com/dp/B0964CHD65/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71PP49jvjLL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Dr. Brown's Anti-Colic Narrow Glass 4-Pack",
                    "price": 31.96,
                    "rating": 4.8,
                    "reviews": 22091,
                    "link": "https://www.amazon.com/dp/B0F54RHSM7/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81PGkAoYIML._SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "BIBS Baby Bottle 270 ml Silicone Nipple",
                    "price": 42.99,
                    "rating": 4.6,
                    "reviews": 920,
                    "link": "https://www.amazon.com/dp/B0FPGB6D2G/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61H4H4w3g4L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Nursing Pillow",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Boppy Original Support Pillow",
                    "price": 39.99,
                    "rating": 4.0,
                    "reviews": 38045,
                    "link": "https://www.amazon.com/dp/B0F8LDHL26/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/51ICfyOYckL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Frida Mom Adjustable Nursing Pillow",
                    "price": 50.0,
                    "rating": 4.6,
                    "reviews": 2184,
                    "link": "https://www.amazon.com/dp/B0B5P2RXYN/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71x2c2b3d4L._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "My Brest Friend Nursing Pillow",
                    "price": 56.99,
                    "rating": 4.7,
                    "reviews": 12467,
                    "link": "https://www.amazon.com/dp/B08J54C2Y8/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/618aurIHl4L._SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Snuggle Me Organic Bare Pillow",
                    "price": 64.99,
                    "rating": 4.9,
                    "reviews": 9214,
                    "link": "https://www.amazon.com/dp/B08SMT92PK/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61nqq8HAyIL._SY355_.jpg"
                }
            ]
        },
        {
            "name": "High Chair",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Cosco Simple Fold High Chair",
                    "price": 59.99,
                    "rating": 4.6,
                    "reviews": 16088,
                    "link": "https://www.amazon.com/dp/B01JRY07BQ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71DryRBVuNL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Graco Slim Snacker High Chair",
                    "price": 99.99,
                    "rating": 4.8,
                    "reviews": 14521,
                    "link": "https://www.amazon.com/dp/B00PTL13LA/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71bAgE8A+oL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Stokke Tripp Trapp High Chair",
                    "price": 279.2,
                    "rating": 4.9,
                    "reviews": 6894,
                    "link": "https://www.amazon.com/dp/B0D5KLGSYS/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/6109NxB5HWL._SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Peg Perego Siesta High Chair",
                    "price": 329.0,
                    "rating": 4.8,
                    "reviews": 2410,
                    "link": "https://www.amazon.com/dp/B006T6CKG6/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61h7d8vF8gL._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Burp Cloths",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Luvable Friends Flannel Cloths",
                    "price": 9.99,
                    "rating": 4.6,
                    "reviews": 31056,
                    "link": "https://www.amazon.com/dp/B0757FF5Z9/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/91RVwda1A-L._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Comfy Cubs Muslin Burp Cloths",
                    "price": 19.99,
                    "rating": 4.8,
                    "reviews": 22104,
                    "link": "https://www.amazon.com/dp/B08CBJ2SSQ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71f4b5d6eL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Copper Pearl Premium Burp Cloths",
                    "price": 23.0,
                    "rating": 4.9,
                    "reviews": 11284,
                    "link": "https://www.amazon.com/dp/B079MFDF4M/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/A1kxr7Rkl0L._SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Burt's Bees Organic Burp Cloths",
                    "price": 26.95,
                    "rating": 4.8,
                    "reviews": 18032,
                    "link": "https://www.amazon.com/dp/B00N4PNYRY/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/711Th9A2nNL._SY355_.jpg"
                }
            ]
        },
        {
            "name": "Breast Pump",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Medela Harmony Manual Breast Pump",
                    "price": 29.99,
                    "rating": 4.5,
                    "reviews": 25102,
                    "link": "https://www.amazon.com/dp/B0006HBS1M/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61f8f8vV9gL._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Spectra - S2 Plus Electric Breast Pump",
                    "price": 177.99,
                    "rating": 4.8,
                    "reviews": 18032,
                    "link": "https://www.amazon.com/dp/B00BLBLR1I/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61F9H9J2V8L._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Spectra - S1 Plus Rechargeable Pump",
                    "price": 225.99,
                    "rating": 4.9,
                    "reviews": 19214,
                    "link": "https://www.amazon.com/dp/B00DBKFFJM/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61D6H6V9g8L._AC_SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Elvie Double Electric Wearable Breast Pump",
                    "price": 549.99,
                    "rating": 4.6,
                    "reviews": 5104,
                    "link": "https://www.amazon.com/dp/B07G375DHR/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61h4G8b5H3L._AC_SY355_.jpg"
                }
            ]
        }
    ],
    "Diapering Needs": [
        {
            "name": "Diapers (Starter Supply)",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Luvs Pro Level Leak Protection 40 Count",
                    "price": 20.99,
                    "rating": 4.3,
                    "reviews": 8521,
                    "link": "https://www.amazon.com/dp/B00FF79658/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/715wWFn1vzL._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Pampers Swaddlers Box 40 Count",
                    "price": 25.99,
                    "rating": 4.8,
                    "reviews": 65098,
                    "link": "https://www.amazon.com/dp/B0178B04JK/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81NvjVv9j9L._AC_SY355_PIbundle-2,TopRight,0,0_SH20_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "The Honest Company Clean Diapers 78 Count",
                    "price": 26.97,
                    "rating": 4.7,
                    "reviews": 14265,
                    "link": "https://www.amazon.com/dp/B0CKV2ZL1Y/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/817J-AgVkNL._AC_SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Earth & Eden Sensitive 192 Count",
                    "price": 59.99,
                    "rating": 4.6,
                    "reviews": 9214,
                    "link": "https://www.amazon.com/dp/B0B5YCSGDD/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81H8y9B1R9L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Baby Wipes",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Amazon Elements Baby Wipes 810 Count",
                    "price": 20.24,
                    "rating": 4.5,
                    "reviews": 11043,
                    "link": "https://www.amazon.com/dp/B07H53W5WP/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71gbIUpYmcL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Huggies Natural Care Wipes 768 Count",
                    "price": 21.99,
                    "rating": 4.8,
                    "reviews": 82012,
                    "link": "https://www.amazon.com/dp/B07SCL613T/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81KJo22+X0L._AC_SY355_PIbundle-12,TopRight,0,0_SH20_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "WaterWipes Original Baby Wipes 720 Count",
                    "price": 44.82,
                    "rating": 4.8,
                    "reviews": 45076,
                    "link": "https://www.amazon.com/dp/B008KJEYLO/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/813fvE8SHRL._AC_SY355_PIbundle-12,TopRight,0,0_SH20_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Kinder by Nature Water-Based Baby Wipes - 672 Count",
                    "price": 45.0,
                    "rating": 4.7,
                    "reviews": 5104,
                    "link": "https://www.amazon.com/dp/B01LXNICJF/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71G4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Diaper Pail",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Diaper Dekor EKO Classic Diaper Pail",
                    "price": 39.99,
                    "rating": 4.5,
                    "reviews": 13154,
                    "link": "https://www.amazon.com/dp/B0D37YXJBF/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/51Uz7GqvPeL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Munchkin Step Diaper Pail",
                    "price": 69.97,
                    "rating": 4.7,
                    "reviews": 18532,
                    "link": "https://www.amazon.com/dp/B01BDQDIGM/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71CfMQJJoHL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Ubbi Steel Odor Locking Pail",
                    "price": 99.99,
                    "rating": 4.4,
                    "reviews": 21088,
                    "link": "https://www.amazon.com/dp/B0CK2K6JXD/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/51go+sKFx5L._SX342_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Munchkin UV Diaper Pail",
                    "price": 129.99,
                    "rating": 4.5,
                    "reviews": 1024,
                    "link": "https://www.amazon.com/dp/B09RCPTWB4/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61G4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Changing Pad",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Summer Infant Contoured Pad",
                    "price": 18.89,
                    "rating": 4.8,
                    "reviews": 29084,
                    "link": "https://www.amazon.com/dp/B009EDSWJA/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/712fV9oRPRL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Munchkin Secure Grip Pad",
                    "price": 34.99,
                    "rating": 4.7,
                    "reviews": 15021,
                    "link": "https://www.amazon.com/dp/B00O64QJOC/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/51bcxL+mU0L._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Skip Hop Wipe-Clean Changing Pad",
                    "price": 89.97,
                    "rating": 4.8,
                    "reviews": 9231,
                    "link": "https://www.amazon.com/dp/B075X8TPMN/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/51tvpEH0MUL._SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Naturepedic Organic Contoured Changing Pad",
                    "price": 118.0,
                    "rating": 4.8,
                    "reviews": 1204,
                    "link": "https://www.amazon.com/dp/B004FTTV5W/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71f4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Diaper Cream",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Desitin Daily Defense Diaper Rash Cream",
                    "price": 7.99,
                    "rating": 4.8,
                    "reviews": 32014,
                    "link": "https://www.amazon.com/dp/B07H7GBJC4/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61f8g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Aquaphor Baby Healing Ointment",
                    "price": 13.99,
                    "rating": 4.9,
                    "reviews": 65104,
                    "link": "https://www.amazon.com/dp/B0107QP1VE/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71G4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Boudreaux's Butt Paste Maximum Strength",
                    "price": 16.99,
                    "rating": 4.8,
                    "reviews": 21045,
                    "link": "https://www.amazon.com/dp/B01LZF07GU/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71h4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Earth Mama Organic Diaper Balm",
                    "price": 23.99,
                    "rating": 4.8,
                    "reviews": 12045,
                    "link": "https://www.amazon.com/dp/B0825WHHGJ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71j4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        }
    ],
    "Clothing & Basics": [
        {
            "name": "Sleep & Plays",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Carter's 3-Pack Sleep 'n Play",
                    "price": 25.0,
                    "rating": 4.8,
                    "reviews": 18562,
                    "link": "https://www.amazon.com/dp/B07NSNHX12/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/91+cp0njVPL._AC_SY445_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Gerber 4-Pack Sleep 'n Play",
                    "price": 25.95,
                    "rating": 4.6,
                    "reviews": 3218,
                    "link": "https://www.amazon.com/dp/B08BV38H37/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/91rugS1eU+S._AC_SX342_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Kyte Baby Bamboo Zip Romper",
                    "price": 37.99,
                    "rating": 4.9,
                    "reviews": 5419,
                    "link": "https://www.amazon.com/dp/B0CN3CHM3T/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/417GOKSy+ZL._AC_SX342_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Burt's Bees Baby Organic Sleep & Play",
                    "price": 18.95,
                    "rating": 4.8,
                    "reviews": 12045,
                    "link": "https://www.amazon.com/dp/B0G232YTND/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71h4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Bodysuits",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Gerber 5-Pack Onesies",
                    "price": 12.95,
                    "rating": 4.5,
                    "reviews": 4123,
                    "link": "https://www.amazon.com/dp/B007CRR7Z0/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61TLWiHnDZL._AC_SX342_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Carter's 5-Pack Onesies",
                    "price": 20.53,
                    "rating": 4.9,
                    "reviews": 42088,
                    "link": "https://www.amazon.com/dp/B083X7MVK8/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/91C8Z9G9j9L._AC_SY445_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Magnetic Me Footie Bodysuit",
                    "price": 40.0,
                    "rating": 4.8,
                    "reviews": 4512,
                    "link": "https://www.amazon.com/dp/B08X8JG5G7/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61k4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Honest Baby 5-Pack Organic Bodysuits",
                    "price": 34.99,
                    "rating": 4.7,
                    "reviews": 8354,
                    "link": "https://www.amazon.com/dp/B08G5WTTLZ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81SYlbbwK3L._AC_SX342_.jpg"
                }
            ]
        },
        {
            "name": "Swaddle Blankets",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Luvable Friends 3-Pack Swaddles",
                    "price": 9.99,
                    "rating": 4.6,
                    "reviews": 12591,
                    "link": "https://www.amazon.com/dp/B077G8FMBY/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/91inuxd3YEL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "SwaddleMe Original 3-Pack",
                    "price": 16.39,
                    "rating": 4.7,
                    "reviews": 29045,
                    "link": "https://www.amazon.com/dp/B07C8L4CTZ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81qMK2B3pXL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Aden + Anais Muslin 4-Pack",
                    "price": 32.95,
                    "rating": 4.8,
                    "reviews": 15421,
                    "link": "https://www.amazon.com/dp/B0B75QS1RF/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71pAg3KDXdL._SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "LifeTree Organic Cotton Muslin Swaddle 2-Pack",
                    "price": 25.99,
                    "rating": 4.8,
                    "reviews": 4120,
                    "link": "https://www.amazon.com/dp/B09Y8SNJ15/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71J4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Socks",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Luvable Friends Fleece Booties",
                    "price": 12.97,
                    "rating": 4.5,
                    "reviews": 6812,
                    "link": "https://www.amazon.com/dp/B00X21MRHI/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81VTay4TbyL._AC_SX342_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Zutano Fleece Booties",
                    "price": 23.0,
                    "rating": 4.8,
                    "reviews": 15204,
                    "link": "https://www.amazon.com/dp/B0733N7PLQ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71K4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "GoumikidsViscose Bamboo Cotton",
                    "price": 19.99,
                    "rating": 4.7,
                    "reviews": 2104,
                    "link": "https://www.amazon.com/dp/B07SH3H9WV/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61L4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Burt's Bees Booties & Mitts",
                    "price": 17.95,
                    "rating": 4.8,
                    "reviews": 9288,
                    "link": "https://www.amazon.com/dp/B07D49GDQK/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71o0fRnLUFL._AC_SX342_.jpg"
                }
            ]
        }
    ],
    "Bath & Health": [
        {
            "name": "Baby Bathtub",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "The First Years Sure Comfort Tub",
                    "price": 34.99,
                    "rating": 4.8,
                    "reviews": 31054,
                    "link": "https://www.amazon.com/dp/B000067EH7/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/41rzsORGdiL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "FridaBaby Grow-With-Me Tub",
                    "price": 49.97,
                    "rating": 4.7,
                    "reviews": 4291,
                    "link": "https://www.amazon.com/dp/B099FM4W4H/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71ok+FA6jWL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Fisher-Price 4-in-1 Sling Tub",
                    "price": 64.4,
                    "rating": 4.8,
                    "reviews": 25012,
                    "link": "https://www.amazon.com/dp/B0DVLQN538/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71Ho9D5xBgL._SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "Stokke Flexi Bath",
                    "price": 79.0,
                    "rating": 4.7,
                    "reviews": 5104,
                    "link": "https://www.amazon.com/dp/B07RJ3C7DX/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61M4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Healthcare Kit",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Safety 1st Healthcare Set",
                    "price": 16.09,
                    "rating": 4.5,
                    "reviews": 38045,
                    "link": "https://www.amazon.com/dp/B00VXMXN30/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81DWcddfyaL._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Braun ThermoScan 7 Ear Thermometer",
                    "price": 39.95,
                    "rating": 4.8,
                    "reviews": 21084,
                    "link": "https://www.amazon.com/dp/B00MUK6M82/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/51kZsqS4XgL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "FridaBaby Bitty Bundle of Joy",
                    "price": 40.99,
                    "rating": 4.8,
                    "reviews": 19021,
                    "link": "https://www.amazon.com/dp/B01J8C1VVC/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71FZy5TSj9L._SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Little Remedies New Parents Survival Kit",
                    "price": 25.0,
                    "rating": 4.8,
                    "reviews": 15104,
                    "link": "https://www.amazon.com/dp/B075G6XMSF/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71N4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Towels & Washcloths",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Luvable Friends Hooded Towel",
                    "price": 11.99,
                    "rating": 4.6,
                    "reviews": 14032,
                    "link": "https://www.amazon.com/dp/B07ZSCJB4K/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81WelyjR7XL._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Hudson Baby Animal Face Towel",
                    "price": 12.99,
                    "rating": 4.8,
                    "reviews": 32091,
                    "link": "https://www.amazon.com/dp/B00X22L0AC/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/911s9uvyuWL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Kyte Baby Bamboo Hooded Towel",
                    "price": 55.0,
                    "rating": 4.9,
                    "reviews": 3104,
                    "link": "https://www.amazon.com/dp/B0B46RBFBD/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61P4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Burt's Bees Organic Towel Set",
                    "price": 29.95,
                    "rating": 4.8,
                    "reviews": 12543,
                    "link": "https://www.amazon.com/dp/B081SFS6SW/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/7155yfK9IqL._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Baby Wash",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Johnson's Head-to-Toe Wash",
                    "price": 7.68,
                    "rating": 4.7,
                    "reviews": 29012,
                    "link": "https://www.amazon.com/dp/B07D2JMJPS/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61KA4Qj0XxL._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Aveeno Baby Wash & Shampoo",
                    "price": 12.62,
                    "rating": 4.8,
                    "reviews": 34088,
                    "link": "https://www.amazon.com/dp/B004L5JCZ4/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61Oy6CZtOkL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Tubby Todd Hair & Body Wash",
                    "price": 51.0,
                    "rating": 4.9,
                    "reviews": 8143,
                    "link": "https://www.amazon.com/dp/B0FY3YPZCG/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61l+srJQfGL._SY355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Earth Mama Sweet Orange Baby Wash",
                    "price": 15.99,
                    "rating": 4.8,
                    "reviews": 5104,
                    "link": "https://www.amazon.com/dp/B000P7M26I/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71Q4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Nasal Aspirator",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "DMI Reusable Nasal Aspirator",
                    "price": 5.99,
                    "rating": 4.5,
                    "reviews": 11024,
                    "link": "https://www.amazon.com/dp/B001OTK6JG/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61R4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "FridaBaby NoseFrida Snotsucker",
                    "price": 15.99,
                    "rating": 4.8,
                    "reviews": 52104,
                    "link": "https://www.amazon.com/dp/B00171WXII/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71S4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Braun Electric Nasal Aspirator",
                    "price": 35.99,
                    "rating": 4.6,
                    "reviews": 18204,
                    "link": "https://www.amazon.com/dp/B07N28G62S/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61T4g8b5H3L._AC_SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "NozeBot Electric Nasal Aspirator",
                    "price": 119.99,
                    "rating": 4.8,
                    "reviews": 2104,
                    "link": "https://www.amazon.com/dp/B08G6SZ2LT/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71U4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        }
    ],
    "Play & Soothing": [
        {
            "name": "Bouncer or Swing",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Bright Starts Playful Pinwheels",
                    "price": 34.99,
                    "rating": 4.6,
                    "reviews": 18054,
                    "link": "https://www.amazon.com/dp/B00KHR7TPK/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/81S7zOrgIyL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Graco Simple Sway Portable Baby Swing",
                    "price": 139.99,
                    "rating": 4.7,
                    "reviews": 22582,
                    "link": "https://www.amazon.com/dp/B0GD8VN5WX/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61dxxxVMHiL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "BabyBjorn Bouncer Balance Soft",
                    "price": 229.99,
                    "rating": 4.9,
                    "reviews": 11231,
                    "link": "https://www.amazon.com/dp/B0D5DL7RWZ/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61NkvY+Db-L._SY355_.jpg"
                },
                {
                    "tier": "Luxury",
                    "title": "4moms MamaRoo Multi-Motion Baby Swing",
                    "price": 349.0,
                    "rating": 4.8,
                    "reviews": 510,
                    "link": "https://www.amazon.com/dp/B0B3F93NYT/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71V4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Play Mat",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Infantino Pond Pals Playmat",
                    "price": 29.97,
                    "rating": 4.6,
                    "reviews": 8412,
                    "link": "https://www.amazon.com/dp/B0D7P22KPN/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/710Jw1KhrYL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Fisher-Price Deluxe Kick & Play",
                    "price": 60.0,
                    "rating": 4.9,
                    "reviews": 52088,
                    "link": "https://www.amazon.com/dp/B076HYSWB9/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71xACtCTsvL._AC_SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "Lovevery The Play Gym",
                    "price": 150.0,
                    "rating": 4.9,
                    "reviews": 6845,
                    "link": "https://www.amazon.com/dp/B075R8BXXC/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71VLpdw5GVL._SX355_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Pehr Organic Cotton Play Mat",
                    "price": 98.0,
                    "rating": 4.8,
                    "reviews": 1104,
                    "link": "https://www.amazon.com/dp/B0CD2WMW6Y/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71W4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        },
        {
            "name": "Pacifier Pack",
            "tiers": [
                {
                    "tier": "Budget",
                    "title": "Philips Avent Soothie 4-Pack",
                    "price": 10.79,
                    "rating": 4.8,
                    "reviews": 65021,
                    "link": "https://www.amazon.com/dp/B0D82PQKPC/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/71nSI-oZHtL._SY355_.jpg"
                },
                {
                    "tier": "Standard",
                    "title": "Tommee Tippee Happy Pacifiers",
                    "price": 14.39,
                    "rating": 4.6,
                    "reviews": 12054,
                    "link": "https://www.amazon.com/dp/B0DPN9YJSW/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61T4dbQ-jnL._SY355_.jpg"
                },
                {
                    "tier": "Premium",
                    "title": "BIBS Natural Rubber Pacifiers",
                    "price": 15.95,
                    "rating": 4.7,
                    "reviews": 18092,
                    "link": "https://www.amazon.com/dp/B08L9HV8JC/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/61BqAe51i4L._AC_SX342_.jpg"
                },
                {
                    "tier": "Organic",
                    "title": "Natursutten Natural Rubber Pacifier",
                    "price": 12.0,
                    "rating": 4.6,
                    "reviews": 6104,
                    "link": "https://www.amazon.com/dp/B09X1YTHWS/?tag=1097fa-20",
                    "img": "https://m.media-amazon.com/images/I/51X4g8b5H3L._AC_SY355_.jpg"
                }
            ]
        }
    ],
    "_metadata": {
        "last_updated": "March 18, 2026 at 1:09 PM"
    }
}

def get_amazon_data(url, current_price, current_img, max_retries=3):
    if url == "#": return current_price, current_img

    browsers = ["chrome110", "chrome120", "safari15_3", "edge101"]

    for attempt in range(max_retries):
        try:
            browser = random.choice(browsers)
            response = requests.get(url, impersonate=browser, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")

            new_price = current_price
            new_img = current_img

            price_whole = soup.find("span", class_="a-price-whole")
            price_fraction = soup.find("span", class_="a-price-fraction")
            if price_whole and price_fraction:
                clean_price = price_whole.text.replace(',', '').replace('.', '') + '.' + price_fraction.text
                new_price = float(clean_price)

            img_tag = soup.find("img", id="landingImage") or soup.find("img", id="imgBlkFront")
            temp_img = None

            if img_tag:
                if img_tag.has_attr("data-a-dynamic-image"):
                    try:
                        dynamic_images = json.loads(img_tag["data-a-dynamic-image"])
                        urls = list(dynamic_images.keys())
                        if urls:
                            temp_img = urls[0]
                    except:
                        pass
                
                if not temp_img and img_tag.has_attr("data-old-hires") and img_tag["data-old-hires"]:
                    temp_img = img_tag["data-old-hires"]

                if not temp_img and img_tag.has_attr("src"):
                    src = img_tag["src"]
                    if not src.endswith('.gif') and not src.startswith('data:image'):
                        temp_img = src

            if temp_img and temp_img.startswith("http") and not temp_img.endswith(".gif"):
                new_img = temp_img
            else:
                new_img = current_img
            
            return new_price, new_img

        except Exception as e:
            print(f"  [!] Connection dropped. Retrying {attempt + 1}/{max_retries}...")
            time.sleep(random.randint(5, 10))

    return current_price, current_img
