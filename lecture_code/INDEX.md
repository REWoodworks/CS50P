# Lecture Code Index

Look up the pattern, then click to jump to the example. Updated as new lectures land.

`L0`–`L6` = the "Lecture N …" files in this folder. "Short" = a file in `Shorts Code/`.

## Input, strings, numbers
- Save input in a variable: [L0 #02](Lecture%200%20Functions%20and%20Variables%20Code.py#L16)
- f-string: [L0 #12](Lecture%200%20Functions%20and%20Variables%20Code.py#L112)
- `.strip()` / `.title()` / chaining them: [L0 #13](Lecture%200%20Functions%20and%20Variables%20Code.py#L121), [L0 #15](Lecture%200%20Functions%20and%20Variables%20Code.py#L147)
- `int()` / `float()` on input: [L0 #19](Lecture%200%20Functions%20and%20Variables%20Code.py#L189), [L0 #21](Lecture%200%20Functions%20and%20Variables%20Code.py#L208)
- Rounding, `:,` and `:.2f` formatting: [L0 #23](Lecture%200%20Functions%20and%20Variables%20Code.py#L230), [L0 #26](Lecture%200%20Functions%20and%20Variables%20Code.py#L269)
- More string methods and slicing: [Short: string methods](Shorts%20Code/ex_2_string_methods_short.py), [Short: slicing](Shorts%20Code/ex_2_string_slicing_short.py)

## Functions and return
- Define and call a function: [L0 #29](Lecture%200%20Functions%20and%20Variables%20Code.py#L301)
- Parameters and defaults: [L0 #30](Lecture%200%20Functions%20and%20Variables%20Code.py#L312), [L0 #31](Lecture%200%20Functions%20and%20Variables%20Code.py#L324)
- `main()` pattern: [L0 #33](Lecture%200%20Functions%20and%20Variables%20Code.py#L353)
- Return a value: [L0 #34](Lecture%200%20Functions%20and%20Variables%20Code.py#L369)
- Return a True/False: [L1 #12](Lecture%201%20Conditionals%20Code.py#L158), [L1 #14](Lecture%201%20Conditionals%20Code.py#L191)
- Return vs. print (side effects): [Short: return values](Shorts%20Code/ex_0_return_values_short.py), [Short: side effects](Shorts%20Code/ex_0_side_effects_short.py)

## Conditionals
- `if` / `elif` / `else`: [L1 #03](Lecture%201%20Conditionals%20Code.py#L32), [L1 #04](Lecture%201%20Conditionals%20Code.py#L46)
- `and` / `or`: [L1 #05](Lecture%201%20Conditionals%20Code.py#L60), [L1 #08](Lecture%201%20Conditionals%20Code.py#L96)
- Chained comparison `90 <= x <= 100`: [L1 #09](Lecture%201%20Conditionals%20Code.py#L113)
- Even/odd with `%`: [L1 #11](Lecture%201%20Conditionals%20Code.py#L147)
- `match` / `case`: [L1 #17](Lecture%201%20Conditionals%20Code.py#L236), [L1 #18](Lecture%201%20Conditionals%20Code.py#L254)

## Loops
- `while` with a counter: [L2 #05](Lecture%202%20Loops%20Code.py#L46)
- `for` over a list / `range()`: [L2 #06](Lecture%202%20Loops%20Code.py#L56), [L2 #07](Lecture%202%20Loops%20Code.py#L64)
- Re-prompt loop with `continue` / `break`: [L2 #11](Lecture%202%20Loops%20Code.py#L94), [L2 #12](Lecture%202%20Loops%20Code.py#L106)
- Numbered list with `range(len(...))`: [L2 #16](Lecture%202%20Loops%20Code.py#L154)
- Nested loops (Mario square): [L2 #30](Lecture%202%20Loops%20Code.py#L317)

## Lists and dictionaries
- List indexes: [L2 #14](Lecture%202%20Loops%20Code.py#L135)
- Dict lookup / loop over a dict: [L2 #18](Lecture%202%20Loops%20Code.py#L171), [L2 #21](Lecture%202%20Loops%20Code.py#L212)
- List of dicts: [L2 #24](Lecture%202%20Loops%20Code.py#L251)
- Shorts: [lists](Shorts%20Code/ex_2_lists_short.py), [list methods](Shorts%20Code/ex_2_list_methods_short.py), [dicts](Shorts%20Code/ex_2_dictionaries_short.py), [dict methods](Shorts%20Code/ex_2_dictionary_methods_short.py), [tuples](Shorts%20Code/ex_2_tuples_short.py), [comprehensions](Shorts%20Code/ex_2_list_dictionary_comprehensions_short.py)

## Exceptions
- `try` / `except ValueError`: [L3 #03](Lecture%203%20Exceptions%20Code.py#L23)
- `try` / `except` / `else`: [L3 #05](Lecture%203%20Exceptions%20Code.py#L45)
- Retry loop: `while True` + `try` + `break`: [L3 #06](Lecture%203%20Exceptions%20Code.py#L57)
- Helper that returns once input is valid: [L3 #08](Lecture%203%20Exceptions%20Code.py#L90)
- `pass` in `except`: [L3 #10](Lecture%203%20Exceptions%20Code.py#L124)
- Shorts: [handling](Shorts%20Code/ex_3_handling_exceptions_short.py), [raising](Shorts%20Code/ex_3_raising_exceptions_short.py)

## Command-line arguments (`sys.argv`)
- Read `sys.argv[1]`: [L4 name0](Lecture%204%20Libraries.py#L73)
- Catch `IndexError`: [L4 name1](Lecture%204%20Libraries.py#L86)
- Check `len(sys.argv)`: [L4 name2](Lecture%204%20Libraries.py#L102)
- **Guard clauses with `sys.exit`** (lines.py pattern): [L4 name3](Lecture%204%20Libraries.py#L120)
- Loop over `sys.argv[1:]`: [L4 name4](Lecture%204%20Libraries.py#L138)

## Libraries and modules
- `random` (choice, randint, shuffle): [L4 generate0](Lecture%204%20Libraries.py#L2), [Short: random](Shorts%20Code/ex_4_random_short.py)
- `statistics`: [L4 average](Lecture%204%20Libraries.py#L60)
- pip package (cowsay): [L4 say0](Lecture%204%20Libraries.py#L155)
- `requests` + JSON: [L4 itunes0](Lecture%204%20Libraries.py#L185), [L4 itunes2](Lecture%204%20Libraries.py#L226), [Short: API calls](Shorts%20Code/ex_4_api_calls_short.py)
- Your own module: [L4 sayings0](Lecture%204%20Libraries.py#L249), [Short: modules](Shorts%20Code/ex_4_creating_modules_packages_short.py)
- `if __name__ == "__main__":`: [L4 sayings2](Lecture%204%20Libraries.py#L320)

## Testing
- `assert`: [L5 test_calculator2](Lecture%205%20Unit%20Tests.py#L91)
- pytest basics: [L5 test_calculator5](Lecture%205%20Unit%20Tests.py#L247)
- Separate test functions: [L5 test_calculator6](Lecture%205%20Unit%20Tests.py#L286)
- `pytest.raises`: [L5 test_calculator7](Lecture%205%20Unit%20Tests.py#L333)
- Return instead of print so it's testable: [L5 hello1](Lecture%205%20Unit%20Tests.py#L385)
- Test folder + `__init__.py`: [L5 test_hello1c](Lecture%205%20Unit%20Tests.py#L442)

## Files
- Write `"w"` / append `"a"`: [L6 names2](Lecture%206%20File%20Input%20Output.py#L43), [L6 names3](Lecture%206%20File%20Input%20Output.py#L58)
- `with open(...) as file:`: [L6 names4](Lecture%206%20File%20Input%20Output.py#L73)
- `readlines()` + `rstrip()`: [L6 names5](Lecture%206%20File%20Input%20Output.py#L87)
- **Loop over a file line by line** (lines.py pattern): [L6 names6](Lecture%206%20File%20Input%20Output.py#L102)
- Collect, then sort: [L6 names7](Lecture%206%20File%20Input%20Output.py#L115)
- `split(",")` and unpack `name, house`: [L6 students0](Lecture%206%20File%20Input%20Output.py#L145), [L6 students1](Lecture%206%20File%20Input%20Output.py#L159)
- Sort dicts with `key=` / `lambda`: [L6 students6](Lecture%206%20File%20Input%20Output.py#L253), [L6 students7](Lecture%206%20File%20Input%20Output.py#L277)
- `csv.reader` / `csv.DictReader`: [L6 students8](Lecture%206%20File%20Input%20Output.py#L307), [L6 students9](Lecture%206%20File%20Input%20Output.py#L340)
- `csv.writer` / `csv.DictWriter`: [L6 students10](Lecture%206%20File%20Input%20Output.py#L361), [L6 students11](Lecture%206%20File%20Input%20Output.py#L379)
- Images with Pillow: [L6 costumes](Lecture%206%20File%20Input%20Output.py#L397), [Short: Pillow](Shorts%20Code/ex_6_pillow_short.py)
- Shorts: [reading/writing](Shorts%20Code/ex_6_reading_and_writing_files.py), [csv](Shorts%20Code/ex_6_csv_short.py)
