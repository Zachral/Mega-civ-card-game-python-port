from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template')

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
        return f"Name: {self.card_name}\nColor: {self.color}\nCost: {self.current_cost}\nRed discount: {self.red_discount}\nBlue discount: {self.blue_discount}\nGreen discount: {self.green_discount}\nOrange discount: {self.orange_discount}\nYellow discount: {self.yellow_discount}\nDiscounted card: {self.discounted_card}\nVictory points: {self.victory_points}\n"


class Hand(Card):
    red_discount_total = 0
    blue_discount_total = 0
    green_discount_total = 0
    orange_discount_total = 0
    yellow_discount_total = 0
    points_total = 0

    cardsInHand = []

    def show_discounts(self):
        return f"Discounts:\nRed: {self.red_discount_total}  Blue: {self.blue_discount_total}   Green: {self.green_discount_total}  Orange: {self.orange_discount_total}    Yellow: {self.yellow_discount_total}    VP: {self.points_total}"
    
    def reset(self):
            self.red_discount_total = 0
            self.blue_discount_total = 0
            self.green_discount_total = 0
            self.orange_discount_total = 0
            self.yellow_discount_total = 0
            self.points_total = 0
            self.cardsInHand.clear()

def add_cards_to_cardstack():
    Card.cardStack.append(Card("Cloth Making", "Orange", 50, 50, 0, 5, 0, 10, 0, "Naval Warfare", 10, 1))
    Card.cardStack.append(Card("Sculpture", "Blue", 50, 50, 5, 10, 0, 0, 0, "Architecture", 10, 1))
    Card.cardStack.append(Card("Mysticism", "Blue and Yellow", 50, 50, 0, 5, 0, 0, 5, "Monument", 10, 1))  
    Card.cardStack.append(Card("Urbanism", "Red", 50, 50, 10, 0, 5, 0, 0, "Diplomacy", 10, 1))  
    Card.cardStack.append(Card("Monarchy", "Red", 60, 60, 10, 0, 0, 0, 5, "Law", 10, 1))
    Card.cardStack.append(Card("Written Record", "Red and Green", 60, 60, 5, 0, 5, 0, 0, "Cartography", 10, 1))  
    Card.cardStack.append(Card("Pottery", "Orange", 60, 60, 0, 5, 0, 10, 0, "Agriculture", 10, 1))
    Card.cardStack.append(Card("Masonry", "Orange", 60, 60, 0, 0, 5, 10, 0, "Engineering", 10, 1))
    Card.cardStack.append(Card("Mythology", "Yellow", 60, 60, 0, 5, 0, 0, 10, "Literacy", 10, 1))
    Card.cardStack.append(Card("Empiricism", "Green", 60, 60, 5, 5, 10, 5, 5, "Medicin", 10, 1))
    Card.cardStack.append(Card("Deism", "Yellow", 70, 70, 0, 0, 0, 10, 5, "Fundamentalism", 10, 1))
    Card.cardStack.append(Card("Theocracy", "Red and Yellow", 80, 80, 5, 0, 0, 0, 5, "Universal Doctrine", 10, 1))
    Card.cardStack.append(Card("Drama and Poetry", "Blue", 80, 80, 0, 10, 0, 0, 5, "Rhetoric", 10, 1))
    Card.cardStack.append(Card("Music", "Blue", 80, 80, 10, 0, 0, 0, 5, "Enlightenment", 10, 1))
    Card.cardStack.append(Card("Astronavigation", "Green", 80, 80, 0, 0, 10, 0, 5, "Calender", 10, 1))
    Card.cardStack.append(Card("Coinage", "Green", 90, 90, 5, 0, 10, 0, 0, "Trade Routes", 10, 1))
    Card.cardStack.append(Card("Metalworking", "Orange", 90, 90, 5, 0, 0, 10, 0, "Military", 10, 1))
    Card.cardStack.append(Card("Architecture", "Blue", 140, 140, 0, 10, 5, 0, 0, "Mining", 20, 3))  
    Card.cardStack.append(Card("Naval Warfare", "Red", 160, 160, 10, 0, 0, 5, 0,"Diaspora", 20, 3))  
    Card.cardStack.append(Card("Monument", "Yellow and Orange", 180, 180, 0, 0, 0, 10, 10, "Wonder of the World", 20, 3))
    Card.cardStack.append(Card("Diplomacy", "Blue", 160, 160, 5, 10, 0, 0, 0, "Provincial Empire", 20, 3))
    Card.cardStack.append(Card("Law", "Red", 150, 150, 10, 0, 0, 0, 5, "Cultural Ascendancy", 20, 3))
    Card.cardStack.append(Card("Cartography", "Green", 160, 160, 0, 5, 10, 0, 0, "Library", 20, 3))
    Card.cardStack.append(Card("Agriculture", "Orange", 120, 120, 0, 0, 5, 10, 0, "Democracy", 20, 3))      
    Card.cardStack.append(Card("Engineering", "Orange and Green", 160, 160, 0, 0, 10, 10, 0, "Roadbuildning", 20, 3)) 
    Card.cardStack.append(Card("Literacy", "Blue and Red", 110, 110, 10, 10, 5, 5, 5, "Mathematics", 20, 3))
    Card.cardStack.append(Card("Medicine", "Green", 140, 140, 0, 0, 10, 5, 0, "Anatomy", 20, 3))
    Card.cardStack.append(Card("Fundamentalism", "Yellow", 150, 150, 0, 5, 0, 0, 10, "Monotheism", 20, 3))
    Card.cardStack.append(Card("Universal Doctrine", "Yellow", 160, 160, 5, 0, 0, 0, 10, "Theology", 20, 3))
    Card.cardStack.append(Card("Rhetoric", "Blue", 130, 130, 5, 10, 0, 0, 0, "Politics", 20, 3))
    Card.cardStack.append(Card("Cartography", "Green", 180, 180, 5, 0, 10, 0, 0, "Public Works", 20, 3))
    Card.cardStack.append(Card("Enlightenment", "Yellow", 160, 160, 0, 0, 0, 5, 10, "Philosophy", 20, 3))
    Card.cardStack.append(Card("Trade Routes", "Orange", 180, 180, 0, 0, 0, 10, 5, "Trade Empire", 20, 3))
    Card.cardStack.append(Card("Military", "Red", 170, 170, 10, 0, 0, 5, 0, "Advanced Military", 20, 3))
    Card.cardStack.append(Card("Mining", "Orange", 230, 230, 0, 0, 5, 20, 0, None, 0, 6))  
    Card.cardStack.append(Card("Provincial Empire", "Red", 260, 260, 20, 0, 0, 0, 5, None, 0, 6))  
    Card.cardStack.append(Card("Diaspora", "Yellow", 270, 270, 0, 5, 0, 0, 20, None, 0, 6))  
    Card.cardStack.append(Card("Wonder of the World", "Blue and Orange", 290, 290, 0, 20, 0, 20, 0, None, 0, 6))
    Card.cardStack.append(Card("Cultural Ascendency", "Blue", 280, 280, 0, 20, 0, 0, 5, None, 0, 6))    
    Card.cardStack.append(Card("Library", "Green", 220, 220, 0, 5, 20, 0, 0, None, 0, 6))
    Card.cardStack.append(Card("Democracy", "Red", 220, 220, 20, 5, 0, 0, 0, None, 0, 6))    
    Card.cardStack.append(Card("Roadbuilding", "Orange", 230, 230, 0, 0, 5, 20, 0, None, 0, 6))  
    Card.cardStack.append(Card("Mathematics", "Blue and Green", 250, 250, 10, 20, 20, 10, 10, None, 0, 6))  
    Card.cardStack.append(Card("Anatomy", "Green", 270, 270, 0, 0, 20, 5, 0, None, 0, 6))
    Card.cardStack.append(Card("Monotheism", "Yellow", 230, 230, 5, 0, 0, 0, 20, None, 0, 6))
    Card.cardStack.append(Card("Theology", "Yellow", 250, 250, 0, 0, 5, 0, 20, None, 0, 6))      
    Card.cardStack.append(Card("Politics", "Blue", 230, 230, 0, 20, 0, 0, 5, None, 0, 6)) 
    Card.cardStack.append(Card("Philosophy", "Yellow and Green", 220, 220, 0, 0, 20, 0, 20, None, 0, 6)) 
    Card.cardStack.append(Card("Public Works", "Red", 230, 230, 20, 0, 0, 5, 0, None, 0, 6))   
    Card.cardStack.append(Card("Trade Empire", "Orange", 260, 260, 5, 0, 0, 20, 0, None, 0, 6)) 
    Card.cardStack.append(Card("Advanced Military", "Red", 240, 240, 20, 0, 5, 0, 0, None, 0, 6)) 
    return

