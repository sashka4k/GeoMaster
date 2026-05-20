# main.py
import tkinter as tk
from tkinter import messagebox
import random
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod

# ==================== МОДЕЛЬ (ДАННЫЕ) ====================

@dataclass
class Country:
    """Класс, представляющий страну"""
    name: str
    capital: str
    region: str


class DataProvider(ABC):
    """Абстрактный класс для поставщика данных"""
    
    @abstractmethod
    def get_all_countries(self) -> List[Country]:
        pass
    
    @abstractmethod
    def get_country_by_name(self, name: str) -> Optional[Country]:
        pass
    
    @abstractmethod
    def get_all_capitals(self) -> List[str]:
        pass


class InMemoryDataProvider(DataProvider):
    """Реализация поставщика данных с хранением в памяти"""
    
    def __init__(self):
        self._countries = self._init_countries()
    
    def _init_countries(self) -> Dict[str, Country]:
        """Инициализация базы данных стран"""
        countries_data = {
            # Европа
            "Россия": ("Москва", "Европа"),
            "Германия": ("Берлин", "Европа"),
            "Франция": ("Париж", "Европа"),
            "Италия": ("Рим", "Европа"),
            "Испания": ("Мадрид", "Европа"),
            "Великобритания": ("Лондон", "Европа"),
            "Польша": ("Варшава", "Европа"),
            "Украина": ("Киев", "Европа"),
            "Нидерланды": ("Амстердам", "Европа"),
            "Бельгия": ("Брюссель", "Европа"),
            "Швеция": ("Стокгольм", "Европа"),
            "Норвегия": ("Осло", "Европа"),
            "Дания": ("Копенгаген", "Европа"),
            "Финляндия": ("Хельсинки", "Европа"),
            "Швейцария": ("Берн", "Европа"),
            "Австрия": ("Вена", "Европа"),
            "Греция": ("Афины", "Европа"),
            "Турция": ("Анкара", "Азия"),
            "Португалия": ("Лиссабон", "Европа"),
            "Ирландия": ("Дублин", "Европа"),
            "Чехия": ("Прага", "Европа"),
            "Венгрия": ("Будапешт", "Европа"),
            "Румыния": ("Бухарест", "Европа"),
            "Болгария": ("София", "Европа"),
            "Сербия": ("Белград", "Европа"),
            "Хорватия": ("Загреб", "Европа"),
            "Исландия": ("Рейкьявик", "Европа"),
            "Словакия": ("Братислава", "Европа"),
            "Словения": ("Любляна", "Европа"),
            "Литва": ("Вильнюс", "Европа"),
            "Латвия": ("Рига", "Европа"),
            "Эстония": ("Таллин", "Европа"),
            "Беларусь": ("Минск", "Европа"),
            "Молдова": ("Кишинёв", "Европа"),
            "Грузия": ("Тбилиси", "Азия"),
            "Армения": ("Ереван", "Азия"),
            
            # Азия
            "Китай": ("Пекин", "Азия"),
            "Индия": ("Нью-Дели", "Азия"),
            "Япония": ("Токио", "Азия"),
            "Южная Корея": ("Сеул", "Азия"),
            "Индонезия": ("Джакарта", "Азия"),
            "Вьетнам": ("Ханой", "Азия"),
            "Таиланд": ("Бангкок", "Азия"),
            "Малайзия": ("Куала-Лумпур", "Азия"),
            "Филиппины": ("Манила", "Азия"),
            "Пакистан": ("Исламабад", "Азия"),
            "Иран": ("Тегеран", "Азия"),
            "Ирак": ("Багдад", "Азия"),
            "Саудовская Аравия": ("Эр-Рияд", "Азия"),
            "Израиль": ("Иерусалим", "Азия"),
            "ОАЭ": ("Абу-Даби", "Азия"),
            "Катар": ("Доха", "Азия"),
            "Кувейт": ("Эль-Кувейт", "Азия"),
            "Казахстан": ("Астана", "Азия"),
            "Узбекистан": ("Ташкент", "Азия"),
            "Туркменистан": ("Ашхабад", "Азия"),
            "Кыргызстан": ("Бишкек", "Азия"),
            "Таджикистан": ("Душанбе", "Азия"),
            "Азербайджан": ("Баку", "Азия"),
            "Афганистан": ("Кабул", "Азия"),
            "Бангладеш": ("Дакка", "Азия"),
            "Монголия": ("Улан-Батор", "Азия"),
            "Непал": ("Катманду", "Азия"),
            "Шри-Ланка": ("Шри-Джаяварденепура-Котте", "Азия"),
            
            # Африка
            "Египет": ("Каир", "Африка"),
            "ЮАР": ("Претория", "Африка"),
            "Марокко": ("Рабат", "Африка"),
            "Нигерия": ("Абуджа", "Африка"),
            "Кения": ("Найроби", "Африка"),
            "Эфиопия": ("Аддис-Абеба", "Африка"),
            "Гана": ("Аккра", "Африка"),
            "Алжир": ("Алжир", "Африка"),
            "Судан": ("Хартум", "Африка"),
            "Тунис": ("Тунис", "Африка"),
            "Ливия": ("Триполи", "Африка"),
            "Сенегал": ("Дакар", "Африка"),
            "Уганда": ("Кампала", "Африка"),
            "Зимбабве": ("Хараре", "Африка"),
            "Ангола": ("Луанда", "Африка"),
            "Танзания": ("Додома", "Африка"),
            "Руанда": ("Кигали", "Африка"),
            "Камерун": ("Яунде", "Африка"),
            "Кот-д'Ивуар": ("Ямусукро", "Африка"),
            "Мадагаскар": ("Антананариву", "Африка"),
            
            # Северная Америка
            "США": ("Вашингтон", "Северная Америка"),
            "Канада": ("Оттава", "Северная Америка"),
            "Мексика": ("Мехико", "Северная Америка"),
            "Куба": ("Гавана", "Северная Америка"),
            "Гватемала": ("Гватемала", "Северная Америка"),
            "Панама": ("Панама", "Северная Америка"),
            "Коста-Рика": ("Сан-Хосе", "Северная Америка"),
            
            # Южная Америка
            "Бразилия": ("Бразилиа", "Южная Америка"),
            "Аргентина": ("Буэнос-Айрес", "Южная Америка"),
            "Перу": ("Лима", "Южная Америка"),
            "Колумбия": ("Богота", "Южная Америка"),
            "Чили": ("Сантьяго", "Южная Америка"),
            "Венесуэла": ("Каракас", "Южная Америка"),
            "Эквадор": ("Кито", "Южная Америка"),
            "Боливия": ("Ла-Пас", "Южная Америка"),
            "Парагвай": ("Асунсьон", "Южная Америка"),
            "Уругвай": ("Монтевидео", "Южная Америка"),
            
            # Австралия и Океания
            "Австралия": ("Канберра", "Океания"),
            "Новая Зеландия": ("Веллингтон", "Океания"),
            "Папуа-Новая Гвинея": ("Порт-Морсби", "Океания"),
            "Фиджи": ("Сува", "Океания"),
        }
        
        return {
            name: Country(name=name, capital=capital, region=region)
            for name, (capital, region) in countries_data.items()
        }
    
    def get_all_countries(self) -> List[Country]:
        return list(self._countries.values())
    
    def get_country_by_name(self, name: str) -> Optional[Country]:
        return self._countries.get(name)
    
    def get_all_capitals(self) -> List[str]:
        return [country.capital for country in self._countries.values()]


# ==================== ЛОГИКА ИГРЫ ====================

class QuestionGenerator:
    """Класс для генерации вопросов"""
    
    def __init__(self, data_provider: DataProvider):
        self._data_provider = data_provider
        self._all_countries = data_provider.get_all_countries()
        self._all_capitals = data_provider.get_all_capitals()
    
    def get_random_country(self) -> Country:
        """Возвращает случайную страну"""
        return random.choice(self._all_countries)
    
    def generate_options(self, correct_capital: str, num_options: int = 4) -> List[str]:
        """Генерирует варианты ответов"""
        options = {correct_capital}
        
        while len(options) < num_options:
            random_capital = random.choice(self._all_capitals)
            if random_capital != correct_capital:
                options.add(random_capital)
        
        options_list = list(options)
        random.shuffle(options_list)
        return options_list


class ScoreManager:
    """Класс для управления счётом"""
    
    def __init__(self, points_per_question: int = 10):
        self._points_per_question = points_per_question
        self._score = 0
        self._questions_asked = 0
    
    @property
    def score(self) -> int:
        return self._score
    
    @property
    def questions_asked(self) -> int:
        return self._questions_asked
    
    @property
    def accuracy(self) -> float:
        if self._questions_asked == 0:
            return 0.0
        return (self._score / (self._questions_asked * self._points_per_question)) * 100
    
    def add_correct(self) -> int:
        """Добавляет очки за правильный ответ"""
        self._score += self._points_per_question
        self._questions_asked += 1
        return self._points_per_question
    
    def add_wrong(self) -> None:
        """Фиксирует неправильный ответ"""
        self._questions_asked += 1
    
    def reset(self) -> None:
        """Сбрасывает счёт"""
        self._score = 0
        self._questions_asked = 0
    
    def get_statistics(self) -> Dict[str, float]:
        """Возвращает статистику в виде словаря"""
        return {
            "score": self._score,
            "questions_asked": self._questions_asked,
            "accuracy": self.accuracy,
            "average": self._score / self._questions_asked if self._questions_asked > 0 else 0
        }


