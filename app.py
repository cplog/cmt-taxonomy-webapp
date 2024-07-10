import streamlit as st
import json

def display_nested_dict_html(d, level=0, max_level=3):
    html = ""
    indent = '&nbsp;' * 4 * level
    card_style = (
        "background-color: #ffffff; "
        "border: 1px solid #dbdbdb; "
        "border-radius: 8px; "
        "margin: 8px 0; "
        "padding: 12px; "
        "box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1); "
        "transition: all 0.3s ease;"
    )
    open_tag = "open" if level < max_level else ""
    
    if isinstance(d, dict):
        for key, value in d.items():
            if isinstance(value, (dict, list)):
                html += f"{indent}<details {open_tag} class='item-card' style='{card_style}'><summary>{key}</summary>"
                html += display_nested_dict_html(value, level + 1, max_level)
                html += f"{indent}</details>"
            else:
                html += f"{indent}<div class='item-card' style='{card_style}'><span class='key'>{key}:</span> <span class='value'>{value}</span></div>"
    elif isinstance(d, list):
        html += f"{indent}<ul class='item-card' style='{card_style}'>"
        for item in d:
            html += f"<li>{display_nested_dict_html(item, level + 1, max_level)}</li>"
        html += f"{indent}</ul>"
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
        background-color: #fafafa;
        color: #262626;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: #262626;
        font-weight: 600;
        font-size: 28px;
        margin-bottom: 24px;
    }
    .sidebar .stTextInput>div>div>input {
        background-color: #fafafa;
        border: 1px solid #dbdbdb;
        border-radius: 4px;
    }
    .item-card {
        transition: all 0.3s ease;
    }
    .item-card:hover {
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    details > summary {
        list-style: none;
        cursor: pointer;
        font-weight: 600;
        color: #262626;
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
        color: #262626;
    }
    .value {
        color: #8e8e8e;
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