def print_cards_in_hand():
    for i in range(len(Hand.cardsInHand)):
        print(Hand.cardsInHand[i])
    return


def update_total_color_discount(index: int):
    Hand.red_discount_total += Hand.cardsInHand[index].red_discount
    Hand.blue_discount_total += Hand.cardsInHand[index].blue_discount
    Hand.green_discount_total += Hand.cardsInHand[index].green_discount
    Hand.orange_discount_total += Hand.cardsInHand[index].orange_discount
    Hand.yellow_discount_total += Hand.cardsInHand[index].yellow_discount
    return

def add_discount_to_specific_card(index: int):
    for i in range(len(Card.cardStack)):
        if Hand.cardsInHand[index].discounted_card == Card.cardStack[i].card_name:
            Card.cardStack[i].original_cost = Card.cardStack[i].original_cost - Hand.cardsInHand[index].amount_discounted_card
            return


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
        elif Card.cardStack[i].color == "Red and Yellow":
            highest_discount = Hand.red_discount_total if Hand.red_discount_total > Hand.yellow_discount_total else Hand.yellow_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
        elif Card.cardStack[i].color == "Red and Green":
            highest_discount = Hand.red_discount_total if Hand.red_discount_total > Hand.green_discount_total else Hand.green_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
        elif Card.cardStack[i].color == "Yellow and Orange" :
            highest_discount = Hand.yellow_discount_total if Hand.yellow_discount_total > Hand.orange_discount_total else Hand.orange_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
        elif Card.cardStack[i].color == "Blue and Red":
            highest_discount = Hand.blue_discount_total if Hand.blue_discount_total > Hand.red_discount_total else Hand.red_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
        elif Card.cardStack[i].color == "Orange and Green" :
            highest_discount = Hand.green_discount_total if Hand.green_discount_total > Hand.orange_discount_total else Hand.orange_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
        elif Card.cardStack[i].color == "Blue and Green":
            highest_discount = Hand.blue_discount_total if Hand.blue_discount_total > Hand.green_discount_total else Hand.green_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
        elif Card.cardStack[i].color == "Yellow and Green" :
            highest_discount = Hand.yellow_discount_total if Hand.yellow_discount_total > Hand.green_discount_total else Hand.green_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
        elif Card.cardStack[i].color == "Blue and Orange":
            highest_discount = Hand.blue_discount_total if Hand.blue_discount_total > Hand.orange_discount_total else Hand.orange_discount_total 
            Card.cardStack[i].current_cost = Card.cardStack[i].original_cost - highest_discount
    return