class GameState:
    """Класс для управления состоянием игры"""
    
    def __init__(self, question_generator: QuestionGenerator, score_manager: ScoreManager):
        self._question_generator = question_generator
        self._score_manager = score_manager
        self._current_country: Optional[Country] = None
        self._current_options: List[str] = []
        self._answer_locked: bool = False
        self._last_correct_answer: Optional[str] = None
    
    @property
    def current_country(self) -> Optional[Country]:
        return self._current_country
    
    @property
    def current_options(self) -> List[str]:
        return self._current_options
    
    @property
    def is_answer_locked(self) -> bool:
        return self._answer_locked
    
    @property
    def last_correct_answer(self) -> Optional[str]:
        return self._last_correct_answer
    
    def new_question(self) -> Tuple[Country, List[str]]:
        """Генерирует новый вопрос"""
        self._current_country = self._question_generator.get_random_country()
        self._current_options = self._question_generator.generate_options(
            self._current_country.capital
        )
        self._answer_locked = False
        self._last_correct_answer = None
        return self._current_country, self._current_options
    
    def submit_answer(self, selected_index: int) -> Tuple[bool, int]:
        """Обрабатывает ответ пользователя"""
        if self._answer_locked:
            return False, 0
        
        self._answer_locked = True
        selected_answer = self._current_options[selected_index]
        is_correct = (selected_answer == self._current_country.capital)
        
        if is_correct:
            points = self._score_manager.add_correct()
            self._last_correct_answer = None
            return True, points
        else:
            self._score_manager.add_wrong()
            self._last_correct_answer = self._current_country.capital
            return False, 0
    
    def reset(self) -> None:
        """Сбрасывает состояние игры"""
        self._score_manager.reset()
        self._answer_locked = False
        self._last_correct_answer = None


# ==================== ПРЕДСТАВЛЕНИЕ (VIEW) ====================

