---
title: Use the Facility Safety Management app
description: Provides an overview of the Facility Safety Management app.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/25/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Facility Safety Management app

The Facility Safety Management app provides step-by-step instructions to facility managers in the organization for using the app to manage the reopening and readiness of the facilities. 

This helps the organizations ensure that they can provide a safe working environment for employees to return to the workplace using the Return to the Workplace solution.

## App at a glance

The Return to Workplace solution supports the organization’s goal to reopen its facilities to its employees as safely and as quickly as possible to return to normal.  The Facility Safety Management app as part of the overall solution provides facility managers with a tool that provides them with the capabilities to manage and support the organization’s journey through their specific reopening plan for their facilities and its associated phases and goals.  

It is the facility manager who facilitates the execution of the organizations reopening plan and their reopening phases that have been configured. More information: [Configure the solution](configure.md). The facility managers in supporting the goal of reopening their facilities safely and quickly will lead the required assessments of facility readiness and review its status. 

The assessments are done by performing checks on the facility’s readiness checklist. When the facility is assumed to be ready based on the results of these checks, the facility manager then moves the facility to the next reopen phase by initiating a phase transition request. The phase transition request is then processed by the organization’s assigned reviewer for approval.  This will implement a four-eyes principle, while the checklist allows for a consistent discussion on readiness throughout the company.  After the reviewer approves the phase transition request, the facility is moved to the next phase where a new checklist is created and managed.  

The left pane lists all the components available in the **Facility Management** area.

> [!div class="mx-imgBorder"]
> ![Facility management](media/facility-manager-facility-active-facilities2.png "Facility management")

## App components

The Facility Safety Management app has the following components:

**Facility Management**

-  **Facilities**- List of the facilities (for example, buildings and plants) that require monitoring to reopen.

-  **Facility Groups** - Provides a flexible way to group facilities. For example, by campus or geographical region.

-  **Facility Types** - Type of facility. For example, building, data center, parking space.

**Reopen Readiness**

-  **Phase Transitions** - A phase transition is used to create a request to transition to a new phase. When the transition is approved, the facility will be updated with the proposed phase and its associated checklist based upon the phase's configured readiness factors.

**Employee**

- **Employee Sentiment** -  Keeps track of general employee well-being. This is self-reported information, but it's a valuable parameter when tracked consistently over time and with bigger groups. This data is typically entered by employees using the employee app.

- **Employee Attestation** - Keeps track of employee health assessments or attestations based on a series of questions answered by the employee. Employee attestation data is typically entered by employees using the employee app.

- **Employee Bookings** - Keeps track of the employee booking having the employee, area, start, and end arrival time. Employee bookings are linked to the employees' attestation record and updates if there is a visit to that booking.

- **Employee Visits** - Keeps track of the visits. Employee visits are linked to an employee and a booking record.

**Guests**

- **Guest Registrations** - Keep track of registered guests. Guest registrations are always linked to a booking and an Employee serves as a host. Guests are stored as a Contact record of type 'Guest'.

## Manage and monitor facilities 

This section covers how to manage and monitor facilities.

### Create a facility 

By default, two facilities are provided as an example.

**To create a new facility**

1. Select **Facilities** in the left pane, and then select **New**.

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
   | Entry Window Interval  | Select the window interval for entry between 30 mins, 1 hour, and none. |
   | Facility Type          | Select the appropriate facility type.   |
   | Facility Group         | Select an appropriate group for the facility. |
   | Reopen Phase           | Select an appropriate reopen phase.  |
   | Address Street 1       | Enter the first line of the street address.            |
   | Address Street 2       | Enter the second line of the street address.             |
   | Address Postal Code    | Enter the postal code.         |
   | Address City           | Enter the city.               |
   | Address State/Province | Enter the state or province.      |
   | Address Country        | Enter a country.        |

3. Select **Save & Close**. The newly created record is available in the
    **Active Facility Types** view.

### Create a floor for a facility 

When creating a facility, you can link a floor and area to this facility. To create a floor for a facility:

1. Select a facility where you want to add a floor from the **Facilities** list. Select **Occupancy** tab and select **+ New Floor**.

   > [!div class="mx-imgBorder"]
   > ![New facility floor form](media/facility-manager-floor.png "New facility floor form")

