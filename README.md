# Naučite Git od nule 

Ovaj repozitorijum je praktični vodič za učenje Git osnova, sa posebnim fokusom na:
- Pravljenje grana (branches)
- Spajanje promena (merge)
- Rad sa udaljenim repozitorijumom (remote)
- Rešavanje konflikata

## 📂 Struktura projekta
```
learn-git-srpski/
├── README.md       - Ovo je glavni dokument
├── tutorial.py         - Prost kalkulator za vežbu
└── .gitignore      - Ignore lista za nepotrebne fajlove
```

## 🛠️ Kako početi
1. Klonirajte repozitorijum:
   ```bash
   git clone https://github.com/PetrarkaR/BEST-Nis-tut
   ```
2. Otvorite folder u editoru (VSCode, PyCharm itd)

## 🌿 Git Grane - Detaljni Tutorijal

### 1. Kreiranje nove grane
Da napravite novu granu za svoje promene:
```bash
git checkout -b moja-nova-grana
```
Primer: `git checkout -b dodaj-stepenovanje`

### 2. Pregled svih grana
Proverite koje grane postoje:
```bash
git branch
```

### 3. Promena grane
Za prelazak na drugu granu:
```bash
git checkout ime-grane
```
Primer: `git checkout main`

### 4. Sinronizacija sa glavnom granom
Uvek počnite ažuriranjem glavne grane:
```bash
git checkout main
git pull origin main
```

### 5. Spajanje grana (merge)
Kada završite promene u svojoj grani, spojite ih u main:
```bash
git checkout main
git merge moja-nova-grana
```

### 6. Slanje promena na GitHub
Posle commita, pošaljite svoju granu na GitHub:
```bash
git push origin ime-vase-grane
```

## 💻 Praktični Primer: Dodajte novu funkcionalnost

Hajde da dodamo stepenovanje u `calc.py` koristeći grane:

1. Napravite novu granu:
   ```bash
   git checkout -b dodaj-stepenovanje
   ```

2. U `calc.py` dodajte funkciju:
   ```python
   def stepenovanje(a, b):
       return a ** b
   ```

3. Dodajte opciju u meni (oko linije 20):
   ```python
   print("5. Stepenovanje")
   ```

4. Dodajte logiku za izbor (u if/elif bloku):
   ```python
   elif izbor == '5':
       print(f"Rezultat: {stepenovanje(broj1, broj2)}")
   ```

5. Sačuvajte promene i uradite commit:
   ```bash
   git add calc.py
   git commit -m "Dodata funkcionalnost stepenovanja"
   ```

6. Pošaljite granu na GitHub:
   ```bash
   git push origin dodaj-stepenovanje
   ```

7. Napravite Pull Request na GitHub interfejsu!

## 🔄 Rešavanje konflikata - Simulacija problema

Da vežbamo rešavanje konflikata:

1. Dva korisnika menjaju istu liniju u `calc.py`
2. Prvi korisnik merguje svoje promene u main
3. Drugi korisnik dobija konflikt pri pokušaju merga
4. Rešite konflikt ručno u editoru
5. Uradite commit sa rešenim konfliktom

```bash
# Nakon konflikta:
git add .
git commit -m "Rešen konflikt u calc.py"
git push
```

## 📋 Preporučeni workflow
1. Uvek pravite novu granu za svaku novu funkcionalnost
2. Često pravite commite sa smislenim porukama
3. Pre merga uvek povucite najnovije promene sa main grane
4. Testirajte kod pre nego što pošaljete PR

## 🗂️ Korisne Git komande
| Komanda                     | Opis                                  |
|-----------------------------|---------------------------------------|
| `git log --oneline --graph` | Pregled istorije sa granama           |
| `git diff ime-grane`        | Prikaz razlika u odnosu na trenutnu granu |
| `git stash`                 | Privremeno sačuvaj promene bez commita|
| `git rebase main`           | Ažuriraj granu na najnoviji main      |

## 📝 Zadatak za vežbu
1. Dodajte novu matematicku funkciju u novoj grani
2. Spojite je u main granu
3. Simulirajte konflikt sa drugim korisnikom
4. Rešite konflikt i potvrdite rešenje
