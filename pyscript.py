import pandas as pd
import re

df = pd.read_csv('quer_csv_all.csv', header=None, names=['questions'])  # Assumes queries are in a single column

# Predefined categories
categories = {
    "1. Soil Data": r".*\b(soil test(ing)?|soil type|soil health|fertilit[y|y]|nutrient level|soil improv|NPK|NPK ratio|soil condition|micronutrient deficienc|organic manure|cow dung|vermicompost|potting mix|pit mixture)\b.*",
    "2. Weather & Climate": r".*\b(weather forecast|climate|weather report|rainfall|temperatur|storm|rain|fog|dew|humidit[y|y]|wind)\b.*",
    "3. Crop Yield": r".*\b(yield|harvest|production|output|how much (.*) produce|less yield|low production|high yield|better yield|bumper harvest)\b.*",
    "4. Crop Health": r".*\b(disease|rot|blight|wilt|chlorosis|necrosis|canker|malformation|stunted growth|yellowing|leaf curl|crinkling|spots|fruit drop|flower drop|deformed|die back|dry(ing)? up|rough skin|fruit crack(ing)?|bunchy top|nutshedding|immature fruit fall(ing)?|shedding|sheath rot|mosaic|fruit scaring beetle|soft(en)?(ing)? of nut|pod borer|collar rot|defoliation|fruit decay|hollow stem|soft shell egg|pencil tip|blossom end rot)\b.*", # Extensive list of crop health issues
    "5. Farm Machinery & Equipment": r".*\b(machinery|equipment|tractor|power tiller|pump set|sprayer|thresher|harvester|jatka machine|seed driller|instrument|tools|diesel pumpset|combine harvester|cutter)\b.*",
    "6. Socio-economic & Demographic": r".*\b(farmer profile|livelihood|landholding|community|gaon sabha|mela)\b.*",  # Added gaon sabha and mela
    "7. Remote Sensing & Satellite Imagery": r".*\b(remote sensing|satellite imagery|satellite data|vegetation index|NDVI)\b.*", # More specific terms
    "8. Extension & Advisory": r".*\b(expert|recommend|best practice|advice|consult|training|demonstration|field visit|package of practice|cultivation practice|cultural practice|management practice|krishi vigyan kendra|kvk|information|how to|guide|practice|method|technique|farming|cultivat|rear(ing)?|grow(ing)?|plant(ing)?|sow(ing)?|harvest(ing)?|storage|preserv)\b.*", # Very broad to catch general inquiries
    "9. Genomic & Phenotypic Trait": r".*\b(variety|hybrid|seed type|breed|trait|clone|genetically modified|high yielding|dwarf|tall|short duration|seedless|local variety|seed selection|improve variety)\b.*",
    "10. Market & Economic": r".*\b(price|market|cost|MSP|selling|economic return|profit|trade|business|loan|finance|credit|subsidy|scheme)\b.*",
    "11. IoT & Sensor": r".*\b(IoT|sensor|remote monitor|wireless|data logger|ph indicator)\b.*",
    "12. Drone & UAV Imagery": r".*\b(drone|UAV|aerial imagery|aerial view)\b.*",
    "13. Supply-chain & Logistics": r".*\b(storage|transport|distribution|delivery|supply chain|logistic|kisan rath|procurement|mandi)\b.*",
    "14. Irrigation": r".*\b(irrigation|water management|water requirement|water logging|watering|drought|flood|water stress|drainage)\b.*",
    "15. Agrochemical": r".*\b(fertilizer|pesticide|herbicide|insecticide|fungicide|bactericide|neem oil|neem cake|growth regulator|growth hormon|crop booster|nutrient|micro nutrient|borax|urea|NPK|manure|chemical|N:P:K|micronutrient spray|rooting hormone|^[a-zA-Z0-9- ]+$)\b.*", # Catches most chemical names/brand names; added "^[a-zA-Z0-9- ]+$" to capture product names
    "16. Seed & Germplasm": r".*\b(seed|seedling|planting material|hybrid seed|improved variety|variety name|sowing time|germination|propagat(ing)? material|rootstock|cuttings|grafting|layering)\b.*", # Included more propagation terms
    "17. Invasive Species, Weed, Pests": r".*\b(pest|insect|weed|disease|infestation|attack|mite|termite|caterpillar|borer|aphid|fly|beetle|grub|grasshopper|snail|slug|rodent|rat|monkey|bird|squirrel|wasp|vector)\b.*",  # Broad coverage of pests
    "18. Environmental Impact": r".*\b(environment|impact|emission|pollution|soil erosion|water quality|biodiversity)\b.*",
    "19. Policy & Legalities": r".*\b(policy|government scheme|scheme|subsidy|loan|insurance|krishi mela|kcc|kisan credit card|pm kisan|ridf|stw|nfsm|atma|rkvy|law|regulation|license|registration|certificate|department of agriculture|dao|krishak bandhu)\b.*", # Added more specific scheme names
    "20. Farmer Data": r".*\b(farmer id|pm kisan form status|kcc loan status|land record|adhaar|client id|rft status|registration id|application status|beneficiary status)\b.*"  # Expanded data-related terms
}

# Function to categorize a query
def categorize_query(query):
    for category, pattern in categories.items():
        if re.match(pattern, query, re.IGNORECASE):  # Case-insensitive matching
            return category
    return "Uncategorized"  # For queries that don't match any category


# Apply the categorization function to your data
df['category'] = df['questions'].apply(categorize_query)

# Save the categorized data (adjust file name as needed)
df.to_csv('categorized_queries.csv', index=False)

print(df)