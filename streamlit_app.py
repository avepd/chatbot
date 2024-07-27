import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_article_content(url):
    try:
        # Pobieranie strony
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie, czy żądanie się powiodło

        # Parsowanie HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Znajdowanie treści artykułu - to może wymagać dostosowania w zależności od struktury strony
        # Tutaj przykładowo zakładamy, że treść artykułu jest w tagu <article>
        article = soup.find('article')
        if not article:
            # Alternatywnie, można szukać innych typowych kontenerów dla treści artykułów
            article = soup.find('div', class_='article-content')
        
        # Wyciągnięcie tekstu
        if article:
            content = article.get_text(separator='\n', strip=True)
            return content
        else:
            return "Nie znaleziono treści artykułu."

    except requests.exceptions.RequestException as e:
        return f"Błąd podczas pobierania strony: {e}"

# Konfiguracja aplikacji Streamlit
st.title("Pobieranie treści artykułu")

# Pobieranie URL od użytkownika
url = st.text_input("Podaj URL artykułu:")

if url:
    # Pobieranie i wyświetlanie treści artykułu
    content = fetch_article_content(url)
    st.write(content)
