# Library Booking Automation (lrbuchung)

A Selenium-based automation tool for booking study spaces at the RWTH Aachen Library.

## Features
- **Environment-Based Config**: Securely handles personal data and credentials via `.env` files.
- **Automated Form Filling**: Handles complex web forms and radio selections automatically.

## Requirements
- Selenium
- Firefox (GeckoDriver) or Chrome (ChromeDriver)

## Setup
1. Copy `.env.example` to `.env`.
2. Fill in your personal details in the `.env` file.
3. Run the snatcher:
   ```bash
   python main.py
   ```
