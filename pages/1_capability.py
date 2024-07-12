import streamlit as st
import pandas as pd

def get_styles():
    return """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .product-card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .factory-card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .capability-group {
        background-color: #f0f0f0;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .btn-primary {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn-primary:hover {
        background-color: #45a049;
    }
    </style>
    """

def setup_ui():
    st.set_page_config(page_title="H&M-Style Garment Manufacturing Matchmaker", layout="wide")
    st.markdown(get_styles(), unsafe_allow_html=True)
    st.title("H&M-Style Garment Manufacturing Matchmaker")
    st.write("""
    <div class="intro">
        Find the perfect factory for your H&M-style garment manufacturing needs. 
        Select your product type and specifications, and we'll match you with suitable factories.
    </div>
    """, unsafe_allow_html=True)

def get_product_types():
    return {
        "T-Shirt": {
            "Fabric": ["Cotton", "Organic Cotton", "Polyester", "Cotton-Polyester Blend", "Modal", "Lyocell", "Bamboo", "Hemp"],
            "Printing": ["Screen Printing", "Digital Printing", "Heat Transfer", "Embroidery", "Sublimation Printing", "DTG Printing"],
            "Cutting": ["Die Cutting", "Laser Cutting", "Automated Cutting", "Rotary Cutting", "Water Jet Cutting"],
            "Sewing": ["Overlock Stitching", "Flatlock Stitching", "Cover Stitching", "Chain Stitching", "Blind Stitching"],
            "Finishing": ["Steam Pressing", "Folding and Packaging", "Labeling", "Hang Tag Attachment", "Bio-Washing", "Softening"]
        },
        "Jeans": {
            "Fabric": ["Denim", "Stretch Denim", "Organic Denim", "Recycled Denim", "Selvedge Denim"],
            "Cutting": ["Laser Cutting", "Manual Cutting", "Automated Cutting", "Water Jet Cutting"],
            "Sewing": ["Lockstitch", "Chainstitch", "Riveting", "Button Attachment", "Topstitching"],
            "Washing": ["Stone Wash", "Acid Wash", "Enzyme Wash", "Laser Distressing", "Ozone Wash"],
            "Finishing": ["Distressing", "Whiskering", "Tagging", "Pressing", "Sand Blasting", "Hand Scraping"]
        },
        "Dress": {
            "Fabric": ["Cotton", "Polyester", "Viscose", "Silk", "Linen", "Chiffon", "Rayon", "Georgette"],
            "Cutting": ["Laser Cutting", "Manual Cutting", "Automated Cutting", "Ultrasonic Cutting"],
            "Sewing": ["French Seams", "Invisible Zippers", "Lining Installation", "Pleating", "Piping"],
            "Embellishment": ["Beading", "Sequin Application", "Lace Attachment", "Appliqué", "Ruffles"],
            "Finishing": ["Ironing", "Steaming", "Tagging", "Hanger Loop Attachment", "Quality Inspection"]
        },
        "Sweater": {
            "Fabric": ["Wool", "Cotton", "Acrylic", "Cashmere", "Mohair", "Synthetic Blend", "Alpaca"],
            "Knitting": ["Flat Knitting", "Circular Knitting", "Fully Fashioned Knitting", "Intarsia Knitting", "Jacquard Knitting"],
            "Finishing": ["Blocking", "Steam Pressing", "Button Attachment", "Labeling", "Softening"],
            "Embellishment": ["Embroidery", "Appliqué", "Jacquard Patterns", "Beading", "Cable Knitting"]
        },
        "Jacket": {
            "Fabric": ["Polyester", "Nylon", "Cotton", "Leather", "Denim", "Wool", "Softshell"],
            "Cutting": ["Laser Cutting", "Die Cutting", "Manual Cutting", "Automated Cutting"],
            "Sewing": ["Lockstitch", "Topstitching", "Zipper Installation", "Lining Attachment", "Edge Stitching"],
            "Finishing": ["Pressing", "Steam Ironing", "Weatherproofing", "Tagging", "Heat Sealing"],
            "Hardware": ["Zipper Attachment", "Button Installation", "Snap Fastener Application", "Velcro Attachment", "Magnetic Closures"]
        },
        "Skirt": {
            "Fabric": ["Cotton", "Polyester", "Denim", "Leather", "Silk", "Linen", "Tulle"],
            "Cutting": ["Laser Cutting", "Manual Cutting", "Automated Cutting", "Ultrasonic Cutting"],
            "Sewing": ["Invisible Zippers", "Waistband Attachment", "Hemming", "Pleating", "Gathering"],
            "Finishing": ["Pressing", "Steaming", "Tagging", "Lining Installation", "Embellishing"]
        },
        "Shorts": {
            "Fabric": ["Cotton", "Denim", "Linen", "Polyester", "Nylon", "Spandex Blend"],
            "Cutting": ["Laser Cutting", "Die Cutting", "Manual Cutting", "Water Jet Cutting"],
            "Sewing": ["Overlock Stitching", "Flat Felled Seams", "Pocket Installation", "Chain Stitching"],
            "Finishing": ["Washing", "Distressing", "Pressing", "Tagging", "Embroidery"],
            "Hardware": ["Button Installation", "Zipper Attachment", "Riveting", "Hook and Eye"]
        },
        "Underwear": {
            "Fabric": ["Cotton", "Modal", "Microfiber", "Lace", "Elastane Blend", "Bamboo"],
            "Cutting": ["Die Cutting", "Laser Cutting", "Ultrasonic Cutting", "Automated Cutting"],
            "Sewing": ["Overlock Stitching", "Flatlock Stitching", "Elastic Attachment", "Bonded Seams"],
            "Finishing": ["Heat Setting", "Steaming", "Labeling", "Packaging", "Sanitizing"]
        },
        "Swimwear": {
            "Fabric": ["Nylon", "Polyester", "Spandex Blend", "Recycled Materials", "Chlorine-Resistant Fabric"],
            "Cutting": ["Die Cutting", "Laser Cutting", "Computerized Cutting", "Water Jet Cutting"],
            "Sewing": ["Overlock Stitching", "Flatlock Stitching", "Elastic Attachment", "Bonded Seams"],
            "Finishing": ["Heat Setting", "Chlorine Resistance Treatment", "Lining Installation", "UV Protection Treatment"],
            "Hardware": ["Clasp Attachment", "Adjustable Strap Installation", "Drawstring Insertion"]
        },
        "Accessories": {
            "Product Types": ["Scarves", "Hats", "Belts", "Bags", "Jewelry", "Gloves"],
            "Materials": ["Fabric", "Leather", "Metal", "Plastic", "Wood", "Synthetic Materials"],
            "Techniques": ["Weaving", "Knitting", "Embroidery", "Laser Cutting", "3D Printing", "Handcrafting"],
            "Finishing": ["Polishing", "Plating", "Dyeing", "Embossing", "Tagging", "Engraving"]
        }
    }

