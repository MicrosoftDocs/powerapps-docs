---
title: Transfer data from Hospital to Regional System | Microsoft Docs
description: Provides an overview of Hospital Emergency Response Solution.
author: pankajarora-msft
manager: annbe
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/09/2020
ms.author: pankar
ms.reviewer: kvivek
searchScope:
  - PowerApps
---
# Transfer data from Hospital to Regional System

Microsoft provides you the following solutions for emergency response:

- The *Hospital Emergency Response solution* enables you to collect data for situational awareness of available beds and supplies, COVID-19 related patients, staffing, and pending discharges at a **hospital level**.

- The *Regional Government Emergency Response and Monitoring solution* enables you to collect data for situational awareness of available beds and supplies, COVID-19 related patients, staffing, and pending discharges at a **regional health organization level**. Each hospital under the regional organization jurisdiction can submit their data by using the regional organization's portal, which is also part of the *Regional Government Emergency Response and Monitoring solution*.

Now, hospitals with the Hospital Emergency Response solution can transfer their data to the Regional Government Emergency Response and Monitoring solution. 

1. Hospitals can publish their data in the hospital solution, such as information about beds, supplies, equipment, and staff, to a Secure File Transfer Protocol (SFTP) server hosted by their regional medical organization. You can schedule data publish and publish on-demand. 

2. The hospital data published on the SFTP server is automatically downloaded to the regional solution and is used to create respective data records (beds, supplies, equipment, and staff) for the hospital in the regional solution. 

> [!NOTE]
> This article demonstrates how you can use an SFTP server to transfer data from hospital to regional solutions. You can also use other ways to transfer data to/from these solutions, such as [import and export data as CSV files](/powerapps/maker/common-data-service/data-platform-import-export) and [use web services](/powerapps/developer/common-data-service/work-with-data-cds). 


## Prerequisites

These are the prerequisites for the data transfer to work successfully.

