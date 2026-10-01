import streamlit as st

st.set_page_config(
    page_title= "Smart Warehouse Inventory Manager",
    page_icon= "🏢",
    layout= "wide",
    initial_sidebar_state= "collapsed"
)

if "products_num" not in st.session_state:
    st.session_state.products_num = 0

if "total_quantity" not in st.session_state:
    st.session_state.total_quantity = 0

if "inventory_data" not in st.session_state:
    st.session_state.inventory_data = []

def side_bar():
    st.subheader("Warehouse Name")
    st.info("NoNa Warehouse")

    st.subheader("Total number of products")
    st.info(st.session_state.products_num)

    st.subheader("Total quantity in stock")
    st.info(st.session_state.total_quantity)

    choice = st.sidebar.radio("Main Sections", 
                     ["Add Product",
                      "View Inventory"])

    return choice

st.title("🏢 Smart Warehouse Inventory Manager", text_alignment= "center")

with st.sidebar:
    choice = side_bar()

if choice == "Add Product":
    col1, col2, col3 = st.columns(3)

    with col2:
        st.header("➕ Add a New Product")
        with st.form("Add Product"):
            productID = st.text_input("Product ID")
            productName = st.selectbox("Product Name",
                        ["Laptop",
                        "Pink Blouse",
                        "Gaming Mouse",
                        "Jeans",
                        "Jean Skirt",
                        "Headphones"])
            quantity = st.number_input("Quantity", min_value=1)
            unit_price = st.number_input("Unit Price", min_value=1)

            category = st.radio("Category", 
                    [
                        "Clothing",
                        "Electronics"
                    ])

            add = st.form_submit_button("Add Product")

            if(add):
                duplicatedID = False
                for product in st.session_state.inventory_data:
                    if product.get("ID") == productID:
                        duplicatedID = True

                if not duplicatedID:
                    st.session_state.total_quantity += quantity
                    st.session_state.inventory_data.append({
                        "ID": productID,
                        "Name": productName,
                        "Quantity": quantity,
                        "Unit Price": unit_price,
                        "category": category,
                    })
                    st.rerun()
                else:
                    st.error("Another product has the same ID")
    
elif choice == "View Inventory":
    st.header("📦 View Inventory")
    



