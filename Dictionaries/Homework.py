
usercodes={
    'sharptip':'168425',
    'frostwinter':'613541',
    'pthondev':'65445681',
    'oxfiend':'272635',
    'fiberdut':'256374147',
    'mothree':'523335785',
    'lmabdat':'2252542',
    'tghdsv':'8745218',
    'toodyse':'5588302',
    'lemans':'458442478'
}



Username=input('Enter your username: ')
Password=input('Enter your password: ')


if Username not in usercodes:
    print('the username  invalid')
    

else:
    if usercodes[Username] == Password:
        print('You are logged in')
    else:   
        print('This password is invalid. Please try again.')




    

