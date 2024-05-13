# -*- coding: utf-8 -*-
"""
- Wczytaj danych i wyświetl kilka pierwszych wierszy, aby zapoznać się ze strukturą danych.
  Sprawdź liczby wierszy i kolumn w zbiorze danych.
- Usuń pingwiny z brakami danych i dodaj nową kolumnę, gdzie każdemu pingwinowi przypiszemy liczbę gdzie 1 to pingwin o największej masie (0,25)
- Oblicz średnią i odchylenie standardowe z cech fizycznych pingwinów (wszystkich i dla każdego z gatanku). (0,5)
- Zwizualizuj dane za pomocą histogramu przedstawiającego rozkład mas pingwinów oraz boxplot prezentującego rozkład mas w zależności od gatunku pingwinów. (0,5)
- Utwórz nowy dataset który zwiera tylko pingwiny z masą nie wiekszą niż 3 odchelnia standardowe od średniej (0,25)
- Zobrazuj zależność między "flipper_length_mm" i "bill_length_mm" za pomocą scatter plotu (uwzględnij gatunek) (0,5)

import seaborn as sns
#Wczytanie danych
pingwiny = sns.load_dataset("penguins")
"""
