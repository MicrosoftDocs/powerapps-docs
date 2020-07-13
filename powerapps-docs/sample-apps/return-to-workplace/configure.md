---
title: Configuration Guide for Solution Administrator
description: Provides an overview of Return to the Workplace Solution.
author: wbakker
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/06/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Configure the Return to the Workplace solution

This article provides step-by-step instructions for IT administrators to configure the Return to the Workplace solution. IT administrators are responsible for making sure the facility manager can guide their facilities throughout the phases. The following steps will be covered in this article:

- [Plan reopening phase](#plan-reopening-phases)

- [Manage facilities](#manage-facilities)

- [Specify solution settings](#specify-solution-settings)

## Prerequisites

The following prerequisites apply to this guide:

- The environment needs to have all the Return to the Workplace components in place with the model-driven apps, canvas apps, and Power BI dashboards.

## Plan reopening phases

Reopening the workplaces safely requires certain planning in phases to ensure the safety of the employees. To open a workplace, you need to define phases. Within these phases, you need to define goals, metrics, and readiness factors. These metrics can be sorted via categories.

In the model-driven app, you select the **Setup** module, that allows you to configure the plan.

> [!div class="mx-imgBorder"]
> ![Phase planning](media/solution-admin-new-setting-phase-planning.png "Phase planning")

To define a reopen phase, you need to define the following:

1. [Define key metrics](#define-key-metrics)

2. [Setup readiness categories](#setup-readiness-categories)

3. [Define readiness factors](#define-readiness-factors)

4. [Setup a reopen phase](#setup-a-reopen-phase)

5. [Set the goals and readiness factors for a phase](#set-the-goals-and-readiness-factors-for-a-phase)

## Define key metrics

There are five key metrics that are tracked and provided within the default solution. You can define more metrics if you want. To create a new key metric:

1. Select **Key Metrics** in the left pane and select **New**.

   > [!div class="mx-imgBorder"]
   > ![Create key metrics](media/solution-admin-key-metrics.png "Create key metrics")

2. Enter a meaningful name in the field.

    | **Field** | **Description**           |
   |-----------|---------------------------|
   | Name      | Enter a name for the key metric. |
   |||

   > [!div class="mx-imgBorder"]
   > ![Key metric form](media/solution-admin-new-key-metric-form.png "Key metric form")

  
3. Select **Save & Close**. The newly created record is available in the **Active Key Metrics** view.

To edit the record, select the newly created record, update the values as required, and select **Save & Close**.

## Setup readiness categories

Readiness categories organize the readiness factors. By default, there are six categories defined. To create a new readiness category:

1. Select **Readiness Categories** in the left pane and select **New**.

   > [!div class="mx-imgBorder"]
   > ![Readiness categories](media/solution-admin-new-readiness-category.png "Readiness categories")

2. Enter a meaningful name for the category.

    | **Field** | **Description**             |
   |-----------|-----------------------------|
   | Name      | Enter name for the new Category.|
   |||

   > [!div class="mx-imgBorder"]
   > ![Readiness category form](media/solution-admin-new-readiness-category-form.png "Readiness category form")

3. Select **Save & Close**. The newly created record is available in the **Active Categories** view.

To edit the record, select the newly created record, update the values as required and, select **Save & Close**.

## Define readiness factors 

Readiness factors are used to determine if the workplaces can move through phases. By default, there are few readiness factors defined in the solution. To create a new readiness factor:

1. Select **Readiness Factors** in the left pane and select **New**.

   > [!div class="mx-imgBorder"]
   > ![Readiness Factors](media/solution-admin-new-readiness-factor.png "Readiness Factors")

2. Enter appropriate values in the fields:

   | **Field** |  **Description** |
   |-------------|------------------------------|
   | Factor | Enter a name for the factor.  |
   | Description | Enter the description for the readiness factor. |
   | Category | Select the appropriate category to assign to your readiness factor. |

   > [!div class="mx-imgBorder"]
   > ![Readiness factors form](media/solution-admin-new-readiness-factor-form.png "Readiness factors forms")

   
3. Select **Save & Close**. The newly created record is available in the **Active Readiness Factors** view.

To edit the record, select the newly created record, update the values as required, and select **Save & Close**.

## Setup a reopen phase

In the reopening plan, you define a couple of phases that guides a facility to safely reopen the workplace. The phases are defined in the solution by default. To create or edit a reopen phase:

1. Select **Reopen Phases** in the left pane and select **New**.

   > [!div class="mx-imgBorder"]
   > ![Reopen phase](media/solution-admin-new-reopen-phase.png "reopen phase")

2. Enter appropriate values in the fields:

    | **Field**   | **Description**       |
   |---------------|------------------------------|
   | Index | Enter a unique index number such that it can be placed in appropriate phase order.|
   | Name | Enter a name for the reopen phase.|
   | Description   | Enter the description for the readiness factor. |
   | Process Stage | Select the appropriate process stage to assign to the new reopen phase. This identifies which stage in the business process flow should be activated. |

   > [!div class="mx-imgBorder"]
   > ![Reopen phase form](media/solution-admin-new-reopen-phase-form.png "Reopen phase form")

  
3. Select **Save & Close**. The newly created record is available in the **Active Reopen Phases** view.

To edit the record, select the newly created record, update the values as required, and select **Save & Close**.

## Set the goals and readiness factors for a phase

To set goals and readiness factors for a phase: 

1. Select **Reopen Phases** in the left pane and select the reopen phase record for which you need to add a new goal (for example, **Initial Return**)

   > [!div class="mx-imgBorder"]
   > ![New goal](media/solution-reopen-phases-active.png "New goal")

2. In the section “Key Metrics” select **+ New Goal.**

   > [!div class="mx-imgBorder"]
   > ![Select new goal](media/solution-admin-new-goal.png "Select new goal")

3. Enter appropriate filed values:

   | **Field**    | **Description**     |
   |--------------|--------------------|
   | Reopen Phase | Enter a name for the reopen phase.  |
   | Key Metric   | Select a key metric for the goal.  |
   | Type         | Select an appropriate goal type from the list. |
   | Value        | Enter a numerical target value for the goal. |


   > [!div class="mx-imgBorder"]
   > ![New goal form](media/solution-admin-new-goal-form.png "New goal form")

4. Select **Save & Close**. The newly created record is available in the **Key Metrics** view.

To edit the record, select the newly created record, update the values as required, and select **Save & Close**.

5. To set the readiness factors for the new reopen phase record, select the **Readiness Factors** tab

   > [!div class="mx-imgBorder"]
   > ![Readiness factors](media/solution-admin-reopen-phase-view-readiness-factors.png "Readiness factors")

6. Select **Add Existing Readiness Factor**

   > [!div class="mx-imgBorder"]
   ![Add existing factors](media/solution-admin-reopen-phase-add-existing-factor.png "Add existing factors")

7. Select the readiness factor that you want to add to your new reopen phase record. You can select multiple records.

8. Select **Add** to complete the selection process to add the selected **Readiness Factors** to your new **Reopen Phase** record.

   > [!div class="mx-imgBorder"]
   > ![Add readiness factors](media/solution-admin-reopen-phase-add-factors.png "Add readiness factors")

## Manage facilities

Facilities are an important part of the Return to the Workplace solution. Various facility types such as buildings, conference centers are defined in the solution by default. The IT administrator is responsible to create or update the existing facility types. The IT administrator can import records to help the facility manager who is responsible for creating facilities.

To manage facilities:

1. [Define facility types](#define-facility-types)

2. [Import facilities](#import-facilities)

## Define facility types

By default, two facility types are provided as an example. To create a new facility type:

1. Select **Facility Types** in the left pane and select **New**.

   > [!div class="mx-imgBorder"]
   > ![Facility type](media/solution-admin-new-facility-type.png "facility type")

2. Enter appropriate values in the fields:

    | **Field**   | **Description**                     |
   |-------------|-------------------------------------|
   | Type        | Enter a name for the type of facility.    |
   | Description | Enter the description for the facility type. |
   |||

   > [!div class="mx-imgBorder"]
   > ![Facility type form](media/solution-admin-new-facility-type-form.png "Facility type for,")

  

3. Select **Save & Close**. The newly created record is available in the **Active Facility Types** view.

To edit the record, select the newly created record, update the values as required, and select **Save & Close**.

## Import facilities 

The facility sample data file is available in the deployment package (.zip file). When you extract the .zip file, the sample data files are available under the
**SampleData** folder.

### How to import facility data from data files

To import sample facility data from the Excel file to the facility entity:

1. On the left navigation pane, select **Facilities** (in the area of Facility Management)

2. Select **Import from Excel** to select the facilities data file.
 
   > [!div class="mx-imgBorder"]
   > ![Import data](media/solution-admin-facilities-excel-import.png "Import data")

3. Browse the **SampleData** folder and select the **Facilities.xlsx** file. Change this file according to your own needs and proceed with the steps to import the data.

4. After the sample data is imported, you'll see the imported records in the entity.

   > [!div class="mx-imgBorder"]
   > ![Active facilities](media/solution-admin-facilities-active.png "Active facilities")

## Specify solution settings

The overall solution requires certain configurations to be made to make sure that the user has the correct information. Through solution settings, your own terms of agreement, health terms of agreement and contact email can be configured. Theming allows you to not only define your own settings, but also to tailor the experience to your company branding.

When setting up the solution, you go through the following steps:

1. [Set solution settings](#set-solution-settings)

2. [Define theming](#define-theming)

## Set solution settings

With solution settings, you define the terms of agreement which is applicable to your company. Solution settings are linked to groups or to the entire organization, this makes it possible to differentiate per facilities. One solution setting will act as default and will be applicable for every facility, which will be the solution setting that has an empty group. To set solution settings:

1. Select **Solution Settings** in the left pane and select **New**.

   > [!div class="mx-imgBorder"]
   > ![Solution Settings](media/solution-admin-view-solution-settings.png)

2. Enter the appropriate values in the fields:

   > [!div class="mx-imgBorder"]
   > ![Solution settings form](media/solution-admin-new-setting.png "Solution settings form")

## Define theming

Theming allows you to change the experience of the employee.

1. Select **Settings** and then **Customizations**.

   > [!div class="mx-imgBorder"]
   > ![Settings](media/solution-admin-settings-themes.png "Settings")

2. Under Customizations, select **Themes**.
   
   > [!div class="mx-imgBorder"]
   > ![Themes](media/solution-admin-settings.png "Themes")

3. From the list, select the default theme.

    > [!div class="mx-imgBorder"]
    > ![All themes](media/solution-admin-settings-all-themes.png "All themes")

4. You can select the different colors from the theme.

   > [!div class="mx-imgBorder"]
   > ![Theme color](media/deploy-theme-colors.png "Theme color")
   
## Sample Data

For demo purpose the solution includes sample data around the different entities in the solution. The data from the following entities is adviced to be removed to import your own data:

- Facilities
- Facility Groups
- Facility Types
- Employees
- Solution Settings

The sample data is also expended with two flows, these need to be disabled when you are not using the sample data.

- Sample Data - Generate Employee Records
- Sample Data - Generate Facility transitions

## Bulk record deletion

Due to privacy regulations we strongly recommend creating bulk record delete jobs to delete personal data after a certain period. This can be achieved by creating bulk record delete jobs.

1.	Select **Settings** and then **Data Management**

2.	Under Data Management select **Bulk record deletion**

   > [!div class="mx-imgBorder"]
   > ![Data Management](media/solution-admin-dm.png "Data Management")

3.	Click **New**

4.	Navigate through the **Bulk Deletion Wizard**

5.	Select the appropriate **entity** and **criteria** 

   > [!div class="mx-imgBorder"]
   > ![Criteria](media/solution-admin-criteria.png "Criteria")

6.	Add a name and a schedule for the bulk record delete job to run

   > [!div class="mx-imgBorder"]
   > ![Brd](media/solution-admin-brd.png "Brd")

7.	Submit the bulk record delete job

<!--
## Issues and feedback

- To report an issue with the Return to the Workplace solution, visit <https://aka.ms/rtw-issues>.

- For feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-feedback>.
-->
