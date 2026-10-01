## Zadanie 3: Różnice między Jinja2 (Flask) a DTL (Django)

Podczas przepisywania szablonów z Jinja2 na Django Template Language (DTL) zmodyfikowano 6 kluczowych elementów:

1. **Generowanie URL (trasy):**
   * Jinja2: `{{ url_for('product_detail', id=p.id) }}`
   * DTL: `{% url 'shop:item_detail' item.id %}` (użycie taga zamiast funkcji, użycie przestrzeni nazw z dwukropkiem i brak przecinków).

2. **Dostęp do elementów listy:**
   * Jinja2: `{{ items[0] }}`
   * DTL: `{{ items.0 }}` (kropka zamiast nawiasów kwadratowych).

3. **Licznik pętli:**
   * Jinja2: `loop.index`
   * DTL: `forloop.counter`

4. **Filtry z argumentami:**
   * Jinja2: `{{ price|round(2) }}`
   * DTL: `{{ price|floatformat:2 }}` (dwukropek zamiast nawiasów).

5. **Warunek boolowski (tak/nie):**
   * Jinja2: `{{ "tak" if ok else "nie" }}`
   * DTL: `{{ ok|yesno:"Tak,Nie" }}`

6. **Brak wsparcia dla matematyki:**
   * Jinja2: `{{ price * 1.23 }}`
   * DTL: Brak obliczeń bezpośrednio w szablonie (logika wykonywana w Pythonie).

**Łącznie zmodyfikowano 6 elementów.**