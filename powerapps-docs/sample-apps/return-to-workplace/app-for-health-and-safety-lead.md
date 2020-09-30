---
title: Use the Workplace Care Management app
description: Provides an overview of how to use the Workplace Care Management app.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/25/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Workplace Care Management app

This article provides step-by-step instructions to case managers in the organization for using the Workplace Care Management app to manage employee cases. 

To assist Health and Safety Leads, and to help ensure proper case handling, this app implements a four-step process. The current stage of an employee case is clearly depicted in the business process flow on the employee case form. Employee cases will be managed through the following process stages:

![Business process flow](media/health-safety-employee-case-bpf.png "Business process flow")

1. **Open** – In this stage, you record basic information about the case. At this moment, you as a Health and Safety Lead also become the case manager.

2. **Investigating** – In this stage, you perform steps to ensure that employee checks and screenings are being completed in accordance with company policy. The result of these checks is a clear instruction to the employee. When this is communicated to the employee, the case is moved to the next stage.

3. **Monitoring** – After the investigating stage is complete and the employee has been given instructions or guidelines, they're monitored until they're
healthy enough to be eligible to return to the workplace.

4. **Resolve** – This is the wrap-up stage for the case, where you can enter closing remarks.

You use this app to:

- [Manage employee and case managers data](#manage-employee-and-case-managers-master-data).

- [Manage employee cases](#manage-employee-cases).

## App at a glance

The left pane lists all the components available in the **Employee Cases** area.

> [!div class="mx-imgBorder"]
> ![Employee case view](media/health-safety-employee-case-view.png "Employee case view")

## App components

The Workplace Care Management app has the following components:

**Employee cases** 

> [!div class="mx-imgBorder"]
> ![List of Employee cases](media/health-safety-employee-cases.png "List of Employee cases")

- **Dashboard** - Gives you a dashboard were you can track the status of employee cases.

- **Employee Case** - List of all the employees. Employees are contacts. In the Employee Cases component, we have three views with different filters:

   - My Employee Cases: Filtered by owner and only shows active cases. This is the default view.

   - Active Employee Cases: Shows all the active employee cases. An employee case is considered active when the status field value is set to active. Active Employee Cases are limited to one per employee.

   - Closed Employee Cases: Shows all the closed employee cases. An employee case is considered closed when it is made inactive either by the case manager or through the process.

> [!div class="mx-imgBorder"]
> ![Employee cases](media/health-safety-employee-case-view-myemployeecases.png "Employee cases")

**Master data**

- **Employee** - List of all the employees. Employees are contacts.

- **Case managers** - List of all the users who have access to the **Employee Cases** area.

> [!div class="mx-imgBorder"]
> ![Master data](media/health-safety-master-data.png "Master data")

## Getting started with the Workplace Care Management app

Employee safety is the main goal for Health and Safety Leads. You use this app to decide whether to revoke an employee's ability to check in to the workplace. The goal of the care management is to provide a clear insight into the work backlog and to make sure that the same process is used to manage all cases.

At the case level, no additional personal or privacy-related information is
stored or gathered. The case must be regarded as a checklist that proper
procedures have been applied.

## Manage employee and case managers master data

### Manage employees

You can create a new employee contact if the contact doesn't exist.

**To create an employee contact**

1. Select **Employee** in the left pane, and then select **New**.

   > [!div class="mx-imgBorder"]
   > ![Create a contact](media/health-safety-employee-new.png "Create a contact")

2. Enter appropriate values in the fields:

   | **Field**   | **Description**  |
   |---------------|------------------|
   | User ID| Enter the employee user ID. |
   | First Name | Enter the first name of the employee. |
   | Middle Name | Enter the middle name of the employee. |
   | Last Name | Enter the last name of the employee.  |
   | Default Facility | Select the employees default facility. |
   | Default Area | Select default area. |
   | Assigned Area | Select an assigned area for the employee. |
   | Email | Enter an employee email address. |
   | Business Phone| Enter the employee mobile or phone number. |
   | Preferred Method of Contact | Select the method of contact the employee prefers from the drop-down list. |
   | Conact Type | Select 'Employee'. |

   > [!div class="mx-imgBorder"]
   > ![Create a contact details](media/health-safety-employee-new2.png "Create a contact details")

3. Select **Save & Close**. The newly created record is available in the
    **Active Contacts** view.

To edit the record, select it, update the values, and then select **Save & Close**.

### Manage case managers

Access to employee cases is restricted to only part of the organization. You can view a list of case managers who can manage employee cases.

**To view the list of case managers**

1. Select **Case Managers** in the left pane.

   > [!div class="mx-imgBorder"]
   > ![View case managers](media/health-safety-case-manager-view.png "View case managers")

2. Select the user record you're interested.

   > [!div class="mx-imgBorder"]
   > ![Select a user](media/health-safety-case-manager-form.png "Select a user")

3. Select **Save & Close**.

To edit the record, select it, update the values, and then select **Save & Close**.

## Manage employee cases

The following illustration of the case manager process explains how a case is created and managed by capturing different data at various stages to identify, investigate, and resolve the case. When a case manager is notified, an employee case is created. The employee case is taken through stages where you get more details and perform a screening (investigating), provide instructions (monitoring), and close the case (resolved).

> [!div class="mx-imgBorder"]
> ![Process flow](media/health-safety-process-flow.png "Process flow")

### Employee case creation

Case managers are the resource who manages employee cases.

1. Select **Employee Cases** from the left pane, and then select **New**.

   > [!div class="mx-imgBorder"]
   > ![New case](media/health-safety-employee-case-new.png "New case")

2. Enter the employee name for the new case.

   > [!div class="mx-imgBorder"]
   > ![Enter name](media/health-safety-employee-case-form.png "Enter name")

3. Save the record.

### Managing a case – moving a case through the process stages

#### Open

This is the first process stage. The Health and Safety Lead starts the case and can verify that all basic information is available. The Health and Safety Lead becomes the case manager and will verify the employee details and assign the case to a different case manager. The key pieces of data to be captured and recorded before moving to the next stage are:

- Health & Safety Lead - Case manager owning the case.

  > [!div class="mx-imgBorder"]
  > ![Open stage](media/health-safety-bpf-open1.png "Open stage")

#### Investigating

In this process stage, the case manager contacts the employee to verify how the employee is feeling, and continues to investigate by capturing and recording the case-related data and updating fields on the case form.
The key pieces of data to be captured and recorded before moving to the next stage are:

- Employee Contacted (Yes/No)

- Screened (Yes/No)

- Risk Assessment

  > [!div class="mx-imgBorder"]
  > ![Investigation stage](media/health-safety-bpf-investigating1.png "Investigation stage")

#### Monitoring

In this process stage, the case manager monitors and manages the cases, ensuring that guidance or instructions that were provided are being followed and that expected target dates for being eligible to return to work are updated for the employee. This stage can be regarded as a holding stage, meaning that it's clear when the next moment of contact will be and when the case needs to be followed up on. The key pieces of data to be captured and recorded before moving to the next stage are:

- Employee Instructions Provided (Yes/No)

  > [!div class="mx-imgBorder"]
  > ![Monitoring](media/health-safety-bpf-monitoring.png "Monitoring")
  
When you provided instructions you could for the time being indicate the employee is not able to enter a facility. When setting **Facility Access Available** to no, the employee won't be able to get a day pass. When you indicate that the facility access is not available on an employee case, you will be able to give **Employee Instructions** which are visible in the app. With the **Facility Access Available Date** you can indicate when the employee will be able to get a day pass again, a flow will automatically reset **Facility Access Available** when this date is reached.

#### Resolve

In this process stage, the case manager completes the process by resolving the
case, and selects **Finish**. After the process is finished, the employee case becomes inactive. The inactive employee case is then considered completed. The key pieces of data to be captured and recorded are:

- Employee Instructions Provided (Yes/No)

  > [!div class="mx-imgBorder"]
  > ![resolve](media/health-safety-bpf-resolve.png "Resolve")

### Complete Employee Case

After you complete the process and select **Finish** in the business process flow, the employee case will become inactive. You can also make employee cases inactive for certain reasons if the employee case is no longer being worked on. In that case, you can deactivate the employee case from the command bar. 

  > [!div class="mx-imgBorder"]
  > ![Deactivate Employee Case](media/health-safety-deactivate.png "Deactivate Employee Case")


## Manual Contact tracing

To facilitate manual contact tracing and tracking possible exposures, three elements have been added:

1. Exposures
2. Case Facilities
3. Case Contacts

### Exposures

When accounting for the whereabouts of an employee, the system stores valuable information in the form of bookings and attestations. That is why those records can be linked to a case. When doing so, a background process is triggered. This process does two things:

1. Create a Case facility record for that day.
2. Create Case Contacts for all the other employees that were:
  a. In the same Area as that person (10 points)
  b. In the same entry window for that facility (if applicable) (5 points)
  c. On the same Floor as that person (3 points)

These Case Contacts must be regarded as suggestions and can then be cleared by the case manager.

> [!NOTE]
> Case Contact record that are created as suggestions do not include guests that were registered.

> [!NOTE]
> These Case Contact suggestions only work for facilities where capacity management has been enabled. See the facility manager app chapter for guidance on how to setup floors and areas.

#### Link an Employee Attestation

To link an Attestation to a Case, follow these steps:

1. Open a Case and open the Exposures tab
2. In the grid, click **Add Existing Employee Attestation**
3. Use the lookup to search for Employee Attestations for the Employee under investigation
4. Select the applicable Employee Attestations and click **Add**

The Employee Attestation record is now linked to the case. This will trigger the background suggestion process that will create Case Contact suggestions that can assist in the manual contact tracing procedure.
Each Employee Attestation can only be linked to one case. If the duplicate detection rules have been setup, there can also be only one active case per employee. This prevents double work.

### Case facilities

As part of the investigation, a case manager might need to register which facilities are involved in this case. When you open an employee case, this can be done on the **Case Facilities** tab.

On the **Case Facilities** tab, select **New Case Facility** to relate a facility to this case. When the record is created, further details can be entered:

| **Field**   | **Description**  |
|---------------|------------------|
| Date From | Enter the start date of the employee visiting that facility. |
| Date To | Enter the end date of the employee visiting that facility.  |
| Comment | Enter additional information, when applicable. |

When a Case Facility is added as part of the suggestion process, both the Date From and Date To fields will be set to the day of the attestation.

### Case contacts

An employee under investigation might have had contact with one or more colleagues. This type of information can be logged on the **Case Contacts** tab.

On the **Case Contacts** tab, select **New Case Contact** to relate an employee to this case. When the record is created, further details can be entered:

| **Field**   | **Description**  |
|---------------|------------------|
| Exposure score | whole number used to sort the suggestions based on estimated exposure |
| Risk Assessment | This field provides an easy way to prioritize other employees based on their interactions with the employee under investigation. |
| Open Case | This can refer to an open case for this employee. By default the lookup will filter on active cases for this employee. If the record was added as a system suggestion, this field will be filled only if only one active case exists. |
| Comment | Enter additional information, when applicable. |

A case can be directly created from a Case Contact record. To do so, select the row in the subgrid and click on the **Create Case** button that appears. This button is only visible when one record is selected. The following actions are performed:
A new Employee Case gets created
- The new Employee Case is linked to the Case Contact record
- The new Employee Case has the Employee of the Case Contact record entered
- The new Employee Case is assigned to the current user
- The user is navigated to the newly created record
- The new Employee Case number is entered in the Open Case field on the Contact record
- The Case Contact record is deactivated with status 'Case Created'

A case manager can enter additional information. Click 'Save & Close' to return to the original Employee Case record.


#### Exposure Score

Exposure score is calculated when the system generates Case Contacts as suggestions when a Case manager links an attestation. The system will only create one record per person. If a person then shared area/entry window/floor via multiple attestations, the exposure score on the existing record is increased. For each day, a Case Contacts gets points only for the highest category applicable. For example; if a case contact suggestion shared Area on one day (10 points) and shared entry window on another day (5 points), the total exposure score for that Case Contact would be 15.

This functionality is purely as a means to sort the suggestions based on 'proximity' to the employee under investigation.

#### Case Contact status

A Case Contact has three statusses:
- To be evaluated (Active)
- Case Created (Inactive)
- Evaluated (Inactive)

With these three statusses, a case manager has the ability to clearly indicated which Case Contacts have been traced and how they have been dealt with.

  
## Overview of Employee Cases
For managing the whole process from beginning to end, you can use the **Workplace Care Management** dashboard. You will find the dashboard under **Dashboards**. The dashboard is separated with two different sections, on the top you will see the list of 4 different views which show different focusses on the employee cases and on the bottom it will show charts to get a quick overview.

  > [!div class="mx-imgBorder"]
  > ![Workplace Care Management Dashboard](media/health-safety-dashboard.png "Workplace Care Management Dashboard")

**Views**

- My High Risk Employee Cases; shows the employee cases which are on high risk.

- My Employee Cases due for Contact; shows the employee cases which aren't contacted yet for over a day.

- My Employee Cases due for Investigation; shows the employee cases which aren't investigated yet for over a day.

- My Outstanding Employee Cases; shows the employee cases outstanding for more then 2 weeks.

**Charts**

- Employee Cases by Risk Level; which shows employee cases by risk level.

- Employee Cases by Duration; which shows employee cases by duration over days.

## Feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.