2. Enter appropriate values in the fields:

   > [!div class="mx-imgBorder"]
   > ![New facility floor details](media/facility-manager-floor2.png "New facility floor details")

   | **Field**       | **Description**   |
   |--------------|------------------------------------------------|
   | Floor        | Name for the floor.    |
   | Floor Index  | Number established for the floor. |
   | Facility     | Select the facility name. |

3. Select **Save & Close**.

### Create an area for a facility

Once a floor is created, the **area** option is available to be linked to it.

1. Select a facility where you want to add an area from the **Facilities** list. Select **Occupancy** tab and select **+ New Area**.

   > [!div class="mx-imgBorder"]
   > ![New facility area form](media/facility-manager-area.png "New facility area form")

2. Enter appropriate values in the fields:

   > [!div class="mx-imgBorder"]
   > ![New facility area details](media/facility-manager-area2.png "New facility area details")

   | **Field**       | **Description**  |
   |--------------|--------------------|
   | Area        | Name for the area. |
   | Facility  | By default, the newly created facility.  |
   | Floor     | By default, the newly floor created. |
   | Capacity    | Number of people allowed in an area.  |

3. Select **Save & Close**. 

To edit the record, select it, update the values, and then select **Save & Close**.

**To assign a facility to a user**

1. A facility can be assigned to a user, to do so switch to the **Active Facilities** view.

   > [!div class="mx-imgBorder"]
   > ![Active Facilities](media/facility-manager-active-facilities.png "Active Facilities")

2. Select a facility, select **Assign**, and then select a **User** to assign the facility.

   > [!div class="mx-imgBorder"]
   > ![Assign a facility to a user](media/facility-manager-assign.png "Assign a facility to a user")

### Monitor a facility

The facility manager can monitor and assesses the current status of their facilities
by reviewing the facility's associated dashboard, details, checklist, and
transitions.

**To monitor a facility**

1. Select **Facility** from the left pane. The default view, **My Facilities**, shows only your facilities. When switching the views, you can see either all the active or inactive facilities. 

2. Select the facility record for which you want to access data. The **General** tab shows the facility manager dashboard, which provides information on facility usage, guide reopening, and analyze the occupancy at a facility.  The report has three main tabs: Facilities, Virus Spread, and Employee Activity.

   **Facilities**:

   The *Readiness* tab shows the status of the readiness checks needed for a facility’s safe reopening. Checks are separated into categories (for example, Employee Experience, Communications, etc.) which can be expanded to show the progress of individual actions. The reproductive number is the average number of people to whom COVID-19 may be transmitted by an infected individual.

   The *Occupancy* tab provides metrics regarding the facility capacity and usage, such as:
      - Facility’s total capacity, and current capacity based on reopening phase.
      - Number of bookings and visits for the most recent day and daily average for the last seven days.
      - Two charts, that can be filtered by date range, and to a floor or an area:
          - Number of bookings and the current capacity.
          - Average daily occupancy, shown as a black bar.  Capacity is represented by the green zone.  Floors and areas with black bars in the red zone are over-capacity. Occupancy can be viewed at the floor or area level.  Hovering over the information symbol (🛈) next to the chart shows detailed instructions.

   The *Daily Arrivals* tab shows booking information to assist in controlling the facility traffic, such as:
      - Capacity and visit metrics, busiest weekday, and arrival time window for the last seven days.
      - Two charts, which can be filtered by date range, display number of bookings by arrival window, and by weekday.

   > [!div class="mx-imgBorder"]
   > ![Facility Manager Readiness](media/pbi-dash-facility-manager-readiness.png "Facility Manager - Readiness")

   **Virus Spread**:

   The Virus Spread section shows the data from public health sources by country (state level for US). There are three tabs: New COVID-19 Cases, Fatal COVID-19 Cases, and Reproductive Number.

   The *New COVID-19 Cases* tab shows the number of cases for the last reporting day, 14-day average, daily trend, and the total number of cases.
   The *Fatal COVID Cases* tab shows information for COVID-19 cases with fatalities.
   The *Reproductive Number* is the average number of people to whom COVID-19 might be transmitted by an infected individual.  Data for the US is at the state level.

   > [!div class="mx-imgBorder"]
   > ![Facility Manager Virus Spread](media/pbi-dash-facility-manager-virus-spread.png "Facility Manager - Virus Spread")

   **Employee Activity**:

   The Employee Activity section summarizes the employee engagement and employee app usage over a period.  The following metrics are shown:
      - Employee App Usage, which shows the number of times the Return to Workplace app has been used to obtain a pass
      - Average employee sentiment
      - Number of passes generated

      There are two charts. One displays the sentiment by date and the other displays the pass generated vs. the number of visits by date, along with the trend over time.

   > [!div class="mx-imgBorder"]
   > ![Facility Manager Employee Activity](media/pbi-dash-facility-manager-employee-activity.png "Facility Manager - Employee Activity")