add_cards_to_cardstack()

@app.route('/')
def main_menu():
    return Hand.show_discounts(Hand) + render_template('main_menu.html')

@app.route('/cards_in_hand')
def show_cards_in_hand():
    cards = Hand.cardsInHand
    return Hand.show_discounts(Hand) + render_template('cards_in_hand.html', cards=cards)

@app.route('/buy_card', methods=['GET', 'POST'])
def buy_card():
    if request.method == 'POST':
        amountToSpend = int(request.form['money'])
        affordable_cards = []
        for i in range(len(Card.cardStack)):
            if Card.cardStack[i].current_cost <= amountToSpend:
                affordable_cards.append((i, Card.cardStack[i]))
        return Hand.show_discounts(Hand) + render_template('buy_card.html', affordable_cards=affordable_cards, amountToSpend = amountToSpend)
    return Hand.show_discounts(Hand) + render_template('buy_card.html')


@app.route('/buy_card_at_index', methods=['POST'])
def buy_card_at_index():
    selected_cards = request.form.getlist('selected_card')
    
    for selected_card_name in selected_cards:
        for index, card in enumerate(Card.cardStack):
            if card.card_name == selected_card_name: 
                Hand.cardsInHand.append(Card.cardStack[index])
                for i,cardInHand in enumerate(Hand.cardsInHand):
                    if cardInHand.card_name == selected_card_name:
                        add_discount_to_specific_card(i)
                        update_total_color_discount(i)
                        # if Hand.cardsInHand[i].discounted_card is not None:
                update_card_prices(index)
                Card.cardStack.remove(Card.cardStack[index])
                Hand.points_total += Card.cardStack[index].victory_points
                break
    return Hand.show_discounts(Hand) + render_template('buy_card.html')

@app.route('/reset', methods=['POST'])
def reset():
   
    Hand.reset(Hand) 
    Card.cardStack.clear()
    add_cards_to_cardstack()

    return redirect(url_for('main_menu'))

if __name__ == '__main__':
    app.run()
