---
title: Extend the Solution
description: Provides an overview of how to extend the Return to the Workplace solution.
author: v-jogha
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/25/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Overview

This article provides a detailed description of the data model, workflows, and flows used by the Return to the Workplace solution. The solution extends the Common Data Model and
utilizes several components of the Common Data Model. Administrators, developers, and end users should be mindful of the solution and possible implications of
other solutions that coexist in the same environment. The definitions provided in this document indicate the intended purpose of the entities, relationships, attributes, flows, and workflows contained in the Return to the Workplace solution. These definitions may be fully or partially adopted depending on your business
requirements.

## Integration and extension

Return to the Workplace solution is built on the Microsoft Power Platform. Additional information on working with model-driven apps and Common Data Service
can be found at the following links:

- [Model-driven apps guide](https://docs.microsoft.com/powerapps/maker/model-driven-apps/model-driven-app-overview)

- [Common Data Service Developer Guide](https://docs.microsoft.com/powerapps/developer/common-data-service/overview)

- [Common Data Service entities](https://docs.microsoft.com/powerapps/developer/common-data-service/entities)

- [Work with data using code in Common Data Service](https://docs.microsoft.com/powerapps/developer/common-data-service/work-with-data-cds)

- [Best practices and guidance for the Common Data Service](https://docs.microsoft.com/powerapps/developer/common-data-service/best-practices/)

- [Business Process Flows](https://docs.microsoft.com/power-automate/business-process-flows-overview)

Future releases of the Return to the Workplace solution are planned to create additional capabilities. Follow Microsoft solution and application lifecycle
management guidance to maintain solution integrity.

- [Introduction to Solutions](https://docs.microsoft.com/powerapps/developer/common-data-service/introduction-solutions)

- [Application lifecycle management (ALM) with Microsoft Power Platform](https://docs.microsoft.com/power-platform/alm/)

Additional information regarding supported extension methods can be found here:

- [Get started with Model-driven apps customization using code](https://docs.microsoft.com/powerapps/developer/model-driven-apps/supported-customizations#unsupported-customizations)

## Entity relationship diagram

The entity relationship diagram shown below illustrates the entities and their relationships. System-generated entities and relationships (such as those used for **Created By** and **Modified By** attributes) are not depicted in the diagram.

![Entity Relationship Diagram](media/data-dictionary-ERD.png)

## Entities

The entities listed below are grouped by the application in the Return to the Workplace solution.

## Core entities

These entities are used across multiple applications and are considered core to the platform.

| **Entity Name**          | **Information in the Table**                                                                                  |
|--------------------------|---------------------------------------------------------------------------------------------------------------|
| Country                  | Contains standard country names.                                                                              |
| Employee                 | Contains people and basic contact information.                                                                |
| Facility                 | Contains basic demographic information on a physical place and reopen phase planning progress.               |
| Facility Group           | Contains logic grouping metadata used to create a hierarchical relationship of facilities.                    |
| Facility Type            | Contains metadata used to segment facilities.                                                                 |
| Solution Setting         | Contains metadata used to drive platform behavior for specific facility groups.                               |
| State                    | Contains standard state names.                                                                                |

## Employee Return to the Workplace

These entities are primarily used by the Employee Return to the Workplace canvas application.

| **Entity Name**          | **Information in the Table**                                                                                  |
|--------------------------|---------------------------------------------------------------------------------------------------------------|
| Area                     | Contains a list of physically or logically segmented spaces.                                                  |
| Floor                    | Contains a list of physically segmented spaces associated to a single facility and multiple areas.            |
| Daily Occupancy          | Daily occupancy indicates the capacity and occupancy for an area on a certain day.                            |
| Employee Attestation     | Contains associations of people to their attestations.                                                        |
| Employee Booking         | Contains associations of people and specific areas, floors, and facilities for a given time.           |
| Employee Facility Search | Contains a list of most recently used employee app facility results associated with system users.             |
| Employee Sentiment       | Contains associations of people and information relevant to their recorded sentiment.                         |
| Employee Visit           | Contains associations of people and facilities for a given time representing a physical entry and exit.|

## Workplace Care Management

These entities are primarily used by the Workplace Care Management model-driven application.

| **Entity Name**          | **Information in the Table**                                                                                  |
|--------------------------|---------------------------------------------------------------------------------------------------------------|
| Case Contact             | Contains individuals associated with an employee case.                                                        |
| Case Facility            | Contains facilities associated with employee cases.                                                           |
| Employee Case            | Contains associations of people and information relevant to their case.                                       |

## Facility Safety Management

These entities are primarily used by the Facility Safety Management model-driven application.

| **Entity Name**          | **Information in the Table**                                                                                  |
|--------------------------|---------------------------------------------------------------------------------------------------------------|
| Goal                     | Contains associations of reopen phases and key metrics with target values.                                    |
| Key Metric               | Contains a list of measurable indications to evaluate progress.                                               |
| Measurement              | Contains a list of key metric values measured at a point in time with relation to a facility.                 |
| Readiness Category       | Contains metadata used to group readiness factors.                                                            |
| Readiness Check          | Contains a list of activities and their status associated with a checklist at a given facility.               |
| Readiness Checklist      | Contains a group of activities associated with a facility and a reopening phase.                              |
| Readiness Factor         | Contains a list of items that are evaluated through the reopening process.                                    |
| Reopen Phase             | Contains a list of associated readiness factors and metrics to be tracked and evaluated at the current stage. |
| Reopen Phase Transition  | Contains a list of requests to move from one phase to another with relevant process information.              |


## Data definitions

This section of the document provides a list of entities, their data attributes,
and the areas of the solution where they are used. System-generated attributes
(such as **Created On**, **Modified On**, etc.) are not displayed.

### Area

| Display Name  | Data Type     | Description     | Platform Use     |
|---------------|---------------|-----------------|------------------|
| Area  | Text | Primary identifier of the record. | Model-driven app and Canvas app |
| Capacity | Whole Number| Used to capture total allowable occupancy for the area. | Model-driven app and canvas app |
| Capacity of Current Phase | Whole Number    | Used to capture allowable occupancy for the area in the current phase.| Model-driven app and canvas app|
| Description   | Text  | Used to capture additional details to describe the area.| Model-driven app and canvas app |
| Facility | Lookup | Used to associate the parent facility. |Model-driven app and canvas app |
| Floor | Lookup | Used to associate the parent floor. | Model-driven app and canvas app |

### Case Contact

| Display Name | Data Type | Description   | Platform Use |
|-----------|---------------|----------------|------------------|
| Name | Text  | Primary identifier of the record. | Model-driven app |
| Do you feel safe returning to work? | Option Set    | The question label used by the canvas app. | Canvas app   |
| Employee | Lookup  | Used to capture the employee.  | Canvas app       |
| Sentiment Date | Date and Time | Used to capture the point in time the sentiment was collected. | Canvas app   |

### Case Facility

| Display Name  | Data Type | Description | Platform Use     |
|---------------|-----------|-------------|------------------|
| Name          | Text      | Primary identifier of the record.                           | Model-driven app |
| Employee Case | Lookup    | Used to associate the employee case with the case facility. | Model-driven app |
| Facility      | Lookup    | Used to associate the facility with the case facility.      | Model-driven app |

### Country

| Display Name   | Data Type | Description                        | Platform Use     |
|----------------|-----------|------------------------------------|------------------|
| Name           | Text      | User-friendly name of the country. | Model-driven app |
| ISO Short Code | Text      | ISO identifier of the country.     | Model-driven app |

### Daily Occupancy

| Display Name     | Data Type    | Description   | Platform Use                 |
|------------------|--------------|------------------|------------------------------|
| Area ID          | Lookup       | Used to associate an area to the daily occupancy. | Model-driven app and canvas app |
| Facility ID      | Lookup       | Used to associate a facility to the daily occupancy.| Model-driven app and canvas app |
| Capacity         | Whole Number | Total capacity for that area.| Model-driven app and canvas app |
| Occupancy        | Whole Number | Occupied spaces for an area. | Model-driven app and canvas app |
| Date             | Date         | The date for which the occupancy and capacity are tracked. | Model-driven app and canvas app |

### Employee (Contact)

| Display Name     | Data Type | Description   | Platform Use |
|------------------|-----------|------------|----------------|
| Default Facility | Lookup    | Used to associate a facility to the employee. | Model-driven app and canvas app |
| User ID          | Text      | Used to provide a unique identifier specific to the organization for the employee. | Model-driven app |

### Employee Attestation

| Display Name     | Data Type     | Description  | Platform Use  |
|------------------|---------------|-------------------------------------------|------------------------------|
| Attestation Date | Date and Time | Used to capture the date and time the attestation was recorded.     | Model-driven app             |
| Attested         | Option Set    | Used to capture if the employee attested: Yes, No                   | Model-driven app and canvas app |
| Employee         | Lookup        | Used to denote the employee completing the attestation.             | Model-driven app             |
| Facility         | Lookup        | Used to associate the facility for which the employee is attesting. | Model-driven app and canvas app |
| Name             | Text          | Used to create a name for the employee attestation record.          | Model-driven app             |

### Employee Booking

| Display Name     | Data Type     | Description   | Platform Use |
|------------------|---------------|---------------|------------------|
| Area | Lookup | Used to associate the location booked. | Model-driven app and canvas app|
| End Arrival Time | Date and Time    | Used to capture the ending point in time for the booking. | Model-driven app; Canvas app |
| Start Arrival Time  | Date and Time | Used to capture the beginning point in time for the booking. | Model-driven app and canvas app|
| Booking Date     | Date          | Used to determine the date of the booking.| Model-driven app and canvas app |
| Employee         | Lookup        | Used to associate the employee creating the booking. | Model-driven app and canvas app|
| Name             | Text          | Primary identifier of the record. | Model-driven app |

### Employee Case

| Display Name                    | Data Type     | Description                                                                                      | Platform Use                 |
|---------------------------------|---------------|--------------------------------------------------------------------------------------------------|------------------------------|
| Case Number                     | Text          | Unique identifier for the employee case.                                                         | Model-driven app             |
| Check In Available              | Option Set    | Used to denote whether the employee can get a pass for a facility.                               | Model-driven app and canvas app |
| Check In Available Date         | Date and Time | Used to specify when the employee will be able to get a pass for a facility.                     | Model-driven app             |
| Employee                        | Lookup        | Used to associate the employee to the employee case.                                             | Model-driven app             |
| Employee Contacted              | Option Set    | Used to denote whether the employee was contacted.                                               | Model-driven app             |
| Employee Instructions Provided  | Option Set    | Used to denote whether the employee was provided instructions.                                   | Model-driven app             |
| Public Health Official Notified | Option Set    | Used to denote whether the appropriate public health officials have been notified if applicable. | Model-driven app             |
| Risk Assessment                 | Option Set    | Used to denote the current risk of the employee case.                                            | Model-driven app             |
| Screened                        | Option Set    | Used to denote whether the screening process has occurred.                                       | Model-driven app             |
| First Time Employee Contacted   | Date and Time | Marked by a workflow and used to in the Power BI dashboards to track performance.                | Model-driven app             |
| First Time to Investigation     | Date and Time | Marked by a workflow and used to in the Power BI dashboards to track performance.                | Model-driven app             |

### Employee Facility Search

| Display Name | Data Type | Description                                         | Platform Use                 |
|--------------|-----------|-----------------------------------------------------|------------------------------|
| Employee     | Lookup    | Used to capture the employee conducting the search. | Model-driven app and canvas app |
| Facility     | Lookup    | Used to capture the facility searched.              | Model-driven app and canvas app |

### Employee Sentiment

| Display Name                       | Data Type     | Description                                                      | Platform Use                 |
|------------------------------------|---------------|------------------------------------------------------------------|------------------------------|
| Employee                           | Lookup        | Used to capture the employee completing the sentiment.           | Model-driven app and canvas app |
| Name                               | Text          | Used to provide a name for the employee sentiment record.        | Model-driven app             |
| Do you feel safe returning to work | Option Set    | Used to capture a response to the question: Sad, Neutral, Happy. | Model-driven app and canvas app |
| Sentiment Date                     | Date and Time | Used to capture the date and time the sentiment was recorded.    | Model-driven app             |

### Employee Visit

| Display Name     | Data Type     | Description  | Platform Use   |
|------------------|---------------|--------------|----------------|
| Employee Attestation | Lookup | Used to associate an attestation.     | Model-driven app             |
| Employee Booking     | Lookup | Used to associate a booking.     | Model-driven app             |
| Employee              | Lookup        | Used to associate the employee creating the visit. | Model-driven app |
| End Time              | Date and Time | Used to denote the end of the visit.     | Model-driven app             |
| Facility              | Lookup          | Used to denote the facility visited.         | Model-driven app             |
| Name                  | Text | Primary identifier of the record.     | Model-driven app             |
| Start Time            | Date and Time | Used to denote the beginning of the visit.     | Model-driven app             |

### Facility 

| Display Name           | Data Type | Description                                                 | Platform Use     |
|------------------------|-----------|-------------------------------------------------------------|------------------|
| Address Street 1       | Text      | Used to provide address information for the facility.       | Model-driven app |
| Address Street 2       | Text      | Used to provide address information for the facility.       | Model-driven app |
| Address City           | Text      | Used to provide address information for the facility.       | Model-driven app |
| Address Country        | Lookup    | Used to associate the standardized state to the facility.   | Model-driven app |
| Address Latitude       | Text      | Used to provide address information for the facility.       | Model-driven app |
| Address Longitude      | Text      | Used to provide address information for the facility.       | Model-driven app |
| Address Postal Code    | Text      | Used to provide address information for the facility.       | Model-driven app |
| Address State/Province | Lookup    | Used to associate the standardized state to the facility.   | Model-driven app |
| Description            | Text      | Used to provide address information for the facility.       | Model-driven app |
| Group                  | Lookup    | Used to associate the group this facility belongs to.       | Model-driven app |
| Number                 | Text      | Used to provide a recognizable identifier for the facility. | Model-driven app |
| Type                   | Lookup    | Denotes the facility type.                                  | Model-driven app |
| Name                   | Text      | Used to provide a recognizable name for the facility.       | Model-driven app |
| Reopen Phase           | Lookup    | Used to associate the current reopen phase.                 | Model-driven app |

### Facility Group

| Display Name          | Data Type | Description                                                  | Platform Use     |
|-----------------------|-----------|--------------------------------------------------------------|------------------|
| Description           | Text      | Used to provide additional details about the facility group. | Model-driven app |
| Name                  | Text      | Used to provide a name for the facility group.               | Model-driven app |
| Parent Facility Group | Lookup    | Used to group facilities in a hierarchical manner.           | Model-driven app |

### Facility Type

| Display Name | Data Type | Description                                                 | Platform Use     |
|--------------|-----------|-------------------------------------------------------------|------------------|
| Description  | Text      | Used to provide additional details about the facility type. | Model-driven app |
| Type         | Text      | Used to provide a name for the facility type.               | Model-driven app |

### Floor

| Display Name                        | Data Type     | Description                                                    | Platform Use     |
|-------------------------------------|---------------|----------------------------------------------------------------|------------------|
| Description | Text    | Used to capture additional details to describe the floor.                     | Model-driven app and canvas app       |
| Facility                      | Lookup | Used to associate the parent facility. |Model-driven app and canvas app     |
| Floor                                | Text          | Primary identifier of the record.                              | Model-driven app and canvas app |
| Floor Index                    | Whole Number  | Used to create a structured order of floors within a facility. | Model-driven app and canvas app       |


### Goal

| Display Name | Data Type  | Description                                                                                              | Platform Use     |
|--------------|------------|----------------------------------------------------------------------------------------------------------|------------------|
| Key Metric   | Lookup     | Used to associate the appropriate key metric.                                                            | Model-driven app |
| Name         | Text       | Used to provide a name for the goal.                                                                     | Model-driven app |
| Reopen Phase | Lookup     | Used to associate the appropriate reopen phase.                                                          | Model-driven app |
| Target Type  | Option Set | Used to designate if the target value should be higher or lower than the value provided by target value. | Model-driven app |
| Target Value | Decimal    | The value used to evaluate success.                                                                      | Model-driven app |

### Key Metric

| Display Name | Data Type | Description                                | Platform Use     |
|--------------|-----------|--------------------------------------------|------------------|
| Name         | Text      | Used to provide a name for the key metric. | Model-driven app |

### Measurement

| Display Name     | Data Type     | Description                                                                       | Platform Use     |
|------------------|---------------|-----------------------------------------------------------------------------------|------------------|
| Facility Group   | Lookup        | Used to associate the appropriate facility group.                                 | Model-driven app |
| Facility         | Lookup        | Used to associate the appropriate facility.                                       | Model-driven app |
| Key Metric       | Lookup        | Used to associate the appropriate key metric.                                     | Model-driven app |
| Measurement Date | Date and Time | Denotes the date and time a measurement was taken displayed in user local format. | Model-driven app |
| Name             | Text          | Used to provide a name for the measurement.                                       | Model-driven app |
| Value            | Decimal       | Used to capture the value of the measurement.                                     | Model-driven app |

### Readiness Category

| Display Name | Data Type | Description                                     | Platform Use     |
|--------------|-----------|-------------------------------------------------|------------------|
| Category     | Text      | Used to provide a name for the category record. | Model-driven app |

### Readiness Check

| Display Name        | Data Type   | Description                                                                  | Platform Use                 |
|---------------------|-------------|------------------------------------------------------------------------------|------------------------------|
| Comment             | Text        | Used to capture additional notes about the readiness check.                  | Model-driven app and canvas app |
| Factor              | Lookup      | Denotes the factor being checked.                                            | Model-driven app and canvas app |
| Check Completed     | Two Options | Denotes completion of the readiness check.                                   | Model-driven app and canvas app |
| Name                | Text        | Denotes the readiness check name.                                            | Model-driven app and canvas app |
| Readiness Checklist | Lookup      | Used to associate the readiness check to the applicable readiness checklist. | Model-driven app and canvas app |

### Readiness Checklist

| Display Name | Data Type | Description                                                       | Platform Use     |
|--------------|-----------|-------------------------------------------------------------------|------------------|
| Description  | Text      | Used to provide additional details for this checklist.            | Model-driven app |
| Facility     | Lookup    | Used to designate the applicable facility for this checklist.     | Model-driven app |
| Name         | Text      | Denotes the readiness checklist name.                             | Model-driven app |
| Reopen Phase | Lookup    | Used to designate the applicable reopen phase for this checklist. | Model-driven app |

### Readiness Factor

| Display Name | Data Type | Description                                                   | Platform Use     |
|--------------|-----------|---------------------------------------------------------------|------------------|
| Category     | Lookup    | Used to group factors by the standard set of category values. | Model-driven app |
| Description  | Text      | Used to provide additional detail about the readiness factor. | Model-driven app |
| Factor       | Text      | The primary name of the readiness factor.                     | Model-driven app |

### Reopening Phase

| Display Name | Data Type    | Description                                          | Platform Use                 |
|--------------|--------------|------------------------------------------------------|------------------------------|
| Description  | Text         | Used to document details about the reopen phase.     | Model-driven app and canvas app |
| Name         | Text         | The name of the reopen phase.                        | Model-driven app             |
| Index        | Whole Number | Used to provide a logical sequence to reopen phases. | Model-driven app             |

### Reopen Phase Transition

| Display Name          | Data Type  | Description                                                                   | Platform Use     |
|-----------------------|------------|-------------------------------------------------------------------------------|------------------|
| Name                  | Text       | The primary identifier of the record.                                         | Model-driven app |
| Facility              | Lookup     | Used to associate the applicable facility.                                    | Model-driven app |
| Proposed Reopen Phase | Lookup     | Used to capture the reopen phase the facility is attempting to transition to. | Model-driven app |
| Current Reopen Phase  | Lookup     | Used to capture the current reopen phase of the applicable facility.          | Model-driven app |
| Review Comments       | Text       | Used to capture notes from the review.                                        | Model-driven app |
| Reviewer              | Lookup     | Used to associate the appropriate reviewer to the transition record.          | Model-driven app |
| Review Status         | Option Set | Used to denote the current status of the reopen phase transition.             | Model-driven app |
| Summary               | Text       | Used to provide an additional context of the transition.                      | Model-driven app |

### Solution Setting

| Display Name         | Data Type  | Description                                                              | Platform Use                 |
|----------------------|------------|--------------------------------------------------------------------------|------------------------------|
| Health Contact Email | Text       | Used to capture the email address of the primary health contact.         | Model-driven app and canvas app |
| Health Contact Name  | Text       | Used to capture the name of the primary health contact.                  | Model-driven app and canvas app |
| Health Contact Phone | Text       | Used to capture the phone number of the primary health contact.          | Model-driven app and canvas app |
| Maximum Temperature  | Decimal    | Used to set the value of the temperature question in the canvas app.     | Canvas app                   |
| Minimal Temperature  | Decimal    | Used to set the value of the temperature question in the canvas app.     | Canvas app                   |
| Name                 | Text       | The primary name of the setting record.                                  | Model-driven app             |
| Target Temperature   | Decimal    | Used to set the value of the temperature question in the canvas app.     | Canvas app                   |
| Temperature Scale    | Option Set | Used to display the value of the temperature question in the canvas app. | Canvas app                   |

### State

| Display Name | Data Type | Description                        | Platform Use     |
|--------------|-----------|------------------------------------|------------------|
| Name         | Text      | User-friendly name of the state.   | Model-driven app |
| State Code   | Text      | ISO identifier of the state.       | Model-driven app |
| Country      | Lookup    | Association to the parent company. | Model-driven app |

## Power Automate Flows

This section of the solution describes the different flows within the solution and explains their different purposes.
These flows can be extended, used, or turned off depending on the business requirements.

| Flow | Entity | Description                        |
|--------------|-----------|-------------------------------------------------|
| Area - Update Capacity for future Occupancies         | Area      | Updates the daily occupancy when then capacity changes on an area |
| Area - Update Capacity of Current Phase   | Area      | Updates the capacity of a current phase when a capacity changes |
| Checklist - Generate Checks      | Checklist    | Generate checks based on readiness factors linked to the reopen phase |
| Checklist - Update Checks      | Checklist    | Makes readiness checks inactive or active based on status changes of the checklist |
| Employee Booking - Update Daily Occupancy      | Employee Booking    | Create or update daily occupancy when an employee booking is created |
| Employee Booking - Update Daily Occupancy on Status      | Employee Booking    | Readucate occupancy in daily occupancy when employee bookings are disabled |
| Employee Visit - Name and match to booking or attestation      | Employee Visit    | Sets the name of the employee visit and matches a visit to bookings and attestations |
| Facility - Apply and Update Phase      | Facility    | Applies a new phase to a facility, which creates a checklist, changes the business process flow and updates the capacities |
| Reopen Phase - Update Capacity      | Reopen phase    | Update capacity when the capacity limits change for a reopen phase |
| Reopen Phase Transition - Update facility reopen phase      | Reopen phase transition    | Updates and changes the reopen phase for a facility |

For the solution, we generate sample data, which makes records every 12 hours to simulate real life.
As mentioned in [Configure the Solution](configure.md), dependent on the purpose of your environment you can disable these flows.

| Flow  | Description                        |
|--------------|--------------------------------------------------|
| Sample Data - Create and Update Employee Cases          | Create employee cases and move them through the different stages |
| Sample Data - Generate Employee Records      | Create employee bookings and employee attestations |
| Sample Data - Generate Facility Transitions   | Create reopen phase transitions and move facilities to other phases  |
| Sample Data - Visits          | Create employee visits |




