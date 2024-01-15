prices = [7,6,4,3,1]
buying_price,buying_day=0,0
for i in  range(len(prices)-2):
    j=i+1
    if prices[i]<prices[j]: 
        buying_price=prices[i]
        buying_day=i
        mx=max(prices[i:])
        ind=prices.index(mx)
        if ind<buying_day& ind==len(prices):
            print("No trasaction : ",0)
        else:
            print("buyind day ",buying_day+1)
            print("buying price", buying_price)
            print("selling day ",ind+1)
            print("selling price",mx)
            print("profit ",mx-buying_price)
            break
    else:
         print("No trasaction : ",0)
         break
