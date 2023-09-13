print("Welcome to the quiz!\n\t\tRules of the game\t\t\n1.There will be 10 questions asked. 7 MCQs and 3 fill in the blanks.\n\ta) For MCQs please type in one of the options given.\n\tb) For the fill in the blanks, please type in the appropriate answer.\n2.Each question will be 1 point. Failing to give the right answer will result in no points.\n3.The final score will be displayed once the quiz is over.\n4.You can leave the quiz at any point.\n5.Have fun!!  ")
f = "yes"
score = 0


while f == "yes":
    q1 = input("Question 1: What is the pH value of the human body? Is it: \na. 9.2 to 9.8\nb. 7.0 to 7.8\nc. 6.1 to 6.3\nd. 5.4 to 5.6.\nPLease type your option here: ")
    if q1.lower() == 'b':
        score+=1
        print("Correct answer!! The pH range of the human body under favorable conditions is 7.0-7.8.")
    else:
        print("Wrong answer!! The pH range of the human body under favorable conditions is 7.0-7.8.")

    f = input("Do you want to continue with the quiz: yes/no: ")
    if f.lower() == "no":
        print("Your final answer is: ", score)
        print("Thank you for attending the quiz!! ")
        break
    elif f.lower() == "yes":
        q2 = input("Question 2: Pustaz grasslands are situated at? Is it: \na. South Africa\nb. China\nc. Hungary\nd. USA\nPlease type your option here: ")
        if q2.lower() == 'c':
            score += 1
            print("Correct answer!! Pustaz grasslands are situated in Hungary.")
        else:
            print("Wrong answer!! Pustaz grasslands are situated in Hungary.")
        f = input("Do you want to continue with the quiz: yes/no: ")
        if f.lower() == "no":
            print("Your final answer is: ", score)
            print("Thank you for attending the quiz!! ")
            break
        elif f.lower() == "yes":
            q3 = input("Question 3: Fill in the blank with the right type of article:\nMy friend was born in _____ USA.\nPLease type the correct article to be used here: ")
            if q3.lower() == "the" or q3.lower() == " the" or q3.lower() == "the " or q3.lower() == " the ":
                score += 1
                print("Correct answer!! The correct article is: the. ")
            else:
                print("Wrong answer!! The correct article is: the. ")
            f = input("Do you want to continue with the quiz: yes/no: ")
            if f.lower() == "no":
                print("Your final answer is: ", score)
                print("Thank you for attending the quiz!! ")
                break
            elif f.lower() == "yes":
                q4 = input("Question 4: Which of the given compounds is used to make fireproof clothing? t"
                           "Is it: \na. Aluminium chloride\nb. Aluminium Sulphate\nc. Magnesium Chloride\nd. Magnesium Sulphate\nPlease type the option here: ")
                if q4.lower() == 'b':
                    score += 1
                    print("Correct answer!! Aluminum Sulphate is used to make fireproof clothing.")
                else:
                    print("Wrong answer!! Aluminum Sulphate is used to make fireproof clothing.")

                f = input("Do you want to continue with the quiz: yes/no: ")
                if f.lower() == "no":
                    print("Your final answer is: ", score)
                    print("Thank you for attending the quiz!! ")
                    break
                elif f.lower() == "yes":
                    q5 = input("Question 5: Which of the given cities is located on the bank of river Ganga? Is it: \na. Patna\nb. Gwalior\nc. Bhopal\nd. Mathura\nPlease type the option here: ")
                    if q5.lower() == 'a':
                        score += 1
                        print("Correct answer!! Patna has located on the bank of river Ganga.")
                    else:
                        print("Wrong answer!! Patna has located on the bank of river Ganga.")

                    f = input("Do you want to continue with the quiz: yes/no: ")
                    if f.lower() == "no":
                        print("Your final answer is: ", score)
                        print("Thank you for attending the quiz!! ")
                        break
                    elif f.lower() == "yes":
                        q6 = input("Question 6: Fill in the blank with the right type of article:\n______ is responsible for nitrogen fixation.\nPLease type the correct answer here: ")
                        if q6.lower() == "bacteria" or q6.lower() == " bacteria" or q6.lower() == "bacteria " or q6.lower() == " bacteria ":
                            score += 1
                            print("Correct answer!! The correct answer is: bacteria. ")
                        else:
                            print("Wrong answer!! The correct answer is: bacteria. ")
                        f = input("Do you want to continue with the quiz: yes/no: ")
                        if f.lower() == "no":
                            print("Your final answer is: ", score)
                            print("Thank you for attending the quiz!! ")
                            break
                        elif f.lower() == "yes":
                            q7 = input("Question 7: Who among the following decides if an individual Bill is a Money Bill or not? Is it: \na. Prime Minister\nb. President\nc. Member of Lok Sabha\nd. Speaker of Lok Sabha\nPlease type the option here: ")
                            if q7.lower() == 'd':
                                score += 1
                                print("Correct answer!! The speaker of Lok Sabha decides the bill as a money bill or not.")
                            else:
                                print("Wrong answer!! The speaker of Lok Sabha decides the bill as a money bill or not.")

                            f = input("Do you want to continue with the quiz: yes/no: ")
                            if f.lower() == "no":
                                print("Your final answer is: ", score)
                                print("Thank you for attending the quiz!! ")
                                break
                            elif f.lower() == "yes":
                                q8 = input("Question 6: Fill in the blank:\nNepenthes Khasiana an endangered and rare plant found in _______(Hint: It is found in a state in India. Please type the state it is found in.)\nPLease type the correct answer here: ")
                                if q8.lower() == "meghalaya" or q8.lower() == " meghalaya" or q8.lower() == "meghalaya " or q8.lower() == " meghalaya ":
                                    score += 1
                                    print("Correct answer!! The correct answer is: Meghalaya. ")
                                else:
                                    print("Wrong answer!! The correct answer is: Meghalaya. ")
                                f = input("Do you want to continue with the quiz: yes/no: ")
                                if f.lower() == "no":
                                    print("Your final answer is: ", score)
                                    print("Thank you for attending the quiz!! ")
                                    break
                                elif f.lower() == "yes":
                                    q9 = input("Question 9: The tropic of cancer does pass through which state of India? Is it: \na. Uttar Pradesh\nb. Madhya Pradesh\nc. Bihar\nd. Andhra Pradesh\nPlease type the option here: ")
                                    if q9.lower() == 'b':
                                        score += 1
                                        print("Correct answer!! The Tropic of Cancer passes through Madhya Prdesh.")
                                    else:
                                        print("Wrong answer!! The Tropic of Cancer passes through Madhya Prdesh.")

                                    f = input("Do you want to continue with the quiz: yes/no: ")
                                    if f.lower() == "no":
                                        print("Your final answer is: ", score)
                                        print("Thank you for attending the quiz!! ")
                                        break
                                    elif f.lower() == "yes":
                                        q10 = input("Question 10: Which of the given industries uses limestone as a raw material? Is it: \na. Paper\nb. Cement\nc. Textile\nd. Leather\nPlease type the option here: ")
                                        if q10.lower() == 'b':
                                            score += 1
                                            print("Correct answer!! The cement industry uses limestone as a raw material.")
                                        else:
                                            print("Wrong answer!! The cement industry uses limestone as a raw material.")

                                        f = "no"
print("Your final score is: ", score,"!!!")

















