# # Project NITI BRD: "VaidyaLink" Patient Portal

## ## 1. Project Overview
- **Project Name:** VaidyaLink
- **Domain:** HealthTech / Telemedicine
- **Primary Tech Stack:** Next.js, Node.js, PostgreSQL
- **AI Tooling Status:** Team using Cursor and Kiro (Force Multiplier active)

## ## 2. Core Objective
To build a secure web-based portal where patients can view their medical records and message their doctors directly. 

## ## 3. Functional Requirements
### ### User Role: Patient
- **Registration:** Secure signup with phone OTP.
- **Health Records:** View a list of uploaded lab reports (PDF format).
- **Messaging:** Send encrypted text messages to assigned doctors.

### ### User Role: Doctor
- **Dashboard:** View patient list and incoming messages.
- **Prescription Upload:** Upload and tag PDF prescriptions for patients.

## ## 4. Technical Specifications
- **Database:** Prisma ORM with PostgreSQL.
- **Authentication:** NextAuth.js with JWT.
- **Storage:** AWS S3 for PDF reports.
- **Architecture:** Clean Architecture with separate service layers for Business Logic.

## ## 5. Compliance & Security
- **Data Privacy:** Must follow HIPAA guidelines for data encryption at rest.
- **Accessibility:** Ensure WCAG 2.1 Level AA compliance for the patient UI.

## ## 6. Out of Scope
- Video consultations (Phase 2).
- Payment integration (Phase 2).