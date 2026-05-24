import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from io import StringIO
import warnings
warnings.filterwarnings('ignore')

data = """Transaction_ID,Store_ID,Store_City,Region,Transaction_Date,Product,Category,Quantity,Unit_Price,Discount,Payment_Type,Customer_Age,Customer_Tier,Return_Flag,Satisfaction_Score,Delivery_Days,Marketing_Channel,Employee_Name,Employee_Experience,Cost_Price
T001,S01,New York,East,2025-01-05,Laptop,Electronics,2,1200,0,Loyalty Card,32,Gold,No,4,3,Email,John Miller,5,900
T002,S02,Los Angeles,West,01/15/2025,Office Chair,Furniture,1,350,0.1,Credit Card,45,Silver,No,5,7,Social Media,Sarah Lee,3,250
T003,S03,Chicago,Midwest,2025-01-20,Desk Lamp,Electronics,-3,25,0.2,Cash,28,Bronze,Yes,2,N/A,TV Ad,,,18
T004,S01,New York,East,2025/01/25,Wireless Mouse,Electronics,5,45,0.15,PayPal,24,Gold,No,?,2,Email,John Miller,5,30
T005,S04,Houston,South,2025-01-30,Coffee Table,Furniture,1,150,,Credit Card,52,Silver,No,4,10,Social Media,Mike Brown,1,100
T006,S02,Los Angeles,West,2025-02-01,Monitor,Electronics,-1,300,0.2,Debit Card,34,Platinum,Yes,1,5,Email,Sarah Lee,3,220
T007,S05,Phoenix,West,2025/02/03,Desk,Furniture,1,450,0,Financing,41,Gold,No,3,12,Direct Mail,,,350
T008,S01,New York,East,02-05-2025,Keyboard,Electronics,3,75,0.5,Credit Card,29,Silver,No,5,2,SMS,John Miller,5,45
T009,S06,Philadelphia,East,2025-02-07,Notebook,Supplies,20,2.5,0,Cash,19,Bronze,No,4,1,In-Store,Emily Davis,2,1.5
T010,S03,Chicago,Midwest,2025-02-10,Gaming Chair,Furniture,1,400,0.15,,,Gold,No,4,8,Social Media,Mike Brown,1,280
T011,S07,San Antonio,South,2025-02-12,Smartphone,Electronics,1,999,0,,-1,Silver,Yes,?,4,Email,David Wilson,8,700
T012,S01,New York,East,2025-02-15,Tablet,Electronics,1,600,0.1,Credit Card,35,Platinum,No,5,1,Email,John Miller,5,450
T013,S08,San Diego,West,2025-02-18,Bookshelf,Furniture,2,200,0.2,PayPal,44,Bronze,Yes,2,14,Social Media,Sarah Lee,3,130
T014,S02,Los Angeles,West,2025-02-20,Chair Mat,Furniture,1,40,0.05,Cash,38,Silver,No,3,5,In-Store,,,25
T015,S09,Dallas,South,2025-02-22,HDMI Cable,Electronics,10,15,0,Debit Card,26,Bronze,No,5,1,Email,Tom Harris,0,10
T016,S03,Chicago,Midwest,2025-02-25,Standing Desk,Furniture,1,550,0,Financing,49,Gold,No,4,9,Direct Mail,Mike Brown,1,400
T017,S01,New York,East,2025-02-28,Mouse Pad,Supplies,-5,12,0.1,Cash,31,Silver,No,3,2,In-Store,John Miller,5,8
T018,S10,Miami,South,2025-03-01,Printer,Electronics,1,250,0,,-1,Bronze,No,?,5,Social Media,N/A,7,180
T019,S02,Los Angeles,West,2025-03-03,Desk Organizer,Supplies,2,35,0.25,Credit Card,27,Gold,No,5,3,Email,Sarah Lee,3,20
T020,S04,Houston,South,2025-03-05,Gaming Monitor,Electronics,1,400,0.1,PayPal,33,Silver,No,4,6,Social Media,Tom Harris,0,300
T021,S11,San Jose,West,2025-03-07,Office Lamp,Electronics,1,65,0,Credit Card,41,Gold,No,5,2,Email,Mike Brown,1,40
T022,S01,New York,East,2025-03-10,Laptop Stand,Accessories,2,30,0.1,Cash,29,Bronze,Yes,2,4,In-Store,John Miller,5,20
T023,S12,Austin,South,2025-03-12,Webcam,Electronics,1,80,0,Debit Card,36,Silver,No,4,3,Email,Emily Davis,2,55
T024,S03,Chicago,Midwest,2025-03-15,Cable Ties,Supplies,50,1,0.1,Cash,22,Bronze,No,3,1,In-Store,Mike Brown,1,0.5
T025,S02,Los Angeles,West,2025-03-18,Ergonomic Mouse,Electronics,2,90,0.3,Credit Card,47,Gold,No,5,2,SMS,Sarah Lee,3,60
T026,S13,Indianapolis,Midwest,2025-03-20,Desk Fan,Electronics,-2,45,0,PayPal,31,Silver,Yes,1,6,Email,,,30
T027,S01,New York,East,2025-03-22,Whiteboard,Office,1,120,0.15,Credit Card,53,Gold,No,4,5,Social Media,John Miller,5,80
T028,S14,Jacksonville,South,2025-03-25,Stapler,Supplies,3,20,0,Cash,25,Bronze,No,5,1,In-Store,Tom Harris,0,12
T029,S02,Los Angeles,West,2025-03-28,Monitor Arm,Accessories,1,85,0.2,Financing,39,Silver,No,?,4,Email,Sarah Lee,3,55
T030,S15,Columbus,Midwest,2025-03-30,Desk Drawer,Furniture,1,110,0.05,Credit Card,44,Gold,No,4,6,Direct Mail,Mike Brown,1,75
T031,S01,New York,East,2025-04-01,USB Hub,Electronics,4,25,0,Debit Card,28,Bronze,No,5,2,Email,John Miller,5,15
T032,S16,Charlotte,South,2025-04-03,Office Chair,Electronics,1,300,0.1,PayPal,37,Silver,Yes,3,9,Social Media,Emily Davis,2,210
T033,S03,Chicago,Midwest,2025-04-05,Standing Mat,Accessories,1,50,0,,-1,Gold,No,?,5,In-Store,Mike Brown,1,30
T034,S02,Los Angeles,West,2025-04-07,Desk Light,Electronics,2,35,0.1,Credit Card,34,Bronze,No,4,3,Email,Sarah Lee,3,20
T035,S17,Fort Worth,South,2025-04-10,Monitor Stand,Accessories,3,25,0.15,Cash,26,Silver,Yes,2,2,Social Media,Tom Harris,0,15
T036,S01,New York,East,2025-04-12,Laptop Bag,Accessories,1,55,0,Credit Card,42,Gold,No,5,1,Email,John Miller,5,35
T037,S18,Detroit,Midwest,2025-04-15,Desk Mat,Accessories,2,40,0.1,PayPal,29,Bronze,No,4,3,SMS,,,25
T038,S04,Houston,South,2025-04-17,Wireless Keyboard,Electronics,1,120,0,Debit Card,31,Silver,No,5,2,Email,Mike Brown,1,85
T039,S19,Memphis,South,2025-04-20,Phone Stand,Accessories,15,12,0.5,Cash,19,Bronze,Yes,1,4,In-Store,Emily Davis,2,8
T040,S02,Los Angeles,West,2025-04-22,Desk Organizer,Supplies,1,45,0,Credit Card,48,Gold,No,4,3,Email,Sarah Lee,3,30
T041,S20,Boston,East,2025-04-25,Gaming Desk,Furniture,1,600,0.2,Financing,35,Platinum,No,5,10,Social Media,David Wilson,8,420
T042,S01,New York,East,2025-04-27,Cable Management,Supplies,8,18,0.05,Cash,27,Bronze,No,3,1,In-Store,John Miller,5,12
T043,S03,Chicago,Midwest,2025-04-30,Office Phone,Electronics,1,250,0.1,Credit Card,52,Silver,No,4,5,Email,Mike Brown,1,180
T044,S21,Seattle,West,2025-05-02,Desk Drawer,Furniture,2,85,0,Cash,33,Gold,No,5,4,In-Store,,,55
T045,S02,Los Angeles,West,2025-05-04,Laptop Cooler,Electronics,1,40,0.15,PayPal,25,Bronze,No,5,2,Email,Sarah Lee,3,25
T046,S01,New York,East,2025-05-06,Standing Desk,Electronics,1,550,0.25,Credit Card,41,Platinum,Yes,1,3,Social Media,John Miller,5,400
T047,S22,Denver,West,2025-05-08,Desk Calendar,Supplies,2,25,0,Cash,38,Silver,No,4,1,In-Store,Tom Harris,0,15
T048,S04,Houston,South,2025-05-10,Mouse Pad,Supplies,-10,8,0.1,Debit Card,29,Bronze,Yes,2,3,Email,Mike Brown,1,5
T049,S03,Chicago,Midwest,2025-05-12,Desk Lamp,Electronics,2,45,0.2,Credit Card,44,Gold,No,3,4,Social Media,Mike Brown,1,30
T050,S23,Portland,West,2025-05-15,Office Chair,Electronics,1,350,0.05,Financing,36,Silver,No,5,8,Direct Mail,Emily Davis,2,250"""

