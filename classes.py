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

    def show_discounts(self):
        return f"Discounts:\nRed: {self.red_discount_total}  Blue: {self.blue_discount_total}    Green: {self.green_discount_total}  Orange: {self.orange_discount_total}    Yellow: {self.yellow_discount_total}    VP: {self.points_total}"

    def reset(self):
            self.red_discount_total = 0
            self.blue_discount_total = 0
            self.green_discount_total = 0
            self.orange_discount_total = 0
            self.yellow_discount_total = 0
            self.points_total = 0
            self.cardsInHand.clear()