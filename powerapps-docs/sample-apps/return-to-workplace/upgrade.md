---
title: Upgrade the Return to the Workplace solution for Microsoft Power Platform | Microsoft Docs
description: Provides an overview of how to upgrade the Return to the Workplace solution.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/25/2020
ms.author: garybird
ms.reviewer: kvivek
---
# Upgrade the Return to Work solution.

This article provide step-by-step instructions on how to upgrade the existing Return to Work solution to the latest version. If you're deploying the solution for the first time, see [deploy solution](deploy.md) article.

## Prerequisites

- You should be a Global administrator or Microsoft Power Platform administrator to perform the installation.

- You must be a Global administrator and must have a Power BI Pro license to configure and publish reports.

- You must have installed the earlier version of **Return to the Workplace** and have the environment details. 

- Upgrading the solution impacts the user experience, so it is advised to upgrade the solution outside of normal business hours and test this on a dev / test or qa environment. 

## Step 1: Update the Package

Update the **Return to the Workplace** solution via the Power Platform admin center. 

  1. Sign in to the Power Platform admin center.

  2. Select **Environments** and then select an environment.

  3. Under **Resources**, select **Dynamics 365 apps**. In the list you will find **Power Platform Return to the Workplace - Apps** which will be the **Return to the Workplace** solution.

> [!div class="mx-imgBorder"]
> ![Welcome screen](media/app-management-environment-view.png "Applications within the Admin Center")

  4. In the status of **Power Platform Return to the Workplace - Apps** will show **Update Available**. From the top menu bar you can select **Update** or select the **Update Available** status to start the update process. From the top menu bar you can also select **Details** to see the process of the installation.

## Step 2: Update the Power BI dashboards

Yet to be documented based on experience.

## Step 3: Install the Workplace Care Management Dashboard

Included in the next version is a new dashboard for the **Heath and Safety Leads**, this dashboard gives you a single overview where you can track employee cases. You can view more details in [use the case management dashboard](dashboard-case-management.md), to install it follow the instructions as provided in the [deploy the solution](deploy.md#step-3-configure-and-publish-power-bi-dashboards).

## Step 4: Update the Facilities

With the new version, we are introducing the notations of areas and floors for a certain facility. A floor indicates how many levels are there within a building. An area allows you to define a space within a floor that has a certain capacity. Through bookings in the employee app, you can book the area and a floor. View the [use the facility management app](app-for-facility-managers.md#manage-and-monitor-facilities) to see how you add floors and areas.

## Step 5: Define capacity for your reopen phases

Capacity is defined on an area, but it is also bound by the phase your facility it is in. Every reopen phase defines a percentage of the capacity, view the [configure the solution](configure.md) section to see how you can indicate this limit per reopen phase.

## Step 6: Employee Cases

Employee cases are made inactive when they are finished starting from this release. For any employee cases which is finished, move them to inactive state by completing them. View the [use the workplace care management app](app-for-health-and-safety-lead.md#manage-employee-cases) for more details on how to complete an employee case.

## Appendix: Update the app and publish Power BI dashboard (US Government customers only)

For GCC customers, we still support the process outside of AppSource, before executing the steps above you need to follow **Appendix: Deploy the app and publish Power BI dashboard (US Government customers only)** in the [Deploy the solution](deploy.md) page.
