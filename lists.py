def arithmetic_arranger(problems,great=False):
    outstring=[]
    first_insert=[]
    second_insert=[]
    third_insert=[]
    fourth_insert=[]
    y=0
    for x in problems:
        f=x.split()
        problems[y]=f
        y+=1
        #print(problems)

    count_problems=len(problems)
    location_in_loop=0
    while count_problems >0:

        a=problems[location_in_loop][0]
        b=problems[location_in_loop][2]
        if problems[location_in_loop][1] =="+":
            c=int(a)+int(b)
        elif  problems[location_in_loop][1] =="-":
            c=int(a)-int(b)
        c=str(c)
        strings_length=len(a)
        if strings_length<len(b):
            strings_length=len(b)
        strings_length=strings_length+2
        #print('this is the length',strings_length)
        l=""
        while len(a)<strings_length:
            a=" "+a
        while len(b)<strings_length-1:
            b=" "+b
        while len(c)<strings_length:
            c=" "+c
        while len(l)<strings_length:
            l="-"+l

        #add the plus and minus signs:
        if problems[location_in_loop][1] =="+":
            b="+"+b
        elif  problems[location_in_loop][1] =="-":
            b="-"+b

        lists=[
        a,
        b,
        l,
        c,

        ]

        for x in lists:
            #print(x)
            outstring.append(x)
            #if location_in_loop/3==0:

        count_problems-=1
        location_in_loop+=1
    #print(outstring)



#from lists insert the data into the lists below:
    first_insert=outstring[::4]
    second_insert=outstring[1::4]
    third_insert=outstring[2::4]
    fourth_insert=outstring[3::4]
    #print('first_insert',first_insert)
    #print('second_insert',second_insert)
    #print('third_insert', third_insert)
    #print('fourth_insert',fourth_insert)
    first_insert_long=[]
    first_insert_counter=len(first_insert)
    for x in first_insert:
        if first_insert_counter>1:
            first_insert_long.append(x+"    ")
        else:
            first_insert_long.append(x+"\n")
        first_insert_counter-=1


        second_insert_long=[]
        second_insert_counter=len(second_insert)
        for x in second_insert:
            if second_insert_counter>1:
                second_insert_long.append(x+"    ")
            else:
                second_insert_long.append(x+"\n")
            second_insert_counter-=1

        third_insert_long=[]
        third_insert_counter=len(third_insert)
        for x in third_insert:
            if third_insert_counter>1:
                third_insert_long.append(x+"    ")
            else:
                third_insert_long.append(x+"\n")
            third_insert_counter-=1

        fourth_insert_long=[]
        fourth_insert_counter=len(fourth_insert)
        for x in fourth_insert:
            if fourth_insert_counter>1:
                fourth_insert_long.append(x+"    ")
            else:
                fourth_insert_long.append(x+"\n")
            fourth_insert_counter-=1



    first_insert_long="".join(first_insert_long)
    second_insert_long="".join(second_insert_long)
    third_insert_long="".join(third_insert_long)
    fourth_insert_long="".join(fourth_insert_long)

    if great==True:
        print(first_insert_long+second_insert_long+third_insert_long+fourth_insert_long)
    else:
        print(first_insert_long+second_insert_long+third_insert_long)

    #if great==True:








#use slicing to add the empty spaces to the values minus the last line '    '

#use slicing to add \n to the last strings_length

# join all the variable together into one big beautiful string






arithmetic_arranger(["99 + 99999", "3801 - 2", "45 + 43", "123 + 49"],True)
