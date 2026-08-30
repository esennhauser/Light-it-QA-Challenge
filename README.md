# Light-it QA Automation Challenge

UI automation framework for the **Medical Appointment System** QA challenge.

The project uses **Python, Behave, Playwright and Allure** to automate critical patient appointment flows.

## Scope

The automation covers the following scenarios:

### 1. Patient Login

Validates that a patient can successfully authenticate and access the dashboard.

### 2. Book Appointment

Validates that a patient can access the appointment booking form and that all required UI components are displayed. The appointment is **not submitted**, avoiding unnecessary test data creation in the environment.

### 3. Reschedule Appointment

Validates that a patient can:

1. Access the appointments page.
2. Select an existing appointment.
3. Open the reschedule form.
4. Select a different date.
5. Select a different available time.
6. Confirm the reschedule.
7. Receive the success message.
8. See the updated appointment in the UI.

The last assertion currently fails because the application does not refresh/update the appointment card after a successful reschedule.

This is an **application defect intentionally detected by the automated test**.

---

## Tech Stack

* Python
* Behave
* Playwright
* Allure
* python-dotenv
* Docker

## Project Structure

```text
.
├── driver/
│   └── driver.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── appointments_page.py
│   └── book_appointment_page.py
├── tests/
│   └── features/
│       ├── environment.py
│       ├── login.feature
│       ├── reschedule_appointment.feature
│       ├── book_appointment.feature
│       └── steps/
│           ├── login_steps.py
│           ├── reschedule_appointment_steps.py
│           └── book_appointment_steps.py
├── behave.ini
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.txt
```

## Design

The project follows the **Page Object Model (POM)** pattern.

Page-specific locators and interactions are encapsulated inside page classes, while Behave step definitions describe the business behavior.

Example:

```text
Feature
   ↓
Step Definition
   ↓
Page Object
   ↓
Playwright
   ↓
Application
```

This keeps test scenarios readable and reduces duplication.

---

# Setup

## Prerequisites

For local execution:

* Python 3.x
* Playwright
* Allure CLI

For Docker execution:

* Docker

## 1. Clone the repository

```bash
git clone <repository-url>
cd Light-it-QA-Automation-Challenge
```

## 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Playwright browsers

```bash
playwright install
```

## Environment Variables

Create a `.env` file or use `.env.example` in the project root:

```env
MEDAPPOINT_EMAIL=your_email
MEDAPPOINT_PASSWORD=your_password
MEDAPPOINT_URL=https://light-it-qa-challenge.vercel.app
```

Credentials are loaded using `python-dotenv`.

The `.env` file is excluded from version control.

---

# Running the Tests

## Local execution

Run all scenarios:

```bash
behave
```

Run a specific feature:

```bash
behave tests/features/login.feature
```

Run all features:

```bash
behave tests/features/
```

---

# Allure Reports

The framework is configured to generate Allure results automatically.

Each Behave step includes a UI screenshot captured after the step completes.

Run:

```bash
behave
```

This generates:

```text
allure-results/
```

Generate the HTML report:

```bash
allure generate allure-results -o allure-report --clean
```

The generated report is a static HTML report and does not require the Allure server to be running.

Open:

```bash
allure open allure-report
```

The report contains screenshots associated with each executed step, which makes UI failures easier to investigate.

---

# Docker

The project can also be executed inside Docker to provide a consistent test environment.

Build the image:

```bash
docker build -t light-it-qa-challenge .
```

Run the tests:

```bash
docker run --rm \
  --env-file .env \
  light-it-qa-challenge
```

The Docker image contains the Python dependencies and Playwright browser required to execute the test suite.

---

# Test Results

Current automated coverage:

| Feature          | Scenario                                        | Result |
| ---------------- | ----------------------------------------------- | ------ |
| Login            | Patient successfully logs in                    | PASS   |
| Book Appointment | Patient can access booking form                 | PASS   |
| Reschedule       | Patient successfully reschedules an appointment | FAIL   |

### Known failing test

The reschedule scenario intentionally fails on the final assertion.

After confirming a reschedule:

```text
Confirm
   ↓
Success message
   ↓
Appointment card
```

The application displays the success message, but the appointment card continues displaying the previous date/time.

Refreshing the page causes the updated appointment to appear.

The test therefore correctly identifies the UI synchronization/update defect instead of hiding it by performing a browser refresh.

---

# Future Improvements

Potential improvements for a production-grade framework include:

* API-level setup and teardown for deterministic test data.
* Better test data management.
* Additional negative and validation scenarios.
* Cross-browser execution.
* Parallel execution.
* CI/CD integration.
* Automatic publishing of Allure reports.
* API/database validation for backend consistency.
* Dedicated test IDs in the application for critical UI elements.
