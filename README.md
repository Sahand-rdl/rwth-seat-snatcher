# RWTH Seat Snatcher 💺

An automated seat-booking assistant for the RWTH Aachen Library system, built with Python and Selenium.

## ⚠️ Ethical Use & Disclaimer
This project was developed for **educational and personal productivity purposes**. It serves as a practical demonstration of browser automation and credential management. 
- **Fair Play**: This tool is designed to assist the user in their existing manual booking process, not to gain an unfair advantage or disrupt the availability of resources for others.
- **Responsibility**: The user is responsible for ensuring their use of this tool aligns with university IT policies and terms of service.
- **Educational Value**: Created to explore Selenium, headless browser interactions, and secure environment-based configuration.

## Features
- **Headless Automation**: Runs silently in the background.
- **Secure Configuration**: Uses `.env` files to protect personal data and credentials.
- **Smart Form Handling**: Automatically navigates the HSZ booking system, handles radio selections, and form submissions.

## Setup
1. Copy `.env.example` to `.env`.
2. Fill in your personal details (Matriculation number, etc.) in the `.env` file.
3. Run the snatcher:
   ```bash
   python main.py
   ```

## Requirements
- Selenium
- Geckodriver (for Firefox) or Chromedriver
