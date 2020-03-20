import sys

def main(argv):
    if len(argv)!=3:
        print("Please enter two strings")
        return
    string1=argv[1]
    string2=argv[2]
    # unequal length or either string is empty, print False
    if len(string1)!=len(string2) or len(string1)==0 or len(string2)==0:
        print("false")
        return
    d1={} # dictionary, which character from string1 map to which character in string2
    for i in range(len(string1)):
        if string1[i] not in d1:
            # map string1[i]:string2[i]
            d1[string1[i]]=string2[i]
        else:
            # return False if the same character in string1 needs to be mapped to another character
            # two characters in string1 can map to same character in string 2 but not the other way round
            if string2[i]!=d1[string1[i]]:
                print("false")
                return
    # so far all characters in string1 can be mapped to string 2, so True
    print("true")
    return

if __name__ == "__main__":
    main(sys.argv)