#enter a string
print('enter string')
s = str(input())


sum = 0
if ')' in s or '(' in s:
    #iterate through a string which contains parentheses
    for i in s:
        #if we meet ')' before '(' - definitely unpaired
        if sum < -1:
            break
            print('unpaired parentheses')
        #each '(' +1 point to Gryffindor, each  ')' is -1
        elif i == '(':
            sum += 1
        elif i == ')':
            sum += -1
    #sum is 0 only if parentheses were paired     
    if sum == 0:
        print('paired parentheses')
    else:
        print('unpaired parentheses')
else:
    print('no parentheses') #if there were no parentheses