# # NITI Module 04: Performance Analytics & Retrospective Engine

## ## Functional & Technical Specification

### ### 1. Module Overview

The Performance Engine is designed to identify the "Delta" between AI-driven predictions and human execution. Its primary goal is to determine if the **Team Competency Factor (TCF)** or the **AI Efficiency Factor (AEF)** needs recalibration based on real-world data.

---

### ### 2. Data Collection: The Feedback Loop

To generate reports, NITI requires two data points from the Trello Board (often managed via custom fields or card comments):

1. **Estimated Hours ():** The original NITI prediction.
2. **Actual Hours ():** The time logged by the developer upon moving a card to "Done."

---

### ### 3. Key Performance Indicators (KPIs) for Junior Teams

| KPI | Formula | Strategic Meaning |
| --- | --- | --- |
| **Estimation Accuracy** |  | Measures if the Technical Lead is over/under-estimating the team. |
| **AI Leverage Index** |  | Determines if the developer is actually using **Cursor/Kiro** effectively or struggling with the tools. |
| **Skill Gap Velocity** |  | Tracks if a developer is getting faster at a "Learning Gap" (e.g., React), signaling growth. |
| **Friction Factor** |  | Highlights specific tasks where the team "got stuck," indicating a need for more Senior oversight. |

---

### ### 4. The "Performance Ups and Downs" Analysis

The **Project Manager Agent** generates a bi-weekly **NITI Pulse Report** that categorizes team performance into three zones:

#### **A. The Growth Zone (Performance Up)**

* **Indicator:** Actual hours are consistently lower than estimated hours for tasks with high .
* **Analysis:** The developer has mastered a previously identified "Learning Gap."
* **NITI Action:** Automatically lowers that developer's  multiplier for the next sprint to increase velocity.

#### **B. The Friction Zone (Performance Down)**

* **Indicator:** Actual hours exceed estimated hours, particularly in "AI-Optimizable" tasks.
* **Analysis:** The developer may be struggling to use **Antigravity/Kiro** properly, or the AI-generated code is causing more bugs than it solves.
* **NITI Action:** The **Technical Lead** flags these cards for "Mandatory Pair Programming" in the next Trello board generation.

#### **C. The Calibration Zone (System Error)**

* **Indicator:** The entire team is consistently over or under the .
* **Analysis:** NITI’s internal "Base Estimates" are misaligned with the project's actual complexity.
* **NITI Action:** Recalibrates the **Base Baseline** for all future tasks.

---

### ### 5. The Virtual Retrospective (Reporting Output)

Instead of a dry spreadsheet, the **Scrum Master Agent** generates a "NITI Retrospective Document" in Markdown for the Stakeholder:

> **NITI Insights: Sprint 02 Retrospective**
> * **Top Performer:** Developer A showed a 25% improvement in "API Logic" tasks.  will be adjusted from 2.0 to 1.7.
> * **Technical Blocker:** "Database Migrations" took 40% longer than planned. The AI-Editor (Kiro) failed to provide valid migration scripts.
> * **Recommendation:** Move "Database" tasks to **Low AI Gain** () to ensure safer manual estimates.
> * **Velocity Forecast:** Based on current trends, Project NITI predicts a 10% increase in capacity for Sprint 03.
> 
> 

---

### ### 6. Technical Implementation

* **Trello Webhooks:** NITI can listen for "Card Moved to Done" events to trigger a prompt for the developer to enter their time.
* **Historical Knowledge Base:** NITI stores the results of every sprint in a JSON file (`performance_history.json`). This file is fed back into the **Context Architect** at the start of every new project to ensure the agents "remember" the team's true speed.

---