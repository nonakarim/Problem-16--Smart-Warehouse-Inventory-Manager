import streamlit as st

# Page Configuration
st.set_page_config(
    page_title= "Smart Warehouse Inventory Manager",
    page_icon= "🏢",
    layout= "wide",
    initial_sidebar_state= "collapsed"
)

# Declaring data I want to survive rerun 

if "products_num" not in st.session_state:
    st.session_state.products_num = 0

if "total_quantity" not in st.session_state:
    st.session_state.total_quantity = 0

if "inventory_data" not in st.session_state:
    st.session_state.inventory_data = []

def side_bar():
    """shows Program Summary in sidebar"""

    # Displays Warehouse Name
    st.subheader("Warehouse Name")
    st.info("NoNa Warehouse")

    # Displays Total Number Of Products in NoNa Warehouse
    st.subheader("Total number of products")
    st.info(st.session_state.products_num)

    # Displays Total Quantity In NoNa Warehouse
    st.subheader("Total quantity in stock")
    st.info(st.session_state.total_quantity)

    # Page Selection
    choice = st.sidebar.radio("Main Sections", 
                     ["Add Product",
                      "View Inventory",
                      "Search Products",
                      "Stock Management"])

    return choice

def data_enter_form():
    id = st.text_input("Product ID")
    name = st.text_input("Product Name")
    category = st.selectbox("Category", 
                            [
                                "Clothing",
                                "Electronics"
                            ])
    quantity = 0
    unit_price = st.number_input("Unit Price", min_value=1)
    add = st.form_submit_button("Add Product")

    return id, name, category, quantity, unit_price, add

def duplicateID(ID):
    for product in st.session_state.inventory_data:
        if product.get("ID") == ID:
            return True

    return False

def duplicateProduct(name):
    for product in st.session_state.inventory_data:
        if product.get("Name") == name:
            return True

    return False

def searchMethod():
    st.subheader("Use:")
    useID = st.checkbox("Product ID")
    useName = st.checkbox("Product Name")
    useCategory = st.checkbox("Product Category")

    return useID, useName, useCategory

def searchUsingID(searchID):
    search_list = []

    for id in st.session_state.inventory_data:
        if id.get("ID") == searchID:
            search_list.append(id)

    return search_list

def searchUsingName(searchName):
    search_list = []

    for name in st.session_state.inventory_data:
        if name.get("Name") == searchName:
            search_list.append(name)

    return search_list

def searchUsingCategory(searchCategory):
    search_list = []
    
    for category in st.session_state.inventory_data:
        if category.get("Category") == searchName:
            search_list.append(category)

    return search_list

def restock_product():
    st.header("A. Restock Product")
    
    names = []

    for name in st.session_state.inventory_data:
        names.append(name.get("Name"))

    product = st.selectbox("Products", names)
    new_quantity = st.number_input("Enter New Quantity", min_value= 1)
    restock = st.button("Restock")

    if restock:
        st.session_state.total_quantity += new_quantity

        for name in st.session_state.inventory_data:
            if name.get("Name") == product:
                name["Quantity"] = new_quantity

        st.rerun()
    

st.title("🏢 Smart Warehouse Inventory Manager", text_alignment= "center")

with st.sidebar:
    choice = side_bar()

if choice == "Add Product":
    col1, col2, col3 = st.columns(3)

    with col2:
        st.header("➕ Add a New Product")
        with st.form("Add Product"):
            productID, productName, category, quantity, unit_price, add = data_enter_form()
    
            if(add):
                duplicatedID = duplicateID(productID)
                duplicatedProduct = duplicateProduct(productName)

                if not productID == "" and not productName == "":
                    if not duplicatedID and not duplicatedProduct:
                        
                        st.session_state.products_num += 1

                        st.session_state.inventory_data.append({
                            "ID": productID,
                            "Name": productName,
                            "Unit Price": unit_price,
                            "Quantity": quantity,
                            "category": category,
                        })
                        st.rerun()
                    else:
                        st.warning("Another product has the same ID or Name")
                else:
                    st.error("May NOT Leave Space Empty")
        
elif choice == "View Inventory":
    col1, col2, col3 = st.columns(3)
    st.header("📦 View Inventory")

    if st.session_state.inventory_data != []:
        st.table(st.session_state.inventory_data)
    else:
        st.info("No Products Yet")

elif choice == "Search Products":
    useID, useName, UseCategory = searchMethod()
    search_list = []

    if useID:
        searchID = st.text_input("Product ID", key= "ID")
        search_list.extend(searchUsingID(searchID))

    if useName:
        searchName = st.text_input("Product Name", key= "Name")
        search_list.extend(searchUsingName(searchName))

    if UseCategory:
        searchCategory = st.text_input("Product Category", key= "Category")
        search_list.extend(searchUsingCategory(searchCategory))

    search = st.button("Search")
    if search:
        seen_ids = set()
        unique_products = []

        for product in search_list:
            product_id = product.get("ID")

        if product_id not in seen_ids:
            unique_products.append(product)
            seen_ids.add(product_id)
        
            st.table(unique_products)

if choice == "Stock Management":
    restock_product()

    
