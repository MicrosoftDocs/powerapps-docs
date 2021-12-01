---
title: Upgrade the Regional Government Emergency Response and Monitoring solution | Microsoft Docs
description: Provides provides detailed instructions for regional IT admins to upgrade the Regional Government Emergency Response and Monitoring solution for their organization.
author: pankajarora-msft
manager: annbe
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/05/2020
ms.author: pankar
ms.reviewer: kvivek
---

# Upgrade the Regional Government Emergency Response and Monitoring solution

Perform the steps in this article to upgrade your *existing* installation of Regional Government Emergency Response and Monitoring solution to the latest version.

If you are installing this solution for the first time, see [Deploy the solution](deploy.md).

## Prerequisites

- Ensure that you have the Global Admin credentials and environment details where
    the Regional Government Emergency Response and Monitoring solution is deployed currently.

-   Ensure all users are disconnected from your environment before you upgrade. You might have to plan the upgrade process at a time when there is minimal obstructions for your users.   

## Step 1: Download the upgrade deployment package

Get the latest deployment package (.zip) from <https://aka.ms/rer-solution>. It's the same deployment package as the one you download during the fresh deployment step.

**IMPORTANT:** Before extracting the .zip file, ensure that you unblock it.

1.  Right-click the .zip file, select **Properties**.

2.  In the properties dialog box, select **Unblock**, and then select **Apply**
    followed by **OK.**

After unblocking the file, extract the .zip file to see the following in the
extracted folder:

On extracting the .zip file, you will see the following in the extracted folder:

|**Folder**  |**Description**  |
|---------|---------|
|**Package**     |  The folder contains the Package Deployer tool and the package that you will import later to set up the solution in your environment.       |
|**Power BI Template**     | Contains the Power BI Report template file (.pbit) that you will use to configure reporting. More information: [Step 3: Publish the latest Power BI dashboard](#step-3-publish-the-latest-power-bi-dashboard)        |
|**SampleData**     |   Contains the sample master data files (.xlsx) that you can use to import sample data.       |

## Step 2: Install the upgrade package

Install the upgrade package in the **same environment** where you have the
existing solution installed. You can install the upgrade package in one of the following 3 ways just like you did when deploying the solution for the **first time**.

- Microsoft AppSource (for Power Apps US Govt customers only). See [Option A: Install the app from Microsoft AppSource (US Govt customers)](deploy.md#option-a-install-the-app-from-microsoft-appsource-us-govt-customers) in the deployment topic

- Microsoft AppSource (for Power Apps commercial version customers). See [Option B: Install the app from Microsoft AppSource](deploy.md#option-b-install-the-app-from-microsoft-appsource) in the deployment topic

- Deployment package that you downloaded earlier. See [Option C: Install the app from the deployment package](deploy.md#option-c-install-the-app-from-the-deployment-package) in the deployment topic

## Step 3: Publish the latest Power BI dashboard

Use the .pbit file in the upgrade package to configure and publish the latest
Power BI dashboard. 

Steps to use the .pbit file are the same as the original deployment; make sure you use the same workspace to overwrite the existing Power BI dashboard if you want to preserver the Power BI report URL that is used for embedding it into Power Apps portal. 

More information: [Step 5: Configure and publish Power BI dashboard](./deploy.md#step-5-configure-and-publish-power-bi-dashboard) in the deployment topic.

## Step 4: Verify the Power BI report URL in your portal

This step is required only if your Power BI report URL has changed in the previous step owing to you publishing the dashboard in a new workspace. Verify the **PowerBI Path** site setting in your portal and update the value with the latest Power BI report URL.

For detailed steps, see [Embed Power BI report in portal](./deploy.md#the-process-1) in the deployment topic.

Make sure to restart our portal for the changes to take effect. More
information: [Restart the portal](./deploy.md#restart-the-portal) in the deployment topic.

## Step 5: Verify the processes

Verify that the **Send Invitation** and **Send Password Reset To Contact**
processes are still valid, that is, they have an account in the **From** field
that can send emails and the rest of the details are fine.

For details about how to fix these processes, see [Step 10: Fix the processes for the app](./deploy.md#step-10-fix-the-processes-for-the-app) in the deployment topic.

## Step 6: Verify the flows for sending emails

Do the following:

|Flow name|Changes|
|--|--|
|**Portal User Request: Send Email on Decline Request**|Update the connection to connect to Microsoft Dataverse and then specify a user account to send emails.|
|**Portal User Request: Send Email to Admins on Request Creation**|Update the connection to connect to Dataverse and then specify a user account to send emails. Additionally, update the portal URL in the email body as per your Portal URL.| 

For detailed information about this, see [Step 11.1: Fix the flows for sending emails](deploy.md#step-111-fix-the-flows-for-sending-emails) in the deployment topic.

## Step 7: Verify the flows for performing tasks

Verify and authorize the connection information of the flows for performing specific tasks.

For details about how to do this, see [Step 11.2: Fix the flows for performing specific tasks](./deploy.md#step-112-fix-the-flows-for-performing-specific-tasks) in the deployment topic.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]