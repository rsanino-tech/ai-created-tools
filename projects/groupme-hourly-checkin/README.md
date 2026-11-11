# GroupMe Hourly Check-In Automation (Muse-Assisted)

## Project overview
I identified a repetitive hourly check-in task at work that I wanted to automate. GroupMe's normal chat interface did not provide the scheduling behavior I needed, so I researched whether its API could support an alternative. I found the GroupMe API and used Muse, an AI assistant, to configure an automated workflow.

**Status:** Reported running on November 10, 2026. Ongoing reliability, precise implementation, and authorization details have not been independently verified.

## Problem
A recurring hourly message/check-in required manual effort during Sunday-through-Thursday work shifts. I wanted a repeatable system that could send the check-in without manually composing each message.

## My contribution
- Identified the repetitive process and defined the desired schedule.
- Researched GroupMe's API as a possible integration path.
- Supplied the API information and workflow instructions to Muse.
- Directed Muse to set up the automation for Sunday through Thursday.
- Reported that the automation began operating on November 10, 2026.

## Tools and concepts
- GroupMe API
- Muse AI assistant
- API integration research
- Scheduled workflow design
- Operational process automation

## Technical ownership and limitations
The integration was configured through Muse, **not independently coded by me**. This is a workflow design and AI-assisted integration case study, not a claim that I wrote a production Python/Bash application or implemented the authentication myself.

The precise API endpoints, scheduler, error handling, authentication mechanism, and execution environment have not yet been documented. No credentials or work messages are included in this public case study.

## Next validation steps
1. Confirm that each scheduled check-in arrives at the intended time and in the intended chat.
2. Document the scheduling mechanism and time zone.
3. Determine how failures and retries are handled.
4. Verify the automation is permitted under workplace policies and GroupMe's terms.
5. Record a redacted example and a simple architecture diagram without exposing tokens, chat identifiers, or sensitive work information.
6. If appropriate, rebuild a separate demonstration using a test group and a small Bash or Python script to demonstrate independent implementation.

## Skills demonstrated
Problem definition, systems thinking, API discovery, workflow design, AI-assisted integration, and iterative operational improvement.
