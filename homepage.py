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
        "Fabric Preparation": [
            ("Fabric inspection and quality control", 6),
            ("Fabric relaxation and conditioning", 4),
            ("Spreading fabric on cutting tables", 5),
            ("Special handling for delicate or difficult fabrics", 8)
        ],
        "Pattern Engineering": [
            ("Pattern creation and digitization", 9),
            ("Grading for different sizes", 7),
            ("Marker making (pattern layout)", 8),
            ("Nesting for optimal fabric utilization", 7)
        ],
        "Cutting Methods": [
            ("Manual cutting (scissors, rotary cutters)", 6),
            ("Die cutting", 5),
            ("Automated cutting (CNC, laser, ultrasonic)", 7),
            ("Specialized cutting for different materials", 8)
        ],
        "Marking and Bundling": [
            ("Marking seam allowances, notches, and reference points", 5),
            ("Piece numbering and size labeling", 3),
            ("Bundle creation and ticketing", 4)
        ]
    }
    render_taxonomy(cut_data)

def render_make():
    make_data = {
        "Pre-sewing Operations": [
            ("Fusing and interfacing application", 6),
            ("Pleating and pressing", 7),
            ("Dart construction", 5),
            ("Embroidery or print application", 8)
        ],
        "Sewing and Assembly": {
            "Stitching Techniques": [
                ("Lockstitch", 3),
                ("Chainstitch", 4),
                ("Overlock/serge stitch", 5),
                ("Coverstitch", 6),
                ("Blind stitch", 7),
                ("Bartack stitch", 5),
                ("Buttonhole stitch", 6),
                ("Decorative stitching", 8)
            ],
            "Seam Types": [
                ("Plain seams", 2),
                ("French seams", 6),
                ("Flat-felled seams", 7),
                ("Bound seams", 7),
                ("Lapped seams", 6),
                ("Welt seams", 8),
                ("Specialty seams", 9)
            ],
            "Component Construction": [
                ("Collar assembly", 7),
                ("Sleeve insertion", 8),
                ("Pocket construction", 6),
                ("Zipper insertion", 7),
                ("Button attachment", 3),
                ("Waistband application", 6)
            ],
            "Special Techniques": [
                ("Quilting", 8),
                ("Ruching", 7),
                ("Gathering", 5),
                ("Pintucking", 7),
                ("Appliqué", 8),
                ("Piping insertion", 7)
            ]
        },
        "Fabric Treatments": [
            ("Washing and distressing", 6),
            ("Enzyme washing", 7),
            ("Stone washing", 6),
            ("Acid washing", 7),
            ("Sandblasting", 8),
            ("Tie-dyeing", 7)
        ],
        "Specialty Processes": [
            ("Leather working techniques", 9),
            ("Knitwear finishing", 8),
            ("Fur handling and assembly", 9)
        ]
    }
    render_taxonomy(make_data)

def render_trim():
    trim_data = {
        "Edge Finishing": [
            ("Hemming (various methods)", 5),
            ("Binding application", 6),
            ("Facing application", 6),
            ("Trimming excess fabric", 3),
            ("Serging/overlocking edges", 4)
        ],
        "Closures and Hardware": [
            ("Button attachment", 3),
            ("Buttonhole creation", 6),
            ("Snap fastener application", 4),
            ("Hook and eye attachment", 5),
            ("Rivet insertion", 5),
            ("Eyelet insertion", 5)
        ],
        "Embellishments": [
            ("Sequin application", 8),
            ("Bead work", 9),
            ("Lace application", 7),
            ("Fringe attachment", 6),
            ("Patch application", 5)
        ],
        "Labels and Tags": [
            ("Brand label attachment", 3),
            ("Size label insertion", 2),
            ("Care instruction tag application", 2),
            ("Hang tag attachment", 1)
        ],
        "Surface Treatments": [
            ("Garment dyeing", 7),
            ("Printing (screen, digital, heat transfer)", 8),
            ("Embossing", 7),
            ("Laser etching", 8),
            ("Fabric painting", 9)
        ],
        "Protective Finishes": [
            ("Water-repellent coating application", 7),
            ("Stain-resistant treatment", 6),
            ("UV-protective finish application", 7),
            ("Flame-retardant treatment", 8),
            ("Anti-microbial finish application", 7)
        ]
    }
    render_taxonomy(trim_data)

setup_ui()

tabs = st.tabs(["Cut", "Make", "Trim"])

with tabs[0]:
    render_cut()

with tabs[1]:
    render_make()

with tabs[2]:
    render_trim()