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
    .section-header {
        font-size: 1.2em;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #1a73e8;
    }
    .subsection-header {
        font-size: 1.1em;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 5px;
        color: #34a853;
    }
    .task-item {
        margin-left: 20px;
        font-size: 1em;
        color: #333;
    }
    .complexity-badge {
        display: inline-block;
        padding: 2px 5px;
        border-radius: 3px;
        font-size: 0.8em;
        margin-left: 5px;
    }
    </style>
    """

def setup_ui():
    st.set_page_config(page_title="Comprehensive Garment Manufacturing Process", layout="wide")
    st.markdown(get_styles(), unsafe_allow_html=True)
    st.title("Comprehensive Garment Manufacturing Process")
    st.write("""
    <div class="intro">
        This interactive app displays a comprehensive overview of the garment manufacturing process, 
        including Cut-Make-Trim (CMT) and additional stages. Explore each section to understand 
        the detailed steps and techniques involved in creating clothing.
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.title("About")
    st.sidebar.info(
        "This app provides an interactive view of the entire garment manufacturing process. "
        "Use the expanders to explore different sections of the process."
    )
    st.sidebar.title("Navigation Tips")
    st.sidebar.info(
        "• Click on an expander to view its contents.\n"
        "• Use the tabs to navigate between major process stages.\n"
        "• Complexity ratings are provided for each task (1-10 scale)."
    )

def render_process_section(data):
    for section, subsections in data.items():
        st.markdown(f"<div class='section-header'>{section}</div>", unsafe_allow_html=True)
        for subsection, tasks in subsections.items():
            with st.expander(subsection):
                st.markdown(f"<div class='subsection-header'>{subsection}</div>", unsafe_allow_html=True)
                for task, complexity, description in tasks:
                    color = get_complexity_color(complexity)
                    st.markdown(
                        f"<div class='task-item'>{task} "
                        f"<span class='complexity-badge' style='background-color: {color};'>"
                        f"Complexity: {complexity}</span></div>",
                        unsafe_allow_html=True
                    )
                    st.write(description)

def get_complexity_color(complexity):
    if complexity <= 3:
        return "#34a853"  # Green for low complexity
    elif complexity <= 6:
        return "#fbbc05"  # Yellow for medium complexity
    else:
        return "#ea4335"  # Red for high complexity

