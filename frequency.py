# This function will grab the total digit counts, whole number, and whole number counts
def find_digit(txt):
    number_cnt = 0
    digit_cnt = 0
    catch_number = []   # Will append digits until whole
    whole_number = []   # Stores Whole Number
    next_number = False # Determines if next value is a digit
    for cnt,i in enumerate(txt):
        if i.isdigit():
            digit_cnt = digit_cnt + 1
            catch_number.append(i)
            # Checking if next value in list is a digit
            if cnt+1 < len(txt) and txt[cnt+1].isdigit():
                next_number = True
            else:
                next_number = False
             # If next value in list is not a digit the whole number will append   
            if next_number is False:
                whole_number.append(''.join(catch_number))
                number_cnt = number_cnt + 1
                catch_number = []
                
    print(f"Digits: {digit_cnt}")
    print(f"Numbers: {number_cnt}")
    print(f"Numbers: {whole_number}")
    
digit_cnt,number_cnt,numbers = find_digit("Hello.  How are you? I am 4 years old.  My favorite color is blue. Next year I will be 5.  My IP address is 128.4.0.46")


added = 0
for i in numbers:
    added = added + int(i)
flo = added/number_cnt

print("NUMBER ANALYSIS\n")
print(f"Number of integers in the file:    {number_cnt}")
print(f"Their sum:                         {added}")
print(f"Their average:                     {round(flo,2)}")
