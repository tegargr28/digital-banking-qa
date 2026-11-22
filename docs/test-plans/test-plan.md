# Test Plan — Digital Banking (ParaBank)

## 1. Objective
Validate the observable behavior of the ParaBank demo's core banking workflows.

## 2. In Scope
- Public homepage availability and navigation.
- Authentication and account workflows after exploration.
- Transfer and transaction workflows using synthetic demo data.
- UI regression checks.

## 3. Out of Scope
- Real banking transactions.
- Production database validation.
- Load, stress, penetration, or destructive security testing against the public demo.

## 4. Test Approach
Manual exploratory testing first, followed by documented test cases and selected Selenium automation.

## 5. Environment
- Application: https://parabank.parasoft.com/parabank/index.htm
- Browser: Chrome (initial target)
- Automation: Python + Selenium + Pytest

## 6. Entry Criteria
Application is reachable; test data and test account behavior have been documented.

## 7. Exit Criteria
Planned tests have execution evidence, defects are documented, and limitations are stated.

## 8. Risks
The public demo may be reset, unavailable, or change without notice. Do not use personal or financial data.
