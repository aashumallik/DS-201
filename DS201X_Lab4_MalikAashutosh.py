
# coding: utf-8

# In[9]:


def Letter_grade(final_points):
    score = float(final_points)
    if score >= 92.5 and score <= 100:
        print("Your points: str(score) Your letter grade: A, good job!")
    elif score >= 82.5 and score <= 92.4:
        print("Your points: " + str(score) + " Your letter grade: B")
    elif score >= 72.5 and score <= 82.4:
        print("Your points: " + str(score) + " Your letter grade: C")
    elif score >= 62.5 and score <= 72.4:
        print("Your points: " + str(score) + " Your letter grade: D")
    else:
        print("Your points: " + str(score)+ " Your letter grade: F, sorry you failed")
          


# In[10]:


def final_score(final_points):
    score = float(final_points)
    if score >= 92.5 and score <= 100:
        print("Your final score is: " + str(score) + " A, good job!")
    elif score >= 82.5 and score <= 92.4:
        print("Your final score is: " + str(score) + " B")
    elif score >= 72.5 and score <= 82.4:
        print("Your final score is: " + str(score) + " C")
    elif score >= 62.5 and score <= 72.4:
        print("Your final score is: " + str(score) + " D")
    else:
        print("Your final score is: " + str(score)+ " F, sorry you failed")
          


# In[11]:

user_cont = "Yes"

total = 0

numgrades = 0
while user_cont in ["Yes", "yes", "Y", "y", "I do"]:
    #Asks the user for their score, converts it to int
    print("Please enter the score: ")
    inp = input()
    score = float(inp)
    #Outputs the grade for the individual assignment
    Letter_grade(score)
    #increment the total score
    total += score
    #Increment the number of grades factored
    numgrades += 1
    #ask the user if they want to continue
    user_cont = input("Do you have more student's Final points?")
    
avg = total/numgrades    
print("Grade report complete! Your final score is ")
final_score(avg)


# In[ ]:



