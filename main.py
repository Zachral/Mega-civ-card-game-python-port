from flask import Flask, request, render_template, Response, request, redirect, url_for
from app import create_app
from classes import Card, Hand

app = create_app()

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

##Prints all cards in cardstack
def print_cardstack():
    for i in range(len(Card.cardStack)):
        print(f"{i+1}:\n{Card.cardStack[i]}") 
    return

##Prints all cards in Hand. 
@app.route("/in_hand/", methods=['POST'])
def print_cards_in_hand():
    for i in range(len(Hand.cardsInHand)):
        print(Hand.cardsInHand[i])
    return

##Loops trough all cards in cardstack and prints all cards the player can afford
def affordable_cards():
    amountToSpend = int(input("Money: "))
    for i in range(len(Card.cardStack)):
        if Card.cardStack[i].current_cost <= amountToSpend:
            print(f"{i+1}:\n{Card.cardStack[i]}") 
    index = int(input("\nWhich card du you want to buy?\n"))
    return index - 1  

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

##Function containing everyrhing that happens when you buy a card. 
@app.route("/buy/", methods=['POST'])
def buy_card_at_index():
    index = affordable_cards()
    update_total_color_discount(index)
    if(Card.cardStack[index].discounted_card != None):
        add_discount_to_specific_card(index)
    update_card_prices(index)
    
    #adds victorypoints and moves the bought card from cardstack to hand
    Hand.points_total += Card.cardStack[index].victory_points
    Hand.cardsInHand.append(Card.cardStack[index])
    Card.cardStack.remove(Card.cardStack[index])

@app.route("/", methods=['GET', 'POST'])
def index():

    add_cards_to_cardstack()

    while(True):
        # if request.method == 'POST':
        #     if request.form.get('show_hand') == 'Show cards in hand':
        #         print_cards_in_hand()
        #     elif  request.form.get('buy_cards') == 'Buy card':
        #         buy_card_at_index()
        # else:        
             return Hand.show_discounts(Hand) + render_template('index.html') #"""<form method="post">
            # <p><input type=submit value="Show cards in hand" name=show_hand>
            # <p><input type=submit value=Buy card name=buy_card>
            # </form>"""
        
    """ userChoice = int(input("Chose an option: "))
        if userChoice == 1:
            print_cardstack()
        elif userChoice == 2:
            print_cards_in_hand()
        elif userChoice == 3:
            buy_card_at_index()
        else:
            print("Invalid choice, try again")
 """
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    


