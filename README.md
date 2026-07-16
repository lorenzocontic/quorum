# QR Business Card Generator

Generate QR business cards from contact information.

This demo project creates QR payloads, prepares export jobs and simulates saving cards as PNG and SVG files.

---

## Workflow

```
Contact
      │
      ▼
 QR Payload
      │
      ▼
 Card Builder
      │
      ▼
PNG Export   SVG Export
```

---

## Output

```
Creating QR Card...

Name : Emily Carter
Company : Bright Studio

PNG exported
SVG exported

Done.
```

---

## Included Components

- Contact model
- QR payload builder
- Export manager
- Card template
- Sample contacts

Run:

python app.py
