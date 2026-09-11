# Fake News Headline Generator

A fun little Python script that generates random, absurd "breaking news" headlines by mixing random subjects, actions, and places/things.

## How it works

The script picks one random item from each of three lists — a **subject**, an **action**, and a **place or thing** — and stitches them together into a silly headline. It keeps generating new headlines until you tell it to stop.

## Requirements

- Python 3.x (no external libraries needed — only the built-in `random` module)

## Usage

Run the script from your terminal:

```bash
python fake_headline_generator.py
```

You'll see a random headline printed, followed by a prompt:

```
Do you want another headline? (yes/no)
```

- Type anything other than `no` (e.g. `yes`) to get another headline.
- Type `no` to exit the program.

## Example output

```
 BREAKING NEWS: A group of monkeys dances with a plate of samosa

Do you want another headline? (yes/no) yes

 BREAKING NEWS: Auto rickshaw driver from delhi celebrates during ipl match

Do you want another headline? (yes/no) no

Thanks for using the fake news headlines generator. Have a fun day
```

## Customizing

Want different headlines? Just edit the `subjects`, `actions`, and `places_or_things` lists in the script and add or remove entries — the generator will automatically pick from whatever's in the lists.

## Disclaimer

This project is purely for fun and satire. The headlines it generates are randomly assembled and not real news.

## License

