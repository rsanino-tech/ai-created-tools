# RecruitFlow AI

An AI-assisted recruiting operations system built with Google Apps Script, Gmail, Google Sheets, Google Calendar, and the OpenAI API.

RecruitFlow AI organizes job-search email, tracks application activity in a dedicated spreadsheet, prepares structured AI analysis, and keeps high-impact actions under human control.

## Business Problem

Job seekers receive application confirmations, recruiter outreach, interview invitations, assessments, next-step requests, offers, and rejection notices across many platforms. Important messages can become buried, deadlines can be missed, and application history becomes difficult to track.

RecruitFlow AI converts scattered recruiting communication into a structured operational workflow.

## Current Status

**Core system and tracker complete. Google-side audit passed. Live OpenAI validation pending private API-key configuration.**

### Audit Results

| Component | Status |
|---|---|
| Apps Script runtime smoke tests | Passed |
| Dedicated RecruitFlow AI Tracker | Created |
| Tracker tabs | 7 of 7 present |
| Gmail access | Passed |
| Google Calendar read access | Passed |
| Automatic Calendar creation | Off |
| Automatic reply drafts | Off |
| Processing trigger | Not installed yet |
| OpenAI API key | Not configured |

Tracker name: **RecruitFlow AI Tracker**

## System Design

RecruitFlow AI combines deterministic workflow automation with an optional AI analysis layer.

```text
Recruiting email
      |
      v
Google Apps Script
      |
      +--> Gmail classification and labels
      +--> Structured tracker update
      +--> Calendar date detection
      +--> AI analysis when enabled
                    |
                    +--> Semantic category
                    +--> Confidence score
                    +--> Company extraction
                    +--> Job-title extraction
                    +--> Interview-date parsing
                    +--> Message summary
                    +--> Suggested reply
      |
      v
Human review before consequential actions
```

## Core Capabilities

- Creates and manages structured Gmail job-search labels
- Processes matching historical Gmail threads
- Supports automatic organization of future recruiting messages
- Maintains a dedicated Google Sheets application tracker
- Verifies the required tracker structure through automated audit checks
- Reads Calendar data for scheduling context
- Supports semantic AI classification when an API key is configured
- Extracts company names and job titles
- Parses interview dates and deadlines
- Generates concise message summaries
- Produces suggested replies for review
- Keeps Calendar creation disabled by default
- Keeps automatic reply-draft creation disabled by default
- Uses fictional data for AI endpoint validation

## Tracker

The system creates a dedicated spreadsheet named:

`RecruitFlow AI Tracker`

The Google-side audit confirms that all **7 required tabs** are present. The tracker is designed to support structured application monitoring, recruiting-email analysis, follow-up planning, and operational reporting.

## AI Validation Plan

A fictional-data-only AI test is installed. After the OpenAI API key is added privately through Apps Script properties, the test will validate:

- Live OpenAI endpoint access
- Semantic recruiting-email classification
- Confidence scoring
- Company extraction
- Job-title extraction
- Interview-date parsing
- Summary generation
- Suggested reply generation

The validation does not require sending a real Gmail message.

## Private API-Key Configuration

The API key must never be committed to GitHub, pasted into documentation, or stored directly in the source code.

Configure it privately in Google Apps Script:

1. Open the RecruitFlow AI Apps Script project.
2. Select **Project Settings**.
3. Under **Script Properties**, choose **Add script property**.
4. Set the property name to:

   `OPENAI_API_KEY`

5. Add the API key as the property value.
6. Save the property.

The key remains outside the public repository.

## Safety Controls

RecruitFlow AI is intentionally conservative around actions that could affect real communications or scheduling.

- Automatic Calendar event creation is disabled
- Automatic reply drafting is disabled
- Human review remains required for consequential actions
- AI testing uses fictional data only
- API credentials are stored privately in Script Properties
- No API keys, tokens, private emails, or personal records should be committed
- Important interviews, offers, deadlines, and follow-ups should always be manually verified

## Gmail Workflow

The Gmail component supports structured categories such as:

- Applications
- Interviews
- Recruiters
- Offers
- Rejections
- Next Steps

Deterministic Gmail rules provide a reliable baseline, while the AI layer is designed to interpret recruiting language that does not match exact keywords.

## Example AI Output

```json
{
  "category": "Interview",
  "confidence": 0.96,
  "company": "Example Company",
  "jobTitle": "Operations Analyst",
  "interviewDate": "2026-08-04T14:00:00-04:00",
  "summary": "The employer is requesting availability for a first-round interview.",
  "suggestedReply": "Thank you for reaching out. I am available at the proposed time and look forward to speaking with the team."
}
```

This example is fictional and contains no real applicant or employer data.

## Skills Demonstrated

- AI workflow design
- Business process analysis
- Google Apps Script
- Gmail automation
- Google Sheets tracker design
- Google Calendar integration
- OpenAI API integration
- Semantic classification
- Structured data extraction
- Human-in-the-loop controls
- Testing and validation
- Privacy and credential management
- Technical documentation
- Operational risk awareness

## Professional Project Summary

Designed and implemented RecruitFlow AI, an AI-assisted recruiting operations system that organizes Gmail job-search communications, maintains a dedicated seven-tab Google Sheets tracker, reads Calendar context, and prepares semantic classification, confidence scoring, entity extraction, interview-date parsing, message summaries, and suggested replies.

Built automated audit checks to validate Apps Script execution, Gmail permissions, Calendar access, tracker creation, and tracker structure. Applied human-in-the-loop safeguards by keeping automatic Calendar creation and automatic reply drafting disabled.

## Remaining Setup

The core build is complete. The remaining activation steps are:

1. Add the OpenAI API key privately through Script Properties.
2. Run the fictional-data-only AI validation.
3. Review the output for classification accuracy and parsing quality.
4. Install the processing trigger when ready for ongoing operation.

## Development Roadmap

Future commits may add:

- Completed live AI validation results
- Processing-trigger installation
- Accuracy and confidence benchmarks
- Human-review queue behavior
- Tracker screenshots using fictional data
- Application-funnel analytics
- Response-rate reporting
- Interview-pipeline visualization
- Additional privacy and error-handling controls

## Privacy Standard

Public repository content must not expose:

- OpenAI API keys
- Google authorization tokens
- Personal Gmail messages
- Recruiter contact details from private correspondence
- Real applicant records
- Private Calendar events
- Spreadsheet IDs tied to personal data

All screenshots, examples, and tests intended for public use should rely on fictional or thoroughly sanitized data.
