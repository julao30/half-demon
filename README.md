# Projekt Python

## Opis
Ten projekt przedstawia walidację hasła.

## Instalacja
```bash
git clone https://github.com/julao30/half-demon.git
cd projekt-python
pip install -r requirements.txt
pip install flask
cd password_validator
python app.py
```

## Użycie
```python
password_validator/app.py
```

## Struktura projektu
```
projekt-python/
├── .github/workflows/
├── .idea
├── .vc/
├── __pycache__
├── password_validaor/
│   ├── app.py
│   ├── password_validator.py
│   ├── test_password_validator.py
├── src/
│   └── main.py
├── tests/
├── .gitignore
├── CHANGELOG.md
├── menu
├── README.md
└── requirements.txt
```

## Rozwiązywanie konfliktów
- Gałęzie 'feature/header-design-a' i 'feature/header-design-b' pokazywały ten sam nagłówek w main.py
- Podczas używania opcji 'merge' z main wystąpił konflikt.
- Został rozwiązany ręcznie przez utworzenie wspólnego nagłówka.

## Walidacja hasła
Funkcja 'is_valid_password(password)' sprawdza, czy hasło spełnia wymagania bezpieczeństwa:
- Minimum 8 znaków
- Wielka i mała litera
- Cyfra
- Znak specjalny
- Brak spacji

Przykład użycia:

```python
is_valid_password("Abcdef1!")
# → True
```

## Deployment
Aplikacja jest automatycznie wdrażana na serwer po pushu do gałęzi 'main'.

### Monitoring
- Endpoint: '/health'
- Rollback: W przypadku błędu deploymentu – cofnięcie commitów i restart serwera

### Secrets
- SSH_KEY
- API_KEY

## Licencja
Ten projekt jest licencjowany pod [licencją MIT](https://pl.wikipedia.org/wiki/Licencja_MIT)

## Autor
- Julia - [julao30](https://github.com/julao30)
