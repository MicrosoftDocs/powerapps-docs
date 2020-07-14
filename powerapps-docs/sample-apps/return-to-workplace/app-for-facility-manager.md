---
title: Use the facility safety management app
description: Provides an overview of facility safety management app.
author: wbakker
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/06/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Facility Safety Management app

The facility safety management app provides step-by-step instructions to facility managers in the organizations on how to use the app to manage the reopening and readiness of the facilities. This helps the organizations ensure that they can provide a safe working environment for employees to return to the workplace using the Return to the Workplace solution.

## App at a glance

The left pane lists all the components available in the **Facility Management** area.

> [!div class="mx-imgBorder"]
> ![Facility management](media/facility-manager-facility-active-facilities.png "Facility management")

## App components

The Facility Safety Management app has the following components:

**Facility Management**

-  **Facilities**-  List of the facilities (for example, buildings, plants, etc.) that require monitoring to reopen.

-  **Facility Groups** - Provides a flexible way to group facilities. For example, by campus, or geographical region.

-  **Areas** - Areas are sub-components of a facility used to distinguish
    the capacity of these sub-components over the various phases.

**Reopen Readiness**

-  **Phase Transitions** - A phase transition is used to create a request to transition to a new phase. When the transition is approved, the facility will be updated with the proposed phase.

-  **Readiness Factors** -  Readiness Factors are yes or no type questions regarding reopening a building. They are linked per Reopening Phase to a checklist on a facility.

- **Measurements** -  The actual values for a metric that allows us to track parameters over time. For a single metric, measurements can be entered per facility.

**Employee**

- **Employee Sentiment** -  Keeps track of general employee wellbeing. This is self-reported information, but it is a valuable parameter when tracked consistently over time and with bigger groups. This data is typically entered by employees using the employee app.

- **Employee Attestation** - Keeps track of employee health assessments or attestations based upon a series of questions answered by the employee. This data is typically entered by employees using the employee app.

## Manage and monitor facilities 

This section covers how to manage and monitor facilities.

### Create a facility 

By default, two facilities are provided as an example. To  create a new facility:

1. Select **Facilities** in the left pane and select **New**.

   > [!div class="mx-imgBorder"]
   > ![New facility ](media/facility-manager-facility-new.png "New facility")

2. Enter appropriate values in the fields:
 
   > [!div class="mx-imgBorder"]
   > ![New facility form](media/facility-manager-facility-form.png "New facility form")

   | **Field**              | **Description**                                |
   |------------------------|------------------------------------------------|
   | Facility Number        | Enter a number for the new facility.                  |
   | Name                   | Enter a  name for the new facility.                    |
   | Description            | Enter the description for the new facility.              |
   | Facility Type          | Select the appropriate facility type.   |
   | Facility Group         | Select appropriate facility group. |
   | Reopen Phase           | Select appropriate reopen phase.  |
   | Address Street 1       | Enter the address street 1 information.            |
   | Address Street 2       | Enter the address street 2 information.             |
   | Address Postal Code    | Enter postal code.         |
   | Address City           | Enter the city.               |
   | Address State/Province | Enter state or province.      |
   | Address Country        | Enter a country.        |

3. Select **Save & Close**. The newly created record is available in the
    **Active Facility Types** view.

To edit the record, select the newly created record, update the values as
required, and select **Save & Close**.

4. A facility can be assigned to a user, to do so switch to the **Active Facilities** view.

   > [!div class="mx-imgBorder"]
   > ![Active Facilities](media/facility-manager-active-facilities.png "Active Facilities")

5. Select a facility and click **Assign**, select the **User** to assign the facility to.

   > [!div class="mx-imgBorder"]
   > ![Assign](media/facility-manager-assign.png "Assign")


### Monitor facility

The facility manager can monitor and assesses the current status of their facilities
by reviewing the facility’s associated dashboard, details, checklist, and
transitions. To monitor a facility.

1. Select **Facility** from  the left pane to see the list of facilities. The default view, My Facilities, shows only your facilities. When switching view you can see either all active or inactive facilities. 

2. Select the desired facility record to access the facility data. The **General** tab shows the facility manager dashboard. The dashboard shows the COVID-19 data based on the address details of the facility, checklist completion for the current phase, employee attestation, and employee sentiment. More information: [Power BI dashboard]().

   > [!div class="mx-imgBorder"]
   > ![Facility at glance](media/facility-manager-facility-at-glance1.png "Facility at glance")

3. Select **Details** tab for the selected facility
 
   > [!div class="mx-imgBorder"]
   > ![Select details ](media/facility-manager-facility-form-populated.png "Select details")

4. Select **Checklist** tab for the selected facility to see checklist items and their completion status.

    > [!div class="mx-imgBorder"]
    > ![Checklist two](media/facility-manager-checklist-2-1.png "Checklist two") 

5. Select **Transitions** tab for the selected facility to see any related transition requests and their status.

   > [!div class="mx-imgBorder"]
   > ![Facility transition](media/facility-manager-facility-transitions.png "Facility transition")

### Updating the checklist

The **Checklist** tab contains a editable grid displaying the check-in the checklist for the current facility or phase combination. The editable grid provides an easy way for the users to find checks by category and then update the individual checks, where applicable. To locate and update checks:

1. Select **Facilities** from the left pane to see the list of active facilities

2. Select a desired facility to access the facility data

3. Select **Checklist** tab for the selected facility to see the checklist items and their completion status.

   > [!div class="mx-imgBorder"]
   > ![Checklist](media/facility-manager-checklist-2-1.png "Checklist")

