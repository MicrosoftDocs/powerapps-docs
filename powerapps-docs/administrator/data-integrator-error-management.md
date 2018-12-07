---
title: Data Integrator error management and troubleshooting
description: Integrate data from multiple sources into Common Data Service for Apps
author: sabinn-msft
ms.service: powerapps
ms.topic: how-to
ms.component: cds
ms.date: 12/07/2018
ms.author: sabinn
search.audienceType: 
  - admin
search.app: 
  - D365CE
  - PowerApps
  - Powerplatform
---
# Data Integrator error management and troubleshooting

The Data Integrator is a point-to-point integration service used to integrate data from multiple sources--for example, Dynamics 365 for Finance and Operations, Dynamics 365 for Sales, and Salesforce, SQL (Preview)--into Common Data Service for Apps (CDS for Apps). It also supports integrating data into Dynamics 365 for Finance and Operations and Dynamics 365 for Sales. The [Integrate data into Common Data Service for Apps](data-integrator.md) topic provides detailed step-by-step instructions to help you set up projects for process-based integration scenarios like Prospect to Cash, Field Service, and Project Service integrations. 

While we are constantly evolving and driving fixes into the platform based on customer feedback, we understand there is a need to provide guidance when you run into issues. This topic walks you through error management and troubleshooting some of these issues.

## View health of project executions

Every time a data integration project is executed (manually or scheduled), you can view the status of the execution on the admin dashboard and/or the project list page.  

> [!div class="mx-imgBorder"] 
> ![](media/DashboardandProjectListing.png "Dashboard and project listing")

The admin dashboard provides a one-stop real-time view of all your project runs and their status with a drill-down to view execution details. The dashboard shows you the individual and summarized count of executions. These are color-coded to show the status of each project: green for completed projects, yellow for completed projects with warnings, and red for projects with an error status. Similarly, the green, yellow, and red icons on the project list page indicate the status of your projects.

Additionally, to view more details, you can drill through project executions via the admin dashboard by selecting individual bar charts.

> [!div class="mx-imgBorder"] 
> ![](media/DashboardDrill-down.png "Dashboard drill down")

Now you can drill through individual errors.

> [!div class="mx-imgBorder"] 
> ![](media/DashboardDrill-down2.png "Dashboard drill down")

You can also view project execution details by selecting the individual projects on the project list page and viewing the historical executions and status on the **Execution history** tab.

> [!div class="mx-imgBorder"] 
> ![](media/ProjectExecutionhistory.png "Project execution history")

If you get a warning or error, you can drill down more by clicking through the executions on the **Execution history** tab.

> [!div class="mx-imgBorder"] 
> ![](media/DashboardDrill-down3.png "Project execution history warning")

## Project monitoring

We highly encourage our customers and partners to subscribe to email-based notifications so you receive email alerts on project executions that completed with either warnings or errors. For each project, on the **Scheduling** tab, you can select email-based notifications and provide multiple email addresses (including group addresses), separated by commas.

> [!div class="mx-imgBorder"] 
> ![](media/RemoteMonitoring.png "Remote monitoring warning")

Any time a project completes with a warning or is in the error state, you get an email notification indicating the project execution status with a drillthrough link to the specific failure.

> [!div class="mx-imgBorder"] 
> ![](media/RemoteMonitoring-EmailNotification.png "Remote monitoring email notification")

Selecting the link takes you directly to your project execution status, which you can further drill through for specific errors.

> [!div class="mx-imgBorder"] 
> ![](media/RemoteMonitoring-EmailNotification-clickthrough.png "Remote monitoring email notification drill down")

## Project execution status

When a data integration project is executed (manually or scheduled), it creates a detailed log with project name, a time stamp showing the last update, and the project status.

Each project execution is marked with the status Completed, Warning, or Error:

* **Completed**
   
   Status if all records were upserted successfully. ("Upsert" or "update insert" is a logic to either update the record, if it already exists, or to insert a new record.) 

   > [!div class="mx-imgBorder"] 
   > ![](media/ProjectStatus_Complete.png "Project status complete")

* **Warning**

   Status if some records were upserted successfully, while some failed or errored out.

   > [!div class="mx-imgBorder"] 
   > ![](media/ProjectStatus_Warning.png "Project status warning")

* **Error**

   Status if none of the records were successful and/or errored out, and there were no upserts or inserts in the destination.

   > [!div class="mx-imgBorder"] 
   > ![](media/ProjectStatus_Error.png "Project status error")

   If the project execution is in the **Error** state, then it will automatically retry execution at the next scheduled run.

You can also manually retry an execution by selecting **Re-run execution** via the ellipsis on the **Execution history** page.

