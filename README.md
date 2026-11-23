# Digital Banking QA Portfolio

[![QA Smoke Tests](https://github.com/tegargr28/digital-banking-qa/actions/workflows/qa-smoke.yml/badge.svg)](https://github.com/tegargr28/digital-banking-qa/actions/workflows/qa-smoke.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Pytest](https://img.shields.io/badge/Pytest-automation-orange)

End-to-end Quality Assurance portfolio built on the **ParaBank public demo** banking application. It covers the full QA cycle — requirements, test design, manual execution, defect reporting, API testing, SQL testing, UI automation, and CI — with **every result backed by a real execution**. Nothing in this repository is fabricated: unexecuted tests stay *Not Run*, and all data is fictional.

**Author:** Tegar · **Application under test:** [ParaBank demo](https://parabank.parasoft.com/parabank/index.htm)

---

## Results at a glance

| Area | Result |
|---|---|
| Requirements covered | 11 (FR-001..FR-011), all validated by executed tests |
| Test scenarios | 13 (SCN-001..SCN-013) |
| UI test cases executed | **33** — 23 Pass, 10 Fail |
| API test cases executed | **8** — all Pass |
| SQL test cases executed | **6** — all Pass |
| Defects found | **8 genuine defects** — 3 Critical, 3 High, 2 Low (all documented, status Open) |
| Execution records | 10 sessions (EXEC-001..EXEC-010) with evidence |
| Automated tests in CI | 4 Selenium tests, green on every merge to `main` |

Full detail lives in the QA master workbook: [`test-cases.xlsx`](test-cases.xlsx) (Requirements, Scenarios, Test Cases, RTM, Bug Reports, Test Execution, API & SQL Cases, Summary).

## Skills demonstrated

| Skill | Evidence in this repository |
|---|---|
| Test design | 13 scenarios and 47 test cases (positive, negative, boundary) traced to requirements in the RTM |
| Manual testing | Full execution of all 33 UI cases across 9 banking features, recorded in EXEC-001..EXEC-010 |
| Defect reporting | 8 reproducible defect reports with steps, expected vs actual results, severity and priority |
| API testing | Postman collection for the ParaBank REST API; transfers verified by exact balance changes |
| SQL / database testing | Local synthetic banking dataset (SQLite) with integrity, reconciliation and duplicate checks |
| Test automation | Python + Selenium + Pytest, Page Object Model, headless Chrome, failure screenshots |
| CI/CD | GitHub Actions pipeline on every pull request; merges only on green; HTML + JUnit reports as artifacts |
| Documentation | SRS, Test Strategy, Test Plan, Automation Guide, CI/CD and Troubleshooting guides |

## Key findings — defects discovered

| ID | Severity | Finding |
|---|---|---|
| BUG-001 | Critical | Web login accepts an **invalid password** and opens the Accounts Overview (the REST API rejects it correctly) |
| BUG-006 | Critical | Bill Pay reports "successful" but the payment is **never posted** — no balance change, no activity entry, no funds check |
| BUG-003 | Critical | Transfer **above the account balance** is accepted, driving the account to −$1,000.00 |
| BUG-002 | High | Zero and **negative** transfer amounts are accepted; a negative amount reverses the money flow |
| BUG-004 | High | Double-clicking Transfer **posts the payment twice** |
| BUG-007 | High | Update Contact Info **always fails** with a generic error; changes are never saved |
| BUG-005 | Low | Empty transfer amount returns a generic internal error instead of a validation message |
| BUG-008 | Low | Empty loan amount returns the same generic internal error instead of validation |

Reproduction steps and evidence for each defect: workbook `test-cases.xlsx`, *Bug Reports* sheet. Interview-ready summaries: [`docs/interview-prep.md`](docs/interview-prep.md).

## Repository map

| Path | Contents |
|---|---|
| `test-cases.xlsx` | QA master workbook — the single source for requirements, cases, defects, executions |
| `automation/` | Selenium UI tests (Page Object Model): homepage, login, transfer |
| `api-testing/` | Postman collection + API testing notes |
| `database-testing/` | Synthetic SQL dataset, queries, and the SQL test runner |
| `docs/` | SRS, strategy, plan, automation, CI/CD, troubleshooting, interview prep |
| `.github/workflows/` | GitHub Actions pipeline (`qa-smoke.yml`) |
| `Jenkinsfile`, `docker-compose.yml` | Jenkins alternative pipeline and local controller |

## Quick start (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -m smoke
```

Headless run (as in CI) and HTML report:

```powershell
$env:HEADLESS="true"
pytest -m smoke --html=reports/report.html --self-contained-html
```

Google Chrome must be installed; Selenium Manager resolves the matching driver on first run. Configuration is environment-driven — see `.env.example`. Only the published public demo account and fictional data are used; never enter real banking credentials, and do not run load or security testing against the public service.

## Documentation index

| Document | Purpose |
|---|---|
| [`docs/requirements-specification.md`](docs/requirements-specification.md) | Functional requirements FR-001..FR-011 and their validation status |
| [`docs/test-strategy.md`](docs/test-strategy.md) | Overall test approach, levels, and tools |
| [`docs/test-plans/test-plan.md`](docs/test-plans/test-plan.md) | Scope, approach, and entry/exit criteria |
| [`docs/test-scenarios/test-scenarios.md`](docs/test-scenarios/test-scenarios.md) | Index of scenarios SCN-001..SCN-013 (workbook is authoritative) |
| [`docs/risk-assessment.md`](docs/risk-assessment.md) | Product and project risks |
| [`docs/test-environment.md`](docs/test-environment.md) | Test environments and data rules |
| [`docs/automation-guide.md`](docs/automation-guide.md) | Automation architecture, configuration, and how to run it |
| [`docs/ci-cd.md`](docs/ci-cd.md) | Pipeline, artifacts, and merge policy |
| [`docs/troubleshooting.md`](docs/troubleshooting.md) | Known issues and resolutions from building this portfolio |
| [`api-testing/README.md`](api-testing/README.md) | Postman collection and API execution notes |
| [`database-testing/README.md`](database-testing/README.md) | Synthetic dataset and SQL test evidence |
| [`docs/interview-prep.md`](docs/interview-prep.md) | STAR-format summaries of the key findings |

## Project journey

| Phase | Outcome |
|---|---|
| 0 — Audit | Repository scaffold audited; gaps catalogued before any change |
| 1 — Automation foundation | Config-driven headless driver factory, failure screenshots, QA workbook built; CI turned green |
| 2 — Docs & login automation | Test Strategy, Risk Assessment, Test Environment; login automation found **BUG-001** |
| 3 — API testing | Postman collection added; all 8 API cases executed, transfers verified to the cent |
| 4 — SQL & full UI execution | 6 SQL cases Pass on a synthetic dataset; 19 remaining UI cases executed, **BUG-002..BUG-005** found |
| 5 — Transfer automation | Selenium transfer test with exact balance-delta assertions, green in CI |
| 6 — Remaining features | Bill Pay, Update Contact, Loan, Open Account executed; **BUG-006..BUG-008** found; all features covered |
| 7 — Documentation | SRS, Automation Guide, CI/CD and Troubleshooting docs added; documentation aligned to professional standards |

---

*Learning and demonstration portfolio. The application under test is a public demo operated by Parasoft; its data may reset without notice. This project does not represent production banking experience, and no real customer or financial data is used anywhere in it.*