- **SFTP server**: The regional health organization must have an SFTP server configured with a folder for each hospital on the SFTP server where the hospital can publish their data. The hospital must get the credentials from regional health organization to connect to the folder on the SFTP server.<br/>
For information about creating an SFTP server, see [SFTP on Azure](https://docs.microsoft.com/samples/azure-samples/sftp-creation-template/sftp-on-azure/)

- **CDC Short Name**: Each **Supply** and **Staffing Type** record must have the **CDC Short Name** value. You can create and manage these records in the **Admin app** of hospital and regional solutions.

- **DOH Number**: Each **Facility** record must have a valid **DOH Number** value. You can create and manage these records in the **Admin app** of hospital and regional solutions.

## Configure your solutions for data transfer

IT admins need to perform some steps to configure the data transfer from Hospital Emergency Response solution to SFTP server and from SFTP server to Regional Government Emergency Response and Monitoring solution.

> [Step 1: Create connections](#step-1-create-connections)

> [Step 2: Enable flows for publishing data to SFTP (Hospital)](#step-2-enable-flows-for-publishing-data-to-sftp-hospital)

> [Step 3: Enable flow for pulling hospital data data from SFTP (Regional)](#step-3-enable-flow-for-pulling-hospital-data-data-from-sftp-regional)

### Step 1: Create connections

Both the hospital and regional systems use Power Automate flows to transfer data between the hospital/regional solutions and SFTP server. In this step, we will create connections for Common Data Service and SFTP to be used by the flows for data transfer.

This step is required for both hospital and regional solutions.

> [!IMPORTANT]
> Create connections before installing the hospital and regional emergency response app solutions or upgrading to the latest version. This will save you a lot of steps later while enabling flows that get installed as part of these solutions. 

1. Sign in to [Power Apps](https://make.powerapps.com).

1. From the top-right corner, select your hospital or regional environment.

1. From the left navigation pane, expand **Data** and select **Connections**.

1. Select **New Connection**, and then type **Common Data Service** in the search box. 

1. From the search results, select **+** next to **Common Data Service (current environment)** connector to add a connection.

    > [!div class="mx-imgBorder"] 
    > ![Common Data Service connector](media/cds-connector.png)

1. On the next screen, select **Create**. 

1. Select or specify the credentials to create the connector. On successful authentication, your connection will be created.

1. Select **New Connection**, and then type **SFTP** in the search box.

1. From the search results, select **+** next to **SFTP - SSH** connector to add a connection.

    > [!div class="mx-imgBorder"] 
    > ![SFTP connector](media/sftp-connector.png)

1. In the **SFTP - SSH** dialog box, provide the credentials to connect to the folder on the SFTP server. These details would have been already provided to you by your regional health organization as mentioned earlier in the **Prerequisites** section.

1. Select **Create**. Power Apps validates the connection details, and on successful authentication, creates an SFTP connection.

At the end of this step, you should have two connections: 1 for Common Data Service and another one for SFTP.

### Step 2: Enable flows for publishing data to SFTP (Hospital)

This step has to be performed by the admins of the Hospital Emergency Response solution after they have installed the solution.

In this step, we will enable the following flows that will publish reviewed data from the hospital solution to SFTP server on a set schedule and on-demand:
- Publish Bed Census Data
- Publish COVID Data
- Publish Data for All Facilities
- Publish Equipment Needs Data
- Publish Staff Updates
- Publish Supply Item Details
- Update Sync Status
- Update Equipment

To enable these flows:

1.  Sign into [Power Automate](https://flow.microsoft.com/).

1.  From the left pane, select **Solutions.** From the solution list, select **Hospital Emergency Response Solution** to open the solution.

1.  In the solution, filter on **Flow** to find all the flows.

    > [!div class="mx-imgBorder"] 
    > ![All flows](media/all-flows-hospital.png)

1.  Select a flow name to open the flow definition. For example, select **Publish Bed Census Data**. 

1.  Verify the embedded connections for this flow. These should be the same connections that you created earlier. If necessary, select **Edit** on the toolbar to authorize/fix the connections for the flow.

1.  Select **Save** to save the changes, and then select **Turn On**.

1.  Repeat steps 4-6 for other flows listed earlier.

### Step 3: Enable flow for pulling hospital data from SFTP (Regional)

This step has to be performed by the admins of the Regional Government Emergency Response and Monitoring solution.

In this step, we will enable the **Create Record when a File is Created in SFTP Location** flow that will automatically create a record for hospital in the regional solution based on the data uploaded from the hospital system in the SFTP server.

1.  Sign into [Power Automate](https://flow.microsoft.com/).

1.  From the left pane, select **Solutions.** From the solution list, select **Regional Emergency Response Solution** to open the solution.

1.  In the solution, filter on **Flow** to find all the flows.

    > [!div class="mx-imgBorder"] 
    > ![Flows in the app](media/conf-all-flows.png "Flows in the app")

1.  Select a **Create Record when a File is Created in SFTP Location** flow to open the flow definition. 

1.  Verify the embedded connections for this flow. These should be the same connections that you created earlier. If necessary, select **Edit** on the toolbar to authorize/fix the connections for the flow.

1.  Select **Save** to save the changes, and then select **Turn On**.


## Review and publish data to SFTP

After your IT admin has configured the solution for data transfer from the hospital solution, you can use the **Review and Publish Data** model-driven app to review the data and mark it as completed for publishing to the folder on the SFTP server.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. From the top-right corner, select your hospital environment.

1. Select **Apps** in the left navigation pane, and then select the **Review and Publish Data** app.

1. In the app, all the facilities are listed. Select a facility for which you want to review the data and publish. This will open the facility record.

    > [!div class="mx-imgBorder"] 
    > ![Facility review](media/facility-review.png)

1. Scroll down the page to review the following data for your facility: Bed Census, COVID Stats, Equipment Needs, Supply Tracking, and Staff Updates. If necessary, update the data in grids, and then select the save icon to save your changes.

    > [!div class="mx-imgBorder"] 
    > ![Update values](media/update-values.png)

1. Once reviewed, you can select a row of data, and select **Mark Complete**. Select **OK** in the confirmation dialog box to complete the action.

    The record's review status changes to **Completed**.

    > [!div class="mx-imgBorder"] 
    > ![Review completed](media/review-completed.png)

The scheduled flows will pick up the completed items for publishing to the SFTP folder that you configured earlier.

### Manually publish data

The scheduled flow publishes data at a certain time, but what if you want to manually or immediately publish the data after reviewing it. 

1.  In the **Review and Publish Data** app, select the record that you want to publish from the **Published History** in the left pane. All the published data for the selected entity are displayed. If you want to view the active records for the entity, use the view selector.

    > [!div class="mx-imgBorder"] 
    > ![Review completed](media/manual-data-publish.png)

1. In this case, we will publish the data that we reviewed in the previous section. So, select the **Active Bed Census** view, select the row that was marked as completed, and then select **Flow** > **Publish Bed Census Data**.

    > [!div class="mx-imgBorder"] 
    > ![Manually run flow](media/manually-run-flow.png)

1. On the next screen, review that the connections are valid, and select Continue

    > [!div class="mx-imgBorder"] 
    > ![Manually run flow](media/publish-data-flow.png)

1. On the next screen select **Run flow**. A message appears stating that the flow run started successfully and how you can monitor the progress.

## Issues and feedback

- To report an issue with the Hospital Emergency Response sample app, visit <https://aka.ms/emergency-response-issues>.

- For feedback about the Hospital Emergency Response sample app, visit <https://aka.ms/emergency-response-feedback>.

