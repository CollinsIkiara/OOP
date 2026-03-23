# OOP Concepts

A collection of Python scripts demonstrating core **Object-Oriented Programming** (OOP) principles including **_abstraction_**, **_inheritance_**, **_encapsulation_**, and **_polymorphism_**.

---

## Table of Contents

- [Overview](#overview)
- [Files](#files)
  - [Discount Calculator](#1-discount_calculatorpy)
  - [Player Interface](#2-player_interfacepy)
  - [Media Catalogue](#3-media_cataloguepy)
  - [Game Character Stats Tracker](#4-game_character_stats_trackerpy)
  - [Salary Tracker](#5-salary_trackerpy)
- [OOP Concepts Covered](#oop-concepts-covered)
- [Requirements](#requirements)
- [Usage](#usage)

---

## Overview

These scripts are standalone Python examples designed to illustrate how OOP concepts are applied in real-world-style scenarios. Each file is self-contained and can be run independently.

---

## Files

### 1. `Discount_Calculator.py`

**Concept:** Abstraction · Inheritance · Polymorphism

A flexible discount engine for an e-commerce platform. It models a product and applies various discount strategies to find the best price for a user.

**Classes:**

| Class | Description |
|---|---|
| `Product` | Represents an item with a `name` and `price`. |
| `DiscountStrategy` *(ABC)* | Abstract base class that enforces `is_applicable()` and `apply_discount()` on all strategies. |
| `PercentageDiscount` | Applies a percentage-based discount (capped at 70%). |
| `FixedAmountDiscount` | Deducts a fixed amount, only if it doesn't undercut the product by more than 10%. |
| `PremiumUserDiscount` | Grants a 20% discount exclusively to `"premium"` tier users. |
| `DiscountEngine` | Accepts a list of strategies and calculates the lowest applicable price. |

**How it works:**

The `DiscountEngine` iterates over all provided strategies, checks applicability, collects all resulting prices, and returns the minimum.

**Example output:**
```
Best price for Wireless Mouse for Premium user: $40.00
```

---

### 2. `Player_Interface.py`

**Concept:** Abstraction · Inheritance

Defines a game player system using an abstract base class. The `Player` class manages movement and path tracking, while subclasses define specific move sets and leveling behavior.

**Classes:**

| Class | Description |
|---|---|
| `Player` *(ABC)* | Holds movement state (`position`, `path`, `moves`) and implements `make_move()`. Declares abstract method `level_up()`. |
| `Pawn` | Concrete player that starts with 4 cardinal moves and gains 4 diagonal moves upon leveling up. |

**How it works:**

`make_move()` picks a random move from the available list and updates the player's position and path history. The `level_up()` method in `Pawn` expands the move set to include diagonals.

---

### 3. `Media_Catalogue.py`

**Concept:** Inheritance · Exception Handling · Custom Exceptions

A media library system that stores and organises `Movie` and `TVSeries` entries, with strict input validation and a custom exception type.

**Classes:**

| Class | Description |
|---|---|
| `MediaError` | Custom exception that carries the offending object alongside an error message. |
| `Movie` | Represents a film with a `title`, `year`, `director`, and `duration`. Validates all fields on creation. |
| `TVSeries` | Extends `Movie` with `seasons` and `total_episodes`. Inherits all movie validations. |
| `MediaCatalogue` | Stores media items and provides filtered views (`get_movies()`, `get_tv_series()`). Only accepts `Movie` instances or subclasses. |

**How it works:**

Items are added via `catalogue.add()`. If an invalid object type is passed, a `MediaError` is raised. `ValueError` is raised for any field that fails validation. The `__str__` method produces a formatted, categorised display of the full catalogue.

**Example output:**
```
Media Catalogue (4 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
2. Inception (2010) - 148 min, Christopher Nolan
=== TV SERIES ===
1. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
2. Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```

---

### 4. `Game_Character_Stats_Tracker.py`

**Concept:** Encapsulation · Properties

Tracks the stats of a game character — health, mana, and level — using Python properties to enforce safe value boundaries.

**Class:**

| Class | Description |
|---|---|
| `GameCharacter` | Manages a character's `name`, `health` (0–100), `mana` (0–50), and `level`. Exposes stats via `@property` with getters and validated setters. |

**How it works:**

- `health` and `mana` setters clamp values to their valid range instead of raising errors, ensuring the character state is always valid.
- `level_up()` increments the level and resets both health and mana to their maximum values.

**Example output:**
```
Name: Kratos
Level: 1
Health: 100
Mana: 50
...
Kratos leveled up to 2!
```

---

### 5. `Salary_Tracker.py`

**Concept:** Encapsulation · Properties · Input Validation

Models an employee record system with enforced business rules around promotions and salary updates using properties and setters.

**Class:**

| Class | Description |
|---|---|
| `Employee` | Stores an employee's `name`, `level`, and `salary`. Uses a class-level `_base_salaries` dict to define valid levels and their minimum pay. |

**How it works:**

- The `level` setter prevents demotions and validates the new level against the predefined tiers: `trainee → junior → mid-level → senior`.
- The `salary` setter ensures a new salary exceeds the base minimum for the current level.
- `__repr__` provides a developer-friendly string, while `__str__` provides a user-friendly one.

**Example output:**
```
Charlie Brown: trainee
Base salary: $1000
'Charlie Brown' promoted to 'junior'.
Salary updated to $2000.
```

---

## OOP Concepts Covered

| Concept | Files |
|---|---|
| **Abstraction** (ABC) | `Discount_Calculator.py`, `Player_Interface.py` |
| **Inheritance** | `Media_Catalogue.py`, `Player_Interface.py`, `Discount_Calculator.py` |
| **Encapsulation** (Properties) | `Game_Character_Stats_Tracker.py`, `Salary_Tracker.py` |
| **Polymorphism** | `Discount_Calculator.py` |
| **Custom Exceptions** | `Media_Catalogue.py` |
| **Input Validation** | `Media_Catalogue.py`, `Salary_Tracker.py`, `Game_Character_Stats_Tracker.py` |

---

## Requirements

- Python 3.10+  
  *(Uses `list[DiscountStrategy]` type hint syntax introduced in 3.9, and `match`-compatible patterns)*

No third-party libraries are required. All files use the Python standard library only.

---

## Usage

Each script can be run directly from the terminal:

```bash
python Discount_Calculator.py
python Player_Interface.py
python Media_Catalogue.py
python Game_Character_Stats_Tracker.py
python Salary_Tracker.py
```

Each file includes example usage at the bottom of the script under the `if __name__ == '__main__':` block or as top-level statements, so you can see output immediately on execution.
