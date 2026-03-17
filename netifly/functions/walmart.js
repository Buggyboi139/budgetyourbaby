// netlify/functions/walmart.js

exports.handler = async function(event, context) {
    // 1. Grab the search term and budget sent from your frontend
    const searchTerm = event.queryStringParameters.searchTerm;
    const maxPrice = event.queryStringParameters.maxPrice;

    if (!searchTerm || !maxPrice) {
        return { statusCode: 400, body: JSON.stringify({ error: "Missing search term or budget" }) };
    }

    // 2. Grab your secret key from Netlify's environment variables
    const apiKey = process.env.SERPAPI_KEY; 

    // 3. Build the URL to ask SerpApi to search Walmart
    const url = `https://serpapi.com/search.json?engine=walmart&query=${encodeURIComponent(searchTerm)}&max_price=${maxPrice}&sort=best_match&api_key=${apiKey}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.organic_results && data.organic_results.length > 0) {
            
            // 4. The Trusted Brand Whitelist
            const trustedBrands = ["Graco", "Chicco", "Pampers", "Huggies", "FridaBaby", "Dr. Brown's", "Philips Avent", "Munchkin", "Safety 1st", "Evenflo", "Skip Hop", "Honest", "WaterWipes", "Delta Children", "Baby Brezza"];
            
            const validProducts = data.organic_results.filter(p => {
                if (!p.primary_offer) return false;
                if (p.primary_offer.offer_price > parseFloat(maxPrice)) return false;
                if (p.rating < 4) return false; // Must be 4+ stars

                const title = p.title.toLowerCase();
                return trustedBrands.some(brand => title.includes(brand.toLowerCase()));
            });

            // Fallback: If no trusted brand fits, just get the best match that fits the budget
            const product = validProducts.length > 0 ? validProducts[0] : data.organic_results.find(p => p.primary_offer && p.primary_offer.offer_price <= parseFloat(maxPrice));

            if (!product) {
                 return { statusCode: 404, body: JSON.stringify({ error: "No products fit this budget" }) };
            }

            // 5. Send the clean data back to the frontend
            return {
                statusCode: 200,
                body: JSON.stringify({
                    title: product.title,
                    price: product.primary_offer.offer_price,
                    image: product.thumbnail,
                    link: product.product_page_url,
                    rating: product.rating
                })
            };
        } else {
            return { statusCode: 404, body: JSON.stringify({ error: "No results from Walmart" }) };
        }

    } catch (error) {
        return { statusCode: 500, body: JSON.stringify({ error: "Failed to fetch Walmart data" }) };
    }
}
