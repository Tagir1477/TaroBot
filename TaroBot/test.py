import random

# Определение карт Таро
class TarotCard:
    def __init__(self, name, description, keywords, good_meaning, bad_meaning):
        self.name = name
        self.description = description
        self.keywords = keywords
        self.good_meaning = good_meaning
        self.bad_meaning = bad_meaning

# Создание колоды Таро
tarot_deck = {
    "The Fool": TarotCard("The Fool", "Новая жизнь, приключение, свобода и неограниченные возможности.", ["начало", "спонтанность", "свобода"], "Новые возможности", "Безрассудство"),
    "The Magician": TarotCard("The Magician", "Талант, способность, изобретательность и креативность.", ["сила", "действие", "искусство"], "Проявление силы воли", "Обман"),
    "The High Priestess": TarotCard("The High Priestess", "Интуиция, тайные знания, духовное просвещение и мистицизм.", ["мудрость", "тайна", "подсознание"], "Мудрость", "Скрытность"),
    "The Empress": TarotCard("The Empress", "Плодородие, изобилие, природа и материнство.", ["изобилие", "творчество", "рост"], "Изобилие", "Потакание"),
    "The Emperor": TarotCard("The Emperor", "Власть, структура, контроль и стабильность.", ["авторитет", "лидерство", "структура"], "Стабильность", "Тирания"),
    # Добавьте остальные карты здесь
}

# Определение раскладки
class TarotSpread:
    def __init__(self, cards):
        self.cards = cards

    def interpret(self):
        interpretations = []
        for card in self.cards:
            interpretations.append(self.interpret_card(card))
        return interpretations

    def interpret_card(self, card):
        # Пример интерпретации карты
        meaning = random.choice([card.good_meaning, card.bad_meaning])
        return f"{card.name}: {meaning}"

    def synergy(self):
        # Пример анализа синергии между картами
        synergy_analysis = "Синергия между картами:\n"
        for card in self.cards:
            synergy_analysis += f"{card.name}: {', '.join(card.keywords)}\n"
        return synergy_analysis

# Функция для генерации случайной раскладки
def generate_random_spread(deck, num_cards):
    if num_cards > len(deck):
        raise ValueError("Number of cards in spread is greater than the number of available cards in the deck.")
    cards = random.sample(list(deck.values()), num_cards)
    spread = TarotSpread(cards)
    return spread

# Основная программа
if __name__ == "__main__":
    num_cards_in_spread = 3  # Например, раскладка из 3 карт

    try:
        spread = generate_random_spread(tarot_deck, num_cards_in_spread)
        print("Выпавшие карты:")
        for card in spread.cards:
            print(f"{card.name}: {card.description}")

        print("\nИнтерпретации:")
        interpretations = spread.interpret()
        for interpretation in interpretations:
            print(interpretation)

        print("\nСинергия:")
        print(spread.synergy())
    except ValueError as e:
        print(e)
