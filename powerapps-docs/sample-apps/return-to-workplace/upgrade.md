---
title: Upgrade the Return to the Workplace solution for Microsoft Power Platform | Microsoft Docs
description: Provides an overview of the Return to the Workplace solution.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/21/2020
ms.author: garybird
ms.reviewer: kvivek
---
# Upgrade the Return to Work solution.

Follow the steps in this article to upgrade your existing installation of Return to Work solution to the latest version. 

If this is the first time you deploy the solution, look into Deploy Solution.

## Prerequisites 

- Ensure you have the Global Admin credentials and environment details where the Return to Work solution is deployed currently. 

- Ensure all users are disconnected from your environment before you upgrade. You might have to plan the upgrade process at a time when there is minimal obstruction for your users. 

## Step 1: Update the Package

Yet to be documented based on experience.

## Step 2: Update the Power BI dashboards

Yet to be documented based on experience.

## Step 3: Update the Facilities

With the new version, we are introducing the notations of areas and floors for a certain facility. A floor indicates how many levels are there within a building. An area allows you to define a space within a floor that has a certain capacity. Through bookings in the employee app, you can book the area and a floor. View the facility manager safety app section to see how you add floors and areas.

## Step 4: Define capacity for your reopen phases

Even though the capacity is defined on an area, it is bound by the phase your facility is in. Every reopen phase defines a percentage of the capacity, view the [configure the solution](configure.md) section to see how you can assign this to a reopen phase. 

## Step 5: Employee Cases

Employee cases are made inactive when they are finished now. For any employee cases you are finished, move them to inactive state.

## Appendix: Update the app and publish Power BI dashboard (US Government customers only)

For GCC customers, we still support the process outside of AppSource, before executing the steps above you need to follow **Appendix: Deploy the app and publish Power BI dashboard (US Government customers only)** in the [Deploy the solution](deploy.md) page.

