# GroupMe API Automation | AI-Assisted Workflow Engineering

**Project date:** November 2026  
**Project owner:** rsanino-tech  
**AI collaborator:** Muse, nicknamed "Lolita"  
**Status:** Operational messaging reported by project owner; scheduling correction reported implemented; independent post-fix validation and source-code review pending.

## Executive summary

This project documents a practical automation built to reduce repetitive GroupMe messaging. Instead of manually entering messages each day, I directed an AI assistant to connect to GroupMe through its developer API and implement a recurring, day-specific messaging protocol.

The notable part is not merely that an AI generated a response or a script. I identified a workflow that needed automating, located the route to an API integration with the assistant's guidance, obtained the necessary GroupMe API credentials, supplied operational requirements, and evaluated the behavior of the resulting system. I carried out the setup conversation from my **phone**, without needing to sit at my Mac.

When I noticed a message had appeared at **11:00 a.m.** contrary to the intended schedule, I flagged the defect, directed a correction, and reviewed examples the assistant provided to explain its change. The assistant reported that it had corrected the timing behavior. A full subsequent execution log is not yet included in this repository, so the correction is documented as *reported fixed, awaiting independent validation*, rather than presented as a proven long-term resolution.

This is an example of **human-directed, AI-assisted automation**: the human defines the business rules and checks outcomes; the AI helps implement the technical steps.

## 1. The problem

The existing process required recurring GroupMe messages to be sent according to a weekly protocol. Each day could require different wording and a specific sending time. Manual posting created avoidable repetitive work and the risk of missing a message.

**Desired outcome:** a reliable scheduled workflow that follows the provided day-by-day instructions and reports whether a task completed.

### Requirements I supplied

- A full week's schedule, with dates and day-specific message wording.
- Specific authorized sending times.
- A variable timing requirement intended to avoid mechanically identical timestamps, while staying within the allowed schedule.
- Automatic execution without manually typing each message into GroupMe.
- Completion updates returned through the Muse chat.
- Correct interpretation of the intended clock times.

The precise messages, group identifiers, and schedule are deliberately not published here. They may be private or operationally sensitive.

## 2. How the integration was set up

The work began as a conversation with Muse on my phone. I described the behavior I wanted, rather than starting by writing application code.

**Observed sequence, based on my project account:**

1. I explained the repetitive messaging problem and gave Muse the schedule, wording, dates, and timing rules.
2. Muse surfaced an API-related setup prompt and directed me to the GroupMe developer interface.
3. I obtained the required GroupMe API credential and connected it to Muse's workflow.
4. I continued specifying the desired behavior in natural language.
5. Muse configured an automation and began reporting task completion in chat.
6. I observed a posting-time discrepancy and initiated troubleshooting.

**Important technical boundary:** I have not yet exported or inspected the implementation, so I am **not** claiming a specific language, runtime, scheduler, hosting provider, endpoint, authentication flow, or code architecture. The GroupMe API integration was used, but the precise implementation needs to be documented from Muse's configuration or exported source.

## 3. My role and the AI's role

| Area | My contribution | Muse / Lolita contribution |
| --- | --- | --- |
| Problem identification | Identified repetitive GroupMe messaging as an automation opportunity | Helped explore a technical implementation |
| Requirements | Supplied the weekly protocol, wording, dates, sending times, and timing constraints | Translated instructions into an automation workflow |
| API onboarding | Followed the GroupMe developer process and provided the integration credential through the tool's setup | Guided API setup and surfaced the relevant connection step |
| Execution | Defined what successful behavior should look like | Performed scheduled posting and returned completion updates, as observed |
| Quality assurance | Noticed an unexpected 11:00 a.m. post | Investigated and presented a proposed correction |
| Defect handling | Reported the issue and required adherence to the specified schedule | Reported a fix and supplied examples of its timing interpretation |
| Acceptance | Reviewed the explanation and identified the need to monitor subsequent posts | Future execution results still need independent verification |

This project should not be described as me personally coding an entire application from scratch. It **does** demonstrate requirements engineering, API integration setup, workflow design, AI orchestration, testing through observation, defect reporting, and iterative improvement.

## 4. Scheduling defect: unexpected 11:00 a.m. post

### Expected behavior

Messages should be sent only at the permitted times defined in the weekly protocol. Any permitted variation must remain within those boundaries.

### Actual behavior

I noticed that a message had been posted at **11:00 a.m.**, a time I did not expect under the protocol. **I found this problem myself**; it was not initially detected or raised by the assistant.

### Initial hypothesis

During troubleshooting, I suspected a possible mismatch between **12-hour and 24-hour time notation**. That was a working hypothesis, **not a verified root cause**. Other possible causes, such as time-zone interpretation, schedule parsing, or the interaction between fixed windows and randomized timing, have not been ruled out by evidence available here.