def get_factories():
    return [
        {
            "name": "EcoThreads Manufacturing",
            "location": "Portland, Oregon",
            "specialties": ["T-Shirts", "Sustainable Clothing"],
            "min_order": 500,
            "capabilities": {
                "Fabric": ["Cotton", "Organic Cotton", "Recycled Polyester"],
                "Printing": ["Screen Printing", "Digital Printing"],
                "Cutting": ["Die Cutting", "Laser Cutting"],
                "Sewing": ["Overlock Stitching", "Flatlock Stitching"],
                "Finishing": ["Steam Pressing", "Folding and Packaging", "Eco-friendly Dyeing"]
            }
        },
        {
            "name": "DenimMasters Co.",
            "location": "Los Angeles, California",
            "specialties": ["Jeans", "Denim Products", "Shorts"],
            "min_order": 1000,
            "capabilities": {
                "Fabric": ["Denim", "Stretch Denim", "Organic Denim", "Recycled Denim"],
                "Cutting": ["Laser Cutting", "Automated Cutting"],
                "Sewing": ["Lockstitch", "Chainstitch", "Riveting"],
                "Washing": ["Stone Wash", "Acid Wash", "Enzyme Wash", "Laser Distressing"],
                "Finishing": ["Distressing", "Whiskering", "Tagging", "Eco-friendly Processing"]
            }
        },
        {
            "name": "LuxeGarments Co.",
            "location": "New York City, New York",
            "specialties": ["Dresses", "Blouses", "Skirts"],
            "min_order": 300,
            "capabilities": {
                "Fabric": ["Silk", "Chiffon", "Lace", "Organic Cotton", "Tencel"],
                "Cutting": ["Laser Cutting", "Manual Cutting"],
                "Sewing": ["French Seams", "Invisible Zippers", "Pleating", "Draping"],
                "Embellishment": ["Beading", "Sequin Application", "Hand Embroidery"],
                "Finishing": ["Steam Pressing", "Hand Finishing", "Eco-friendly Dry Cleaning"]
            }
        },
        {
            "name": "ActiveWear Experts",
            "location": "Seattle, Washington",
            "specialties": ["Swimwear", "Athletic Wear", "Underwear"],
            "min_order": 750,
            "capabilities": {
                "Fabric": ["Nylon", "Spandex Blend", "Recycled Polyester", "Moisture-Wicking Fabrics"],
                "Cutting": ["Computerized Cutting", "Ultrasonic Cutting"],
                "Sewing": ["Flatlock Stitching", "Elastic Attachment", "Seamless Technology"],
                "Finishing": ["Heat Setting", "Chlorine Resistance Treatment", "UV Protection Finishing"],
                "Innovation": ["Wearable Tech Integration", "3D Knitting"]
            }
        },
        {
            "name": "WinterWear Wizards",
            "location": "Burlington, Vermont",
            "specialties": ["Sweaters", "Jackets", "Cold Weather Accessories"],
            "min_order": 500,
            "capabilities": {
                "Fabric": ["Wool", "Cashmere", "Synthetic Blends", "Fleece", "Down"],
                "Knitting": ["Flat Knitting", "Circular Knitting", "Fully Fashioned Knitting"],
                "Sewing": ["Overlock Stitching", "Zipper Installation", "Lining Attachment"],
                "Finishing": ["Blocking", "Steam Pressing", "Weatherproofing"],
                "Embellishment": ["Embroidery", "Appliqué", "Jacquard Patterns"]
            }
        }
    ]

