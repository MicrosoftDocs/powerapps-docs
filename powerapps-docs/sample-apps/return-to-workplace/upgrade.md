---
title: Overview of the Return to the Workplace solution for Microsoft Power Platform | Microsoft Docs
description: Provides an overview of the Return to the Workplace solution.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/21/2020
ms.author: garybird
ms.reviewer: kvivek
---
# Upgrade the Return to Work solution.

Follow the steps in this document to upgrade your existing installation of Return to Work solution to the lates version. 

If this is the first time you deploy the solution, look into Deploy Solution.

# Prerequisistes 

- Ensure you have the Global Admin credentials and environment details where the Return to Work solution is deployed currently. 

- Ensure all users are disconnected from your environmnet before you upgrade. You might have to plan the upgrade process at a time when there is minimal obstruction for your users. 

## Step 1: Update the Package

When you have installed the package via AppSource, updates will appears in the Power Platform admin center.

1. Sign in to the [Power Platform admin center](https://aka.ms/ppac).

2. Create a Common Data Service environment with a database. More information: [Create and manage environments](https://docs.microsoft.com/power-platform/admin/create-environment)

   > [!IMPORTANT]
   > If you select a security group for the database while you're creating it, the apps can be shared only with users who are members of the security group.

3. Create appropriate users, and assign security roles. More information: [Create users and assign security roles](https://docs.microsoft.com/power-platform/admin/create-users-assign-online-security-roles)

After you've created your environment, you can access it by using the following URL: `https://[myenv].crm.dynamics.com`, where [myenv] is the name of your environment. Make a note of this environment URL.

## Step 2: Update the Power BI dashboards

...

## Step 3: Update the Facilities

With the new version we are introducing the notitions of areas and floors for a certain facility. A floor indicates how many levels are there within a building. An area allows you to define a space within a floors which has a certain capacity. Through bookings in the employee app, you can book the area and a floor. View the facility manager safety app section to see how you add floors and areas.

## Step 4: Define capacity for your reopen phases

Even though the capacity is defined on an area, it is bound by the phase your facility is in. Every reopen phase defines a percentage of the capacity, view the configure the solution section to see how you can assign this to a reopen phase. 

## Step 5: Employee Cases


## Appendix: Update the app and publish Power BI dashboard (US Government customers only)

Get the larest deployment package (.zip) from ______________. Notice its the same deployment package as the one you download during the fresh deployment step.

**Important**: Before extracting the .zip file, ensure that you unblock it. 

1. Right-click the .zip file, select **Properties**.

2. In the properties dialog box, select **Unblock**, and then select **Apply** followed by **OK**.

After unblocking the file, extract the .zip file to see the following in the extracted folder:

On extracting the .zip file, you will see the following in the extracted folder:

| **Name**              | **Description**                                |
   |------------------------|------------------------------------------------|
   | Package        | Enter a number for the new facility.                  |
   | Power BI                  | Enter a  name for the new facility.                    |
   
