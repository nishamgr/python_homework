import sqlite3
import pandas as pd

def main():
    # connecting to the sqlite db
    conn = sqlite3.connect("../db/lesson.db")
    # sql statement
    query = """
    SELECT 
        line_items.line_item_id,
        line_items.quantity,
        products.product_id,
        products.product_name,
        products.price 
    FROM line_items
    JOIN products
        ON line_items.product_id = products.product_id
    """
    # loads result into df
    df = pd.read_sql_query(query, conn)  
    print(df.head())
    
    df['total'] = df['quantity'] * df['price']
    print(df.head())
    
    summary = df.groupby('product_id').agg({
        'line_item_id' : 'count',
        'total': 'sum',
        'product_name': 'first'
    }).reset_index()

    # sort bt product_name
    summary = summary.sort_values(by='product_name')
    print(summary.head())
    # write to csv
    summary.to_csv("order_summary.csv", index=False)
    

    conn.close()
    
if __name__ == "__main__":
    main()