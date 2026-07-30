# Gmail Job Search Email Organizer

A one-time Google Apps Script setup that creates a structured Gmail workflow for organizing job-search communications.

The system creates nested `Job Search/...` labels, classifies existing messages using Gmail search rules, and creates persistent Gmail filters that automatically organize future recruiting emails.

## Business Problem

Job seekers receive application confirmations, recruiter outreach, interview invitations, assessments, next-step requests, offers, and rejection notices from many different systems. Important messages can become buried in a crowded inbox, increasing the risk of missed deadlines and delayed responses.

This project converts an unstructured Gmail inbox into a repeatable job-search operations workflow.

## Current Status

**Working rules-based automation.**

The current version uses deterministic Gmail search queries, keyword matching, Google Apps Script, nested labels, and persistent Gmail filters. It does not currently use a language model to interpret email meaning.

## Current Workflow

```text
Existing Gmail messages
        |
        v
Google Apps Script setup
        |
        +--> Create missing labels
        +--> Search historical threads
        +--> Apply matching labels
        +--> Create future Gmail filters

New Gmail message
        |
        v
Persistent Gmail filters
        |
        v
Automatic job-search classification
```

## Example Label Structure

- `Job Search`
- `Job Search/Applications`
- `Job Search/Interviews`
- `Job Search/Recruiters`
- `Job Search/Offers`
- `Job Search/Rejections`
- `Job Search/Next Steps`

## Example Classification Rules

| Category | Example matching terms |
|---|---|
| Applications | `application received`, `application submitted`, `thank you for applying` |
| Interviews | `interview`, `schedule a call`, `availability`, `phone screen` |
| Recruiters | `recruiter`, `talent acquisition`, `sourcing`, `opportunity` |
| Next Steps | `next steps`, `assessment`, `take-home`, `background check` |
| Offers | `offer`, `offer letter`, `compensation package` |
| Rejections | `unfortunately`, `not moving forward`, `other candidates` |

## Features

- One-time Apps Script setup
- Automatic creation of nested Gmail labels
- Historical email classification
- Persistent Gmail filters for future messages
- Rule-priority and overlap considerations
- Duplicate-filter awareness
- Permission and privacy guidance
- Verification and troubleshooting procedures
- No server, paid hosting, deployment, or recurring Apps Script trigger required

## Skills Demonstrated

- Workflow automation
- Business process analysis
- Google Apps Script
- Gmail search and filtering
- Requirements translation
- Classification-rule design
- Process documentation
- Testing and validation
- Risk and privacy awareness
- Operational maintenance planning

## Professional Project Summary

Designed and implemented a Gmail workflow automation using Google Apps Script and persistent Gmail filters to classify job-search communications into applications, recruiter outreach, interviews, next steps, offers, and rejections, reducing manual inbox review and improving application tracking.

The project also includes a structured label taxonomy, validation procedures, rule-overlap considerations, duplicate-filter controls, privacy safeguards, troubleshooting guidance, and long-term maintenance documentation.

## Planned AI Enhancements

The next version will explore semantic classification so the system can interpret recruiting messages even when they do not contain an exact configured phrase.

Planned capabilities include:

- Semantic email classification using a language model
- Confidence scoring
- Human-review routing for uncertain messages
- Company and job-title extraction
- Interview date and deadline extraction
- AI-generated message summaries
- Suggested follow-up drafts
- Google Sheets application tracking
- Calendar integration
- Job-search analytics dashboard

## Planned AI Workflow

```text
Incoming recruiting email
        |
        v
Google Apps Script
        |
        v
Approved language model
        |
        v
Structured classification result
        |
        +--> Category
        +--> Company
        +--> Job title
        +--> Action required
        +--> Deadline
        +--> Confidence score
        +--> Summary
        |
        v
Validation and human review
        |
        v
Gmail label + tracker + optional calendar action
```

## Installation Overview

1. Open Google Apps Script.
2. Create a new project.
3. Add the project source code.
4. Review all label names and Gmail search queries.
5. Test each query directly in Gmail.
6. Run the setup function once.
7. Review and approve the requested Gmail permissions.
8. Confirm the execution completed successfully.
9. Verify the labels and filters in Gmail settings.
10. Inspect sample messages from each category.

## Safety Notes

- Review the complete source before authorizing it.
- Do not place passwords, API keys, or access tokens in the project.
- Begin with label-only actions.
- Avoid automatic deletion, forwarding, or archival unless deliberately configured.
- Test search rules before processing historical messages.
- Review important interview, offer, and deadline messages manually.
- Do not publish screenshots or sample messages containing personal information.

## Limitations

The current classifier is based on Gmail search expressions and known recruiting phrases. It may miss messages that use unexpected wording, and broad rules may create false positives.

Automated labels should support human review, not replace it.

## Development Roadmap

This project is intentionally being published as a working first version. Future commits will document code improvements, test results, rule refinements, screenshots, semantic classification experiments, and integrations. This commit history will demonstrate the system's growth from deterministic workflow automation toward an AI-assisted operations tool.
