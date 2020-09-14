gst_free_products = []
gst_rate = 0.0
def price_after_gst(gross_price, product):
    if product in gst_free_products:
        gst = 0
    else:
        gst = gross_price * gst_rate
    return gross_price + gst

def customer_price(purch_price, product, best_before_days):
    base_price = purch_price + purch_price*0.1
    if best_before_days <= 1:
        reduction = base_price*0.6
    elif best_before_days <= 4:
        reduction = base_price*0.3
    else:
        reduction = 0
        gross_price = base_price - reduction
    return round(price_after_gst(gross_price, product), 2)


    


        