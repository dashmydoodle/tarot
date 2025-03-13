import random



deck = { 
    'The Fool': 'The Fool is a card of fresh starts and limitless potential. If you\'re looking for simple Yes or No guidance and receive The Fool, the answer is YES. Move forward with absolute trust.',
    'The Magician' : 'The Magician is a card of inspiration and manifestation. If you\'re looking for simple Yes or No guidance and receive The Magician, the answer is YES. Act with total confidence.',
    'The High Priestes' : 'The High Priestess is a card of introspection. If you\'re looking for simple Yes or No guidance and receive The High Priestess, the answer is NO. Pause and wait for your intuition to make itself known.',
    'The Empress' : 'The Empress is a card of comfort and creativity. If you\'re looking for simple Yes or No guidance and receive The Empress, the answer is YES. Cultivate an attitude of abundance and prioritize what makes you happy.',
    'The Emperor' : 'The Emperor is a card of protection and boundaries. If you\'re looking for simple Yes or No guidance and receive The Emperor, the answer is YES. Take the lead and act decisively.',
    'The Hierophant' : 'The Hierophant is a card of leadership and tradition. If you\'re looking for simple Yes or No guidance and receive The Hierophant, the answer is YES. Act in the best interests of your community and reputation.',
    'The Lovers' : 'The Lovers is a card of choice and personal growth. If you\'re looking for simple Yes or No guidance and receive The Lovers, the answer is YES. Take full responsibility in whatever you do next.',
    'The Chariot' : 'The Chariot is a card of momentum. If you\'re looking for simple Yes or No guidance and receive The Chariot, the answer is YES. Move swiftly and choose excitement over worry.',
    'Strength' : 'Strength is a card of vulnerability and courage. If you\'re looking for simple Yes or No guidance and receive Strength, the answer is YES. Speak from the heart and trust others to meet you with support.',
    'The Hermit' : 'The Hermit is a card of solitude and wisdom. If you\'re looking for simple Yes or No guidance and receive The Hermit, the answer is NO. Separate yourself from others\' opinions for the time being.',
    'Wheel of Fortune' : 'The Wheel of Fortune is a card of patterns and cycles. If you\'re looking for simple Yes or No guidance and receive The Wheel of Fortune, the answer is NO. Wait for now -- elements are still in motion.',
    'Justice' : 'Justice is a card of clarity and honor. If you\'re looking for simple Yes or No guidance and receive Justice, the answer is NO. Wait until all the facts are known before taking action.',
    'The Hanged Man' : 'The Hanged Man is a card of seeing matters in a whole new way. If you\'re looking for simple Yes or No guidance and receive The Hanged Man, the answer is NO. Sit still and observe.',
    'Death' : 'Death is a card of total transformation. If you\'re looking for simple Yes or No guidance and receive Death, the answer is YES. Open yourself to new experiences and allow them to change you.',
    'Temperance' : 'Temperance is a card of unseen support. If you\'re looking for simple Yes or No guidance and receive Temperance, the answer is NO. Take a break and allow yourself a moment to breathe.',
    'The Devil' : 'The Devil is a card of feeling trapped. If you\'re looking for simple Yes or No guidance and receive The Devil, the answer is NO. Think through the unintended consequences of whatever you\'re considering.',
    'The Tower' : 'The Tower is a card of destruction that clears the way for new beginnings. If you\'re looking for simple Yes or No guidance and receive The Tower, the answer is NO. Let the dust settle before deciding what comes next.',
    'The Star' : 'The Star is a card of hope. If you\'re looking for simple Yes or No guidance and receive The Star, the answer is YES. Believe in the best case scenario.',
    'The Moon' : 'The Moon is a card of mystery. If you\'re looking for simple Yes or No guidance and receive The Moon, the answer is NO. Look for what\'s not so obvious before making your next move.',
    'The Sun' : 'The Sun is a card of understanding and enthusiasm. If you\'re looking for simple Yes or No guidance and receive The Sun, the answer is YES. Go into your next steps with eyes wide open.',
    'Judgement' : 'Judgement is a card of adventure and awakening. If you\'re looking for simple Yes or No guidance and receive Judgement, the answer is YES. Follow your sense of purpose and calling, regardless of the situation.',
    'The World' : 'The World is a card of unity and wholeness. If you\'re looking for simple Yes or No guidance and receive The World, the answer is YES. View your present experience as a full circle moment, a fitting conclusion to a certain chapter.'
}

random.shuffle(deck)