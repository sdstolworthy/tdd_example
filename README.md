# TDD Mobbing Exercise

We are creating a palindrome identification product.

## User Story

As a user of the palindrome package, I want to be able to correctly identify
alphanumeric palindromes (both words and numbers).

### Acceptance Criteria

- [ ] A word that reads the same backwards and forwards is a palindrome
- [ ] A number that reads backwards and forwards the same, ignoring any decimals or commas, is a palindrome
- [ ] Case should be ignored
- [ ] Single-character entities are not palindromes

### Examples

Both racecar and RAcECar are palindromes
Penguin and tux are not
9009 and 900.9 are palindromes
a single-letter word is not a palindrome