def main():
    setup_ui()
    
    # Define the process data with detailed descriptions
    process_data = {
        "1. Design and Pre-production": {
            "Concept Development": [
                ("Market research and trend analysis", 7, "Research current market trends, consumer preferences, and competitors."),
                ("Mood board creation", 6, "Create a visual representation of ideas, themes, and inspirations for the collection."),
                ("Sketch development", 8, "Develop detailed sketches of each garment, including front, back, and side views."),
            ],
            "Pattern Making": [
                ("Initial pattern drafting", 9, "Draft the initial pattern pieces based on the sketches and garment specifications."),
                ("Pattern grading", 7, "Adjust the pattern for different sizes while maintaining the design integrity."),
                ("Digitization of patterns", 6, "Convert physical patterns into digital formats for easier modifications and storage."),
            ],
            "Sampling": [
                ("Prototype creation", 8, "Create the first sample garment to test the design and fit."),
                ("Fit testing", 7, "Evaluate the fit and make necessary adjustments to the pattern."),
                ("Sample refinement", 6, "Refine the sample based on feedback and ensure it meets the desired quality standards."),
            ],
        },
        "2. Material Sourcing and Preparation": {
            "Fabric Selection": [
                ("Fiber and fabric type selection", 7, "Choose appropriate fibers and fabrics based on the garment's purpose and design."),
                ("Color and print selection", 6, "Select colors and prints that align with the collection's theme."),
                ("Quality assessment", 8, "Assess the fabric's quality, durability, and suitability for the garment."),
            ],
            "Trim and Accessory Sourcing": [
                ("Button, zipper, and hardware selection", 5, "Select suitable buttons, zippers, and other hardware components."),
                ("Label and tag ordering", 4, "Order labels and tags that match the brand's requirements."),
                ("Packaging material procurement", 3, "Source packaging materials that ensure the garment's protection during shipping."),
            ],
        },
        "3. Cut": {
            "Fabric Preparation": [
                ("Fabric inspection and quality control", 6, "Inspect the fabric for any defects or inconsistencies."),
                ("Fabric relaxation and conditioning", 5, "Allow the fabric to relax and condition to avoid shrinkage post-production."),
                ("Spreading fabric on cutting tables", 4, "Spread the fabric evenly on cutting tables to prepare for cutting."),
            ],
            "Marker Making": [
                ("Digital marker creation", 7, "Create digital markers to optimize fabric usage."),
                ("Marker efficiency optimization", 8, "Adjust markers to minimize fabric waste."),
                ("Nesting for minimal waste", 9, "Arrange patterns on the fabric to reduce leftover material."),
            ],
            "Cutting Methods": [
                ("Manual cutting", 5, "Cut fabric manually using scissors or rotary cutters."),
                ("Automated cutting (CNC, laser)", 8, "Use automated machines for precise and efficient cutting."),
                ("Die cutting", 6, "Employ die cutting for consistent shapes and sizes."),
            ],
        },
        "4. Make": {
            "Pre-sewing Operations": [
                ("Fusing and interfacing application", 6, "Apply fusible interfacing to strengthen specific garment areas."),
                ("Pleating and pressing", 7, "Create pleats and press the fabric to set the shapes."),
                ("Embroidery or print application", 8, "Add embroidery or prints as per the design specifications."),
            ],
            "Assembly": [
                ("Seam sewing", 5, "Sew the garment's main seams together."),
                ("Dart construction", 6, "Sew darts to shape the garment."),
                ("Pocket attachment", 7, "Attach pockets to the garment."),
            ],
            "Specialized Techniques": [
                ("Buttonhole creation", 7, "Create buttonholes with precision."),
                ("Zipper insertion", 6, "Insert zippers accurately."),
                ("Collar and cuff attachment", 8, "Attach collars and cuffs as per the design."),
            ],
        },
        "5. Trim": {
            "Edge Finishing": [
                ("Hemming", 5, "Finish the garment's edges with hems."),
                ("Binding application", 6, "Apply bindings to the edges for a neat finish."),
                ("Serging/overlocking edges", 4, "Serg or overlock the edges to prevent fraying."),
            ],
            "Embellishments": [
                ("Button attachment", 4, "Attach buttons securely."),
                ("Sequin or bead application", 8, "Apply sequins or beads for decorative purposes."),
                ("Appliqué", 7, "Add appliqués to enhance the garment's design."),
            ],
            "Labels and Tags": [
                ("Care label insertion", 3, "Insert care labels with washing instructions."),
                ("Brand label attachment", 4, "Attach brand labels to the garment."),
                ("Size tag application", 3, "Apply size tags as per the specifications."),
            ],
        },
        "6. Finishing and Quality Control": {
            "Pressing and Shaping": [
                ("Steam pressing", 5, "Press the garment with steam to remove wrinkles."),
                ("Garment shaping", 7, "Shape the garment to ensure proper fit."),
                ("Crease setting", 6, "Set creases as per the design."),
            ],
            "Quality Inspection": [
                ("Visual inspection", 6, "Inspect the garment visually for any defects."),
                ("Measurement verification", 5, "Verify the garment's measurements against the specifications."),
                ("Functionality testing", 7, "Test the garment's functionality, such as zipper operation."),
            ],
            "Packaging": [
                ("Folding and bagging", 4, "Fold and bag the garment for shipping."),
                ("Hang tag attachment", 3, "Attach hang tags with branding and pricing information."),
                ("Boxing for shipment", 5, "Box the garment for shipment."),
            ],
        },
        "7. Specialized Processes": {
            "Sustainable Practices": [
                ("Zero-waste pattern cutting", 9, "Implement zero-waste pattern cutting to reduce fabric waste."),
                ("Upcycling techniques", 8, "Use upcycling techniques to repurpose old garments."),
                ("Eco-friendly dyeing and finishing", 7, "Apply eco-friendly dyeing and finishing methods."),
            ],
            "High-Tech Integration": [
                ("Wearable technology incorporation", 10, "Incorporate wearable technology into garments."),
                ("Smart fabric utilization", 9, "Utilize smart fabrics with special properties."),
                ("3D-printed components", 8, "Use 3D printing for components like buttons and embellishments."),
            ],
            "Haute Couture Techniques": [
                ("Hand beading and embroidery", 10, "Apply hand beading and embroidery for intricate designs."),
                ("Custom draping and fitting", 9, "Perform custom draping and fitting for bespoke garments."),
                ("Intricate fabric manipulation", 8, "Manipulate fabrics for unique textures and patterns."),
            ],
        },
    }
    
    # Create tabs for each major process stage
    tabs = st.tabs(list(process_data.keys()))
    
    # Render each section in its corresponding tab
    for i, (section, data) in enumerate(process_data.items()):
        with tabs[i]:
            render_process_section({section: data})

if __name__ == "__main__":
    main()