df = pd.read_csv(StringIO(data))

def clean_data(df):
    df_clean = df.copy()
    
    df_clean['Quantity'] = pd.to_numeric(df_clean['Quantity'], errors='coerce')
    df_clean['Quantity'] = df_clean['Quantity'].abs()
    df_clean['Quantity'].fillna(df_clean['Quantity'].median(), inplace=True)
    
    df_clean['Unit_Price'] = pd.to_numeric(df_clean['Unit_Price'], errors='coerce')
    df_clean['Unit_Price'].fillna(df_clean['Unit_Price'].median(), inplace=True)
    df_clean['Cost_Price'] = pd.to_numeric(df_clean['Cost_Price'], errors='coerce')
    df_clean['Cost_Price'].fillna(df_clean['Cost_Price'].median(), inplace=True)
    
    df_clean['Discount'] = pd.to_numeric(df_clean['Discount'], errors='coerce')
    df_clean['Discount'].fillna(0, inplace=True)
    
    df_clean['Revenue'] = df_clean['Quantity'] * df_clean['Unit_Price'] * (1 - df_clean['Discount'])
    df_clean['Profit'] = df_clean['Revenue'] - (df_clean['Quantity'] * df_clean['Cost_Price'])
    df_clean['Profit_Margin'] = (df_clean['Profit'] / df_clean['Revenue']) * 100
    
    def parse_date(date_str):
        if pd.isna(date_str):
            return np.nan
        date_str = str(date_str).strip()
        formats = ['%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d', '%d-%m-%Y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except:
                continue
        return np.nan
    
    df_clean['Transaction_Date'] = df_clean['Transaction_Date'].apply(parse_date)
    df_clean = df_clean.dropna(subset=['Transaction_Date'])
    
    df_clean['Customer_Age'] = pd.to_numeric(df_clean['Customer_Age'], errors='coerce')
    df_clean.loc[df_clean['Customer_Age'] < 18, 'Customer_Age'] = df_clean['Customer_Age'].median()
    df_clean['Customer_Age'].fillna(df_clean['Customer_Age'].median(), inplace=True)
    
    df_clean['Satisfaction_Score'] = pd.to_numeric(df_clean['Satisfaction_Score'], errors='coerce')
    df_clean['Satisfaction_Score'].fillna(df_clean['Satisfaction_Score'].median(), inplace=True)
    
    df_clean['Delivery_Days'] = pd.to_numeric(df_clean['Delivery_Days'], errors='coerce')
    df_clean['Delivery_Days'].fillna(df_clean['Delivery_Days'].median(), inplace=True)
    
    df_clean['Employee_Name'] = df_clean['Employee_Name'].fillna('Unassigned')
    df_clean['Employee_Experience'] = pd.to_numeric(df_clean['Employee_Experience'], errors='coerce')
    df_clean['Employee_Experience'].fillna(0, inplace=True)
    
    df_clean['Customer_Tier'] = df_clean['Customer_Tier'].fillna('Bronze')
    df_clean['Return_Flag'] = df_clean['Return_Flag'].fillna('No')
    df_clean['Marketing_Channel'] = df_clean['Marketing_Channel'].fillna('Unknown')
    
    return df_clean

df_clean = clean_data(df)

print("="*80)
print("RETAIL CHAIN INTELLIGENCE PLATFORM")
print("="*80)

print(f"\nTotal Revenue: ${df_clean['Revenue'].sum():,.2f}")
print(f"Total Profit: ${df_clean['Profit'].sum():,.2f}")

store_perf = df_clean.groupby('Store_ID').agg({'Profit': 'sum', 'Revenue': 'sum'})
store_perf['Margin'] = (store_perf['Profit'] / store_perf['Revenue']) * 100
worst_stores = store_perf.sort_values('Profit').head(3)

print("\n" + "="*80)
print("BOTTLENECKS IDENTIFIED")
print("="*80)

print("\nWorst Performing Stores:")
for store in worst_stores.iterrows():
    print(f"  Store {store[0]}: Lost ${abs(store[1]['Profit']):,.0f} | Margin: {store[1]['Margin']:.1f}%")

cat_perf = df_clean.groupby('Category').agg({'Profit': 'sum', 'Revenue': 'sum', 'Return_Flag': lambda x: (x == 'Yes').sum()})
cat_perf['Margin'] = (cat_perf['Profit'] / cat_perf['Revenue']) * 100
cat_perf['Return_Rate'] = (cat_perf['Return_Flag'] / len(df_clean)) * 100
worst_cat = cat_perf[cat_perf['Profit'] < 0]

print("\nWorst Performing Categories:")
for cat in worst_cat.iterrows():
    print(f"  {cat[0]}: Lost ${abs(cat[1]['Profit']):,.0f} | Margin: {cat[1]['Margin']:.1f}% | Returns: {cat[1]['Return_Rate']:.1f}%")

emp_perf = df_clean[df_clean['Employee_Name'] != 'Unassigned'].groupby('Employee_Name').agg({'Profit': 'sum', 'Satisfaction_Score': 'mean'})
worst_emp = emp_perf.sort_values('Profit').head(1)
best_emp = emp_perf.sort_values('Profit', ascending=False).head(1)

print("\nEmployee Performance:")
print(f"  Best: {best_emp.index[0]} - ${best_emp['Profit'].iloc[0]:,.0f} profit | Satisfaction: {best_emp['Satisfaction_Score'].iloc[0]:.1f}/5")
print(f"  Worst: {worst_emp.index[0]} - ${worst_emp['Profit'].iloc[0]:,.0f} profit | Satisfaction: {worst_emp['Satisfaction_Score'].iloc[0]:.1f}/5")

delivery_impact = df_clean.groupby(pd.cut(df_clean['Delivery_Days'], bins=[0,2,5,10,20,50]))['Satisfaction_Score'].mean()
print("\nDelivery Impact on Satisfaction:")
for interval in delivery_impact.index:
    print(f"  {interval} days: {delivery_impact[interval]:.1f}/5 satisfaction")

return_rates = df_clean.groupby('Category').apply(lambda x: (x['Return_Flag'] == 'Yes').mean() * 100)
print("\nReturn Rates by Category:")
for cat, rate in return_rates.items():
    print(f"  {cat}: {rate:.1f}%")

tier_profit = df_clean.groupby('Customer_Tier')['Profit'].mean()
print("\nCustomer Tier Value (Avg Profit per Transaction):")
for tier, profit in tier_profit.items():
    print(f"  {tier}: ${profit:.0f}")

region_perf = df_clean.groupby('Region').agg({'Profit': 'sum', 'Store_ID': 'nunique'})
region_perf['Profit_per_Store'] = region_perf['Profit'] / region_perf['Store_ID']
print("\nRegional Performance:")
for region in region_perf.iterrows():
    print(f"  {region[0]}: ${region[1]['Profit_per_Store']:,.0f} profit/store | {region[1]['Store_ID']:.0f} stores")

best_region = region_perf.sort_values('Profit_per_Store', ascending=False).head(1)
print(f"\nBest Expansion Region: {best_region.index[0]} - ${best_region['Profit_per_Store'].iloc[0]:,.0f} profit per store")

best_cat = cat_perf.sort_values('Profit', ascending=False).head(1)
print(f"\nTop Growth Category: {best_cat.index[0]} - ${best_cat['Profit'].iloc[0]:,.0f} profit | {best_cat['Margin'].iloc[0]:.1f}% margin")

total_bottleneck = abs(worst_stores['Profit'].sum()) + abs(worst_cat['Profit'].sum()) + abs(worst_emp['Profit'].iloc[0])
print(f"\nTotal Bottleneck Cost: ${total_bottleneck:,.0f}")

print("\n" + "="*80)
print("EXECUTIVE SUMMARY & RECOMMENDATIONS")
print("="*80)

print(f"""
Current State:
- Revenue: ${df_clean['Revenue'].sum():,.0f}
- Profit: ${df_clean['Profit'].sum():,.0f}
- Profit Margin: {(df_clean['Profit'].sum()/df_clean['Revenue'].sum()*100):.1f}%
- Avg Satisfaction: {df_clean['Satisfaction_Score'].mean():.1f}/5
- Avg Delivery: {df_clean['Delivery_Days'].mean():.1f} days

Immediate Actions (30 days):
1. Retrain or replace {worst_emp.index[0]} (lost ${abs(worst_emp['Profit'].iloc[0]):,.0f})
2. Discontinue {worst_cat.index[0]} category (lost ${abs(worst_cat['Profit'].iloc[0]):,.0f})
3. Fix delivery to under 3 days (satisfaction drops {4.5 - delivery_impact.iloc[1]:.1f} points when >5 days)

Growth Opportunities (60-90 days):
1. Open 2 new stores in {best_region.index[0]} region (${best_region['Profit_per_Store'].iloc[0]:,.0f} per store)
2. Expand {best_cat.index[0]} category nationally ({best_cat['Margin'].iloc[0]:.1f}% margin)
3. Launch Platinum loyalty program (${tier_profit['Platinum']:.0f} vs ${tier_profit['Bronze']:.0f} Bronze)

Projected Impact:
- Bottleneck recovery: +${total_bottleneck:,.0f}
- New stores: +${best_region['Profit_per_Store'].iloc[0] * 2:,.0f}
- Total potential upside: +${total_bottleneck + (best_region['Profit_per_Store'].iloc[0] * 2):,.0f}
- New profit margin: {((df_clean['Profit'].sum() + total_bottleneck + (best_region['Profit_per_Store'].iloc[0] * 2)) / df_clean['Revenue'].sum() * 100):.1f}%
""")

fig = plt.figure(figsize=(16, 12))
fig.suptitle('RETAIL CHAIN INTELLIGENCE DASHBOARD', fontsize=18, fontweight='bold')

ax1 = plt.subplot(2, 3, 1)
cat_profit = df_clean.groupby('Category')['Profit'].sum().sort_values()
colors = ['red' if x < 0 else 'green' for x in cat_profit.values]
ax1.barh(cat_profit.index, cat_profit.values, color=colors)
ax1.set_xlabel('Profit ($)')
ax1.set_title('Profit by Category')
ax1.axvline(x=0, color='black', linewidth=1)
for bar, val in zip(ax1.patches, cat_profit.values):
    ax1.text(val, bar.get_y() + bar.get_height()/2, f'${val:,.0f}', ha='left' if val>0 else 'right', fontsize=9)

ax2 = plt.subplot(2, 3, 2)
store_profit = df_clean.groupby('Store_ID')['Profit'].sum().sort_values().head(8)
colors2 = ['darkred' if x < 0 else 'darkgreen' for x in store_profit.values]
ax2.barh(store_profit.index, store_profit.values, color=colors2)
ax2.set_xlabel('Profit ($)')
ax2.set_title('Worst Performing Stores')
for bar, val in zip(ax2.patches, store_profit.values):
    ax2.text(val, bar.get_y() + bar.get_height()/2, f'${val:,.0f}', ha='left' if val>0 else 'right', fontsize=8)

ax3 = plt.subplot(2, 3, 3)
delivery_impact.plot(kind='bar', ax=ax3, color='purple', alpha=0.7)
ax3.set_xlabel('Delivery Days')
ax3.set_ylabel('Satisfaction Score (1-5)')
ax3.set_title('Delivery Impact on Satisfaction')
ax3.set_ylim(1, 5)
ax3.axhline(y=4, color='green', linestyle='--', label='Target (4.0)')
ax3.legend()
ax3.set_xticklabels(['0-2', '3-5', '6-10', '11-20', '20+'], rotation=45)

ax4 = plt.subplot(2, 3, 4)
emp_data = emp_perf.sort_values('Profit', ascending=False).head(6)
ax4.barh(emp_data.index, emp_data['Profit'], color='skyblue')
ax4.set_xlabel('Total Profit ($)')
ax4.set_title('Top 6 Employee Performance')
for bar, val in zip(ax4.patches, emp_data['Profit']):
    ax4.text(val, bar.get_y() + bar.get_height()/2, f'${val:,.0f}', ha='left', fontsize=8)

ax5 = plt.subplot(2, 3, 5)
tier_profit.plot(kind='bar', ax=ax5, color=['gold', 'silver', 'brown', 'orange'])
ax5.set_xlabel('Customer Tier')
ax5.set_ylabel('Avg Profit per Transaction ($)')
ax5.set_title('Profit by Customer Tier')
for bar, val in zip(ax5.patches, tier_profit.values):
    ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'${val:.0f}', ha='center', va='bottom', fontsize=9)

ax6 = plt.subplot(2, 3, 6)
return_rates.plot(kind='bar', ax=ax6, color='coral')
ax6.set_xlabel('Category')
ax6.set_ylabel('Return Rate (%)')
ax6.set_title('Return Rate by Category')
plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45)
for bar, val in zip(ax6.patches, return_rates.values):
    ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{val:.1f}%', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('executive_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

df_clean.to_csv('cleaned_retail_data.csv', index=False)

print("\n" + "="*80)
print("FILES GENERATED")
print("="*80)
print("  executive_dashboard.png - Dashboard image for LinkedIn")
print("  cleaned_retail_data.csv - Cleaned dataset with revenue and profit")
