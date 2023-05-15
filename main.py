class Card:

    def __init__(self, card_name, color, current_cost, original_cost, 
                 red_discount, blue_discount, green_discount, orange_discount, yellow_discount, 
                 discounted_card, amount_discounted_card, victory_points):
        self.card_name = card_name
        self.color = color
        self.current_cost = current_cost
        self.original_cost = original_cost
        self.red_discount = red_discount
        self.blue_discount = blue_discount
        self.green_discount = green_discount
        self.orange_discount = orange_discount
        self.yellow_discount = yellow_discount
        self.discounted_card = discounted_card
        self.amount_discounted_card = amount_discounted_card
        self.victory_points = victory_points

    cardStack = []
    
    def __str__(self): 
        return f"Name: {self.card_name}\nColor: {self.color}\nCost: {self.current_cost}\nRed discount: {self.red_discount}\nBlue discount: {self.blue_discount}\nGreen discount: {self.green_discount}\nOrange discount: {self.orange_discount}\nYellow discount: {self.yellow_discount}\nDiscounted card: {self.discounted_card}\nDiscount amount: {self.amount_discounted_card}\nVictory points: {self.victory_points}\n"

class Hand(Card): 
    
    red_discount_total = 0
    blue_discount_total = 0
    green_discount_total = 0
    orange_discount_total = 0
    yellow_discount_total = 0
    points_total = 0

    cardsInHand = []


def add_cards_to_cardstack():
    Card.cardStack.append(Card("Cloth Making", "Orange", 50, 50, 0, 5, 0, 10, 0, "Naval Warfare", 10, 1))
    Card.cardStack.append(Card("Sculpture", "Blue", 50, 50, 5, 10, 0, 0, 0, "Architecture", 10, 1))
    Card.cardStack.append(Card("Mysticism", "Blue and Yellow", 50, 50, 0, 5, 0, 0, 5, "Monument", 10, 1))  
    Card.cardStack.append(Card("Urbanism", "Red", 50, 50, 10, 0, 5, 0, 0, "Diplomacy", 10, 1))  
    Card.cardStack.append(Card("Architecture", "Blue", 140, 140, 0, 10, 5, 0, 0, "Mining", 20, 3))  
    Card.cardStack.append(Card("Naval Warfare", "Red", 160, 160, 10, 0, 0, 5, 0,"Diaspora", 20, 3))  
    Card.cardStack.append(Card("Monument", "Yellow and Orange", 180, 180, 0, 0, 0, 10, 10, "Wonder of the World", 20, 3))  
    Card.cardStack.append(Card("Mining ", "Orange", 230, 230, 0, 0, 5, 20, 0, None, 0, 6))  
    Card.cardStack.append(Card("Provincial Empire", "Red", 260, 260, 20, 0, 0, 0, 5, None, 0, 6))  
    Card.cardStack.append(Card("Diaspora", "Yellow", 270, 270, 0, 5, 0, 0, 20, None, 0, 6))  
    Card.cardStack.append(Card("Wonder of the World", "Blue and Orange", 290, 290, 0, 20, 0, 20, 0, None, 0, 6))  
    return

def print_cardstack():
    for i in range(len(Card.cardStack)):
        print(f"{i+1}:\n{Card.cardStack[i]}") 
    return

##Updates the color discounts and victorypoints in Hand. Redo as a for-loop? 
def update_total_color_discount(index: int):
    Hand.red_discount_total += Card.cardStack[index].red_discount
    Hand.blue_discount_total += Card.cardStack[index].blue_discount
    Hand.green_discount_total += Card.cardStack[index].green_discount
    Hand.orange_discount_total += Card.cardStack[index].orange_discount
    Hand.yellow_discount_total += Card.cardStack[index].yellow_discount
    return

##Updates the discount to a specific card if applicable
def add_discount_to_specific_card(index: int):
    for i in range(len(Card.cardStack)):
        if Card.cardStack[index].discounted_card == Card.cardStack[i].card_name:
            Card.cardStack[i].current_cost = Card.cardStack[i].current_cost - Card.cardStack[index].amount_discounted_card
            return
        
##Updates the color discunt to all cards in the cardstack. 
def update_card_prices(index: int):
    for i in range(len(Card.cardStack)):
        if Card.cardStack[i].color == "Red":
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - Hand.red_discount_total
        elif Card.cardStack[i].color == "Blue":
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - Hand.blue_discount_total
        elif Card.cardStack[i].color == "Green":
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - Hand.green_discount_total
        elif Card.cardStack[i].color == "Orange":
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - Hand.orange_discount_total
        elif Card.cardStack[i].color == "Yellow":
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - Hand.yellow_discount_total
        elif Card.cardStack[i].color == "Blue and Yellow":
            highest_discount = Hand.blue_discount_total if Hand.blue_discount_total > Hand.yellow_discount_total else Hand.yellow_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
        elif Card.cardStack[i].color == "Yellow and Orange" :
            highest_discount = Hand.yellow_discount_total if Hand.yellow_discount_total > Hand.orange_discount_total else Hand.orange_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
    return

def buy_card_at_index():
    index = int(input("Which card do you want to buy?"))
    update_total_color_discount(index)
    if(Card.cardStack[index].discounted_card != None):
        add_discount_to_specific_card(index)
    update_card_prices(index)
    
    #adds victorypoints and moves the bought card from cardstack to hand
    Hand.points_total += Card.cardStack[index].victory_points
    Hand.cardsInHand.append(Card.cardStack[index])
    Card.cardStack.remove(Card.cardStack[index])

##Prints all cards in Hand. 
def print_cards_in_hand():
    for i in range(len(Hand.cardsInHand)):
        print(Hand.cardsInHand[i])
    return

add_cards_to_cardstack()

while(True):
    print("\nMain menu")
    print("1.Print all cards in cardstack")
    print("2.Print all cards you bought")
    print("3. Buy a card")
    userChoice = int(input("Chose an option: "))
    if userChoice == 1:
        print_cardstack()
    elif userChoice == 2:
        print_cards_in_hand()
    elif userChoice == 3:
        buy_card_at_index()
    else:
        print("Invalid choice, try again")
    


