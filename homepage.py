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
            "Fabric inspection and quality control": [  
                ("Visual and instrumental inspection for defects", 6),  
                ("Measuring fabric weight, width, and other specifications", 4)  
            ],  
            "Fabric relaxation and conditioning": [  
                ("Allowing fabric to relax before cutting to prevent shrinkage", 4),  
                ("Humidity control", 5)  
            ],  
            "Spreading fabric on cutting tables": [  
                ("Manual spreading", 5),  
                ("Automated spreading machines", 6)  
            ],  
            "Special handling for delicate or difficult fabrics (e.g., silk, velvet, leather)": [  
                ("Using specific techniques and equipment to prevent damage", 8)  
            ]  
        },  
        "Pattern Engineering": {  
            "Pattern creation and digitization": [  
                ("Using CAD software for precision", 8)  
            ],  
            "Grading for different sizes": [  
                ("Ensuring consistency across sizes", 7)  
            ],  
            "Marker making (pattern layout)": [  
                ("Optimizing fabric usage", 6),  
                ("Nesting for optimal fabric utilization", 7),  
                ("Reducing waste through strategic pattern placement", 7)  
            ]  
        },  
        "Cutting Methods": {  
            "Manual cutting (scissors, rotary cutters)": [  
                ("Suitable for small batches and custom orders", 5)  
            ],  
            "Die cutting": [  
                ("Efficient for repetitive shapes", 6)  
            ],  
            "Automated cutting (CNC, laser, ultrasonic)": [  
                ("High precision and efficiency for large batches", 8)  
            ],  
            "Specialized cutting for different materials (e.g., leather skiving)": [  
                ("Techniques adapted to specific fabric properties", 7)  
            ]  
        },  
        "Marking and Bundling": {  
            "Marking seam allowances, notches, and other reference points": [  
                ("Using chalk, markers, or digital methods", 5)  
            ],  
            "Piece numbering and size labeling": [  
                ("Ensuring accurate assembly", 4)  
            ],  
            "Bundle creation and ticketing": [  
                ("Organizing pieces for efficient workflow", 5)  
            ]  
        }  
    }  
    render_taxonomy(cut_data)  
  
def render_make():  
    make_data = {  
        "Pre-sewing Operations": {  
            "Fusing and interfacing application": [  
                ("Adding structure and support", 6)  
            ],  
            "Pleating and pressing": [  
                ("Creating design elements and ensuring crisp lines", 7)  
            ],  
            "Dart construction": [  
                ("Shaping the garment to fit the body", 5)  
            ],  
            "Embroidery or print application": [  
                ("Adding decorative or brand-specific elements", 8)  
            ]  
        },  
        "Sewing and Assembly": {  
            "Stitching Techniques": [  
                ("Lockstitch", 6),  
                ("Chainstitch", 7),  
                ("Overlock/serge stitch", 8),  
                ("Coverstitch", 7),  
                ("Blind stitch", 6),  
                ("Bartack stitch", 7),  
                ("Buttonhole stitch", 8),  
                ("Decorative stitching (e.g., embroidery, smocking)", 9)  
            ],  
            "Seam Types": [  
                ("Plain seams", 5),  
                ("French seams", 6),  
                ("Flat-felled seams", 7),  
                ("Bound seams", 6),  
                ("Lapped seams", 7),  
                ("Welt seams", 8),  
                ("Specialty seams (e.g., waterproof, stretchy)", 9)  
            ],  
            "Component Construction": [  
                ("Collar assembly", 6),  
                ("Sleeve insertion", 7),  
                ("Pocket construction (various types)", 6),  
                ("Zipper insertion (various methods)", 8),  
                ("Button attachment", 7),  
                ("Waistband application", 6)  
            ],  
            "Special Techniques": [  
                ("Quilting", 8),  
                ("Ruching", 7),  
                ("Gathering", 6),  
                ("Pintucking", 7),  
                ("Appliqué", 8),  
                ("Piping insertion", 7)  
            ],  
            "Fabric Treatments": [  
                ("Washing and distressing (e.g., for denim)", 7),  
                ("Enzyme washing", 6),  
                ("Stone washing", 7),  
                ("Acid washing", 8),  
                ("Sandblasting", 7),  
                ("Tie-dyeing", 8)  
            ],  
            "Specialty Processes": [  
                ("Leather working techniques", 8),  
                ("Knitwear finishing", 7),  
                ("Fur handling and assembly", 9)  
            ]  
        }  
    }  
    render_taxonomy(make_data)  
  
