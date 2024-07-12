import streamlit as st
import json

def display_nested_dict_html(d, level=0, max_level=3):
    html = ""
    indent = '&nbsp;' * 4 * level
    card_style = (
        "background-color: #ffffff; "
        "border: 1px solid #e0e0e0; "
        "border-radius: 12px; "
        "margin: 4px 0 4px 20px; "  # Adjusted margin-left for indentation
        "padding: 12px; "
        "box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); "
        "transition: all 0.3s ease;"
    )
    open_tag = "open" if level < max_level else ""
    
    if isinstance(d, dict):
        for key, value in d.items():
            if isinstance(value, dict):
                html += f"{indent}<details {open_tag} class='item-card' style='{card_style}'><summary>{key}</summary>"
                html += display_nested_dict_html(value, level + 1, max_level)
                html += f"{indent}</details>"
            elif isinstance(value, list):
                html += f"{indent}<details {open_tag} class='item-card' style='{card_style}'><summary>{key}</summary>"
                html += f"{indent}<div class='json-array'>{json.dumps(value, indent=4)}</div>"
                html += f"{indent}</details>"
            else:
                html += f"{indent}<div class='item-card' style='{card_style}'><span class='key'>{key}:</span> <span class='value'>{value}</span></div>"
    elif isinstance(d, list):
        html += f"{indent}<div class='json-array'>{json.dumps(d, indent=4)}</div>"
    else:
        html += f"{indent}<div class='item-card' style='{card_style}'>{d}</div>"
    
    return html

# Default data (unchanged)
default_data_catalog = {
    "Data Catalog": {
        "Supplier": {
            "Supplier Profile": {
                "Parent company": "",
                "Associated Customers": {
                    "Associated LF Customers": "",
                    "Top 5 LF Customers": ""
                },
                "Supplier Status": {
                    "Active": "",
                    "Inactive": ""
                },
                "Is LF Supplier": {
                    "Years of relationship with LF": "",
                    "LF division engaging": ""
                },
                "Number of facilities": "",
                "Product Family": {
                    "Product Category": {
                        "Product Category Range": ""
                    }
                },
                "Entity Website URL": "",
                "Stock Symbol": "",
                "Stock Listing Country": ""
            },
            "Legal Entity": {
                "Entity Full Name": "",
                "Entity Short Name": "",
                "Entity Local Name": "",
                "Telephone Number": "",
                "Fax Number": "",
                "Address": "",
                "Zip (Postal) Code": "",
                "Registration Country": "",
                "Address in local language": "",
                "Years Established": "",
                "Business Registration Number": "",
                "VAT Number": "",
                "Export Licenses": ""
            },
            "Contact Info": {
                "Merchandising Contact": {
                    "Contact Person Name": "",
                    "Contact Person's Title": "",
                    "Contact Person's Email": ""
                }
            }
        }
    }
}

st.set_page_config(page_title="Data Catalog", layout="wide")

st.markdown("""
    <style>
    .main {
        background: #f5f5f5;
        color: #333333;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: #333333;
        font-weight: 600;
        font-size: 28px;
        margin-bottom: 24px;
    }
    .sidebar .stTextInput>div>div>input {
        background-color: #ffffff;
        border: 1px solid #cccccc;
        border-radius: 8px;
        padding: 8px;
    }
    .sidebar {
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        padding: 16px;
        border-radius: 12px;
    }
    .item-card {
        transition: all 0.3s ease;
    }
    .item-card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
    }
    details > summary {
        list-style: none;
        cursor: pointer;
        font-weight: 600;
        color: #333333;
    }
    details > summary::before {
        content: "+";
        display: inline-block;
        width: 1em;
        margin-right: 0.5em;
        text-align: center;
        transition: transform 0.3s ease;
    }
    details[open] > summary::before {
        transform: rotate(45deg);
    }
    .key {
        font-weight: 600;
        color: #333333;
    }
    .value {
        color: #666666;
    }
    .json-array {
        background-color: #f9f9f9;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 8px;
        margin: 4px 0;
        white-space: pre-wrap;
        font-family: monospace;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Data Catalog")

with st.sidebar:
    st.header("Import Data")
    uploaded_file = st.file_uploader("Upload JSON file", type="json")
    json_text = st.text_area("Or paste JSON here")

if uploaded_file is not None:
    try:
        data_catalog = json.load(uploaded_file)
    except json.JSONDecodeError:
        st.error("Invalid JSON file. Please upload a valid JSON file.")
        data_catalog = default_data_catalog
elif json_text:
    try:
        data_catalog = json.loads(json_text)
    except json.JSONDecodeError:
        st.error("Invalid JSON text. Please enter valid JSON.")
        data_catalog = default_data_catalog
else:
    data_catalog = default_data_catalog

html_content = display_nested_dict_html(data_catalog)
st.markdown(html_content, unsafe_allow_html=True)