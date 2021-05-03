# CLMM Solve

from hint 2

* `grep CLUE crimescene >> clues.txt`

```
CLUE: Footage from an ATM security camera is blurry but shows that the perpetrator is at least 6' tall.
CLUE: Found a wallet believed to belong to the killer: no ID, just loose change, and membership cards for AAA, Delta SkyMiles, the local library, and the Museum of Bash History. The cards are totally untraceable and have no name, for some reason.
CLUE: Questioned the barista at the local coffee shop. He said a person left right before they heard the shots. The name on their latte was Annabel, they had blond spiky hair and a New Zealand accent.
```

* `cat people | grep Annabel >> clues.txt`

```
Annabel Sun	F	26	Hart Place, line 40
Oluwasegun Annabel	M	37	Mattapan Street, line 173
Annabel Church	F	38	Buckingham Place, line 179
Annabel Fuglsang	M	40	Haley Street, line 176
```

* `cd streets`
* `cat Hart_Place`
* `head -n 40 Hart_Place`
* `man cat`
* `cat -n Hart_Place`
* `cat -n Hart_Place | grep 40`
* `cat -n Hart_Place | grep " 40"`
* `cat -n Buckingham_Place | grep " 179" >> ../clues.txt`

```
    40	SEE INTERVIEW #47246024
   179	SEE INTERVIEW #699607
```

* `ls ..`
* `cd ../interviews`
* `cat interview-47246024`
* `cat interview-699607 >> ../clues.txt` 


```
Interviewed Ms. Church at 2:04 pm.  Witness stated that they did not see anyone they could identify as the shooter, that they ran away as soon as the shots were fired.

However, they report seeing the car that fled the scene. Describes it as a blue Honda, with a license plate that starts with "L337" and ends with "9"
```

* `cd ..`
* `cat vehicles | grep "L337"`
* `grep "Honda" vehicles`

```
10116  cat vehicles | grep -A 5 "L337"
10117  cat vehicles | grep -A 5 "L337" | grep -A 4 "Blue"
10118  cat vehicles | grep -A 5 "L337" | grep -A 4 -B 1 "Blue"
10119  cat vehicles | grep -A 5 "L337" | grep -A 4 "Blue" | grep -B 1 "6'"
10120  cat vehicles | grep -A 5 "L337" | grep -A 4 "Honda" |  grep -A 3 "Blue" |  grep -B 1 "6'"
```
* `cat vehicles | grep -A 5 "L337" | grep -A 4 "Honda" | grep -A 3 "Blue" | grep -B 1 "6'"`

* `cat AAA Delta_Skymiles Terminal_City_Library Museum_of_Bash_History | grep "Jeremy Bowers"`
* `cd ..`
* `cat people | grep "Jeremy Bowers"`
* `cat people | grep -e "Erika Owens" -e "Joe Germuska" -e "Jeremy Bowers" -e "Jacqui Maher" >> clues.txt`
* `cd streets`

```
cat -n Plainfield_Street | grep " 275" >> ../clues.txt
cat -n Trapelo_Street | grep " 98" >> ../clues.txt
cat -n Plainfield_Street | grep " 275" >> ../clues.txt
cat -n Dunstable_Road | grep " 284" >> ../clues.txt
```

* `cd ../interviews`

```
cat interview-5455315
cat interview-5455315
cat interview-9620713
cat interview-29741223
```

Jeremy Bowers how could you! 😱

* `cd ../..`
* `history >> solution.txt`