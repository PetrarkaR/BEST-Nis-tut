# Git Fork Workflow Tutorial

## 🎯 Uvod
Ovaj vodič će vam pomoći da naučite kako da koristite Git kroz fork workflow. Ovo je idealan pristup za timove gde članovi nemaju direktan pristup glavnom repozitorijumu.

## 📋 Preduslovi
- GitHub nalog
- Git instaliran na računaru
- Osnovne CLI (Command Line Interface) veštine

- Pravljenje svog access tokena
    1. Gore desno kliknite na svoj profil i otvorite settings
    2. Scrollujte dole i nadjite developer settings
    3. Personal Access Token
    4. Token(Classic)
    5. Generate new token (classic)
    6. Checkujte repo
    7. Generisite token skroz dole
    8. OBAVEZNO ZAPAMTITE SIFRU NEGDE NECE JE VIDITE OPET
    
- Kad vam trazi username kucate svoj username meni npr LuXx8833 a posle kad trazi password tu se stavlja token

## 🚀 Prvi koraci

### 1. Fork repozitorijuma
1. Posetite `https://github.com/PetrarkaR/BEST-Nis-tut`
2. Kliknite "Fork" dugme u gornjem desnom uglu
3. Sačekajte da GitHub napravi kopiju na vašem nalogu

### 2. Kloniranje vašeg fork-a
```bash
# Zamenite YOUR-USERNAME sa vašim GitHub korisničkim imenom
git clone https://github.com/YOUR-USERNAME/BEST-Nis-tut.git
cd BEST-Nis-tut
```

### 3. Povezivanje sa originalnim repozitorijumom
```bash
# Dodajte original kao "upstream" remote
git remote add upstream https://github.com/PetrarkaR/BEST-Nis-tut.git

# Proverite remote-ove
git remote -v
```

## 💻 Rad na projektu

### 1. Sinhronizacija sa originalnim repozitorijumom
```bash
# Preuzmite promene
git fetch upstream

# Prebacite se na main granu
git checkout main

# Ažurirajte vašu main granu
git merge upstream/main

# Ažurirajte vaš fork
git push origin main
```

### 2. Kreiranje nove grane za funkcionalnost
```bash
# Napravite i prebacite se na novu granu
git checkout -b feature/nova-funkcionalnost
```

### 3. Rad na kodu
Otvorite `tutorial.py` i dodajte vašu funkcionalnost. Na primer:
```python
def nova_funkcija(x, y):
    return x * y

# Dodajte u meni
print("6. Nova Funkcija")

# Dodajte u logiku izbora
elif izbor == '6':
    print(f"Rezultat: {nova_funkcija(broj1, broj2)}")
```

### 4. Commit promena
```bash
# Dodajte promene
git add tutorial.py

# Napravite commit
git commit -m "Dodata nova funkcionalnost"

# Pošaljite promene na vaš fork
git push origin feature/nova-funkcionalnost
```

## 📤 Kreiranje Pull Request-a

1. Idite na vaš fork na GitHub-u
2. Kliknite "Pull Request"
3. Odaberite vašu feature granu
4. Za base repository izaberite originalni repozitorijum
5. Napišite jasan opis promena
6. Kliknite "Create Pull Request"

## 🔄 Rešavanje konflikata

Ako se pojavi konflikt:

```bash
# Sinhronizujte se sa upstream-om
git fetch upstream

# Prebacite se na vašu granu
git checkout feature/nova-funkcionalnost

# Spojite promene iz upstream/main
git merge upstream/main

# Rešite konflikte u editoru
# Nakon rešavanja:
git add .
git commit -m "Rešen konflikt"
git push origin feature/nova-funkcionalnost
```

## ⚠️ Važna pravila

1. **Nikad ne radite direktno na main grani**
2. Uvek napravite novu granu za svaku funkcionalnost
3. Držite PR-ove malim i fokusiranim
4. Redovno sinhronizujte vaš fork
5. Pišite jasne commit poruke

## 📝 Git cheat sheet

| Komanda | Opis |
|---------|------|
| `git status` | Pregled stanja |
| `git log --oneline` | Pregled istorije |
| `git fetch --all` | Preuzmi sve promene |
| `git branch -a` | Lista svih grana |
| `git remote -v` | Lista svih remote-ova |

## 🎓 Zadaci za vežbu

1. Forkujte repozitorijum
2. Napravite novu granu
3. Dodajte novu matematičku funkciju u `tutorial.py`
4. Pošaljite Pull Request
5. Rešite konflikt ako se pojavi

## 🆘 Česti problemi i rešenja

### Problem: Ne mogu da push-ujem promene
```bash
git push origin feature/nova-funkcionalnost -f  # Koristite force push oprezno!
```

### Problem: Pogrešna upstream grana
```bash
# Proverite trenutni upstream
git remote -v

# Dodajte ispravan ako je potrebno
git remote add upstream https://github.com/PetrarkaR/BEST-Nis-tut.git
```

### Problem: Konflikti pri merge-u
```bash
# Prekinite merge
git merge --abort

# Počnite ponovo
git fetch upstream
git merge upstream/main
```

## 📚 Dodatni resursi

- [Git dokumentacija](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## 🤝 Pravila doprinosa

1. Svaki PR mora da ima jasan opis
2. Kod mora biti testiran
3. Pratite postojeći stil koda
4. Jedan PR = jedna funkcionalnost
