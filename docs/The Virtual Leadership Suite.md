# # NITI Module 01: The Virtual Leadership Suite

## ## Functional & Technical Specification

### ### 1. Module Overview

The Virtual Leadership Suite is a multi-agent orchestration layer that serves as the "Cognitive Engine" of Project NITI. Its purpose is to simulate a high-performing software engineering leadership team. Unlike static LLM personas, these agents are **stateful within a session** and **contextually aware** of the specific project domain and the developers' profiles.

---

### ### 2. Detailed Agent Architectures

#### **A. Context Architect (The Pre-Processor)**

* **Functional Goal:** To eliminate "Generic AI" behavior. This agent acts as the system's initialization sequence.
* **Technical Logic:**
* **Input:** BRD (Unstructured) + Industry Standards (Knowledge Base).
* **Processing:** Performs Named Entity Recognition (NER) to identify the tech stack, regulatory requirements (GDPR, HIPAA), and project complexity.
* **Output:** Generates a `session_config` object that re-defines the `backstory` and `goal` of all subsequent agents.


* **Example:** If the BRD mentions "Payments," the Architect injects "PCI-DSS Compliance Expert" into the Product Owner’s persona.

#### **B. Product Owner (The Value Strategist)**

* **Functional Goal:** Transform business "wants" into actionable User Stories.
* **Technical Logic:**
* **Heuristics:** Uses the **INVEST** principle (Independent, Negotiable, Valuable, Estimable, Small, Testable).
* **Task:** Maps business requirements to a prioritized Product Backlog.
* **Constraint:** Must categorize every story by "Business Value Impact" (High/Med/Low).



#### **C. Technical Architect (The Structural Auditor)**

* **Functional Goal:** Design the system skeleton and determine "AI-Augmentation" potential.
* **Technical Logic:**
* **AI Suitability Scoring:** Analyzes tasks against a "Pattern Library." If a task matches a common pattern (e.g., "REST Endpoint"), it tags the task with an `AI_OPTIMIZATION_INDEX` of 0.6.
* **Responsibility:** Defines the **Tech Stack** and **Folder Structure** to be used by the developers.



#### **D. Technical Lead (The Quality & Estimation Gate)**

* **Functional Goal:** Bridge the gap between the Architect's vision and the Junior Team's reality.
* **Technical Logic:**
* **Input:** Markdown Team Profile + Architect’s Base Estimates.
* **Estimation Engine:** Applies the **TCF (Team Competency Factor)**. It identifies "Skill Gaps" (e.g., Developer A is assigned a Redux task but has Redux listed as a "Learning Gap").
* **Action:** It injects "Technical Implementation Guides" into Trello cards for tasks where the team is weak.



#### **E. Project Manager (The Delivery Strategist)**

* **Functional Goal:** Convert verified tasks into a time-bound Project Plan.
* **Technical Logic:**
* **Critical Path Analysis:** Identifies blockers (e.g., Backend Auth must be done before Frontend Login UI).
* **Capacity Modeling:** Calculates the "Sprint Load" based on the Junior Team's adjusted hours.



#### **F. Delivery Manager (The API Orchestrator)**

* **Functional Goal:** Physical manifestation of the plan.
* **Technical Logic:**
* **Tooling:** Uses a custom `TrelloTool` (Python/Requests).
* **Mapping:** Translates Agent outputs into JSON payloads for Trello (Labels, Checklists, Due Dates, Descriptions).



---

### ### 3. Inter-Agent Communication Flow (The "Council" Logic)

The Suite operates through a **Sequential and Hierarchical Task Flow**:

1. **Drafting:** Product Owner proposes the Backlog.
2. **Validation:** Technical Architect reviews for structural flaws.
3. **Refinement:** Technical Lead adjusts hours based on the **Team Profile**.
4. **Optimization:** Project Manager adjusts the timeline based on **AI-Editor gains**.
5. **Finalization:** The group generates a **Consensus Report** for your review.

---

### ### 4. Technical Guardrails for Inexperienced Teams

To maximize output from junior developers, the Leadership Suite is programmed to enforce these rules:

* **Atomic Rule:** No task can exceed **8 hours**. If the PM proposes a 12-hour task, the Tech Lead must force a split.
* **Clarity Rule:** Every Trello card must contain a "How to verify" section.
* **AI Integration:** The Tech Lead must specify which **Cursor/Kiro** commands are most useful for a specific card (e.g., "Use `@docs` to reference the Stripe API").

---

### ### 5. Success Criteria for this Module

* **Persona Accuracy:** Agents respond as specialists, not generalists.
* **Estimate Realism:** Final hours reflect the actual friction of a junior developer learning a new skill.
* **Automation Readiness:** The output is structured JSON/Dictionary ready for the Trello API.

---