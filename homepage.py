import streamlit as st  
import pandas as pd  
  
def get_styles():  
    return """  
    <style>  
    body {  
        font-family: 'Arial', sans-serif;  
    }  
    .intro {  
        font-size: 1.1em;  
        background-color: #f0f0f0;  
        padding: 15px;  
        border-radius: 5px;  
        margin-bottom: 20px;  
    }  
    .checkbox {  
        font-size: 1.1em;  
    }  
    .leaf {  
        margin-left: 20px;  
        font-size: 1em;  
        color: #333;  
    }  
    .leaf.level-1 {  
        color: #1a73e8;  
    }  
    .leaf.level-2 {  
        color: #34a853;  
    }  
    .leaf.level-3 {  
        color: #fbbc05;  
    }  
    .leaf.level-4 {  
        color: #ea4335;  
    }  
    </style>  
    """  
  
def setup_ui():  
    st.set_page_config(page_title="CMT Taxonomy")  
    st.markdown(get_styles(), unsafe_allow_html=True)  
    st.title("CMT (Cut-Make-Trim) Taxonomy")  
    st.write("""  
    <div class="intro">  
        This interactive app displays a comprehensive taxonomy of the Cut-Make-Trim (CMT) process in garment manufacturing.   
        Expand each section to explore the detailed steps and techniques involved in creating clothing.  
    </div>  
    """, unsafe_allow_html=True)  
    st.sidebar.title("About")  
    st.sidebar.info(  
        "This app provides an interactive view of the Cut-Make-Trim (CMT) process in garment manufacturing. "  
        "Use the checkboxes to expand or collapse different sections of the taxonomy."  
    )  
    st.sidebar.title("Navigation Tips")  
    st.sidebar.info(  
        "• Click on a checkbox to expand or collapse a section.\n"  
        "• Sub-items are indented for easy visualization of the hierarchy.\n"  
        "• Use the scrollbar on the right to navigate through the entire taxonomy."  
    )  
  
def render_taxonomy(data, level=0):  
    for key, value in data.items():  
        if isinstance(value, dict):  
            expanded = st.checkbox(f"{'  ' * level}{key}", key=f"{key}_{level}")  
            if expanded:  
                render_taxonomy(value, level + 1)  
        elif isinstance(value, list):  
            expanded = st.checkbox(f"{'  ' * level}{key}", key=f"{key}_{level}")  
            if expanded:  
                df = pd.DataFrame(value, columns=["Task", "Complexity"])  
                st.table(df)  
  
def render_cut():  
    cut_data = {  
        "Fabric Preparation": {  
            "Inspection and Quality Control": [  
                ("Visual inspection for defects", 6),  
                ("Measurement of fabric width and length", 4),  
                ("Testing fabric properties (shrinkage, colorfastness)", 7)  
            ],  
            "Relaxation and Conditioning": [  
                ("Allowing fabric to relax", 4),  
                ("Controlling humidity and temperature", 5)  
            ],  
            "Spreading Fabric": [  
                ("Manual spreading", 5),  
                ("Automated spreading", 6)  
            ],  
            "Handling Special Fabrics": [  
                ("Handling delicate fabrics", 8),  
                ("Handling stretchy fabrics", 7)  
            ]  
        },  
        "Pattern Engineering": {  
            "Pattern Creation": [  
                ("Manual pattern making", 8),  
                ("Digital pattern making", 9)  
            ],  
            "Grading": [  
                ("Manual grading", 7),  
                ("Digital grading", 8)  
            ],  
            "Marker Making": [  
                ("Manual marker making", 6),  
                ("Digital marker making", 7)  
            ]  
        },  
        "Cutting": {  
            "Manual Cutting": [  
                ("Using scissors", 5),  
                ("Using rotary cutters", 6)  
            ],  
            "Automated Cutting": [  
                ("Using cutting machines", 8),  
                ("Laser cutting", 9)  
            ],  
            "Handling Cut Pieces": [  
                ("Bundling and labeling", 5),  
                ("Transporting to sewing section", 4)  
            ]  
        }  
    }  
    render_taxonomy(cut_data)  
  
def render_make():  
    make_data = {  
        "Sewing": {  
            "Machine Sewing": [  
                ("Single needle lockstitch", 6),  
                ("Overlock stitching", 7),  
                ("Coverstitching", 8)  
            ],  
            "Hand Sewing": [  
                ("Hand basting", 5),  
                ("Hand hemming", 6)  
            ],  
            "Special Techniques": [  
                ("Embroidery", 9),  
                ("Applique", 8)  
            ]  
        },  
        "Assembly": {  
            "Joining Pieces": [  
                ("Seaming", 7),  
                ("Topstitching", 6)  
            ],  
            "Attaching Components": [  
                ("Sewing zippers", 8),  
                ("Sewing buttons", 7),  
                ("Attaching labels", 5)  
            ]  
        },  
        "Finishing": {  
            "Pressing": [  
                ("Using steam irons", 6),  
                ("Using pressing machines", 7)  
            ],  
            "Trimming": [  
                ("Trimming threads", 4),  
                ("Cutting excess fabric", 5)  
            ],  
            "Quality Control": [  
                ("Inspecting seams", 7),  
                ("Checking measurements", 6)  
            ]  
        }  
    }  
    render_taxonomy(make_data)  
  
def render_trim():  
    trim_data = {  
        "Packaging": {  
            "Folding": [  
                ("Manual folding", 5),  
                ("Automated folding", 6)  
            ],  
            "Bagging": [  
                ("Using poly bags", 4),  
                ("Using eco-friendly bags", 5)  
            ]  
        },  
        "Labeling": [  
            ("Attaching size labels", 4),  
            ("Attaching care labels", 5)  
        ],  
        "Final Inspection": [  
            ("Visual inspection", 6),  
            ("Measurement verification", 5)  
        ],  
        "Shipping": [  
            ("Packing into cartons", 4),  
            ("Arranging logistics", 6)  
        ]  
    }  
    render_taxonomy(trim_data)  
  
def main():  
    setup_ui()  
    st.header("Cut")  
    render_cut()  
    st.header("Make")  
    render_make()  
    st.header("Trim")  
    render_trim()  
  
if __name__ == "__main__":  
    main()  
