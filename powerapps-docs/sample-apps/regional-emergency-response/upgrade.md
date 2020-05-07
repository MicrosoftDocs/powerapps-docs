---
title: Upgrade the Regional Government Emergency Response and Monitoring solution | Microsoft Docs
description: Provides provides detailed instructions for regional IT admins to upgrade the Regional Government Emergency Response and Monitoring solution for their organization.
author: KumarVivek
manager: annbe
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/29/2020
ms.author: kvivek
ms.reviewer: kvivek
searchScope:
  - PowerApps
---

# Upgrade the Regional Government Emergency Response and Monitoring solution

Perform the steps in this article to upgrade your *existing* installation of Regional Government Emergency Response and Monitoring solution to the latest version.

If you are installing this solution for the first time, see [Deploy the solution](deploy.md).

## Prerequisites

- Ensure that you have the Global Admin credentials and environment details where
    the Regional Government Emergency Response and Monitoring solution is deployed currently.

-   Ensure all users are disconnected from your environment before you upgrade. You might have to plan the upgrade process at a time when there is minimal obstructions for your users.   

-   Ensure you have copied the Email contents to a Word file from the Send
    Invitation, Send Password Reset To Contact processes

## Step 1: Download the upgrade deployment package

Get the latest deployment package (.zip) from <https://aka.ms/rer-solution>. It's the same deployment package as the one you download during the fresh deployment step.

**IMPORTANT:** Before extracting the .zip file, ensure that you unblock it.

1.  Right click the .zip file, select **Properties**.

2.  In the properties dialog box, select **Unblock**, and then select **Apply**
    followed by **OK.**

After unblocking the file, extract the .zip file to see the following in the
extracted folder:

On extracting the .zip file, you will see the following in the extracted folder:

|**Folder**  |**Description**  |
|---------|---------|
|**Package**     |  The folder contains the Package Deployer tool and the package that you will import later to set up the solution in your environment.       |
|**Power BI Template**     | Contains the Power BI Report template file (.pbit) that you will use to configure reporting. More information: [Step 5: Configure and publish Power BI dashboard](#step-5-configure-and-publish-power-bi-dashboard)        |
|**SampleData**     |   Contains the sample master data files (.xlsx) that you can use to import sample data.       |

## Step 2: Install the upgrade package

Install the upgrade package in the **same environment** where you have the
existing solution installed. You can install the upgrade package in one of the following 3 ways just like you did when deploying the solution for the **first time**.

- Microsoft AppSource (for Power Apps US Govt customers only). See [Option A: Install the app from Microsoft AppSource (US Govt customers)](#option-a-install-the-app-from-microsoft-appsource-us-govt-customers) in the deployment topic

- Microsoft AppSource (for Power Apps commercial version customers). See [Option B: Install the app from Microsoft AppSource](#option-b-install-the-app-from-microsoft-appsource) in the deployment topic

- Deployment package that you downloaded earlier. See [Option C: Install the app from the deployment package](#option-c-install-the-app-from-the-deployment-package) in the deployment topic

## Step 3: Publish the latest Power BI dashboard

Use the .pbit file in the upgrade package to configure and publish the latest
Power BI dashboard. 

Steps to use the .pbit file are the same as the original deployment; make sure you use the same workspace to overwrite the existing Power BI dashboard if you want to preserver the Power BI report URL that is used for embedding it into Power Apps portal. 

More information: [Step 5: Configure and publish Power BI
dashboard](https://docs.microsoft.com/powerapps/sample-apps/regional-emergency-response/deploy#step-5-configure-and-publish-power-bi-dashboard)

## Step 4: Verify the Power BI report URL in your portal

This step is required only if your Power BI report URL has changed in the previous step owing to you publishing the dashboard in a new worksoaceVerify the **PowerBI Path** site setting in your portal and update the value
with the latest Power BI report URL.

For detailed steps, see [Embed Power BI report in
portal](https://docs.microsoft.com/powerapps/sample-apps/regional-emergency-response/deploy#the-process-1)

Make sure to restart our portal for the changes to take effect. More
information: [Restart the
portal](https://docs.microsoft.com/powerapps/sample-apps/regional-emergency-response/deploy#restart-the-portal)

## Step 5: Verify the Send Invitation and Send Password Reset To Contact processes

Verify that the **Send Invitation** and **Send Password Reset To Contact**
processes are still valid, that is, they have an account in the **From** field
that can send emails and the rest of the details are fine.

For details about how to fix these processes, see:

-   [Step 10: Fix the Send Invitation
    process](https://docs.microsoft.com/powerapps/sample-apps/regional-emergency-response/deploy#step-10-fix-the-send-invitation-process)

-   [Step 11: Fix the Send Password Reset To Contact
    process](https://docs.microsoft.com/powerapps/sample-apps/regional-emergency-response/deploy#step-11-fix-the-send-password-reset-to-contact-process)

## Step 6: Verify the Flow supply tracking flow is enabled

This flow enables the frontline user to add supplies through the portal that
gets saved in Common Data Service.

For details about how to fix these processes, see [Step 13: Verify the Flow
supply tracking flow is
enabled](https://docs.microsoft.com/powerapps/sample-apps/regional-emergency-response/deploy#step-13-verify-the-flow-supply-tracking-flow-is-enabled).

## Step 7: Update the details of flows for sending emails

In this step, we are going to do the following:

|Flow name|Changes|
|--|--|
|**Portal User Request: Send Email on Decline Request**|Update the connection to connect to Common Data Service as a user account that should be used for sending the emails, like no-reply\@[*customerdomain*].com. This user account must be already set up in your environment with the server-side synchronization enabled.|
|**Portal User Request: Send Email to Admins on Request Creation**|Update the connection to connect to Common Data Service as a user account that should be used for sending the emails, like no-reply\@[*customerdomain*].com. This user account must be already set up in your environment with the server-side synchronization enabled. Additionally, update the portal URL in the email body as per your Portal URL.| 

1.  Sign into [Power Automate](https://flow.microsoft.com/).

2.  In the left pane, select **Solutions.** From the solution list, select **Regional Emergency Response Solution** to open the solution.

    > [!div class="mx-imgBorder"] 
    > ![Open the solution](media/deploy-open-solution.png "Open the solution")

3.  In the solution, filter on **Flow** to find the **Flow supply tracking** record. Ensure that the status is set to **On**.

    > [!div class="mx-imgBorder"] 
    > ![Find the Flow Supply Tracking record](media/deploy-find-record.png "Find the Flow Supply Tracking record")

4.  If it is not set to **On**, select the flow name to open the flow definition.

5.  In the flow definition, select **Turn On** in the toolbar.

