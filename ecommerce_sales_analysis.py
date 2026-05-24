import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# ============================================
#  DATA AS TEXT 
# ============================================
data_text = """Order_ID,Date,Product_Category,Sub_Category,Units,Sales_Amount,Discount,Region,Payment_Type,Return_Flag
ORD-1001,2024-01-15,Electronics,Laptop,2,1899.99,0,North,CC,No
ORD-1002,2024-01-22,Clothing,Jeans,1,59.99,0.1,South,PayPal,No
ORD-1004,2024-01-30,Electronics,Phone,0,0,0,East,CC,Yes
ORD-1005,2024-02-15,Home,Chair,3,149.97,0,West,COD,No
ORD-1007,2024-02-20,Clothing,Shoes,2,119.98,0.05,North,CC,No
ORD-1008,2024-02-28,Electronics,Laptop,1,949.99,0,South,Debit,No
ORD-1009,2024-03-04,Beauty,Makeup,5,44.95,0,East,PayPal,No
ORD-1011,2024-03-10,Clothing,Jacket,1,129.99,0.2,North,CC,No
ORD-1012,2024-03-15,Home,Lamp,2,79.98,0,West,COD,No
ORD-1013,2024-03-20,Electronics,Phone,1,699.99,0.1,South,CC,No
ORD-1014,2024-04-05,Clothing,Unknown,3,89.97,0,North,Debit,No
ORD-1016,2024-04-12,Sports,Gym Bag,1,39.99,0,East,CC,No
ORD-1017,2024-04-18,Electronics,Unknown,1,1299.99,0,West,PayPal,No
ORD-1019,2024-04-22,Home,Desk,1,399.99,0,South,COD,No
ORD-1020,2024-05-01,Clothing,Shoes,0,0,0,North,CC,No
ORD-1023,2024-05-12,Beauty,Skincare,3,89.97,0.1,West,PayPal,No
ORD-1024,2024-05-19,Clothing,Jeans,0,0,0,South,CC,Yes
ORD-1025,2024-05-25,Electronics,Headphones,1,199.99,0,North,COD,No
ORD-1027,2024-06-09,Home,Chair,4,199.96,0.1,West,Debit,No
ORD-1028,2024-06-15,Beauty,Makeup,0,0,0.15,North,PayPal,No
ORD-1029,2024-06-20,Clothing,Jacket,1,129.99,0.25,South,CC,No
ORD-1031,2024-06-28,Electronics,Laptop,1,999.99,0,East,COD,No
ORD-1032,2024-07-03,Home,Lamp,1,39.99,0,West,CC,No
ORD-1034,2024-07-10,Sports,Shoes,2,159.98,0,North,Debit,No
ORD-1035,2024-07-17,Electronics,Phone,0,0,0,South,PayPal,Yes
ORD-1036,2024-07-22,Clothing,Jeans,3,179.97,0.05,East,CC,No
ORD-1037,2024-07-28,Beauty,Skincare,2,59.98,0,West,COD,No
ORD-1039,2024-08-04,Home,Desk,1,450,0,North,CC,No
ORD-1040,2024-08-10,Electronics,Headphones,1,199.99,0.1,South,Debit,No
ORD-1042,2024-08-15,Clothing,Shoes,2,119.98,0,East,PayPal,No
ORD-1043,2024-08-20,Sports,Gym Bag,1,39.99,0,West,CC,No
ORD-1044,2024-08-25,Beauty,Makeup,4,35.96,0,North,COD,No
ORD-1045,2024-08-30,Home,Chair,1,49.99,0.1,South,CC,Yes
ORD-1046,2024-09-05,Electronics,Tablet,1,399.99,0,East,Debit,No
ORD-1048,2024-09-12,Clothing,Jacket,1,129.99,0,West,PayPal,No
ORD-1049,2024-09-18,Sports,Bike,1,499.99,0.05,North,CC,No
ORD-1050,2024-09-22,Electronics,Unknown,2,2399.98,0,South,COD,No
ORD-1052,2024-09-28,Home,Lamp,1,39.99,0,East,CC,No
ORD-1053,2024-10-03,Beauty,Skincare,2,59.98,0.2,West,Debit,No
ORD-1054,2024-10-10,Clothing,Shoes,3,179.97,0,North,PayPal,No
ORD-1056,2024-10-17,Electronics,Phone,0,0,0.1,South,CC,No
ORD-1057,2024-10-21,Home,Desk,1,399.99,0,East,COD,No
ORD-1058,2024-10-28,Sports,Shoes,1,79.99,0,West,CC,No
ORD-1060,2024-11-02,Clothing,Jeans,0,0,0,North,Debit,Yes
ORD-1061,2024-11-09,Beauty,Makeup,3,26.97,0.15,South,PayPal,No
ORD-1062,2024-11-14,Electronics,Laptop,1,1199.99,0,East,CC,No
ORD-1063,2024-11-19,Home,Chair,2,99.98,0,West,COD,No
ORD-1065,2024-11-24,Sports,Gym Bag,0,0,0,North,CC,No
ORD-1066,2024-12-01,Clothing,Jacket,2,259.98,0.1,South,Debit,No
ORD-1068,2024-12-07,Electronics,Headphones,1,199.99,0,East,PayPal,No
ORD-1069,2024-12-12,Beauty,Skincare,4,119.96,0.05,West,CC,No
ORD-1070,2024-12-18,Home,Lamp,1,39.99,0,North,COD,No
ORD-1072,2024-12-22,Clothing,Shoes,2,119.98,0.25,South,CC,No
ORD-1073,2024-12-26,Electronics,Tablet,1,399.99,0,East,Debit,No
ORD-1074,2024-12-30,Sports,Bike,2,999.98,0.1,West,PayPal,No
ORD-1075,2025-01-04,Home,Desk,1,450,0,North,CC,No
ORD-1077,2025-01-09,Clothing,Jeans,3,179.97,0,South,COD,No
ORD-1078,2025-01-14,Electronics,Phone,0,0,0,East,CC,Yes
ORD-1079,2025-01-19,Beauty,Makeup,5,44.95,0,West,Debit,No
ORD-1080,2025-01-24,Sports,Shoes,2,159.98,0,North,PayPal,No
ORD-1081,2025-01-29,Home,Chair,1,49.99,0,South,CC,No
ORD-1083,2025-02-03,Electronics,Laptop,1,1299.99,0.1,East,COD,No
ORD-1084,2025-02-08,Clothing,Jacket,1,129.99,0,West,CC,No
ORD-1085,2025-02-13,Beauty,Skincare,0,0,0,North,Debit,No
ORD-1087,2025-02-18,Sports,Gym Bag,2,79.98,0,South,PayPal,No
ORD-1088,2025-02-23,Home,Lamp,3,119.97,0.1,East,CC,No
ORD-1089,2025-02-28,Electronics,Headphones,2,399.98,0.05,West,COD,No
ORD-1090,2025-03-05,Clothing,Shoes,1,59.99,0,North,CC,No
ORD-1092,2025-03-10,Beauty,Makeup,4,35.96,0.15,South,Debit,No
ORD-1093,2025-03-15,Electronics,Tablet,1,399.99,0,East,PayPal,No
ORD-1094,2025-03-20,Home,Desk,2,900,0.05,West,CC,No
ORD-1096,2025-03-25,Sports,Bike,1,499.99,0,North,COD,No
ORD-1097,2025-03-30,Clothing,Jeans,2,119.98,0,South,CC,Yes
ORD-1098,2025-04-04,Electronics,Phone,1,649.99,0.1,East,Debit,No
ORD-1100,2025-04-09,Beauty,Skincare,3,89.97,0,West,PayPal,No"""

