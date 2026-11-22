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
This repository is a starter scaffold. Test cases and automation must be expanded only after the application has been explored and actual behavior has been observed. Do not report unexecuted tests as passed.
