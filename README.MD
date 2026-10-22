## Environment Setup
Run in linux terminal:

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies, then the package
pip install -r requirements.txt
pip install -e .

# Create a local environment variables file
cp .env.template .env
```
To use LLMs via API, enter your api tokens in .env file.

___

## Wywołanie modelu
input
```py
system="Odpowiadaj krótko i jasno po polsku.",
        user="Wyjaśnij, czym jest token w modelu językowym.",
        max_tokens=160,
```
output
```
{'input_ids': tensor([[151644,   8948,    198,     46,   9796,    363,  62944,   1630, 137235,
             78,    600,    502,    300,   2152,   3193,   1471,  39929,     13,
         151645,    198, 151644,    872,    198,  66907,   5580,   7393,     77,
           3172,     11,  17988,   1600,  13296,   3950,    289,   1614,     84,
         132938,    363,   1600,     13, 151645,    198, 151644,  77091,    198]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
Token to element w języku naturalnym, który jest używany do przetwarzania tekstu. W języku angielskim to "token" lub "word". Jest to jedna z głównych elementów w modeli języka naturalnego, która umożliwia interpretację i interpretację tekstowych.

Model: Qwen/Qwen2.5-0.5B-Instruct | tryb: local | wejście: 45 tokenów | wyjście: 64 tokenów | czas: 9.67 s
```

## Dlaczego liczby tokenów nie można wiarygodnie oszacować liczbą słów?
W zależności od języka i tokenizera, słowa dzielone są w różny sposób. Jedno słowo może być rozbite na 1 lub kilka tokenów. Emoji lub znaki interpunkcyjne także.
___
### Potwierdzam, że to repozytorium będzie rozwijane w kolejnych laboratoriach.