## Quick tips on troubleshooting common scenarios 

Here are some quick tips that will help you troubleshoot some of the common scenarios.

### Connection or environment issues 

If you are unable to see your connections or environments in the drop-down while trying to create a Connection set, here are some of the things you can do to troubleshoot the issue:

> [!div class="mx-imgBorder"] 
> ![](media/ConnectionSet1.png "Connection set")

* **Connection**: Ensure you have created your connections under Data/Connections on [https://web.powerapps.com ](https://web.powerapps.com) and that they are in the **Connected** state. If you see a **Fix Connection** notification, you should double-check the credentials used for the account, and use the **Switch account** option from the ellipsis to reauthenticate.

   > [!div class="mx-imgBorder"] 
   > ![](media/ConnectionsIssue.png "Connections issue")

* **Environment**: If you don’t see your environments in the drop-down, ensure that the account you used to create the connections has the appropriate access to the entity. A good way to test this is by creating a *flow* (using Microsoft Flow). 

  Here is an example of creating a simple flow to test your connection to Dynamics 365 for Finance and Operations:

  1. Create a new flow (choose **Create from blank**) under **Business logic/Flow** from [https://web.powerapps.com](https://web.powerapps.com).

      > [!div class="mx-imgBorder"] 
      > ![](media/ConnectionstestFlow1.png "Connections new flow")

  2. Select a **Recurrence** trigger. Under **New Step**, search for and select **Dynamics 365 for Finance and Operations connector**.

      > [!div class="mx-imgBorder"] 
      > ![](media/ConnectionstestFlow2.png "Connections recurrence trigger")

  3.  Select **Create record** as an action. In the drop-down, ensure that you are logged in with the appropriate account. This is the same account you use to create a connection for your data integration projects.

      > [!div class="mx-imgBorder"] 
      > ![](media/ConnectionstestFlow3.png "Connections create record")

  4. Select the drop-down under **Instance** to show all the Dynamics 365 Finance and Operations environments. This is a good step to verify that your account (from the previous step) has access to the environments. 

      > [!div class="mx-imgBorder"] 
      > ![](media/ConnectionstestFlow4.png "Connections instances")

  5. Once you have picked your environment, confirm that you have access to all the entities under it.

      > [!div class="mx-imgBorder"] 
      > ![](media/ConnectionstestFlow5.png "Connections confirm access to entities")

* **Organizations**: This is where you would specify the Legal Entity (LE) (for example, USMF) for Dynamics 365 for Finance and Operations, the Business Unit (BU) for Dynamics 365 for Sales, or the CDS for Apps organization name. If you miss this step, you get a message that contains valid names corresponding to your application that you then need to plug in under Organizations.

### Project validation errors 

First, you validate a data integration project, and then execute it. Some of the top reasons for validation errors include:

* Incorrect company/business unit selected during project creation 
* Missing mandatory columns 
* Incomplete or duplicate mapping 
* Field type mismatch

Here is an example of how the error manifests in the case of duplicate mapping. The orange banner indicates mapping issues.

> [!div class="mx-imgBorder"] 
> ![](media/ProjectValidationErrors1.png "Mapping issues")

When you drill further into the project execution history, you see there is a duplicate field issue.

> [!div class="mx-imgBorder"] 
> ![](media/ProjectValidationErrors2.png "Duplicate field issue")

When you inspect the mapping, you can identify duplicates. In this case, the source field **fax** is incorrectly mapped to ADDRESSCITY.

> [!div class="mx-imgBorder"] 
> ![](media/ProjectValidationErrors3.png "Incorrect mapping")

Once you fix the mapping, the error should go away, and you should be able to execute the project successfully.

> [!div class="mx-imgBorder"] 
> ![](media/ProjectValidationErrors4.png "Mapping fixed")

### Project execution issues 

If you are notified of a project execution that completed with a warning or is in an error state, the first step is to drill into the execution history. From the project list page, select the individual project and review the latest execution on the **Execution history** tab. You can then click through to the specific error.

> [!div class="mx-imgBorder"] 
> ![](media/Tshoot-WarningError1.png "Troubleshooting error")

If this is an integration project where Dynamics 365 for Finance and Operations is the source, go to the Data Management workspace in Dynamics 365 Finance and Operations. Then filter projects based on your data integration project name, or specifically choose the type of import or export job.

> [!div class="mx-imgBorder"] 
> ![](media/Tshoot-WarningError2.png "Data Management workspace")

Additionally, you can open the job history of the project and drill through the job ID based on the time stamp of your execution. You can also inspect the execution log, view historical runs, and view the staging data.

> [!div class="mx-imgBorder"] 
> ![](media/Tshoot-WarningError3.png "Project job history")




