# Project CHIPIFY BRD: “CHIPIFY – AI-Driven ASIC Design Automation Platform”

## 1. Project Overview
- **Project Name:** CHIPIFY  
- **Domain:** Semiconductor / EDA / AI-Driven Hardware Design  
- **Primary Tech Stack:** Next.js, FastAPI (Python), Docker, OpenLANE, Icarus Verilog, MongoDB  
- **AI Tooling Status:** Generative AI + Agentic AI (CrewAI) integrated  
- **Target Users:** Startups, students, hardware engineers, research teams  

> CHIPIFY is an AI-powered, cloud-native platform that automates the ASIC design flow from RTL to GDSII using open-source EDA tools, significantly reducing design complexity, setup effort, and turnaround time. :contentReference[oaicite:0]{index=0}

---

## 2. Core Objective
To democratize chip design by providing an end-to-end automated platform where users can:
- Generate Verilog RTL from natural language using Generative AI  
- Verify, simulate, and synthesize designs automatically  
- Execute a full RTL-to-GDSII flow without local EDA setup  
- Receive intelligent summaries of tool logs and errors  

---

## 3. Functional Requirements

### User Role: Designer / Developer
- **Authentication:** Secure login and session management.
- **Design Input (Two Modes):**
  - Natural language specification for AI-generated Verilog.
  - Manual upload of Verilog RTL files.
- **Simulation & Verification:**
  - Automatic simulation using Icarus Verilog.
  - Pass/fail feedback with error highlighting.
- **ASIC Flow Execution:**
  - Trigger OpenLANE flow to generate GDSII.
  - View progress and execution status in real time.
- **Notifications:**
  - Receive real-time job updates via push notifications.
- **Log Insights:**
  - View AI-generated summaries of OpenLANE and verification logs.

### User Role: System / AI Agent
- **Design Agent:** Generates syntactically correct Verilog from user intent.
- **Verification Agent:** Simulates and validates RTL against test vectors.
- **Fixer Agent:** Iteratively refines code based on simulation failures.
- **Log Summarizer Agent:** Parses logs and produces human-readable reports.

---

## 4. Technical Specifications

### Backend & Automation
- **Framework:** FastAPI (Python, ASGI)
- **EDA Tools:**
  - Icarus Verilog – RTL simulation & verification
  - OpenLANE 2 – Full ASIC design flow (RTL → GDSII)
- **Containerization:** Docker-based execution for reproducibility and scalability
- **Workflow Orchestration:** Shell scripting + API-driven pipelines

### AI & Agentic System
- **Framework:** CrewAI
- **LLMs:** Open-source LLMs (via LM Studio), Gemini, Azure OpenAI
- **Capabilities:**
  - Verilog generation
  - Iterative design-verify-fix loop
  - Log analysis and summarization

### Data & Communication
- **Database:** MongoDB (user data, job metadata)
- **Message Broker:** RabbitMQ (async task handling)
- **Notifications:** Firebase Cloud Messaging (FCM)
- **Streaming:** Server-Sent Events (SSE) for real-time updates

### Frontend
- **Framework:** Next.js (TypeScript)
- **UI Libraries:** Material UI, Tailwind CSS
- **State Management:** Redux Toolkit

---

## 5. Architecture Overview
- **Cloud-native, containerized design execution**
- **Decoupled frontend, backend, and AI agents**
- **Asynchronous processing for long-running EDA tasks**
- **Scalable agent-based AI workflow mimicking human design cycles**

---

## 6. Compliance & Non-Functional Requirements
- **Security:** Secure authentication, isolated container execution
- **Scalability:** Horizontal scaling via containerized workloads
- **Reliability:** Deterministic builds using fixed toolchain versions
- **Usability:** Minimal hardware expertise required to run ASIC flows

---

## 7. Key Differentiators
- Agent-based iterative refinement (Design → Verify → Fix)
- Full RTL-to-GDSII automation using open-source tools
- No local EDA installation or licensing required
- AI-generated log summaries for faster debugging
- 30–50% reduction in design cycle time with higher productivity

---

## 8. Out of Scope (Phase 1)
- Power, performance, and area optimization dashboards
- Commercial PDK integrations
- Multi-user collaborative design workspaces
- Tape-out and fabrication services

---

## 9. Future Scope
- Interactive GUI for AI-assisted code refinement
- Integrated power, area, and timing analysis
- Unified single-system deployment (GenAI + Tool Automation)
- Advanced visualization of layout and metrics

---
