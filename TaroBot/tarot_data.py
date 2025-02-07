# tarot_data.py

tarot_deck = {
    "The Fool": {
        "description": "Новая жизнь, приключение, свобода и неограниченные возможности.",
        "keywords": ["начало", "спонтанность", "свобода"],
    },
    "The Magician": {
        "description": "Талант, способность, изобретательность и креативность.",
        "keywords": ["сила", "действие", "искусство"],
    },
    "The High Priestess": {
        "description": "Интуиция, тайные знания, духовное просвещение и мистицизм.",
        "keywords": ["мудрость", "тайна", "подсознание"],
    },
    "The Empress": {
        "description": "Плодородие, изобилие, природа и материнство.",
        "keywords": ["изобилие", "творчество", "рост"],
    },
    "The Emperor": {
        "description": "Власть, структура, контроль и стабильность.",
        "keywords": ["авторитет", "лидерство", "структура"],
    },
    "The Hierophant": {
        "description": "Традиция, общественные нормы, духовное руководство и образование.",
        "keywords": ["традиция", "духовность", "обучение"],
    },
    "The Lovers": {
        "description": "Любовь, единство, партнерство и выбор.",
        "keywords": ["влечение", "гармония", "решение"],
    },
    "The Chariot": {
        "description": "Управление, успех, воля и уверенность.",
        "keywords": ["победа", "решимость", "контроль"],
    },
    "Strength": {
        "description": "Сила духа, мужество, терпение и внутренние ресурсы.",
        "keywords": ["храбрость", "стойкость", "терпение"],
    },
    "The Hermit": {
        "description": "Мудрость, самоанализ, уединение и поиск истины.",
        "keywords": ["интроспекция", "медитация", "осознание"],
    },
    "Wheel of Fortune": {
        "description": "Удача, судьба, циклы и перемены.",
        "keywords": ["судьба", "изменение", "везение"],
    },
    "Justice": {
        "description": "Справедливость, истина, закон и равновесие.",
        "keywords": ["честность", "баланс", "ответственность"],
    },
    "The Hanged Man": {
        "description": "Жертвенность, новое видение, пауза и самоотречение.",
        "keywords": ["отпускание", "интуиция", "перспектива"],
    },
    "Death": {
        "description": "Конец, трансформация, обновление и неизбежность перемен.",
        "keywords": ["трансформация", "конец", "новый старт"],
    },
    "Temperance": {
        "description": "Умеренность, баланс, гармония и синергия.",
        "keywords": ["баланс", "гармония", "синергия"],
    },
    "The Devil": {
        "description": "Материальные привязанности, искушения, ограничения и зависимость.",
        "keywords": ["искушение", "ограничение", "материализм"],
    },
    "The Tower": {
        "description": "Внезапные перемены, разрушение, откровение и кризис.",
        "keywords": ["кризис", "разрушение", "перемены"],
    },
    "The Star": {
        "description": "Надежда, вдохновение, вера и исцеление.",
        "keywords": ["надежда", "вдохновение", "исцеление"],
    },
    "The Moon": {
        "description": "Иллюзии, подсознание, интуиция и тайны.",
        "keywords": ["иллюзия", "интуиция", "тайна"],
    },
    "The Sun": {
        "description": "Счастье, успех, жизненная сила и радость.",
        "keywords": ["радость", "успех", "свет"],
    },
    "Judgement": {
        "description": "Пробуждение, возрождение, оценка и завершение.",
        "keywords": ["возрождение", "оценка", "решение"],
    },
    "The World": {
        "description": "Завершение, целостность, успех и достижение целей.",
        "keywords": ["завершение", "успех", "целостность"],
    }
}

# Вывод для проверки
for card, info in tarot_deck.items():
    print(f"{card}: {info['description']} ({', '.join(info['keywords'])})")
