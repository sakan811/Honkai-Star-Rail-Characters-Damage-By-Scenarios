# Honkai Star Rail Characters' Damage Simulation

**Simulate** 10-cycles for 1,000 battles to find the **average damage** of Honkai Star Rail's **Characters**.

Latest Update: 8 August 2024.

## Status
[![CodeQL](https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios/actions/workflows/codeql.yml/badge.svg)](https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios/actions/workflows/codeql.yml)

[![Python application](https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios/actions/workflows/python-app.yml/badge.svg)](https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios/actions/workflows/python-app.yml)

## Visualizations
[Click here](docs/VISUALS.md) for visualizations.

## Simulation Disclaimers
**_The result of this simulation might not reflect the actual in-game damage._**

This simulation **focuses exclusively** on the **elements** that **directly impact** character **damage** output. 
As a result, **not all** aspects of character behavior, interactions, or game mechanics were simulated.

Simulate each character for 1,000 battles, 10 cycles each.

Every simulated character has 2,000 ATK, 50% Crit Rate, and 100% Crit Damage.

Basic ATK, Skill, Ultimate, Talent, and Trace are at level 10.

Character's level is 80.

Eidolons, Light Cones, and Relics were not considered.

## To Run a Simulation
### Setup a Project
- Clone this repo: https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios.git
- Create **.env** file with the following variables:
  ```
  DB_NAME=hsr_char_action_dmg
  DB_PASSWORD=
  ```

### Setup a Database
- Install **[PostgreSQL](https://www.postgresql.org/)**
- install **[pgAdmin](https://www.pgadmin.org/)**
- Enter your superuser's **password** in **.env** file for **DB_PASSWORD** variable. 
- Run **pgAdmin**
- Open **SQL** console in **pgAdmin**
- Execute:
  ```
  create database hsr_char_action_dmg;
  ```

## Codebase Details
### Test Status
[![CodeQL](https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios/actions/workflows/codeql.yml/badge.svg)](https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios/actions/workflows/codeql.yml)

[![Python application](https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios/actions/workflows/python-app.yml/badge.svg)](https://github.com/sakan811/Honkai-Star-Rail-Characters-Damage-By-Scenarios/actions/workflows/python-app.yml)

### Brief Codebase Documents
[Click here](docs/DOCS.md) to read a brief docs of this codebase.