def product_selector(product_types):
    st.header("Step 1: Select Your Product")
    product = st.selectbox("Choose a product type:", list(product_types.keys()))
    return product

def capability_selector(product, product_types):
    st.header("Step 2: Specify Your Requirements")
    selected_capabilities = {}
    for category, options in product_types[product].items():
        st.subheader(category)
        selected = st.multiselect(f"Select {category} options:", options)
        if selected:
            selected_capabilities[category] = selected
    return selected_capabilities

def find_matching_factories(selected_capabilities, factories):
    matching_factories = []
    for factory in factories:
        if all(any(capability in factory['capabilities'].get(category, []) 
                   for capability in capabilities)
               for category, capabilities in selected_capabilities.items()):
            matching_factories.append(factory)
    return matching_factories

def display_matching_factories(matching_factories):
    st.header("Step 3: Matching Factories")
    if matching_factories:
        st.success(f"We found {len(matching_factories)} matching factories!")
        for factory in matching_factories:
            st.markdown(f"""
            <div class="factory-card">
                <h3>{factory['name']}</h3>
                <p><strong>Location:</strong> {factory['location']}</p>
                <p><strong>Specialties:</strong> {', '.join(factory['specialties'])}</p>
                <p><strong>Minimum Order Quantity:</strong> {factory['min_order']}</p>
                <p><strong>Capabilities:</strong></p>
                <ul>
                    {"".join(f"<li>{cat}: {', '.join(caps)}</li>" for cat, caps in factory['capabilities'].items())}
                </ul>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No matching factories found. Try adjusting your requirements.")

def main():
    setup_ui()
    product_types = get_product_types()
    factories = get_factories()
    
    product = product_selector(product_types)
    
    st.markdown(f"""
    <div class="product-card">
        <h2>{product}</h2>
        <p>Please select the specific capabilities you need for your {product}.</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected_capabilities = capability_selector(product, product_types)
    
    if st.button("Find Matching Factories", key="find_factories"):
        matching_factories = find_matching_factories(selected_capabilities, factories)
        display_matching_factories(matching_factories)

if __name__ == "__main__":
    main()