trades = {'pizza slice': [1,0.5,1.45,0.75], "wasabi root":[1.95,1,3.1,1.49],"snowball":[0.67,0.31,1,0.48],"shells":[1.34,0.64,1.98,1]}

names = ["pizza slice","wasabi root","snowball","shells"]

manual_trades = []
best_amount = 0
best_trades = []

def liquidate(number, item):
    return number * trades[item][3]

def find_best_manual_trade(trades,start,amount):
    #trades: dict of trade numbers, start: first currency, amount is number of currency
    num_org = amount * trades[start]
    best_amount = 0
    for i in range(4):
        
        manual_trades = []
        manual_trades.append(start + " to " + names[i])
        items_1 = amount * trades[start][i]

        for j in range(4):
            manual_trades = [start + " to " + names[i]]
            manual_trades.append(names[i] + " to " + names[j])
            items_2 = items_1 * trades[names[i]][j]

            #if(liquidate(items,names[j])>best_amount):
            #    best_amount = liquidate(items,names[j])
            #    best_trades = manual_trades

            for k in range(4):
                manual_trades = [start + " to " + names[i], names[i] + " to " + names[j]]
                manual_trades.append(names[j] + " to " + names[k])
                items_3 = items_2 * trades[names[j]][k]

                for l in range(4):
                    manual_trades = [start + " to " + names[i], names[i] + " to " + names[j], names[j] + " to " + names[k]]
                    manual_trades.append(names[k] + " to " + names[l])
                    items_4 = items_3 * trades[names[k]][l]


                    if(liquidate(items_4,names[l])>best_amount):
                        best_amount = liquidate(items_4,names[l])
                        best_trades = manual_trades + [names[l] + " to " + "shells"]
                    
              
    return best_trades, best_amount

print(find_best_manual_trade(trades,"shells",2000000))

        