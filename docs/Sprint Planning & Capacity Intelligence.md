# # NITI Module 05: Sprint Planning & Capacity Intelligence

**Algorithmic Bin-Packing, Capacity Validation, and Stakeholder Approval**

## ## 1. Module Overview

The Sprint Planning module is the "Decision Engine" of NITI. It calculates the **Net Available Hours ()** for a 2-week cycle and programmatically selects the highest-priority tasks that fit the team's capacity. It utilizes a **Bin-Packing Algorithm** to ensure that no developer is over-allocated.

---

## ## 2. Strategic Capacity Logic

NITI calculates capacity not just on raw hours, but on **Focus-Adjusted Availability**.

* **Gross Hours:** 80 hours (2 weeks).
* **Focus Factor ():** Typically 0.8 (accounts for meetings and context switching).
* **Contingency Buffer ():** 10-15% reserved for unplanned technical debt or bugs.
* **The Formula:** 


---

## ## 3. The Sprint Goal & Commitment Pipeline

Before generating the technical plan, the **Product Owner** and **Technical Architect** collaborate to define a **Sprint Goal**—a high-level objective (e.g., *"Enable User Authentication and Profile Management"*).

### ### Step 1: JSON Sprint Blueprint

NITI generates a cached JSON object representing the proposed sprint:

```json
{
  "sprint_metadata": {
    "sprint_number": 1,
    "sprint_goal": "Implement Core Auth & Database Schema",
    "start_date": "2025-01-01",
    "end_date": "2025-01-14"
  },
  "allocations": [
    {
      "developer": "Dev_Junior_01",
      "capacity_hours": 64.0,
      "assigned_tasks": ["AUTH-01", "AUTH-02"],
      "total_assigned_hours": 62.5
    }
  ]
}

```

### ### Step 2: The Excel Review Sheet (Governance)

NITI flattens the JSON into a **Sprint Forecast Sheet**. This allows the user to perform "What-If" scenarios before the Trello push.

| Developer | Task ID | Task Title | NITI Est. Hrs | **Priority Override** | **Reassign To** | **Remove from Sprint** |
| --- | --- | --- | --- | --- | --- | --- |
| Dev_Junior_01 | AUTH-01 | JWT Middleware | 8.0 | High |  | [ ] |
| Dev_Junior_01 | UI-05 | Login Screen | 4.5 | Medium | Dev_Junior_02 | [ ] |
| **TOTALS** |  |  | **12.5 / 64** |  |  |  |

---

## ## 4. The Feedback Loop & Trello Manifestation

1. **Review:** The user marks tasks for removal or reassignment in Excel.
2. **Sync:** NITI re-reads the Excel and updates the **Sprint JSON Cache**.
3. **Manifest:** The **Delivery Manager** creates the Trello list `Sprint 01: [Goal Name]` and moves only the approved cards into it.

---

## ## 5. Trello "Sprint Support" Implementation

To mimic advanced Scrum tools in Trello, NITI configures:

* **Sprint Goal Card:** A "Cover Card" at the top of the list clearly stating the Sprint Goal.
* **Capacity Labels:** Visual indicators if a developer's total hours on the board exceed their .
* **Butler Automation:** Automatically tags cards with a `Sprint-01` label for cross-sprint reporting.

---

## ## 6. Benefits for Junior Team Management

* **Psychological Safety:** By defining a **Sprint Goal**, the team understands *why* they are working, not just *what* they are coding.
* **Automated Gatekeeping:** The "Bin-Packing" logic prevents the "Hero Culture" where one junior dev tries to take on 80% of the work.
* **Clear Exit Criteria:** When the Trello list `Sprint 01` is empty (all cards moved to Done), the sprint is objectively successful.