4. Select the category from the **Categories** drop-list that you want to search
    within to locate the checks you want to review or update.

   > [!div class="mx-imgBorder"]
   > ![Category drop-list](media/facility-manager-categories-droplist1.png "Category drop-list")

5. Select the dropdown and select **Yes** to confirm the check is completed, add the **date** in the completion 
   date column.

6. Select **Save** to update the checklist.

    > [!div class="mx-imgBorder"]
    > ![Add comments](media/facility-manager-facility-completed-check1.png "Add comments")

## Moving facility to a new phase

When a facility manager asserts that a facility should be moved to a new phase,
the manager can apply for a transition. Only the facility manager can create
a new transition record that indicates the new phase.
A reviewer must **Accept** or **Reject** the transition. Either way, the transition
record is closed and stored as a historical track record. When the transition is
accepted, the proposed phase is applied to the facility.

The new phase comes with its own set of metrics, goals, and checklist. These
will be made available on the facility by a background process. So there will be
a small delay between accepting a transition and the actual changes on the
facility record.

A reviewer, for instance, a facility manager supervising many facility managers
in a facility group, can find the backlog in the phase transitions sub-area. For example, the list can be filtered by the facility group or by the reviewer to find out that the phase transitions require attention.

> [!div class="mx-imgBorder"]
> ![Open phase transitions](media/facility-manager-open-phase-transitions.png "Open phase transitions")

### Create transition request

To create a transition request:

1. Select **Facilities** in the left pane and select a facility record from the active facilities list.

2. Select **Transitions** tab from the selected facility. If there are any existing or previous transition requests established, they will appear in the
subgrid.

3. Select **New Reopen Phase Transition**.

   > [!div class="mx-imgBorder"]
   > ![New reopen phase transition](media/facility-manager-reopen-phase-transition-subgrid.png "New reopen phase transition")


4. Enter appropriate values in the fields:

   > [!div class="mx-imgBorder"]
   > ![Phase transition form](media/facility-manager-phase-transition-form.png "Phase transition form")

   | **Field**    | **Description**    |
   |-----------------------|---------------|
   | Proposed Reopen Phase | Select the desired next reopen phase to transition to.|
   | Summary | Enter the summary information regarding moving to the next or targeted reopen phase. |
   | Reviewer | Select appropriate resources to review and approve the new transition. |

5. Select **Save & Close**. The newly created record is available in the
    **Transitions** tab subgrid for the facility.

To edit the record, select the newly created record, update the values as
required, and select **Save & Close**. After approving or rejecting a phase transition, the record can't be updated.

### Approve transition

To approve transition requests:

1. Select **Phase Transitions** in the left pane.

   > [!div class="mx-imgBorder"]
   > ![Phase transition](media/facility-manager-phase-transition-reopen-transitions.png "Phase transition")


2. Filter the transitions with the name on the **Reviewer** column.

3. Select the **Transition** record. Complete any analysis required before selecting an **Approved** or **Rejected** value in the **Review Status** field 

4. For approvals, select **Approved** status value and enter in any associated comments in the **Review Comments** field.

   > [!div class="mx-imgBorder"]
   > ![Approved transitions](media/facility-manager-phase-transition-form-approved.png  "Approve transitions")

5. Select **Save & Close**. Transition **Review Status** is updated and appropriate back-end processes are triggered to move the facility to the targeted reopen phase.

### Reject transitions

A reviewer must **Accept** or **Reject** transitions. To review and perform approve or reject the transition:

1. Select **Phase Transitions** in the left pane.

   > [!div class="mx-imgBorder"]
   > ![Phase transition](media/facility-manager-phase-transition-reopen-transitions.png "Phase transition")

2. Filter the transitions with the name on the **Reviewer** column.

3. Select **Transition** record. Complete any analysis required before selecting an **Approved** or **Rejected** value in the **Review Status** field.

4. For rejections, select **Rejected** status value and enter in any
    associated comments in the **Review Comments** field.

   > [!div class="mx-imgBorder"]
   > ![Rejected transitions](media/facility-manager-phase-transition-form-rejected.png "Rejected transitions")

5. Select **Save & Close**. Transition **Review Status** is updated and is processed to move the facility to the requested reopen phase. The facility remains in the current phase and status.

## Monitor employee attestations

Facility managers can monitor whether or not their organization’s employees are
feeling healthy enough to be eligible to return to their facility. They can track employee self-attestations of their health based upon a series of
questions answered by the employees. This data is typically entered by the employee using the employee app. Facility managers can view the summary of the responses in **Employee Attestations** subarea in the facility manager app.

> [!div class="mx-imgBorder"]
> ![Employee Attestations](media/facility-manager-employee-attestations.png "Employee Attestations")

## Monitor employee sentiments

Keeps track of general employee sentiment on how they are feeling about the
prospect of returning to their workplace facility. This information is
self-reported, but it is a valuable parameter when tracked
consistently over time and with bigger groups. This data is typically entered by the employee using the employee app. Facility managers can view the summary of the responses in **Employee Attestations** subarea in the facility manager app.

> [!div class="mx-imgBorder"]
![Employee sentiment](media/facility-manager-employee-sentiment.png "Employee sentiment")

<!--
## Issues and feedback

- To report an issue with the Return to the Workplace solution, visit <https://aka.ms/rtw-issues>.

- For feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-feedback>.
-->
