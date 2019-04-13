# mod10_demo
Demo of mod10 used in M+K=C-K=M cryptography
script to demonstrate mod10 Message + Key = Ciphertext and reverse
shows it horizontally and vertically, uses terminal columns and lines
to limit output to reasonable amounts.

The repository includes a screenshot of the script run within Linux

# dictionary_gen
Dictionary Generator in Python used as part of M+K=C cryptography

'dictionary', in this context refers to a custom assignment of letters to numbers, for cryptography
That is, rather than a=1, b=2, a custom dictionary assigns random values to a range of letters, with the potential letters always being a subset of the larger selection.  In this case, 00-99 for only 30 letters.

These are then used as part of a M+K=C (message+key=cipher) process, ideally utilizing a one time pad as key source.
