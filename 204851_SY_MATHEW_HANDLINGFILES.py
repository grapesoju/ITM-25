products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code, property):
    return products[code][property]

def checker(order_list, code):
    codes=[]
    for x in order_list:
        codes.append(x['code'])
    if code in codes:
        return True, codes.index(code)
    else:
        return False, 0


def main():
    order_list=[]
    total=0
    x=True
    
    while x:
        order=input()
        
        if order=='/':
            x=False
            
        else:
            code_list=order.split(',')
            code=code_list[0]
            quantity=code_list[1]
            int_qty=int(quantity)
            
            if code in products:
                subtotal=get_property(code, 'price')*int_qty
                
                check=checker(order_list, code)
                if check[0]:
                    order_list[check[1]]['subtotal']+=subtotal
                    order_list[check[1]]['quantity']+=int_qty
                    
                else:
                    ordered_item=dict([('code', code), ('quantity', int_qty), ('subtotal', subtotal)])
                    order_list.append(ordered_item)
                total+=subtotal
                
            else:
                print('The code you entered is invalid')
                
    
    
                
    with open('receipt.txt', 'w') as receipt:
        header='''
        ==
        CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
        '''
        order_list= sorted(order_list, key=lambda k:k['code'])
    
        receipt.write(header)
        body=''
        for order in order_list:
            order_code=order['code']
            order_name=products[order_code]['name']
            order_qty=order['quantity']
            order_subtotal=order['subtotal']
            body+=f'{order_code}\t\t{order_name}\t\t{order_qty}\t\t\t{order_subtotal}\t\t\n'
            
        receipt.write(body)
        
        total_payment=f'''
        Total: \t\t\t\t\t\t\t\t\t{total}
        ==
        '''
        
        
        receipt.write(total_payment)
    
main()