---
title: "Add reporting to your model-driven app" 
ms.custom: ""
ms.date: 06/06/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.assetid: b4098c96-bce1-4f57-804f-8694e6254e81
caps.latest.revision: 15
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Add reporting to your model-driven app

PowerApps apps can include reports that provide useful business information to the user. These reports are based on SQL Server Reporting Services and provide the same set of features that are available for typical SQL Server Reporting Services reports.

> [!div class="mx-imgBorder"] 
> ![](media/progress-against-goals-report.png "Progress against goals standard report")

System reports are available to all users. Individuals who create or otherwise own reports can share them with specific colleagues or teams, or can make the reports available to the organization, so that all users can run them. These reports use FetchXML queries that are proprietary to Common Data Service and Dynamics 365 for Customer Engagement apps and retrieve data to build the report. Reports that you create in a PowerApps app are Fetch-based reports.

Reports can be built in any of the following ways.

- From a model-driven app using the report wizard. More information: [Create or edit a report using the Report Wizard](/dynamics365/customer-engagement/basics/create-edit-copy-report-wizard) 
- From a model-driven app using an advanced find query. To do this, you build an advanced find query and then select **Download as FetchXML**. Next, open the xml file in the report wizard, fill in the required fields, and save the report. More information: [Add a report](/dynamics365/customer-engagement/basics/add-existing-report) 
- Create custom reports using SQL Server Data Tools and Report Authoring Extensions. More information: [Reporting and Analytics Guide](/dynamics365/customer-engagement/analytics/reporting-analytics-with-dynamics-365)


## Add reporting your Unified Interface app
You can add fetch-based reporting functionality to your app so that users can run, share, create, and edit reports. To do this, you add the report entity to your app's site map. 

1. Sign in to PowerApps and open an existing app for editing. 
2. In App Designer, select the pencil icon next to Site Map. 
3. In the Sitemap Designer, select Add and then select Area. 
4. In the Title box, enter *Reports* or another name that you want. 
5. Select the **Reports** area, select Add, select Group, and then in the group Title box enter *Reports* or another name that you want. 
6. Select the group Reports, select Add, select Subarea and enter the following properties: 

   - Type: Entity
   - Entity: From the list of entities, select the Report entity.  
   - Title: Enter a descriptive title, such as *Reports*.

   ![Add report entity to site map](media/report-entity-sitemap.png)

7. Select Save and Close to return to the app designer. 


8. In App Designer select Save, and then select Publish.


Now the app displays a Reports area where app users can view, run, assign, share, and edit the reports they have permission to as well as create new reports using the report wizard. 

> [!div class="mx-imgBorder"] 
> ![](media/report-feature-in-app.png "Report view")

<!-- Link to Mint's end user reporting topics -->