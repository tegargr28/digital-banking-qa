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
- **Phase 2 — Documentation and login automation:** Test Strategy, Risk Assessment, and Test Environment documents added (`docs/`); Selenium login coverage (valid and invalid credentials) added under `automation/`.
- **Next:** Postman API collection, local synthetic SQL dataset and queries, wider manual execution of the designed test cases, transfer-funds automation.

See `docs/test-strategy.md` for scope and approach, and the workbook's Test Execution sheet for the execution record behind every reported status.
