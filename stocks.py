# Create a simple dictionary with ticker symbols and company names.
stockDict = { 
'GM': 'General Motors',
'CAT':'Caterpillar',
'EK':"Eastman Kodak",
'GE': 'General Electric'
}

# Create a simple list of blocks of stock.
# 'GE', 'CAT' are tuples
purchases = [ 
( 'GE', 100, '10-sep-2001', 48 ), # this is a block of stock
( 'CAT', 100, '1-apr-1999', 24 ),
( 'GE', 200, '1-jul-1998', 56 ) 
]
# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name.
portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]
    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1] 
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

    try:
        portfolio[ticker].append(purchase) # append the purchase to the ticker list
    except KeyError:
        portfolio[ticker] = list() # if the key does not exist yet, create it
        portfolio[ticker].append(purchase)    

    print('I purchased {} stock for ${}'.format(full_company_name, full_purchase_price))

# Create a second purchase summary that which accumulates total investment by ticker symbol. 
# In the above sample data, there are two blocks of GE.
# These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased.
# The program makes one pass through the data to create the dict.
# A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.   
for ticker, purchases in portfolio.items():
    print(ticker)
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print(purchase)
    print('Total value of stock in portfolio: ${}\n\n'.format(total_portfolio_stock_value))    
