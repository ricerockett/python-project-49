# Brain-games

[![Actions Status](https://github.com/ricerockett/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ricerockett/python-project-49/actions)
<a href="https://codeclimate.com/github/ricerockett/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/a67c4008414ace56d86c/maintainability" /></a>

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [prompt](https://pypi.org/project/prompt/)                                  | "Prompt and verify user input on the command line."     |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement"                 |

## DESCRIPTION
The project contains 5 logical games:

  1. brain-even 

     User gets a number and should answer "yes" if the number is even or
     "no" otherwise.
     
  3. brain-calc

     User gets a math expression and should find the result of 
     this expression.
     
  5. brain-gcd

     User gets a pair of numbers and should find the greatest 
     common divisor of given numbers.
     
  7. brain-progression

     User gets an arithmetic progression with one missed number and
     should find missed number.
     
  9. brain-prime

     User gets a number and answer "yes" if given number is prime or
     "no" otherwise.
     
Each game provides you with 3 question, you have to answer all 3 correctly 
in order to win. 1 wrong answer consider you loose.

## INSTALLATION INSTRUCTIONS
NOTE: To install and run project you should have poetry installed.

  1. Unpack the Brain-games repo archive that you downloaded. 

  2. To install the application, open a console, cd into repo root directory 
     and enter following sequence of commands:

       make install
       
       make build
       
       make package-install

     This will initialize poetry environment, building a package from source 
     code and further installation of the package.

## USAGE INSTRUCTIONS

  1. To start a game enter the name of the game into console e.g. brain-even.
## DEINSTALLATION INSTRUCTIONS
  
  1. To uninstall the application, open a console, cd into repo root directory 
     and enter following command:

       make package-uninstall


### Brain-even asciinema:
<a href="https://asciinema.org/a/637163" target="_blank"><img src="https://asciinema.org/a/637163.svg" /></a>

### Brain-calc asciinema:
<a href="https://asciinema.org/a/R0KTCyZn9Ygpaofm1fmsABzTM" target="_blank"><img src="https://asciinema.org/a/R0KTCyZn9Ygpaofm1fmsABzTM.svg" /></a>

### Brain-GCD asciinema:
<a href="https://asciinema.org/a/Jr2dgVHPkc5s6VJw4joSGmdnC" target="_blank"><img src="https://asciinema.org/a/Jr2dgVHPkc5s6VJw4joSGmdnC.svg" /></a>

### Brain-progression asciinema:
<a href="https://asciinema.org/a/3A3haOPKMP5o3nRslcYPH2CwY" target="_blank"><img src="https://asciinema.org/a/3A3haOPKMP5o3nRslcYPH2CwY.svg" /></a>

### Brain-prime asciinema:
<a href="https://asciinema.org/a/V7Oc7ApdwM4CBMVLqQHjAVPLc" target="_blank"><img src="https://asciinema.org/a/V7Oc7ApdwM4CBMVLqQHjAVPLc.svg" /></a>
