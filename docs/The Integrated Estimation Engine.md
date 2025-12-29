# # NITI Module 02: The Integrated Estimation Engine

## ## Functional & Technical Specification

### ### 1. The Estimation Philosophy

Project NITI rejects the "Fixed Hour" fallacy. Instead, it utilizes **Probabilistic Estimation** based on the **PERT** (Program Evaluation and Review Technique) distribution, then applies specific weights for the team's profile and toolset.

### ### 2. The Multiplier Math: TCF & AEF

The engine calculates two primary variables to refine the  ():

#### **A. Team Competency Factor (TCF)**

Derived from the Markdown profile, the TCF represents the friction of inexperience.

* **Expert (Baseline):** 
* **Mid-Level (Familiar Tech):** 
* **Junior (Familiar Tech):** 
* **Junior (Learning Gap/New Tech):** 

#### **B. AI Efficiency Factor (AEF)**

The AEF represents the reduction in labor provided by editors like Cursor and Kiro. This is not a flat discount; it is task-dependent.

* **Boilerplate/Scaffolding:**  (50% faster)
* **Standard Logic/Refactoring:**  (30% faster)
* **Complex Debugging/Security:**  (10% faster)

---

### ### 3. The NITI Final Formula

The **Technical Lead** agent performs the final calculation for every task using this logic:

**Example Scenario:**

* **Task:** Create a REST API for User Profiles.
* **Base Hours ():** 4 Hours (Senior level).
* **Developer:** Junior ( because the profile lists "Backend" as a learning gap).
* **Tooling:** Using Cursor/Antigravity ( for boilerplate API).
* **Calculation:** .

---

### ### 4. Technical Detail: The "Profile Parser" Logic

The **Technical Lead** doesn't just read the Markdown; it maps keywords from the **Project Architecture** to the **Team Profile**.

| Project Requirement | Profile Keyword Match | Logic Applied |
| --- | --- | --- |
| "React State Management" | Found in "Learning Gaps" | Increase  to 2.2; add "Redux Tutorial" to Trello checklist. |
| "UI Components" | Found in "Strengths" | Decrease  to 1.1; set AI Efficiency to max (0.5). |
| "AI Editor Proficiency" | "Advanced (Kiro/Cursor)" | Apply aggressive AI Efficiency discounts. |

---

### ### 5. Output: The Consensus Report (Data Schema)

This module produces a structured JSON object that the **Project Manager** uses to finalize the Trello cards.

```json
{
  "task_id": "AUTH_01",
  "base_estimate": 6.0,
  "assigned_to": "Dev_Junior_01",
  "tcf_applied": 1.8,
  "aef_applied": 0.7,
  "final_hours": 7.56,
  "risk_score": "Medium",
  "justification": "Increased due to auth skill gap; partially offset by Cursor proficiency."
}

```

### ### 6. Operational Guardrails

1. **The 8-Hour "Atomic" Ceiling:** If  exceeds 8 hours, the engine triggers a **Sub-Tasking Routine** to break the card into two smaller Trello cards.
2. **Context Injection:** For every task with an , NITI generates a "Copilot Hint" (e.g., *"Prompt Cursor to use the @Schema context for this task"*).

---

To implement the review phase effectively, **Project NITI** will generate a **Pre-Commit Consensus Report** in Excel/CSV format. This acts as the "Dharma" (Authority) check, where you can manually override AI estimates, change assignees, or adjust the AI-Efficiency factors based on your intuition before the **Delivery Manager** triggers the Trello API.

---

# # NITI Module 02.1: The Pre-Commit Review Logic (Excel Generation)

### ### 1. Functional Workflow

Before any data touches Trello, the **Project Manager Agent** exports the "Consensus Report." The process follows this industrial standard:

1. **Generation:** NITI produces the Excel file with all calculated multipliers.
2. **Review:** You open the file and edit the `Manager_Override_Hours` or `Feedback_Notes` columns.
3. **Re-Ingestion:** NITI reads the modified Excel and uses the **Override** values as the final truth for Trello card creation.

---

### ### 2. The Excel Schema (Consensus Report)

The generated file will contain the following structure to ensure full transparency of the AI's logic:

| Task ID | User Story Title | Assigned Dev | Base Hrs | TCF (Team Factor) | AEF (AI Factor) | **NITI Calculated Hrs** | **Manager Override Hrs** | Reviewer Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AUTH-01 | Implement JWT Auth | Dev_Junior_A | 4.0 | 2.2 | 0.9 | **7.92** |  | *Leave blank to accept NITI* |
| UI-05 | Profile Dashboard UI | Dev_Junior_B | 6.0 | 1.2 | 0.5 | **3.60** |  | *Reduced due to high AI gain* |
| DB-02 | Schema Migration | Dev_Junior_A | 2.0 | 1.5 | 0.7 | **2.10** |  |  |

