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

class Hand: 
    
    red_discount_total = 0
    blue_discount_total = 0
    green_discount_total = 0
    orange_discount_total = 0
    yellow_discount_total = 0

    cardsInHand = []


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


def print_cardstack():
    for i in range(len(Card.cardStack)):
        print(Card.cardStack[i]) 


print_cardstack()



