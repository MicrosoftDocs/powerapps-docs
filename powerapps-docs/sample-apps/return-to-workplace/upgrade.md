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
<!--I'm not sure what the reasoning is for using "upgrade" versus "update" in this article. It does seem that "upgrade" is correct when there's a new version of software, though the UI says "update."-->
This article provides step-by-step instructions for how to upgrade the existing Return to the Workplace solution to the latest version. If you're deploying the solution for the first time, see [Deploy the Return to the Workplace solution](deploy.md).

## Prerequisites

- You should<!--What does "should" mean here? Can this say "must"?--> be a Global administrator or Microsoft Power Platform administrator to do the installation.

- You must be a Global administrator and must have a Power BI Pro license to configure and publish reports.

- You must have installed the earlier version of Return to the Workplace and have the environment details. 

> [!TIP]
> Upgrading the solution affects<!--Via Writing Style Guide.--> the user experience. We recommend that you upgrade the solution outside of normal business hours, and test the changes on a development or test environment before moving it to a production environment. 

## Step 1: Update the solution
<!--Why not "upgrade" in this H2?-->
You can update the Return to the Workplace solution by using the Power Platform admin center.

> [!NOTE]
> If you're a US Government customer, you'll have to update<!--Should this be "upgrade"?--> the solution by using the latest version of the deployment package available on GitHub. More information: [Appendix: Deploy the app and publish Power BI dashboard (US Government customers only)](deploy.md#appendix-deploy-the-app-and-publish-power-bi-dashboard-us-government-customers-only)

  1. Sign in to the [Power Platform admin center](https://admin.powerapps.com).

  2. On the left pane, select **Environments**, and then select the environment where you want to upgrade<!--And conversely, should this be "update" to match the H2?--> the solution.

  3. On the left pane<!--Edit okay? There isn't a command bar in the screenshot.-->, select **Resources** > **Dynamics 365 apps**. From the list of apps, select<!--Edit okay? I don't know what "you'll find" means.--> **Power Platform Return to the Workplace - Apps**, which is the Return to the Workplace solution.

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
<!--Suggest setting off the procedure with a procedure heading. Notice the nifty markdown that suppresses the error message about using emphasis for a heading.-->
<!--markdownlint-disable MD036-->
**To install the update**

1. Select **Get it** on the notification banner or in the notification center, or find the app in AppSource and select **Get it now**. If you have a direct link for the update, select the link.

2. Select **Install to a new workspace**.<!--Edits suggested. I think you should really focus on telling the user what to do, and then provide auxiliary information like this disclaimer.-->
  
    > [!IMPORTANT]
    > Overwriting the existing version is currently not supported.

    > [!div class="mx-imgBorder"]
    > ![Update app overwrite](media/power-bi-update-app-overwrite.png "Update app overwrite")

<!--
    Select **Install to a new workspace** to install a fresh version of the workspace and app that you'll need to reconfigure (connect to data, define navigation and permissions).
-->
  
3. Install the app in a new workplace by following these steps in the deployment topic:

    - [Step 3: Configure and publish Power BI dashboards](/powerapps/sample-apps/return-to-workplace/deploy#step-3-configure-and-publish-power-bi-dashboards)
    - [Step 4: Schedule report refresh](/powerapps/sample-apps/return-to-workplace/deploy#step-4-schedule-report-refresh)
    - [Step 5: Embed the Power BI report in the model-driven app](/powerapps/sample-apps/return-to-workplace/deploy#step-5-embed-the-power-bi-report-in-the-model-driven-app)

## Step 3: Install the Workplace Care Management dashboard

You can use the Workplace Care Management dashboard to track overall employee cases. More information: [Use the Workplace Care Management dashboard](dashboard-case-management.md)

To install the Workplace Care Management dashboard, follow the instructions in [Deploy the Return to the Workplace solution](deploy.md#step-3-configure-and-publish-power-bi-dashboards).

## Step 4: Update facilities

With the new version, we're introducing the notion of areas and floors that you can define for a particular facility.

- A *floor* indicates how many levels are present in the building.
- An *area* defines a space within a floor that has a certain capacity. Through bookings in the Employee Return to the Workplace app, you can book an area. More information: [Use the Facility Safety Management app](app-for-facility-manager.md#manage-and-monitor-facilities)

## Step 5: Define capacity for your reopen phases

Capacity is defined in an area, but it's also bound by the phase your facility is in. Every reopen phase defines the percentage by which capacity will be limited. More information: [Configure the solution](configure.md)

## Step 6: Make employee cases inactive
<!--Edit suggested, to make this heading into a step like the others.-->
In the new version of the solution, employee cases become inactive when they're finished. For any employee cases that are finished, you can move them to the inactive state by completing them.<!--I don't know what the difference is between finishing and completing a case.--> More information: [Use the Workplace Care Management app](app-for-health-and-safety-lead.md#manage-employee-cases)

## Give feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.