3. Exploring the Facility

   - Select the **Details** tab for the facility.
     > [!div class="mx-imgBorder"]
     > ![Select details ](media/facility-manager-facility-form-populated.png "Select details")


   - Select the **Checklist** tab to see the checklist items and their completion status.

     > [!div class="mx-imgBorder"]
     > ![Checklist items](media/facility-manager-checklist-2-1.png "Checklist items") 
     
     > [!NOTE]
     > Checklist items are configured as part of the global process for managing reopen phases and their associated readiness factors. Therefore, new checks are added as readiness factors on a reopen phase and not on the facility.    

   - Select the **Transitions** tab to see any related transition requests and their status.

     > [!div class="mx-imgBorder"]
     > ![Facility transition](media/facility-manager-facility-transitions.png "Facility transition")

   
   - Select the **Occupancy** tab to see and add floors and areas to the facility.

     > [!div class="mx-imgBorder"]
     > ![Facility transition occupancy](media/facility-manager-facility-ocupancy.png "Facility transition occupancy")

   - Select the **Related** tab to see any related actions.

     > [!div class="mx-imgBorder"]
     > ![Facility transition related](media/facility-manager-facility-related.png "Facility transition related")


### Updating the checklist

The **Checklist** tab contains an editable grid displaying the checklist for the current facility or phase combination. The editable grid provides an easy way to find checklist items by category and then update the individual items, where applicable. 

**To find and update checklist items**

1. Select **Facilities** from the left pane.

2. Select the facility for which you want to find and update checklist items.

3. Select the **Checklist** tab.

   > [!div class="mx-imgBorder"]
   > ![Checklist items and status](media/facility-manager-checklist-2-1.png "Checklist items and status")

4. Select **Category**, and then select the category you want to search in.

   > [!div class="mx-imgBorder"]
   > ![Category drop-down list](media/facility-manager-categories-droplist1.png "Category drop-down list")

5. Select the drop-down and select **Yes** to confirm the check is completed. 

6. Add the date in the **Completion date** column, and then select **Save** to update the checklist.

    > [!div class="mx-imgBorder"]
    > ![Update the completion date for a checklist item](media/facility-manager-facility-completed-check1.png "Update the completion date for a checklist item")

## Moving facility to a new phase

When a facility manager asserts that a facility should be moved to a new phase, the manager can apply for a transition. Only the facility manager can create a new transition record that indicates readiness to move to a new phase. After a new transition is created and saved, it appears in the subgrid with the transitions tab of the facility record with a status of **Submitted**.  A reviewer is assigned to the reopen phase transition request. The reviewer once assigned can start acting on the reopen phase transition request by accepting or rejecting the request. Upon approval or rejection of the transition record, it is processed and when complete, the request is considered as closed and stored as a historical record. 

When the process is complete, the transition record appears in the subgrid as with either **Accepted** (approved request) or **Rejected** (rejected request) status. When a transition request is accepted, the transition record proposed phase is applied to the facility record’s reopen phase field.  This update triggers the background process that updates the business process flow stage, aligning the reopen phase and the current business process flow stage.

Additionally, the background process creates a new checklist for the facility along with a new set of metrics and goals. The new checklist that is created is based upon the readiness factors that were previously set up and configured by the facility manager for the selected reopen phase. The new checklist can then be accessed from the facility record’s checklist tab.  

> [!NOTE]
> During the execution of the background processes there may be a delay before these updates are completed and viewable in the facility’s manager’s view of the screen.  You might need to select the refresh button to see the updates on the screen).

A reviewer&mdash;for instance, a facility manager supervising many facility managers in a facility group&mdash;can find the backlog in **Phase transitions**. For example, the list can be filtered by the facility group or by the reviewer to find the phase transitions that require attention.

