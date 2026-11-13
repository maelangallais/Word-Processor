# 📝 Word-Processor

A lightweight, custom **text editor / word processor** built in MicroPython for the **NumWorks** calculator.

---

## ✨ Features

- **Full Calculator Keyboard Mapping**: Every key from `a` to `!` is mapped for text entry.
- **Multi-Layer Keyboards**: Switch character layers using **`Shift`**, **`Alpha`**, and **`X,N,T`** (press **`Var`** to preview available characters on the current layer).
- **Smart Key Repeat**: Pressing a key triggers an immediate action; holding it for more than `0.5s` enables continuous repeat for smoother typing.
- **Smart Cursor Navigation**: Move across text with directional arrows; cursor column position is remembered across line changes and constrained to existing text boundaries.
- **Color Customization**: Change text color on the fly.

---

## ⌨️ Controls

- **Directional Arrows** : Move cursor (`Left` / `Right` / `Up` / `Down`).
- **Toolbox** : Change text color.
- **Backspace** : Delete character.
- **EXE** : Insert new line.
- **Shift / Alpha / X,N,T** : Switch keyboard character layers.
- **Var** : Display character map for the active keyboard layer.

*Note: Documents are held in memory during the session and are not saved to persistent storage.*

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `ion`, `time`).

---

## 🛠️ Details

The project has been created the November 13 of 2023.
