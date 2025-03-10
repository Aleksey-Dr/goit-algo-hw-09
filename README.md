<a id="top"></a>
# Порівняння жадібного алгоритму та алгоритму динамічного програмування

<a href="#1"><img src="https://img.shields.io/badge/Опис завдання / Task description-512BD4?style=for-the-badge"/></a> <a href="#2"><img src="https://img.shields.io/badge/Результати / Results-ECD53F?style=for-the-badge"/></a> <a href="#3"><img src="https://img.shields.io/badge/Оцінка ефективності / Performance evaluation-007054?style=for-the-badge"/></a> <a href="#4"><img src="https://img.shields.io/badge/Висновки / Conclusions-A9225C?style=for-the-badge"/></a>
___
<a id="1"></a>
## <img src="https://img.shields.io/badge/Опис завдання / Task description-512BD4?style=for-the-badge"/>

1. Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.
2. Функція динамічного програмування find_min_coins. Ця функція також повинна приймати суму для видачі решти, але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом. Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}

[Вгору / Top :arrow_double_up:](#top)
___
<a id="2"></a>
## <img src="https://img.shields.io/badge/Результати / Results-ECD53F?style=for-the-badge"/>

- Жадібний алгоритм: {50: 2, 10: 1, 2: 1, 1: 1}
- Динамічне програмування: {1: 1, 2: 1, 10: 1, 50: 2}

[Вгору / Top :arrow_double_up:](#top)
___
<a id="3"></a>
## <img src="https://img.shields.io/badge/Оцінка ефективності / Performance evaluation-007054?style=for-the-badge"/>

### Жадібний алгоритм:
- Часова складність: O(k), де `k` — кількість номіналів монет.
- Підходить для швидкого знаходження решти, але не завжди гарантує мінімальну кількість монет для всіх можливих наборів номіналів.

### Алгоритм динамічного програмування:
- Часова складність: O(n * k), де `n` — сума для видачі решти, а `k` — кількість номіналів монет.
- Завжди гарантує мінімальну кількість монет для формування будь-якої суми, але є більш затратним за часом, особливо для великих сум.

[Вгору / Top :arrow_double_up:](#top)
___
<a id="4"></a>
## <img src="https://img.shields.io/badge/Висновки / Conclusions-A9225C?style=for-the-badge"/>

- Жадібний алгоритм є ефективним та швидким у використанні, особливо коли набори монет підходять для жадібного підходу.
- Алгоритм динамічного програмування підходить для більш універсальних рішень, де потрібно мінімізувати кількість монет, але він потребує більше часу для виконання.
- У нашому прикладі жадібний алгоритм і алгоритм динамічного програмування дають однаковий результат для стандартного набору монет.

[Вгору / Top :arrow_double_up:](#top)