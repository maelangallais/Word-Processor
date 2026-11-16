# 📝 Word-Processor

A lightweight, custom **text editor / word processor** built in MicroPython for the **NumWorks** calculator.

---

## ✨ Features

- **Full Calculator Keyboard Mapping**: Every key from `a` to `!` is mapped for text entry.
- **Multi-Layer Keyboards (5 Layers)**: Switch character layers on the fly, with cursor color/width indicating the active layer:
  - **Default**: Lowercase letters (`a`–`z`), space, `,`, and `.`.
  - **`Alpha`**: Uppercase letters (`A`–`Z`), space, `?`, and `!`.
  - **`Shift`**: Digits (`0`–`9`), math operators, brackets, and symbols.
  - **`X,N,T`**: Extended symbols and punctuation (`@`, `#`, `&`, `≠`, `≈`, `→`, `∞`, `°`, `±`, etc.).
  - **`Var` (Accented Characters)**: Dedicated layer for accented characters (`à`, `â`, `ä`, `é`, `è`, `ê`, `ë`, `î`, `ï`, `ô`, `ö`, `ù`, `û`, `ü`, `ÿ`, `ç`).
- **Character Map Preview (`×10ˣ`)**: Press **`×10ˣ`** to open a visual on-screen keypad map showing every character available in the currently active layer, along with key labels for layer switches (`A-Z`, `1-9`, `@&#`, `à-é`), `col` (shown in the next color), `map`, `last`, Space, Backspace, and Enter. Press **`×10ˣ`** again to exit the preview.
- **Insert Last Character (`Ans`)**: Press **`Ans`** to re-insert the last typed character at the cursor position with the currently selected text color.
- **Smart Key Repeat**: Pressing a key triggers an immediate action; holding it for more than `0.5s` enables continuous repeat for smoother typing.
- **Smart Cursor Navigation**: Move across text with directional arrows; cursor column position is remembered across line changes and constrained to existing text boundaries.
- **Color Customization**: Cycle through 12 text colors on the fly (indicated by the bottom bar).

---

## ⌨️ Controls

- **Directional Arrows** : Move cursor (`Left` / `Right` / `Up` / `Down`).
- **Shift / Alpha / X,N,T / Var** : Toggle keyboard character layers (digits & math / uppercase / extended symbols / accented characters).
- **×10ˣ** : Open/close the character map preview for the active layer.
- **Ans** : Insert the last used character.
- **Toolbox** : Cycle text color.
- **Backspace** : Delete character.
- **EXE** : Insert new line.

*Note: Documents are held in memory during the session and are not saved to persistent storage.*

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `ion`, `time`, `math`).

---

## 🛠️ Details

The project has been created the November 13 of 2023.
