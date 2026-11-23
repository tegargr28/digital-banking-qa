# Digital Banking QA

End-to-end Quality Assurance portfolio project using the public ParaBank demo application.

## Scope
- Manual testing: test plan, scenarios, test cases, defect reports.
- UI automation: Python, Selenium WebDriver, Pytest, Page Object Model.
- API testing: Postman collection (to be added after API exploration).
- Database testing: local synthetic dataset and SQL exercises. No access to ParaBank's production database is assumed.
- CI: GitHub Actions and Jenkins.
- Containerization: Docker Compose for a local Jenkins controller.

## Application Under Test
ParaBank demo: https://parabank.parasoft.com/parabank/index.htm

Use only the public demo with non-sensitive, synthetic test data. Do not enter real banking credentials or personal information, and do not perform load or security testing against the public service.

## Local setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
pytest -m smoke
```

The first Selenium run may download/resolve a compatible browser driver through Selenium Manager. Google Chrome must be installed.

## Run headless
```powershell
$env:HEADLESS="true"
pytest -m smoke
```

## Reports
```powershell
pytest -m smoke --html=reports/report.html --self-contained-html
```

## Jenkins
A starter `Jenkinsfile` is included. Run Jenkins locally with:
```powershell
docker compose up -d
```
Open http://localhost:8080 and complete the initial Jenkins setup. Install/configure a Python-capable agent and ensure Chrome/ChromeDriver are available on that agent before running browser tests. The included pipeline assumes a Linux agent with Python, Google Chrome, and Git installed; adjust the agent label to match your environment.

## Project status
Learning and demonstration portfolio. All results are recorded only after real execution; unexecuted tests stay **Not Run** and are never reported as passed.

- **Phase 0 — Audit:** complete. The repository started as a scaffold; gaps were catalogued before any changes.
- **Phase 1 — Automation foundation:** merged via PR #1. Config-driven headless driver factory, automatic failure screenshots, Jenkins headless default, additional pytest markers. The QA master workbook `test-cases.xlsx` (Requirements, Test Scenarios, 22 Test Cases, RTM, Bug Reports, Test Execution, API and SQL Test Cases, Test Summary) is built on the project template. Five ParaBank REST API checks were executed for real; the UI smoke test passed in GitHub Actions CI after the driver fix.
- **Phase 2 — Documentation and login automation:** Test Strategy, Risk Assessment, and Test Environment documents added (`docs/`); Selenium login coverage (valid and invalid credentials) added under `automation/`. The login suite found a real defect — **BUG-001**: the ParaBank web login accepts an invalid password (the API rejects it correctly). The defect is recorded in the workbook and the automation test is marked `xfail` against it.
- **Phase 3 — API testing:** Postman collection for the ParaBank REST API added (`api-testing/`), mirroring the workbook's API cases. All 8 designed API cases have been executed for real (EXEC-001 and EXEC-006), including a transfer whose balance changes were verified to the cent.
- **Phase 4 — SQL testing and full manual UI execution:** a local synthetic dataset (`database-testing/`, SQLite, fictional data) backs the 6 SQL cases — all executed and passing (EXEC-007). A full manual browser session then executed the remaining 19 UI cases (EXEC-008): 14 passed and 5 failed, surfacing four more genuine defects — **BUG-002** (zero/negative transfer amounts accepted; a negative amount reverses the money flow), **BUG-003** (transfer above the balance accepted, driving the account to -$1000.00), **BUG-004** (double submission posts a transfer twice), **BUG-005** (empty amount returns a generic internal error instead of a validation message). Workbook totals: 22 UI cases executed (16 Pass, 6 Fail), 8 API cases Pass, 6 SQL cases Pass, 5 defects recorded — all from real executions.
- **Phase 5 — Transfer automation:** Selenium coverage for the valid-transfer case (TRF-TC-001) added under `automation/` (Accounts Overview and Transfer Funds page objects), asserting the exact balance deltas on both accounts.
- **Known coverage gaps (deliberate):** Bill Payment has a scenario but no detailed cases yet; Update Contact Info, Request Loan, and Open New Account have no scenarios/cases — business rules will be observed in the application before cases are designed, never assumed.

See `docs/interview-prep.md` for STAR-format summaries of the key findings.

See `docs/test-strategy.md` for scope and approach, and the workbook's Test Execution sheet for the execution record behind every reported status.
