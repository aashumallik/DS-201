
# coding: utf-8

# In[20]:

import random
#@Aashutosh Mallik
NUM_DOORS = 3

def get_random_number_winning_door():
    door = random.randint(0,NUM_DOORS -1)
    return door


# In[21]:


def get_scenario(winning_door): 
    doors = ["no_price"]*NUM_DOORS
    doors[winning_door] = "price"
    return doors


# In[22]:

def simulate(switch):

    winning_door = get_random_number_winning_door()
    scenario = get_scenario( winning_door)
    choice_human = random.randint(0, NUM_DOORS-1)

    while(True):
        open_door_by_host = random.randint(0, NUM_DOORS-1)
        if open_door_by_host == choice_human or scenario[open_door_by_host] == "price":
            continue
        else:
            break

    if switch:
        list_choices = set([0,1,2])
        list_choices.remove(choice_human)
        list_choices.remove(open_door_by_host)

        choice_human = list(list_choices)[0]


    # Did the contestant win?
    won = (scenario[choice_human] == "price")
    return won


# In[23]:

def chance_to_win_if_stay():
    won_staying = 0
    for i in range(10000):
        won = simulate(False)
        if won:
            won_staying += 1

    return won_staying / 10000.0


# In[24]:

def chance_to_win_if_not_stay():
    won_switching = 0
    for i in range(10000):
        won = simulate(True)
        if won:
            won_switching += 1

    return won_switching / 10000.0


# In[25]:

def chance_to_win():
    prob_won_switch = chance_to_win_if_not_stay()
    prob_won_not_switch = chance_to_win_if_stay()
    print('Prob. Switching won ' + str(prob_won_switch) )
    print('Prob. Not Switching won ' + str(prob_won_not_switch))


if __name__ == '__main__':
    chance_to_win()