# ============================================
# LOAD DATA FROM TEXT STRING
# ============================================
df = pd.read_csv(io.StringIO(data_text))

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter out zero-sales for revenue analysis
df_positive = df[df['Sales_Amount'] > 0].copy()

# ============================================
# PRINT VERIFICATION
# ============================================
print("="*50)
print("DATA VERIFICATION")
print("="*50)
print(f"Total rows: {len(df)}")
print(f"Rows with positive sales: {len(df_positive)}")
print(f"Total revenue: ${df_positive['Sales_Amount'].sum():,.2f}")
print(f"Return rate: {len(df[df['Return_Flag']=='Yes'])/len(df)*100:.1f}%")
print(f"Average discount: {df['Discount'].mean()*100:.1f}%")
print("="*50)

# ============================================
# GRAPH 1: Sales by Category
# ============================================
fig, ax = plt.subplots(figsize=(10, 6))
category_sales = df_positive.groupby('Product_Category')['Sales_Amount'].sum().sort_values(ascending=False)
category_sales.plot(kind='bar', color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E'], edgecolor='black', ax=ax)
ax.set_title('💰 Total Sales by Product Category', fontsize=14, fontweight='bold')
ax.set_xlabel('Product Category', fontsize=12)
ax.set_ylabel('Sales Amount ($)', fontsize=12)
ax.tick_params(axis='x', rotation=45)
for i, v in enumerate(category_sales.values):
    ax.text(i, v + 50, f'${v:,.0f}', ha='center', fontweight='bold')
plt.tight_layout()
plt.show()

# ============================================
# GRAPH 2: Monthly Sales Trend
# ============================================
fig, ax = plt.subplots(figsize=(12, 5))
df_positive['Month'] = df_positive['Date'].dt.to_period('M')
monthly_sales = df_positive.groupby('Month')['Sales_Amount'].sum()
ax.plot(range(len(monthly_sales)), monthly_sales.values, marker='o', linewidth=2, markersize=8, color='#2E86AB')
ax.fill_between(range(len(monthly_sales)), monthly_sales.values, alpha=0.3, color='#2E86AB')
ax.set_title('📈 Monthly Sales Trend', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales Amount ($)', fontsize=12)
ax.set_xticks(range(len(monthly_sales)))
ax.set_xticklabels(monthly_sales.index.astype(str), rotation=45)
for i, v in enumerate(monthly_sales.values):
    ax.text(i, v + 50, f'${v:,.0f}', ha='center', fontsize=9)
plt.tight_layout()
plt.show()

# ============================================
# GRAPH 3: Returns by Category
# ============================================
fig, ax = plt.subplots(figsize=(10, 6))
returns_by_cat = df[df['Return_Flag'] == 'Yes'].groupby('Product_Category').size()
returns_by_cat = returns_by_cat.reindex(category_sales.index, fill_value=0)
ax.barh(returns_by_cat.index, returns_by_cat.values, color='#C73E1D', edgecolor='black')
ax.set_title('⚠️ Number of Returns by Category', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Returns', fontsize=12)
ax.set_ylabel('Product Category', fontsize=12)
for i, v in enumerate(returns_by_cat.values):
    if v > 0:
        ax.text(v + 0.1, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.show()

# ============================================
# GRAPH 4: Sales by Region (Pie Chart)
# ============================================
fig, ax = plt.subplots(figsize=(8, 8))
region_sales = df_positive.groupby('Region')['Sales_Amount'].sum()
colors = ['#FFD166', '#06D6A0', '#118AB2', '#EF476F']
wedges, texts, autotexts = ax.pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%', 
                                    colors=colors, startangle=90, explode=[0.05]*len(region_sales))
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax.set_title('🌍 Sales Distribution by Region', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# ============================================
# GRAPH 5: Top 10 Products by Sales
# ============================================
fig, ax = plt.subplots(figsize=(12, 6))
subcat_sales = df_positive.groupby('Sub_Category')['Sales_Amount'].sum().sort_values(ascending=False).head(10)
ax.bar(range(len(subcat_sales)), subcat_sales.values, color='#2E86AB', edgecolor='black')
ax.set_title('🏆 Top 10 Sub-Categories by Sales', fontsize=14, fontweight='bold')
ax.set_xlabel('Sub-Category', fontsize=12)
ax.set_ylabel('Sales Amount ($)', fontsize=12)
ax.set_xticks(range(len(subcat_sales)))
ax.set_xticklabels(subcat_sales.index, rotation=45, ha='right')
for i, v in enumerate(subcat_sales.values):
    ax.text(i, v + 50, f'${v:,.0f}', ha='center', fontweight='bold')
plt.tight_layout()
plt.show()

print("\n✅ All graphs generated successfully!")
print("📊 You should see 5 charts: Category Sales, Monthly Trend, Returns, Regional Sales, Top Products")
