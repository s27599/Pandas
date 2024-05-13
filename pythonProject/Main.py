import seaborn as sns
import matplotlib.pyplot as plt

pingwiny = sns.load_dataset("penguins")
print(pingwiny.head())
# print(pingwiny.describ e())

rowsCount, columnsCount = pingwiny.shape
print("rows count:", rowsCount)
print("columns count:", columnsCount)

pingwiny = pingwiny.dropna(subset=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex'])

pingwiny = pingwiny.sort_values(by='body_mass_g', ascending=False)
pingwiny['numer_pingwina'] = range(1, len(pingwiny) + 1)
print(pingwiny.head())

print()
avg = pingwiny.mean(numeric_only=True)
sDeviation = pingwiny.std(numeric_only=True)

print("Average:\n", avg)
print()
print("sDeviation\n", sDeviation)

SpeciesAvg = pingwiny.groupby('species').mean(numeric_only=True)
SpeciesSDeviation = pingwiny.groupby('species').std(numeric_only=True)

print("Species average:\n", SpeciesAvg)
print()
print("Species sDeviation\n", SpeciesSDeviation)


plt.figure(figsize=(10, 5))
plt.hist(pingwiny['body_mass_g'], color='lightsalmon', edgecolor='black')
plt.title('Rozkład mas pingwinów')
plt.xlabel('Masa')
plt.ylabel('Liczba pingwinów')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x='species', y='body_mass_g', data=pingwiny)
plt.title('rozkład mas w zależności od gatunku pingwinów')
plt.xlabel('Gatunek')
plt.ylabel('Masa')
plt.show()

pingwinyZMasaNieWieksza = pingwiny[pingwiny['body_mass_g'] <= (avg['body_mass_g'] + 3 * sDeviation['body_mass_g'])]

plt.figure(figsize=(10, 5))
sns.scatterplot(data=pingwinyZMasaNieWieksza, x='flipper_length_mm', y='bill_length_mm', hue='species')
plt.title('zależność między "flipper_length_mm" i "bill_length_mm"')
plt.xlabel('Długość płetwy')
plt.ylabel('Długość dzioba')
plt.legend(title='Gatunek')
plt.grid(True)
plt.show()