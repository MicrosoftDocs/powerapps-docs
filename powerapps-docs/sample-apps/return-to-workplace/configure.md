---
title: Configuration guide for the Return to the Workplace solution administrator
description: Provides an overview of Return to the Workplace Solution.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/21/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Configure the Return to the Workplace solution

This article provides step-by-step instructions to IT administrators for configuring the Return to the Workplace solution. IT administrators are responsible for making sure the facility manager can guide their facilities throughout the phases. The following steps will be covered in this article:

- [Plan reopening phases](#plan-reopening-phases)

- [Manage facilities](#manage-facilities)

- [Specify solution settings](#specify-solution-settings)

## Prerequisites

- The environment needs to have all the Return to the Workplace components in place with the model-driven apps, canvas apps, and Power BI dashboards.

## Plan reopening phases

Reopening workplaces safely requires planning in phases to ensure the safety of the employees. Within these phases, you need to define goals, metrics, and readiness factors.

In the model-driven app, you select the **Solution Setup** module, which allows you to configure the plan.

> [!div class="mx-imgBorder"]
> ![Phase planning](media/solution-admin-new-setting-phase-planning.png "Phase planning")

**To define a reopen phase**

1. [Define key metrics](#define-key-metrics).

2. [Set up readiness categories](#set-up-readiness-categories).

3. [Define readiness factors](#define-readiness-factors).

4. [Set up a reopen phase](#set-up-a-reopen-phase).

5. [Set the goals and readiness factors for a phase](#set-the-goals-and-readiness-factors-for-a-phase).

## Define key metrics

By default, the solution provides and tracks five key metrics. You can define more metrics if you want. 

**To create a new key metric**

1. Select **Key Metrics** in the left pane, and then select **New**.

   > [!div class="mx-imgBorder"]
   > ![Create key metrics](media/solution-admin-key-metrics.png "Create key metrics")

2. Enter a meaningful name for the metric.

   > [!div class="mx-imgBorder"]
   > ![Key metric form](media/solution-admin-new-key-metric-form.png "Key metric form")

3. Select **Save & Close**. The newly created record is available in the **Active Key Metrics** view.

To edit the record, select it, update the values, and then select **Save & Close**.

## Set up readiness categories

Readiness categories organize the readiness factors. By default, six categories are defined. 

**To create a new readiness category**

1. Select **Readiness Categories** in the left pane, and then select **New**.

   > [!div class="mx-imgBorder"]
   > ![Readiness categories](media/solution-admin-new-readiness-category.png "Readiness categories")

2. Enter a meaningful name for the category.

   > [!div class="mx-imgBorder"]
   > ![Readiness category form](media/solution-admin-new-readiness-category-form.png "Readiness category form")

3. Select **Save & Close**. The newly created record is available in the **Active Categories** view.

To edit the record, select it, update the values, and then select **Save & Close**.

## Define readiness factors 

Readiness factors are used to determine whether the workplaces can move through phases. Some readiness factors are defined in the solution by default.

**To create a new readiness factor**

1. Select **Readiness Factors** in the left pane, and then select **New**.

   > [!div class="mx-imgBorder"]
   > ![Readiness factors](media/solution-admin-new-readiness-factor.png "Readiness factors")

2. Enter appropriate values in the fields:

   | **Field** |  **Description** |
   |-------------|------------------------------|
   | Factor | Enter a name for the factor.  |
   | Description | Enter the description for the readiness factor. |
   | Category | Select the appropriate thing to assign your readiness factor to.|

   > [!div class="mx-imgBorder"]
   > ![Readiness factors form](media/solution-admin-new-readiness-factor-form.png "Readiness factors forms")

3. Select **Save & Close**. The newly created record is available in the **Active Readiness Factors** view.

To edit the record, select it, update the values, and then select **Save & Close**.

## Set up a reopen phase

In the reopening plan, you define phases that guide a facility to safely reopen the workplace. The phases are defined in the solution by default.

**To create or edit a reopen phase**

1. Select **Reopen Phases** in the left pane, and then select **New**.

   > [!div class="mx-imgBorder"]
   > ![Reopen phase](media/solution-admin-new-reopen-phase.png "Reopen phase")

2. Enter appropriate values in the fields:

    | **Field**   | **Description**       |
   |---------------|------------------------------|
   | Index | Enter a unique index number to place the phase in the order you want.|
   | Name | Enter a name for the reopen phase.|
   | Description   | Enter the description for the phase. |
   | Process Stage | Select the appropriate process stage to assign the new reopen phase to. This identifies which stage in the business process flow should be activated. |

   > [!div class="mx-imgBorder"]
   > ![Reopen phase form](media/solution-admin-new-reopen-phase-form.png "Reopen phase form")

3. Select **Save & Close**. The newly created record is available in the **Active Reopen Phases** view.

To edit the record, select it, update the values, and then select **Save & Close**.

## Set the goals and readiness factors for a phase

**To set goals for a phase**

1. Select **Reopen Phases** in the left pane, and select the reopen phase record for which you want to add a new goal (in this example, we use the **Initial Return** phase).

   > [!div class="mx-imgBorder"]
   > ![Select a phase to add a goal to](media/solution-reopen-phases-active.png "Select a phase to add a goal to")

2. Under **Key Metrics**, select **+ New Goal**.

   > [!div class="mx-imgBorder"]
   > ![Select a new goal](media/solution-admin-new-goal.png "Select a new goal")

3. Enter appropriate values in the fields:

   | **Field**    | **Description**     |
   |--------------|--------------------|
   | Reopen Phase | The name of the phase you're adding a goal to will appear here.|
   | Key Metric   | Select a key metric for the goal.  |
   | Type         | Select an appropriate goal type from the list. |
   | Value        | Enter a numerical target value for the goal. |

   > [!div class="mx-imgBorder"]
   > ![New goal form](media/solution-admin-new-goal-form.png "New goal form")

4. Select **Save & Close**. The newly created record is available in the **Key Metrics** view.

To edit the record, select it, update the values, and then select **Save & Close**.

**To set readiness factors for a phase**

1. Select the **Readiness Factors** tab.

   > [!div class="mx-imgBorder"]
   > ![Readiness factors](media/solution-admin-reopen-phase-view-readiness-factors.png "Readiness factors")

2. Select **Add Existing Readiness Factor**.

   > [!div class="mx-imgBorder"]
   ![Add existing factors](media/solution-admin-reopen-phase-add-existing-factor.png "Add existing factors")

3. Select the readiness factor that you want to add to your reopen phase record. You can select multiple records.

4. Select **Add** to complete the selection process to add the selected readiness factors to your Reopen Phase record.

   > [!div class="mx-imgBorder"]
   > ![Add readiness factors](media/solution-admin-reopen-phase-add-factors.png "Add readiness factors")

## Manage facilities

Facilities are an important part of the Return to the Workplace solution. By default, the solution includes two facility types&mdash;buildings and conference centers&mdash. The IT administrator is responsible for creating, updating the existing facility types, and importing records. 

**To manage facilities**

1. [Define facility types](#define-facility-types).

2. [Import facilities](#import-facilities).

## Define facility types

By default, two facility types are provided as an example.

**To create a new facility type**

1. Select **Facility Types** in the left pane, and then select **New**.

   > [!div class="mx-imgBorder"]
   > ![Facility type](media/solution-admin-new-facility-type.png "facility type")

2. Enter appropriate values in the fields:

    | **Field**   | **Description**                     |
   |-------------|-------------------------------------|
   | Type        | Enter a name for the type of facility.    |
   | Description | Enter the description for the facility type. |

   > [!div class="mx-imgBorder"]
   > ![Facility type form](media/solution-admin-new-facility-type-form.png "Facility type form")

3. Select **Save & Close**. The newly created record is available in the **Active Facility Types** view.

To edit the record, select it, update the values, and then select **Save & Close**.

## Import facilities

The facility sample data file is available in the package. When you want to import your own facilities, you can [download a template to use for data import](https://docs.microsoft.com/power-platform/admin/download-template-data-import).

**To import sample facility data to the Facility entity**

1. On the left pane, under **Facility Management**, select **Facilities**.

2. Select **Import from Excel**, and select the facilities data file.
 
   > [!div class="mx-imgBorder"]
   > ![Import data](media/solution-admin-facilities-excel-import.png "Import data")

3. After the sample data is imported, you'll see the imported records in the entity.

   > [!div class="mx-imgBorder"]
   > ![Active facilities](media/solution-admin-facilities-active.png "Active facilities")

## Specify solution settings

The overall solution requires certain configurations to be made to make sure that the user has the correct information. You can use solution settings to configure your own terms of agreement, health terms of agreement, and contact email. You can also use themes to tailor the experience to your company branding.

When setting up the solution, do the following:

1. [Set solution settings](#set-solution-settings).

2. [Define a theme](#define-a-theme).

## Set solution settings

With solution settings, you define the terms of agreement that are applicable to your company. Solution settings are linked to groups or to the entire organization, which makes it possible to differentiate them for individual facilities. One solution setting will act as the default and will be applicable for every facility, which will be the solution setting that has an empty group. To set solution settings:

1. Select **Solution Settings** in the left pane, and then select **New**.

   > [!div class="mx-imgBorder"]
   > ![Solution Settings](media/solution-admin-view-solution-settings.png)

2. Enter the appropriate values in the fields:

   > [!div class="mx-imgBorder"]
   > ![Solution settings form](media/solution-admin-new-setting.png "Solution settings form")

## Define a theme

You can use a theme to enhance the user experience.

1. Select **Settings**, and then select **Customizations**.

   > [!div class="mx-imgBorder"]
   > ![Settings](media/solution-admin-settings-themes.png "Settings")

2. Under Customizations, select **Themes**.

   > [!div class="mx-imgBorder"]
   > ![Themes](media/solution-admin-settings.png "Themes")

3. From the list, select the default theme.

    > [!div class="mx-imgBorder"]
    > ![All themes](media/solution-admin-settings-all-themes.png "All themes")

4. You can select different colors from the theme.

   > [!div class="mx-imgBorder"]
   > ![Theme color](media/deploy-theme-colors.png "Theme color")
   
## Contoso Sample Data

To try out the solution, when installing the Return to the Workplace solution, Contoso sample data is installed with it. This sample data includes data around the entities listed below. Advised is to import or create your own data for these entities.

- Facilities
- Facility Groups
- Facility Types
- Employees
- Solution Settings

Usage sample data is generated by two flows, these need to be disabled when you are not using the Contoso sample data.

- Sample Data - Generate Employee Records
- Sample Data - Generate Facility transitions

## Bulk record deletion

Due to privacy regulations, we strongly recommend that you create bulk record-delete jobs to delete personal data after a certain period.

**To create bulk record-delete jobs**

1.	Select **Settings**, and then select **Data Management**

2.	Under **Data Management**, select **Bulk record deletion**.

   > [!div class="mx-imgBorder"]
   > ![Data Management](media/solution-admin-dm.png "Data Management")

3.	Select **New**.

4.	Go through the **Bulk Deletion Wizard**.

5.	Select the appropriate **entity** and **criteria**.

   > [!div class="mx-imgBorder"]
   > ![Criteria](media/solution-admin-criteria.png "Criteria")

6.	Add a name and a schedule for the bulk record-delete job to run.

   > [!div class="mx-imgBorder"]
   > ![Bulk record delete job](media/solution-admin-brd.png "Bulk record delete job")

7.	Submit the bulk record-delete job.

