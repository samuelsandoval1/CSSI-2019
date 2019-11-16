#Example4

def Triangle(s1,s2,s3):
    hyp = 0
    leg1 = 0
    leg2 = 0

    if int(s1) > int(s2) and int(s1) > int(s3):
        hypo = s1
        leg1 = s2
        leg2 = s3

    elif int(s2) > int(s1) and int(s2) > int(s3):
        leg1 = s2
        hypo = s1
        leg2 = s3

    elif int(s3) > int(s2) and int(s3) > int(s1):
        leg1 = s3
        leg2 = s2
        hypo = s1

    side_sum = int(leg1) + int(leg2)
    print leg1, leg2, hypo
    print side_sum
    if side_sum > int(hypo):
        print "Is a triangle"
    elif side_sum == int(hypo):
        print "It is not a trinagle"
    else:
        print "It is not a triangle"

a = raw_input("Enter a length: ")
b = raw_input("Enter a length: ")
c = raw_input("Enter a length: ")

Triangle(a,b,c)
