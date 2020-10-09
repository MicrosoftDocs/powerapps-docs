---
title: Upgrade the Return to the Workplace solution for Microsoft Power Platform | Microsoft Docs
description: Provides an overview of how to upgrade the Return to the Workplace solution.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/27/2020
ms.author: garybird
ms.reviewer: kvivek
---
# Upgrade the Return to the Workplace solution

This article provides step-by-step instructions for how to upgrade the existing Return to the Workplace solution to the latest version. If you're deploying the solution for the first time, see [Deploy the Return to the Workplace solution](deploy.md). Follow upgrade the solution steps and after that follow the upgrade path which is applicable for you.

## Prerequisites

- You must be a Global administrator or Microsoft Power Platform administrator to do the installation.

- You must be a Global administrator and must have a Power BI Pro license to configure and publish reports.

- You must have installed the earlier version of Return to the Workplace and have the environment details. 

> [!TIP]
> Upgrading the solution affects the user experience. We recommend that you upgrade the solution outside of normal business hours, and test the changes on a development or test environment before moving it to a production environment. 

## Step 1: Update the solution

You can update the Return to the Workplace solution by using the Power Platform admin center.

> [!NOTE]
> If you're a US Government customer, you'll have to update the solution by using the latest version of the deployment package available on GitHub. More information: [Appendix: Deploy the app and publish Power BI dashboard (US Government customers only)](deploy.md#appendix-deploy-the-app-and-publish-power-bi-dashboard-us-government-customers-only)

  1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com).

  2. On the left pane, select **Environments**, and then select the environment where you want to update the solution.

  3. On the left pane, select **Resources** > **Dynamics 365 apps**. From the list of apps, select **Power Platform Return to the Workplace - Apps**, which is the Return to the Workplace solution.

     > [!div class="mx-imgBorder"]
     > ![List of apps in the admin center](media/app-management-environment-view.png "List of apps in the admin center")

  4. The status field indicates that there's an update available for **Power Platform Return to the Workplace - Apps**. From the command bar, select **Update** or select the **Update Available** status to start the update process. From the command bar, you can also select **Details** to see the progress of the installation.
  
For more information about the update process, see [Manage Dynamics 365 apps](https://docs.microsoft.com/power-platform/admin/manage-apps).

## Step 2: Update Power BI dashboards

When a new version of the  **Return to the Workplace** solution is available, you can be notified in two ways:

- An update banner appears in the Power BI Service informing you that a new app version is available.

    > [!div class="mx-imgBorder"]
    > ![Power BI banner](media/power-bi-new-app-version-notification-banner.png "Power BI banner")

- You'll receive a notification on Power BI's notification pane.

    > [!div class="mx-imgBorder"]
    > ![Power BI notification pane](media/power-bi-new-app-version-notification-pane.png "Power BI notification pane")

> [!NOTE]
> If you're a US Government customer, you'll have to update the Power BI dashboard using the latest version of the deployment package available on GitHub. More information: [Appendix: Deploy the app and publish Power BI dashboard (US Government customers only)](deploy.md#appendix-deploy-the-app-and-publish-power-bi-dashboard-us-government-customers-only)

1. To install the update, either select **Get it** on the notification banner or in the notification center, or find the app in the AppSource and select **Get it now**. If you have a direct link for the update, select the link.

2. You'll be asked whether you want to overwrite the current version or to install the new version in a new workspace. By default, **Overwrite an existing version** is selected.

   > [!div class="mx-imgBorder"]
   > ![Update App overwrite](media/power-bi-update-app-overwrite.png "Update App overwrite")

If you already installed the existing version, leave it on **Overwrite an existing version**. Select **Install to a new workspace** to install a fresh version of the workspace and app that you need to reconfigure (connect to data, define navigation and permissions).
  
3. Install the app in a new workplace by following these steps in the deploy topic:
    - [Step 3: Configure and publish Power BI dashboards](/powerapps/sample-apps/return-to-workplace/deploy#step-3-configure-and-publish-power-bi-dashboards)
    - [Step 4: Schedule report refresh](/powerapps/sample-apps/return-to-workplace/deploy#step-4-schedule-report-refresh)
    - [Step 5: Embed the Power BI report in the model-driven app](/powerapps/sample-apps/return-to-workplace/deploy#step-5-embed-the-power-bi-report-in-the-model-driven-app)


## Upgrade from version 1.0 to 1.1

### Step 1: Install the Workplace Care Management dashboard

You can use the Workplace Care Management dashboard to track overall employee cases. More information: [Use the Workplace Care Management dashboard](dashboard-case-management.md)

To install the Workplace Care Management dashboard, follow the instructions in [Deploy the Return to the Workplace solution](deploy.md#step-3-configure-and-publish-power-bi-dashboards).


### Step 2: Update facilities

With the new version, we are introducing the notion of areas and floors for a facility. A floor indicates how many levels are present within a facility. An area allows you to define a space within a floor that has a certain capacity. Through bookings in the Employee app, you can book an area. More information: [Use the Facility Safety Management app](app-for-facility-manager.md).

Facilities now also have entry windows defined, which allow you to indicate in which time window people can enter the building. More information: [Use the Facility Safety Management app](app-for-facility-manager.md).


### Step 3: Define capacity for your reopen phases

Capacity is defined for an area, but it's also bound by the phase your facility is in. Every reopen phase defines the percentage by which capacity will be limited. More information: [Configure the solution](configure.md)


### Step 4: Make employee cases inactive

In the new version of the solution, employee cases become inactive when they're completed. For any employee cases that are completed, you can move them to the inactive state by completing them. More information: [Use the Workplace Care Management app](app-for-health-and-safety-lead.md#manage-employee-cases)


## Upgrade from version 1.1 to 1.2

### Step 1: Configure the solution settings

With the introduction of V1.2, you will see more options appearing in the solution settings. Numerous features are now configurable in the solution settings. For guests, we added new terms of agreements which are required. More information: [Configure the solution](configure.md#set-solution-settings)


### Step 2: Setup duplicate detection rules for employee cases

To limit the number of employee cases on an employee, there is a possibility to setup duplicate detection rules which give you a warning when making multiple employee cases. More information: [Configure the solution](configure.md#set-duplicate-detection-rules-for-employee-cases)


### Step 3: Facility access available

In previous versions there was a possibility to indicate on an employee case if the employee is allowed to enter a facility. In this release, we changed this process so it blocks the employee from entering a facility. More information: [Manage employee cases - Monitoring](app-for-health-and-safety-lead.md#manage-employee-cases)

### Step 4: Send guest pass.

With the introduction of guest passes, we also allow you to share passes with guests. From within the employee app, these **Share** buttons send out an email via Outlook to the guest who is invited. To setup this up look at: [Deploy the solution - Turn on Flows](deploy.md)


## Give feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.
