import random

tarot_deck = [ 
    {'name ' : 'The Fool', 'meaning': 'The Fool is a card of fresh starts and limitless potential. If you\'re looking for simple Yes or No guidance and receive The Fool, the answer is YES. Move forward with absolute trust.'},
    {'name' : 'The Magician', 'meaning' : 'The Magician is a card of inspiration and manifestation. If you\'re looking for simple Yes or No guidance and receive The Magician, the answer is YES. Act with total confidence.'},
    {'name' : 'The High Priestess', 'meaning' : 'The High Priestess is a card of introspection. If you\'re looking for simple Yes or No guidance and receive The High Priestess, the answer is NO. Pause and wait for your intuition to make itself known.'},
    {'name' : 'The Empress', 'meaning' : 'The Empress is a card of comfort and creativity. If you\'re looking for simple Yes or No guidance and receive The Empress, the answer is YES. Cultivate an attitude of abundance and prioritize what makes you happy.'},
    {'name' : 'The Emperor', 'meaning' : 'The Emperor is a card of protection and boundaries. If you\'re looking for simple Yes or No guidance and receive The Emperor, the answer is YES. Take the lead and act decisively.'},
    {'name' : 'The Hierophant', 'meaning' : 'The Hierophant is a card of leadership and tradition. If you\'re looking for simple Yes or No guidance and receive The Hierophant, the answer is YES. Act in the best interests of your community and reputation.'},
    {'name' : 'The Lovers', 'meaning' : 'The Lovers is a card of choice and personal growth. If you\'re looking for simple Yes or No guidance and receive The Lovers, the answer is YES. Take full responsibility in whatever you do next.'},
    {'name' : 'The Chariot', 'meaning' : 'The Chariot is a card of momentum. If you\'re looking for simple Yes or No guidance and receive The Chariot, the answer is YES. Move swiftly and choose excitement over worry.'},
    {'name' : 'Strength', 'meaning' : 'Strength is a card of vulnerability and courage. If you\'re looking for simple Yes or No guidance and receive Strength, the answer is YES. Speak from the heart and trust others to meet you with support.'},
    {'name' : 'The Hermit', 'meaning' : 'The Hermit is a card of solitude and wisdom. If you\'re looking for simple Yes or No guidance and receive The Hermit, the answer is NO. Separate yourself from others\' opinions for the time being.'},
    {'name' : 'Wheel of Fortune', 'meaning' : 'The Wheel of Fortune is a card of patterns and cycles. If you\'re looking for simple Yes or No guidance and receive The Wheel of Fortune, the answer is NO. Wait for now -- elements are still in motion.'},
    {'name' : 'Justice', 'meaning' : 'Justice is a card of clarity and honor. If you\'re looking for simple Yes or No guidance and receive Justice, the answer is NO. Wait until all the facts are known before taking action.'},
    {'name' : 'The Hanged Man', 'meaning' : 'The Hanged Man is a card of seeing matters in a whole new way. If you\'re looking for simple Yes or No guidance and receive The Hanged Man, the answer is NO. Sit still and observe.'},
    {'name' : 'Death', 'meaning' : 'Death is a card of total transformation. If you\'re looking for simple Yes or No guidance and receive Death, the answer is YES. Open yourself to new experiences and allow them to change you.'},
    {'name' : 'Temperance', 'meaning' : 'Temperance is a card of unseen support. If you\'re looking for simple Yes or No guidance and receive Temperance, the answer is NO. Take a break and allow yourself a moment to breathe.'},
    {'name' : 'The Devil', 'meaning' : 'The Devil is a card of feeling trapped. If you\'re looking for simple Yes or No guidance and receive The Devil, the answer is NO. Think through the unintended consequences of whatever you\'re considering.'},
    {'name' : 'The Tower', 'meaning' : 'The Tower is a card of destruction that clears the way for new beginnings. If you\'re looking for simple Yes or No guidance and receive The Tower, the answer is NO. Let the dust settle before deciding what comes next.'},
    {'name' : 'The Star', 'meaning' : 'The Star is a card of hope. If you\'re looking for simple Yes or No guidance and receive The Star, the answer is YES. Believe in the best case scenario.'},
    {'name' : 'The Moon', 'meaning' : 'The Moon is a card of mystery. If you\'re looking for simple Yes or No guidance and receive The Moon, the answer is NO. Look for what\'s not so obvious before making your next move.'},
    {'name' : 'The Sun', 'meaning' : 'The Sun is a card of understanding and enthusiasm. If you\'re looking for simple Yes or No guidance and receive The Sun, the answer is YES. Go into your next steps with eyes wide open.'},
    {'name' : 'Judgement', 'meaning' : 'Judgement is a card of adventure and awakening. If you\'re looking for simple Yes or No guidance and receive Judgement, the answer is YES. Follow your sense of purpose and calling, regardless of the situation.'},
    {'name' : 'The World', 'meaning' : 'The World is a card of unity and wholeness. If you\'re looking for simple Yes or No guidance and receive The World, the answer is YES. View your present experience as a full circle moment, a fitting conclusion to a certain chapter.'}
    ]

print('Welcome! Please ask your question for a \'Yes\' or \'No\' answer.')

random.shuffle(tarot_deck)


def card_draw(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]

question = input('Please ask your question: ')

if question.endswith('?'):
    drawn_cards = card_draw(tarot_deck, 1)
    print(f'\nThe Tarot answer to your \'{question}\' question: ')
    for card in drawn_cards:
        print(f"{card['name']} : {card['meaning']}")
else:
    print("Please enter a valid question ending with a '?'.")