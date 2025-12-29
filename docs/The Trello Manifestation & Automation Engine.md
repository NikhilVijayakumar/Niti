# # NITI Module 03: The Trello Manifestation & Automation Engine

## ## Functional & Technical Specification

### ### 1. Module Overview

The **Trello Manifestation Engine** is the bridge between the AI Council's logic and the development team's daily workflow. It is responsible for creating the project infrastructure, enforcing the organizational taxonomy, and ensuring that every card is "Self-Documenting" to minimize the need for junior developers to seek external clarification.

---

### ### 2. Technical Architecture: The "Duta" (Delivery) Tool

The **Delivery Manager** agent utilizes a custom Python-based Trello Toolkit.

#### **A. Workspace Initialization**

NITI does not just create cards; it establishes a **Standardized Agile Environment**:

* **Board Creation:** Named after the project (e.g., `NITI: [Project Name]`).
* **List Hierarchy:** 1.  `Product Backlog` (Future work)
2.  `Sprint Backlog` (Current commitment)
3.  `In Progress / AI-Augmentation` (Active work)
4.  `Peer Review / QA` (Lead oversight)
5.  `Done` (Verified against DoD)

#### **B. API Payload Construction**

For every task approved in the **Consensus Report**, NITI constructs a complex JSON payload for the Trello `POST /1/cards` endpoint.

---

### ### 3. The "High-Fidelity" Card Anatomy

To maximize output from inexperienced developers, NITI populates Trello cards with much more than just a title. Every card must follow this schema:

| Card Element | Source Agent | Content Detail |
| --- | --- | --- |
| **Description** | Product Owner | User Story in `As a... I want... So that...` format. |
| **Tech Blueprint** | Tech Architect | Architectural requirements (e.g., "Use functional components," "Ensure 404 handling"). |
| **Efficiency Hints** | Tech Architect | Specific **Cursor/Kiro** prompts (e.g., `"@file:api.js Generate a POST route for..."`). |
| **Checklist** | Tech Lead | Step-by-step implementation guide tailored to the dev's **Learning Gaps**. |
| **Estimate Label** | Project Manager | Custom label showing `Estimated: X.X Hours`. |
| **Definition of Done** | Scrum Master | Mandatory validation steps (e.g., "Run Linter," "Verify on Mobile view"). |

---

### ### 4. Logic for "Junior-Specific" Context Injection

The **Technical Lead** agent performs a final "Context Injection" during the API call:

* **Skill-Gap Alert:** If the **Team Profile** identifies a gap, NITI automatically appends a `Tutorial` link or a `Snippet` example directly into the Trello card description.
* **AI-Force Multiplier:** For tasks with high AI-Suitability, the card is tagged with a `⚡ AI-Opt` label, signaling to the dev that they should rely heavily on **Antigravity** or **Cursor** for this specific task.

---

### ### 5. API Governance & Rate Limiting

To ensure stability when generating large boards (e.g., 50+ cards), the **Delivery Manager** implements:

* **Exponential Backoff:** Prevents hitting Trello's API rate limits.
* **State Verification:** Checks if a list or label already exists before attempting creation to avoid duplication.
* **Batch Processing:** Groups card creations to maintain a clean sequence on the board.

---

### ### 6. Post-Deployment: The "Handover" Report

Once the board is manifested, the module generates a final **NITI Deployment Summary**:

* **Total Sprint Hours:** Cumulative adjusted hours.
* **Board URL:** The direct link to the new Trello workspace.
* **Risk Heatmap:** Identifying which cards have the highest "Risk Score" due to the combination of junior experience and complex logic.

---

