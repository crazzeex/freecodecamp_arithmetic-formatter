#check if the criterias are met
def checks(problems):
    for i in problems:
        top_num = i.split()[0]
        bot_num = i.split()[2]
        math_sign = i.split()[1]

        if len(problems) > 5:
            return("Error: Too many problems.")

        if math_sign != '+' and math_sign != '-':
            return ("Error: Operator must be '+' or '-'.") 
        
        if len(top_num) > 4 or len(bot_num) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        
        try: 
          if type(int(top_num)) is not int or type(int(bot_num)) is not int:
            return ("Error: Numbers must only contain digits.")
        except:
          return ("Error: Numbers must only contain digits.")

        if len(top_num) > 4 or len(bot_num) > 4:
            return ("Error: Numbers cannot be more than four digits")
    
    return 1

#arranges and formats the problems
def arithmetic_arranger(problems, state = False):
    ln1 = ""
    ln2 = ""
    ln3 = ""
    ln4 = ""
    checker = checks(problems)
    if checker != 1:
      return checker
  
    else:
        for i in problems:
            top_num = i.split()[0]
            bot_num = i.split()[2]
            math_sign = i.split()[1]
            spaces = "    "

            #if top number is longer than bottom number, spaces needed will depend on top number
            if int(len(top_num)) > int(len(bot_num)) or int(len(top_num)) == int(len(bot_num)):
                max_len = int(len(top_num)) + 2
                ln1 += " "*2 + top_num + spaces
                ln2 += math_sign + " "*(max_len - len(bot_num) - 1) + bot_num  + spaces
                ln3 += "-"*max_len + spaces
                if state == True:
                    if math_sign == '+':
                        result = int(top_num) + int(bot_num)
                        ln4 += " "*(max_len - len(str(result))) + str(result) + spaces
                
                    elif math_sign == '-':
                        result = int(top_num) - int(bot_num)
                        ln4 += " "*(max_len - len(str(result))) + str(result) + spaces
                    
            #if bottom number is longer than top number, spaces needed will depend on bottom number
            elif int(len(top_num)) < int(len(bot_num)):
                max_len = int(len(bot_num)) + 2
                ln1 +=  " "*(max_len - len(top_num)) + top_num + spaces
                ln2 += math_sign + " "*(max_len - len(bot_num) - 1) + bot_num + spaces
                ln3 += "-"*max_len + spaces
                
                if state == True: 
                    if math_sign == '+':
                        result = int(top_num) + int(bot_num)
                        ln4 += " "*(max_len - len(str(result))) + str(result) + spaces
                    
                    elif math_sign == '-':
                        result = int(top_num) - int(bot_num)
                        ln4 += " "*(max_len - len(str(result))) + str(result) + spaces
                        
    if state == True: 
        arranged_problems = (ln1.rstrip() + "\n" + ln2.rstrip() + "\n" + ln3.rstrip() + "\n" + ln4.rstrip())
    else: 
        arranged_problems = (ln1.rstrip() + "\n" + ln2.rstrip() + "\n" + ln3.rstrip())
    
    return (arranged_problems)

#test cases
print (arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "9999 + 9999", "523 - 49" ]))
print (arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print (arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print (arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