class GameView:
    """Класс для отображения интерфейса"""
    
    def __init__(self, root: tk.Tk):
        self._root = root
        self._root.title("Столицы мира - Географическая викторина")
        self._root.geometry("700x580")
        self._root.configure(bg="#2c3e50")
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Настройка пользовательского интерфейса"""
        # Заголовок
        title_label = tk.Label(self._root, text="🌏 СТОЛИЦЫ МИРА 🌎", 
                                font=("Arial", 22, "bold"), 
                                bg="#2c3e50", fg="#f1c40f")
        title_label.pack(pady=15)
        
        # Статистика
        stats_frame = tk.Frame(self._root, bg="#34495e", height=55)
        stats_frame.pack(fill="x", padx=10, pady=5)
        stats_frame.pack_propagate(False)
        
        self._score_label = tk.Label(stats_frame, text="🏆 СЧЁТ: 0", 
                                      font=("Arial", 13, "bold"), 
                                      bg="#34495e", fg="#f39c12")
        self._score_label.pack(side="left", padx=25, pady=10)
        
        self._questions_label = tk.Label(stats_frame, text="❓ ВОПРОСОВ: 0", 
                                          font=("Arial", 13, "bold"), 
                                          bg="#34495e", fg="white")
        self._questions_label.pack(side="left", padx=25, pady=10)
        
        self._accuracy_label = tk.Label(stats_frame, text="📈 ТОЧНОСТЬ: 0%", 
                                         font=("Arial", 13, "bold"), 
                                         bg="#34495e", fg="#1abc9c")
        self._accuracy_label.pack(side="left", padx=25, pady=10)
        
        # Основная игровая область
        game_frame = tk.Frame(self._root, bg="#ecf0f1")
        game_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Вопрос
        self._question_label = tk.Label(game_frame, text="", 
                                         font=("Arial", 17, "bold"), 
                                         bg="#ecf0f1", fg="#2c3e50")
        self._question_label.pack(pady=25)
        
        # Фрейм для кнопок
        options_frame = tk.Frame(game_frame, bg="#ecf0f1")
        options_frame.pack(pady=10)
        
        # Кнопки вариантов
        self._option_buttons = []
        for i in range(4):
            btn = tk.Button(options_frame, text="", 
                           font=("Arial", 12), 
                           width=28, height=1,
                           bg="#3498db", fg="white",
                           activebackground="#2980b9")
            btn.pack(pady=6)
            self._option_buttons.append(btn)
        
        # Кнопка следующего вопроса
        self._next_btn = tk.Button(game_frame, text="➡ СЛЕДУЮЩИЙ ВОПРОС ⬅", 
                                    font=("Arial", 12, "bold"),
                                    bg="#2ecc71", fg="white",
                                    activebackground="#27ae60",
                                    width=32, height=1,
                                    state="disabled")
        self._next_btn.pack(pady=15)
        
        # Статус
        self._status_label = tk.Label(game_frame, text="", 
                                       font=("Arial", 11), 
                                       bg="#ecf0f1", fg="#7f8c8d")
        self._status_label.pack()
        
        # Нижняя панель
        bottom_frame = tk.Frame(self._root, bg="#34495e", height=42)
        bottom_frame.pack(fill="x", side="bottom")
        bottom_frame.pack_propagate(False)
        
        self._reset_btn = tk.Button(bottom_frame, text="🔄 СБРОСИТЬ СЧЁТ", 
                                     font=("Arial", 9, "bold"),
                                     bg="#e74c3c", fg="white")
        self._reset_btn.pack(side="right", padx=15, pady=6)
        
        self._info_label = tk.Label(bottom_frame, text="📚 ВСЕГО СТРАН: 0", 
                                     font=("Arial", 10, "bold"), 
                                     bg="#34495e", fg="#bdc3c7")
        self._info_label.pack(side="left", padx=15, pady=6)
    
    def update_statistics(self, score: int, questions: int, accuracy: float):
        """Обновляет отображение статистики"""
        self._score_label.config(text=f"🏆 СЧЁТ: {score}")
        self._questions_label.config(text=f"❓ ВОПРОСОВ: {questions}")
        self._accuracy_label.config(text=f"📈 ТОЧНОСТЬ: {accuracy:.1f}%")
    
    def update_question(self, country_name: str, options: List[str]):
        """Обновляет вопрос и варианты ответов"""
        self._question_label.config(text=f"🏛️ СТОЛИЦА СТРАНЫ: {country_name}?")
        for i, option in enumerate(options):
            self._option_buttons[i].config(text=option, bg="#3498db", state="normal")
    
    def show_correct_feedback(self, button_index: int, points: int):
        """Показывает обратную связь для правильного ответа"""
        self._status_label.config(text=f"✅ ПРАВИЛЬНО! +{points} ОЧКОВ ✅", fg="#27ae60")
        self._option_buttons[button_index].config(bg="#27ae60")
    
    def show_wrong_feedback(self, button_index: int, correct_answer: str):
        """Показывает обратную связь для неправильного ответа"""
        self._status_label.config(text=f"❌ ПРАВИЛЬНЫЙ ОТВЕТ: {correct_answer} ❌", fg="#e74c3c")
        self._option_buttons[button_index].config(bg="#e74c3c")
        
        for i, btn in enumerate(self._option_buttons):
            if btn.cget("text") == correct_answer:
                self._option_buttons[i].config(bg="#27ae60")
                break
    
    def reset_buttons_state(self):
        """Сбрасывает состояние кнопок"""
        for btn in self._option_buttons:
            btn.config(state="disabled")
    
    def enable_next_button(self):
        """Активирует кнопку следующего вопроса"""
        self._next_btn.config(state="normal")
    
    def disable_next_button(self):
        """Деактивирует кнопку следующего вопроса"""
        self._next_btn.config(state="disabled")
    
    def set_status_message(self, message: str, color: str = "#7f8c8d"):
        """Устанавливает статусное сообщение"""
        self._status_label.config(text=message, fg=color)
    
    def set_info_text(self, text: str):
        """Устанавливает информационный текст"""
        self._info_label.config(text=text)
    
    def bind_option_click(self, callback):
        """Привязывает обработчик к кнопкам вариантов"""
        for i, btn in enumerate(self._option_buttons):
            btn.config(command=lambda idx=i: callback(idx))
    
    def bind_next_click(self, callback):
        """Привязывает обработчик к кнопке следующего вопроса"""
        self._next_btn.config(command=callback)
    
    def bind_reset_click(self, callback):
        """Привязывает обработчик к кнопке сброса"""
        self._reset_btn.config(command=callback)
    
    def show_statistics_dialog(self, stats: Dict[str, float], total_countries: int):
        """Показывает диалоговое окно со статистикой"""
        messagebox.showinfo("📊 СТАТИСТИКА ИГРЫ 📊", 
            f"📌 ВСЕГО ВОПРОСОВ: {int(stats['questions_asked'])}\n"
            f"🏆 НАБРАНО ОЧКОВ: {int(stats['score'])}\n"
            f"📈 ТОЧНОСТЬ: {stats['accuracy']:.1f}%\n"
            f"⭐ СРЕДНИЙ БАЛЛ: {stats['average']:.1f}\n\n"
            f"🌍 ДОСТУПНО СТРАН: {total_countries}\n"
            f"🚀 ПРОДОЛЖАЙТЕ В ТОМ ЖЕ ДУХЕ!")
    
    def show_reset_confirmation(self) -> bool:
        """Показывает диалог подтверждения сброса"""
        return messagebox.askyesno("⚠️ ПОДТВЕРЖДЕНИЕ ⚠️", 
                                   "ВЫ УВЕРЕНЫ, ЧТО ХОТИТЕ СБРОСИТЬ СЧЁТ И НАЧАТЬ ЗАНОВО?")


# ==================== КОНТРОЛЛЕР ====================

class GameController:
    """Контроллер, управляющий игрой"""
    
    def __init__(self, view: GameView, game_state: GameState, data_provider: DataProvider):
        self._view = view
        self._game_state = game_state
        self._data_provider = data_provider
        
        self._setup_callbacks()
        self._start_new_game()
    
    def _setup_callbacks(self):
        """Настраивает обработчики событий"""
        self._view.bind_option_click(self._on_answer_selected)
        self._view.bind_next_click(self._on_next_question)
        self._view.bind_reset_click(self._on_reset_game)
    
    def _start_new_game(self):
        """Начинает новую игру"""
        self._update_ui_from_state()
        self._view.set_info_text(f"📚 ВСЕГО СТРАН: {len(self._data_provider.get_all_countries())}")
        self._on_next_question()
    
    def _update_ui_from_state(self):
        """Обновляет UI на основе состояния игры"""
        stats = self._game_state._score_manager.get_statistics()
        self._view.update_statistics(
            int(stats['score']),
            int(stats['questions_asked']),
            stats['accuracy']
        )
    
    def _on_answer_selected(self, button_index: int):
        """Обработчик выбора ответа"""
        if self._game_state.is_answer_locked:
            return
        
        is_correct, points = self._game_state.submit_answer(button_index)
        
        if is_correct:
            self._view.show_correct_feedback(button_index, points)
        else:
            self._view.show_wrong_feedback(button_index, self._game_state.last_correct_answer)
        
        self._view.reset_buttons_state()
        self._view.enable_next_button()
        self._update_ui_from_state()
        
        stats = self._game_state._score_manager.get_statistics()
        if int(stats['questions_asked']) % 10 == 0 and int(stats['questions_asked']) > 0:
            self._view.show_statistics_dialog(stats, len(self._data_provider.get_all_countries()))
    
    def _on_next_question(self):
        """Обработчик перехода к следующему вопросу"""
        country, options = self._game_state.new_question()
        self._view.update_question(country.name, options)
        self._view.disable_next_button()
        self._view.set_status_message("👉 ВЫБЕРИТЕ ПРАВИЛЬНЫЙ ВАРИАНТ 👈", "#7f8c8d")
    
    def _on_reset_game(self):
        """Обработчик сброса игры"""
        if self._view.show_reset_confirmation():
            self._game_state.reset()
            self._update_ui_from_state()
            self._view.set_status_message("🔄 СЧЁТ СБРОШЕН! НАЧИНАЕМ ЗАНОВО 🔄", "#f39c12")
            self._on_next_question()


# ==================== ТОЧКА ВХОДА ====================

def main():
    root = tk.Tk()
    
    # Создание зависимостей (Dependency Injection)
    data_provider = InMemoryDataProvider()
    question_generator = QuestionGenerator(data_provider)
    score_manager = ScoreManager()
    game_state = GameState(question_generator, score_manager)
    view = GameView(root)
    controller = GameController(view, game_state, data_provider)
    
    root.mainloop()

if __name__ == "__main__":
    main()