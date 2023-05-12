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

    def __str__(self): 
        return f"Name: {self.card_name}\nColor: {self.color}\nCost: {self.current_cost}\nRed discount: {self.red_discount}\nBlue discount: {self.blue_discount}\nGreen discount: {self.green_discount}\nOrange discount: {self.orange_discount}\nYellow discount: {self.yellow_discount}\nDiscounted card: {self.discounted_card}\nDiscount amount: {self.amount_discounted_card}\nVictory points: {self.victory_points}\n"
    
    cardStack = []

class Hand: 
    def __init__(self, red_discount_total = 0, blue_discount_total = 0, green_discount_total = 0,\
                  orange_discount_total = 0, yellow_discount_total = 0):
        self.red_discount_total = red_discount_total
        self.blue_discount_total = blue_discount_total
        self.green_discount_total = green_discount_total
        self.orange_discount_total = orange_discount_total
        self.yellow_discount_total = yellow_discount_total

    cardsInHand = []



