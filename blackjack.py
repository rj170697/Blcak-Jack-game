#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10,'Ace':1 }


# In[3]:


class card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f' {self.rank} of {self.suit} '        


# In[4]:


class player:
    def __init__ (self,bank_account,name):
        self.player_card=[]
        self.bank_account=bank_account
        self.name=name
    def add_card_p(self,new_card):
        self.player_card.append(new_card)
    def account_add(self,bet_money):
        self.bank_account=self.bank_account + bet_money
    def account_subs(self,bet_money):
        self.bank_account=self.bank_account-bet_money
    def __str__(self):
        return f'your balance is {self.bank_account}'
    
    


# In[5]:


class deck:
    def __init__(self):
        self.new_deck=[]
        for i in suits:
            for j in ranks:
                card_made=card(i,j)
                self.new_deck.append(card_made)
    def shuffle(self):
        random.shuffle(self.new_deck)
    def deal_one(self):
        return self.new_deck.pop(0)
        
            


# In[6]:


class dealer:
    def __init__(self):
        self.dealer_card=[]
        
    def add_card_d(self,new_card):
        self.dealer_card.append(new_card)
        
        


# In[ ]:





# In[7]:


def replay(k):
    k.upper()
    return k=='Y'
    


# In[8]:


print('welcome to blck jack')
player_name=input('enter your name')
player_money=int(input('enter amount'))
player_1=player(player_money,player_name)
game_deck=deck()
dealer_1=dealer()
game_on = True
while game_on:
    game_deck.shuffle()
    player_bet=int(input('bet money on this round '))
    player_value=0
    dealer_value=0
    count_p=0
    if player_bet<=player_1.bank_account:
        print('rouds start')
        round_on=True
        
        for i in range(2):
            player_1.add_card_p(game_deck.deal_one())
            dealer_1.add_card_d(game_deck.deal_one())
        print(f'the dealer card {dealer_1.dealer_card[0]}')
        
    else:
        
        print('you cant bet this amount')
        round_on=False
        break
    for i in  range(count_p+2):
        player_value=player_value+player_1.player_card[i].value

        
    while round_on:
        print('your cards')
        for i in  range(count_p+2):
            print(player_1.player_card[i])
            

        choice_p=input('want to hit ?')
        
        if choice_p.upper()=='Y':
            
            player_1.add_card_p(game_deck.deal_one())
            player_value=player_value+player_1.player_card[count_p+2].value
            count_p += 1
            if player_value>21:
                print('dealer wins')
                player_1.account_subs(player_bet)
                print(f'you loose {player_bet}, your account {player_1.bank_account}')
                round_on=False
                game_on=False
                dealer_turn=False
        
        
        
        
        
        
            
        else:
            round_on=False
            dealer_turn=True
        
        
        
        
    print('your cards')    
    for i in range(count_p+2):
            print( player_1.player_card[i])     
   
    
    if dealer_turn:
        
        for i in range(count_p):
            
            dealer_1.add_card_d(game_deck.deal_one())
        
        
        for j in range(count_p+2):
            dealer_value=dealer_value+dealer_1.dealer_card[j].value 
        if dealer_value>21 or player_value>dealer_value:
            print('you win')
            player_1.account_add(player_bet)
            print(f'you win {player_bet},your account {player_1.bank_account}')
            break
            dealer_turn=False
        elif dealer_value>player_value:
            print('you loose,dealer win')
            player_1.account_subs(player_bet)
            print(f'you loose {player_bet}, your account {player_1.bank_account}')
        elif player_value==dealer_value:
            print('draw')
            break
    
        print('your cards')
        for i in range(count_p+2):
            print( player_1.player_card[i])
        print('dealer cards')    
        for j in range(count_p+2):
            print(dealer_1.dealer_card[j]) 
        ask_player=input('play one more?')
        k=ask_player.upper()
        if  not replay(k[0]):
            break
            game_on=False
        
        


# In[9]:


replay('Y')


# In[10]:


k='y'


# In[11]:


y=k.upper()


# In[12]:


y.upper()


# In[ ]:




