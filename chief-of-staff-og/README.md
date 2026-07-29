# Chief of Staff OG

> A private, AI-assisted command system designed to reduce decision fatigue, organize competing responsibilities, and turn scattered information into a clear daily plan.

## Project Snapshot

| Area | Details |
|---|---|
| Project type | Personal operations system and AI chief-of-staff concept |
| Primary focus | Prioritization, planning, personal operations, and decision support |
| Alternate name | Onyx Ghost |
| Current stage | Private working system under active development |
| Public source code | Not included |
| Creator | Rafael Saninocencio |

## Why This Project Exists

Managing work, family responsibilities, bills, health goals, job applications, learning plans, creative projects, and long-term ideas across separate apps creates unnecessary friction. Important information becomes scattered, priorities compete with one another, and the user spends too much time deciding what to do next.

Chief of Staff OG was created to act as a personal operating layer: one place to collect priorities, surface what matters, and support better daily decisions.

The system is not intended to replace human judgment. Its purpose is to make that judgment easier by organizing context, reducing noise, and presenting the next useful action.

## Core Use Case

At the beginning of the day, the system should help answer:

- What requires attention today?
- Which task has the greatest consequence if ignored?
- What deadlines, bills, messages, or applications are approaching?
- Which personal and professional goals are currently active?
- What can be delayed, delegated, grouped, or removed?
- What progress has been made across ongoing projects?

## Current and Planned Capabilities

### Daily briefing

A concise operational summary designed to surface the most important information for the day.

### Priority management

Tasks are organized by urgency, consequence, effort, and relationship to larger goals rather than treated as one undifferentiated list.

### Goals and project tracking

The system maintains visibility across career, financial, health, education, family, creative, and technical initiatives.

### Notes and brain-dump capture

Unstructured thoughts can be captured quickly, then organized into actions, projects, references, or archived material.

### Career operations

The design includes support for job applications, recruiter messages, interview preparation, study plans, and portfolio development.

### Personal operations

Planned views include bills due, weight and health tracking, important family responsibilities, and recurring commitments.

### Communication awareness

Future integrations may surface important email, calendar events, and other time-sensitive information without forcing the user to check multiple systems manually.

## System Structure

The private working system is organized around clear operational domains:

```text
chief-of-staff-og/
├── README.md
├── AGENTS.md
├── 00-owner-context/
├── 01-goals/
├── 02-projects/
├── 03-systems/
├── 04-finance/
├── 05-career/
└── 99-archive/
```

This structure separates permanent context, active goals, ongoing projects, reusable systems, financial information, career work, and archived material.

## Product Principles

### 1. Reduce decision fatigue

The system should narrow the field of choices and clearly identify the highest-value next action.

### 2. Preserve context

Recommendations should reflect the user's real responsibilities, constraints, active projects, and long-term direction.

### 3. Separate signal from noise

Not every task deserves equal visibility. The dashboard and briefings should emphasize consequence and relevance.

### 4. Keep the human in control

AI can organize, summarize, compare, and recommend. Final decisions remain with the user.

### 5. Build for trust

Private information, credentials, financial details, personal communications, and sensitive context must remain protected.

## Development Roadmap

### Phase 1: Structured tracking

- Define owner context
- Organize goals and active projects
- Build repeatable daily and weekly review systems
- Establish task and priority logic
- Create a consistent information architecture

### Phase 2: AI interpretation

- Summarize active responsibilities
- Recommend daily priorities
- Identify overdue or neglected commitments
- Turn notes into structured actions
- Surface conflicts between goals, time, and resources

### Phase 3: Connected operations

Potential integrations include:

- Gmail
- Google Calendar
- Job-search sources
- Local AI through Ollama
- Messaging or notification tools such as Telegram

Any integration must be implemented with explicit privacy controls and limited access.

## AI-Assisted Development

Artificial intelligence has been used as a collaborator for planning, organizing information, drafting system logic, refining workflows, and exploring integrations.

The project concept, operating philosophy, priorities, personal context, acceptance criteria, and final decisions are human-led.

## Skills Demonstrated

- AI product strategy
- Personal operations design
- Information architecture
- Workflow design
- Requirements definition
- Prioritization systems
- Knowledge management
- Automation planning
- Privacy-aware product thinking
- Iterative system development

## Security and Privacy

Chief of Staff OG is intentionally documented at a high level because the working system may contain sensitive personal information.

The public portfolio will not include:

- Credentials, tokens, or API keys
- Private email or calendar content
- Financial account details
- Personal addresses or identifying records
- Private family information
- Internal system paths or network information
- Raw owner-context files

> The private implementation demonstrates the system. This public documentation demonstrates the product thinking, architecture, and operational design without exposing protected information.

## Project Boundaries

This portfolio entry represents the current Chief of Staff OG system and its development direction. It is not presented as a commercially released product, a fully autonomous agent, or a replacement for professional financial, medical, legal, or career advice.

## Status

**Active private development.** Public documentation will expand as components can be safely separated from personal data.

## Creator

**Rafael Saninocencio**  
GitHub: `rsanino-tech`