> [!NOTE]
> Transitions from one phase to another cannot be completed without an approved transition and therefore it is highly recommended that organizations ensure that someone has been given the responsibility to monitor the transitions and ensure they have the appropriate assigned reviewer.

> [!div class="mx-imgBorder"]
> ![Open phase transitions](media/facility-manager-open-phase-transitions.png "Open phase transitions")

### Create a transition request

1. Select **Facilities** in the left pane, and select a facility record from the active facilities list.

2. Select the **Transitions** tab. If any existing or previous transition requests were established, they'll appear in the subgrid.

3. Select **New Reopen Phase Transition**.

   > [!div class="mx-imgBorder"]
   > ![New reopen phase transition](media/facility-manager-reopen-phase-transition-subgrid.png "New reopen phase transition")

4. Enter appropriate values in the fields:

   > [!div class="mx-imgBorder"]
   > ![Phase transition form](media/facility-manager-phase-transition-form.png "Phase transition form")

   | **Field**    | **Description**    |
   |-----------------------|---------------|
   | Proposed Reopen Phase | Select the next reopen phase you want to transition to.|
   | Summary | Enter the summary information about moving to the next or targeted reopen phase. |
   | Reviewer | Select appropriate resources to review and approve the new transition. By default, this only shows facility managers, by changing the view you can select other users. |

5. Select **Save & Close**. The newly created record is available in the **Transitions** tab subgrid for the facility.

To edit the record, select it, update the values, and then select **Save & Close**. After the phase transition is approved or rejected, the record can't be updated.

### Approve or reject a transition

1. Select **Phase Transitions** in the left pane.

   > [!div class="mx-imgBorder"]
   > ![Phase transition](media/facility-manager-phase-transition-reopen-transitions.png "Phase transition")

2. Filter the transitions by name on the **Reviewer** column.

3. Select the **Transition** record. Complete any analysis required before selecting **Approved** or **Rejected** in the **Review Status** field.

4. For approvals, select **Approved** and enter any comments in the **Review Comments** field. Select **Save & Close**.

   > [!div class="mx-imgBorder"]
   > ![Approved transitions](media/facility-manager-phase-transition-form-approved.png  "Approve transitions")

5. For rejections, select **Rejected** and enter any comments in the **Review Comments** field. Select **Save & Close**.

   > [!div class="mx-imgBorder"]
   > ![Rejected transitions](media/facility-manager-phase-transition-form-rejected.png "Rejected transitions")

The review status for the transition is updated, and appropriate back-end processes are triggered to move the facility to the targeted reopen phase.

### Create transition records via the business process flow

For ease of use, you can also use the business process flow to create new transition records. There are two cases:

1. Moving forward

Given that the facility is not in the final phase, the user can select on the circle of the current stage and select **Next Stage**. The business process flow won't move instantly, but in the background, a new transition record is created and the user will be navigated to that record. The record is pre-populated with the next phase and is ready for approval.

2. Moving backward

Given that the facility is not in the first phase, the user can select on the circle of the current stage and select **<** to move back. Or the user can select the circle of any previous stage and select **Set Active**. The business process flow changes immediately. In the background, a phase transition record is created and approved automatically. This in turn triggers the background process that updates the facility with the checklist, metrics, and goals corresponding to the selected phase. Wait for some time for the changes to happen. The user can continue to perform other tasks.

## Monitor employee attestations

Facility managers can monitor whether their organization's employees are feeling healthy enough to be eligible to return to their facility. They can track employee self-attestations of their health based on a series of questions the employees' answer. This data is typically entered by the employee using the employee app. Facility managers can view the summary of the responses in the **Employee Attestations** area of the facility manager app.

> [!div class="mx-imgBorder"]
> ![Employee Attestations](media/facility-manager-employee-attestations.png "Employee Attestations")

## Monitor employee sentiments

This area of the Facility Safety Management app keeps track of general employee sentiment about the prospect of returning to their workplace. This information is self-reported, but it's a valuable parameter when tracked consistently over time and with larger groups. This data is typically entered by the employee using the Employee app. Facility managers can view the summary of the responses in the **Employee Attestations** area of the Facility Safety Management app.

> [!div class="mx-imgBorder"]
![Employee sentiment](media/facility-manager-employee-sentiment.png "Employee sentiment")

## Feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.