def render_trim():  
    trim_data = {  
        "Edge Finishing": [  
            ("Hemming (various methods)", 6),  
            ("Binding application", 7),  
            ("Facing application", 6),  
            ("Trimming excess fabric", 5),  
            ("Serging/overlocking edges", 6)  
        ],  
        "Closures and Hardware": [  
            ("Button attachment", 7),  
            ("Buttonhole creation", 8),  
            ("Snap fastener application", 6),  
            ("Hook and eye attachment", 5),  
            ("Rivet insertion", 7),  
            ("Eyelet insertion", 6)  
        ],  
        "Embellishments": [  
            ("Sequin application", 8),  
            ("Bead work", 7),  
            ("Lace application", 6),  
            ("Fringe attachment", 7),  
            ("Patch application", 6)  
        ],  
        "Labels and Tags": [  
            ("Brand label attachment", 5),  
            ("Size label insertion", 4),  
            ("Care instruction tag application", 5),  
            ("Hang tag attachment", 4)  
        ],  
        "Surface Treatments": [  
            ("Garment dyeing", 7),  
            ("Printing (screen, digital, heat transfer)", 8),  
            ("Embossing", 7),  
            ("Laser etching", 8),  
            ("Fabric painting", 7)  
        ],  
        "Protective Finishes": [  
            ("Water-repellent coating application", 8),  
            ("Stain-resistant treatment", 7),  
            ("UV-protective finish application", 8),  
            ("Flame-retardant treatment", 9),  
            ("Anti-microbial finish application", 8)  
        ]  
    }  
    render_taxonomy(trim_data)  
  
def render_quality_control():  
    qc_data = {  
        "Inspection": [  
            ("In-line quality checks", 7),  
            ("Final garment inspection", 8),  
            ("Measurement verification", 6)  
        ],  
        "Pressing and Shaping": [  
            ("Seam pressing", 6),  
            ("Final pressing and steaming", 7),  
            ("Shaping on forms or mannequins", 8)  
        ],  
        "Packaging": [  
            ("Folding and bagging", 5),  
            ("Hanger insertion", 4),  
            ("Box packaging", 6),  
            ("Special packaging for delicate items", 7)  
        ],  
        "Testing": [  
            ("Fabric performance testing (e.g., colorfastness, shrinkage)", 8),  
            ("Garment durability testing", 7),  
            ("Fit model testing", 6),  
            ("Wash testing", 7)  
        ]  
    }  
    render_taxonomy(qc_data)  
  
def render_specialized_processes():  
    sp_data = {  
        "Haute Couture Techniques": [  
            ("Hand beading and embroidery", 9),  
            ("Fabric manipulation (e.g., origami folding, fabric flowers)", 8),  
            ("Custom fitting and draping", 9)  
        ],  
        "Technical Garment Manufacturing": [  
            ("Seam sealing for waterproof garments", 8),  
            ("Welded seam construction", 9),  
            ("Integration of wearable technology", 8),  
            ("Protective gear assembly (e.g., bulletproof vests)", 9)  
        ],  
        "Sustainable Practices": [  
            ("Zero-waste pattern cutting", 8),  
            ("Upcycling and garment reconstruction", 7),  
            ("Use of eco-friendly dyes and treatments", 8),  
            ("Implementation of circular fashion principles", 9)  
        ]  
    }  
    render_taxonomy(sp_data)  
  
def main():  
    setup_ui()  
    tabs = st.tabs(["Cut", "Make", "Trim", "Quality Control and Finishing", "Specialized Processes"])  
  
    with tabs[0]:  
        st.header("Cut")  
        render_cut()  
  
    with tabs[1]:  
        st.header("Make")  
        render_make()  
  
    with tabs[2]:  
        st.header("Trim")  
        render_trim()  
  
    with tabs[3]:  
        st.header("Quality Control and Finishing")  
        render_quality_control()  
  
    with tabs[4]:  
        st.header("Specialized Processes")  
        render_specialized_processes()  
  
if __name__ == "__main__":  
    main()  