### Corrective action

I brought the unexpected posting time to Lolita's attention and directed it to correct the schedule so that messages would appear only at the specified times. Lolita said it had fixed the issue and provided examples of the adjusted behavior.

### Verification status

The explanation and examples were reviewed, but the actual scheduler configuration, execution logs, and subsequent production sends have not been attached. Therefore:

- **Confirmed by owner observation:** an unexpected post appeared at 11:00 a.m.
- **Confirmed by owner account:** the defect was raised with Muse, which returned an explanation and examples.
- **Reported by Muse:** timing logic was corrected.
- **Not yet independently verified:** the precise root cause, code change, and error-free operation over a complete subsequent weekly cycle.

### Regression test plan

Before declaring the defect fully closed:

1. Record the authorized schedule with dates, times, time zone, and permitted variation windows.
2. Compare each planned execution time with its actual GroupMe timestamp.
3. Test both morning and afternoon times, especially 11:00 a.m., 11:00 p.m., noon, and midnight where relevant.
4. Check whether variable delays ever push messages outside permitted windows.
5. Verify day changes, time-zone handling, and daylight-saving transitions as applicable.
6. Confirm that each authorized message posts once and no unauthorized extra posts occur.
7. Retain a sanitized log of results and mark the issue closed only after the agreed observation period.

## 5. Operational and technical lessons

### Natural language can define a real workflow

I did not need to begin with detailed knowledge of a programming language. I started with operational requirements and worked with an AI assistant to implement the integration. This is sometimes described as *vibe coding*, but the essential transferable skill is turning an outcome into clear, testable instructions.

### API literacy matters

The integration required recognizing that GroupMe offered a developer API and that credentials could authorize communication with the service. I learned to pursue that route instead of assuming the chat app's interface was the only way to automate the work.

### AI completion messages are not sufficient proof

A chat confirmation that a task was completed is useful, but a real verification process compares it with the expected schedule and the actual message timestamps. The 11:00 a.m. incident illustrates why human oversight and logs matter.

### Variable scheduling requires guardrails

Timing variation and strict scheduled windows can conflict. The system should prioritize permitted sending windows over randomized delays. The exact rule for acceptable variation must be explicit and tested.

### Debugging begins with observation

I caught the issue by noticing behavior that differed from the protocol. I raised it, considered a possible clock-format cause, and requested a correction. I did not assume the first explanation proved the root cause.

## 6. Skills demonstrated

**Directly supported by this project account:**

- Operational problem identification and workflow improvement
- Translating business rules into automation requirements
- API discovery and integration onboarding
- Human-in-the-loop AI collaboration
- Scheduling requirements and exception handling
- Monitoring outputs and identifying defects
- Troubleshooting communication and corrective-action review
- Technical documentation and evidence-aware reporting

**Skills not claimed without further evidence:** personally writing the underlying integration code, designing its hosting architecture, administering its scheduler, or independently validating the complete production deployment.

## 7. Architecture: conceptual only

```text
Human operator (phone)
        |
        v
Muse / Lolita (AI assistant)
        |
        v
Configured automation / scheduling mechanism
        |
        v
GroupMe API integration
        |
        v
GroupMe messages
        |
        +--> Completion reports / observation
                         |
                         v
               Human review and bug reports
```

This is a **logical workflow diagram**, not a verified infrastructure diagram. The actual scheduler and execution environment remain to be documented.

## 8. Evidence and artifacts to add

The repository currently contains project documentation, **not the original automation source code**. Suggested evidence for a future update:

- Redacted screenshot of the weekly protocol
- Sanitized screenshot of the Muse API setup workflow
- Redacted configuration export or source code, if available
- Before/after examples of the timing correction
- Scheduled-versus-actual execution log for one full week
- A short test report confirming no duplicate or out-of-window posts

Never commit API keys, access tokens, bot IDs that should remain private, group membership data, private message content, or screenshots containing secrets.

## 9. Next steps

1. Export or inspect the actual Muse automation configuration.
2. Identify the scheduler, runtime, and GroupMe API method used.
3. Confirm how credentials are stored and rotated.
4. Capture sanitized evidence of the timing correction.
5. Run the regression test plan and update the status.
6. Add source files only after reviewing them for secrets and private information.
7. Consider error alerts, retry limits, duplicate prevention, and audit logs if supported.

## 10. Portfolio takeaway

This project reflects a practical approach to technology: **identify a problem, find an integration path, define requirements, use AI as an implementation partner, observe the result, and correct defects.**

My contribution was not limited to asking an AI to "make something." I specified the operating rules, carried out the API onboarding, identified a scheduling failure, and directed the correction. The next stage is to strengthen technical validation and document the underlying implementation.

---

*Documentation based on the project owner's account as of November 11, 2026. Implementation details and post-fix performance should be updated as direct evidence becomes available.*
