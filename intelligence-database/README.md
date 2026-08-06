# Meadows Intelligence Database

A property-first employer intelligence project designed to reconstruct a large commercial ecosystem from fragmented public records.

## Business Problem

Job boards hide many employers, especially small manufacturers, distributors, contractors, laboratories, professional firms, and businesses with limited online visibility. A company-first web search produced an incomplete list because it did not first establish the physical structure of the business complex.

## Solution Approach

The project uses a controlled research hierarchy:

`Development -> Parcel -> Building -> Address -> Suite -> Occupancy -> Company`

The workflow begins by mapping the physical environment, then identifies occupants and classifies companies by dynamically discovered industry.

## Current Status

**Active build / research system.**

The live working dataset is maintained privately because it contains research notes, unresolved records, source links, and location-level information. This public case study documents the methodology, data model, governance rules, and portfolio value without exposing private working data.

## Core Capabilities

- Property-first scope definition and geofence control
- Parcel, building, address, and suite inventory design
- Multi-source company discovery and verification
- Dynamic industry classification
- Duplicate and contradiction tracking
- Evidence-tier and confidence documentation
- Building and suite coverage auditing
- Human-in-the-loop archive workflow
- Research logs and unresolved-record queues
- Spreadsheet-based operational intelligence

## Human-Control Rule

Companies are not automatically discarded. Records remain in the active review dataset until the user manually marks a row for archival. Status and uncertainty are documented without allowing the system to make consequential exclusion decisions by itself.

## Data Model

The public schema template is available in [`schema.csv`](./schema.csv).

Primary entities include:

- Subdevelopments
- Parcels
- Buildings
- Suites and commercial spaces
- Occupancy relationships
- Companies
- Industries
- Verification sources
- Contradictions
- Research actions

## Workflow

1. Establish the master development boundary.
2. Identify all associated subdevelopments and parcels.
3. Inventory every commercial building and address.
4. Enumerate known suites, units, bays, and spaces.
5. Research occupants through official, commercial, regulatory, and historical sources.
6. Classify each company by actual business activity.
7. Log conflicts, missing spaces, and verification gaps.
8. Audit coverage against the physical capacity of each building.
9. Preserve human review before archiving or excluding records.

## Skills Demonstrated

- AI-assisted research orchestration
- Workflow and systems design
- Requirements definition
- Data modeling
- Process controls
- Human-in-the-loop governance
- Research validation
- Data quality management
- Operational documentation
- Continuous improvement

## Portfolio Value

This project demonstrates the ability to take a vague operational objective—"find every employer in a large business complex"—and convert it into an auditable intelligence workflow with clear entities, controls, completion gates, and exception handling.

## Privacy

The public repository contains no private credentials, personal messages, restricted records, or unredacted working datasets. Example records must be fictional or sanitized.
