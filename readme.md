# Genetic word match

This Python script defines a word: FRIEDRICHSHAGEN.
Then it defines 50 random strings of the same length.
The it starts a loop where each random string is evaluated based on how many characters match the original string.
From the best matched, new strings (children) are created and matched again. Once in a while, a mutation takes place to bring new possibilities in the pool.

```
target = "FRIEDRICHSHAGEN"
```

```
step 0, AVGYPLUSTVKEGTT, avg: 0.042666666666666665
step 0, NISMLXIQZTERGAE, avg: 0.042666666666666665
step 0, HAAEHFMBLKUADON, avg: 0.042666666666666665
step 0, LIKRLXIQZTTXQRQ, avg: 0.042666666666666665
step 0, HTMGPIRRCKUADON, avg: 0.042666666666666665
step 0, NISMLXILHBDYWHF, avg: 0.042666666666666665
step 0, FJDTWAVNHGJCTUH, avg: 0.042666666666666665
step 0, IHJORFIEOXERGAE, avg: 0.042666666666666665
step 0, IHJORAOCVZZAIEC, avg: 0.042666666666666665
step 0, IHJORAOCVZZAVOY, avg: 0.042666666666666665
step 0, OTURRCKBLPRJCDZ, avg: 0.042666666666666665
.
.
step 2242, FRIEDRICHSHAMEN, avg: 0.8237037037037038
step 2242, FRIEORICRRHAREN, avg: 0.8237037037037038
step 2242, FRIEDRICRSHAYEN, avg: 0.8237037037037038
step 2242, FRIEDXIARRHAYEN, avg: 0.8237037037037038
step 2242, FRIEDRICRRHAGEN, avg: 0.8237037037037038
step 2242, FRIEDRICRSHAREN, avg: 0.8237037037037038
step 2242, FRIEDRICHSHAGTN, avg: 0.8237037037037038
step 2242, FRIEDRECHSHAREN, avg: 0.8237037037037038
step 2242, FRIEDRICHYHAGEN, avg: 0.8237037037037038
step 2242, FRINDRICRRHAREN, avg: 0.8237037037037038
step 2242, FRIEDRIMHSHAREN, avg: 0.8237037037037038
step 2242, FRIEDRICHSHAGEN, avg: 0.8237037037037038
```
