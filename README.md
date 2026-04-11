# BudgetYourBaby

## Overview
BudgetYourBaby is a dynamic web application engineered to aggregate, calculate, and manage localized pricing data for consumer goods. The application processes financial metrics and inventory data to provide real-time budget forecasting.

## Architecture & Data Flow
The application operates on a decoupled architecture, utilizing automated backend scripts to maintain a sanitized data store that the frontend client consumes.

* **Frontend Client:** Lightweight HTML/Vanilla JS interface that handles state management and dynamic DOM updates based on user interaction.
* **Data Store:** State is maintained via `products.json`, acting as a static API endpoint for the client.
* **Backend Automation:** A Python pipeline (`update_prices.py`) orchestrated by shell scripts (`run_update.sh`) handles data acquisition and synchronization, ensuring the primary data store remains current without manual intervention.

## Technology Stack
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Backend/Processing:** Python 3
* **Automation:** Bash / Shell Scripting
* **Data Storage:** JSON

## Threat Model & Security Considerations
This project was developed with a defensive mindset, analyzing potential attack vectors inherent to financial data processing applications.

### 1. Client-Side Manipulation (DOM/State)
* **Vector:** The application relies on client-side JavaScript for budget calculations. A malicious actor could manipulate local state variables or DOM elements via the browser console to force negative pricing values, potentially causing integer underflows or logic bypasses if this data were submitted to a backend processing server.
* **Mitigation Strategy:** In a fully integrated production environment involving user accounts, all financial calculations must be re-verified server-side before database commits. 

### 2. External Data Ingestion / Supply Chain
* **Vector:** The `update_prices.py` automation script processes external data to update the `products.json` store. If the upstream data source is compromised or manipulated to include malicious payloads (e.g., XSS payloads within product titles), the script could blindly ingest and serve this to the frontend.
* **Mitigation Strategy:** Implementation of strict input validation and sanitization within the Python pipeline before committing any external strings to the JSON data store.

### 3. Access Control (Beta Environment)
* **Vector:** The repository includes a parallel `/beta/` directory containing unreleased features and duplicate data stores. Insecure direct object reference (IDOR) or forced browsing could allow unauthorized users to access staging environments, potentially leaking future business logic or unstabilized code.
* **Mitigation Strategy:** Enforce strict server-level routing rules and authentication checks to isolate beta environments from the production namespace.

## Deployment
The application is structured for deployment via static hosting platforms (e.g., GitHub Pages), utilizing continuous integration pipelines to execute the automated price update scripts.