---

### ### 3. Technical Implementation for Overrides

The **Technical Lead** agent is programmed to prioritize human feedback. The logic follows this hierarchy:

* **Feedback Integration:** If you provide text in the `Reviewer Comments` column, NITI will append this text to the **Trello Card Description** as a "Stakeholder Note," ensuring the developer sees your specific guidance.

---

### ### 4. Impact on Sprint Planning

By reviewing this in Excel, you can see the **Total Sprint Load** at the bottom of the sheet. If the total hours exceed your team's 2-week capacity (e.g., total is 180 hours but team capacity is 160), you can:

1. **De-prioritize:** Mark a row as `Pushed to Backlog`.
2. **Trim:** Lower the hours in the `Override` column.
3. **Re-assign:** Change the `Assigned Dev` to balance the load.

---

### ### 5. Why the Excel Phase is Critical

* **Correction of Hallucinations:** If the AI overestimates a simple task, you can fix it in seconds.
* **Stakeholder Accountability:** It provides a "Paper Trail" of why a project is estimated to take a certain amount of time.
* **Team Morale:** It allows you to manually add "Learning Time" for a developer if you feel the AI was too aggressive with the  discount.

---

This is the correct technical approach for **Project NITI**. Producing JSON as an intermediate "Source of Truth" ensures data integrity, allows for programmatic validation, and makes the conversion to Excel (via libraries like `pandas` or `openpyxl`) clean and error-free.

---

# # NITI Module 02.2: Data Pipeline & Excel Conversion

## ## Functional & Technical Specification

### ### 1. The Data Pipeline Flow

The transition from AI thought to a user-reviewable file follows this rigid pipeline:

1. **JSON Generation:** The **Project Manager Agent** aggregates all outputs (User Stories, TCF/AEF math, and Assignees) into a structured JSON schema.
2. **Validation Layer:** A Python script validates the JSON (checking for missing hours, broken links, or empty descriptions).
3. **Excel Transformation:** The validated JSON is flattened and injected into a formatted Excel template.
4. **Local Caching:** The file is saved locally (e.g., `niti_sprint_01_review.xlsx`) for the user.

---

### ### 2. The JSON Schema (NITI Intermediate Cache)

The LLM will be instructed to produce the following structure to ensure the conversion script has all necessary metadata:

```json
{
  "project_metadata": {
    "project_name": "NITI_Beta",
    "sprint_cycle": "14_Days",
    "total_capacity_hours": 160
  },
  "backlog": [
    {
      "task_id": "NT-101",
      "title": "User Authentication API",
      "assignee": "Dev_Junior_A",
      "metrics": {
        "base_hours": 4.0,
        "tcf": 1.5,
        "aef": 0.7,
        "niti_estimate": 4.2
      },
      "technical_notes": "Use Kiro for boilerplate Express middleware.",
      "priority": "High"
    }
  ]
}

```

---

### ### 3. Technical Conversion Logic (Python Snippet)

The **Delivery Manager** agent (or a dedicated script) will execute a function similar to this:

```python
import pandas as pd

def convert_niti_json_to_excel(json_data):
    # Flatten the JSON for tabular display
    df = pd.json_normalize(json_data, record_path=['backlog'])
    
    # Add the empty review columns for the User
    df['Manager_Override_Hours'] = ""
    df['User_Feedback'] = ""
    
    # Export with professional formatting
    df.to_excel("NITI_Review_Sheet.xlsx", index=False)
    return "Excel generated. Awaiting user review."

```

---

### ### 4. The "Round-Trip" Feedback Loop

To ensure your feedback is actually captured and pushed to Trello, NITI implements a **Two-Way Sync**:

1. **Outbound:** NITI → JSON → Excel.
2. **User Action:** You open the Excel, enter `8.0` in `Manager_Override_Hours` for a task, and save.
3. **Inbound:** NITI reads the Excel → Updates the JSON Cache → **Delivery Manager** pushes only the updated values to the Trello API.

---

### ### 5. Why JSON Caching is Essential

* **Resilience:** If the Trello API fails during a push, NITI doesn't need to "re-think" the project (saving you API costs). It simply restarts the push from the JSON cache.
* **Audit Trail:** You keep a permanent record of what the AI suggested versus what you actually approved.
* **Version Control:** You can compare the JSON from Sprint 1 to Sprint 2 to see if the AI is becoming more accurate in its predictions.

---