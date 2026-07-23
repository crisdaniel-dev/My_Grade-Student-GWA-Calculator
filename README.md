# My_Grade — Student GWA Calculator

This is a simple Python program I made to compute my GWA based on our BSIS curriculum here in CTU. I made this during summer break. I was bored, so I decided to turn something I usually compute manually into an actual program using my learnings during my first year and this program has more selection structure and I did not use loops or some ideas that will make this line of code shorter. It is because I challenged myself to just make it hardcoded and to put my understanding into one program using selection structure and try except ValueError.

## What it does

- Shows the subjects per year and semester (from our curriculum)
- Lets you input your grades and computes your GWA automatically

## How I made it

I used nested if/elif statements to handle the year level, semester, and subjects. It's a long program (more than 1000 lines) because I listed all subjects from 1st year to 4th year, but the logic is simple: multiply each grade by its units, add them up, then divide by total units. That's basically how GWA works. I also added remarks based on the computed average.

## Bugs I found and fixed

While testing my own code, I noticed a problem: most of my `int(input())` lines didn't have error handling. So if someone typed a letter instead of a number, the program would just crash. Only my very first input had a try/except.

I went back and added try/except to all of them so the program won't crash and will just show an error message instead. I also fixed a small mistake in my year level checker — it allowed 0 and 5 to pass through even though valid years are only 1 to 4.
## Tools used

Python 3, no external libraries.

## Author

Crisdaniel M. Inot — BSIS 1st year, Cebu Technological University (Main Campus)
