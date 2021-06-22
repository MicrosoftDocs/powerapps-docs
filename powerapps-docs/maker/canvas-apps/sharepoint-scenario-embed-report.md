---
title: Embed the Power BI project report in SharePoint Online
description: Learn about how to embed Power BI report in SharePoint Online site.
author: NickWaggoner
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 06/18/2020
ms.author: niwaggon
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Embed the Power BI project report in SharePoint Online
> [!NOTE]
> This article is part of a tutorial series on using Power Apps, Power Automate, and Power BI with SharePoint Online. Make sure you read the [series introduction](sharepoint-scenario-intro.md) to get a sense of the big picture, as well as related downloads.

We'll now embed our Power BI report in the same SharePoint Online site that hosts our two lists. Power BI supports a variety of approaches to embedding, including directly integrating into SharePoint pages for web and mobile views.

With this type of embedding, Power BI embeds the report as a web part, provides appropriate access for users, and lets you click through from the embedded report to the report at powerbi.com. First, we'll generate an embed link in Power BI, then use that link in a page that we create. For more information on embedding, see [Embed with report web part in SharePoint Online](/power-bi/service-embed-report-spo).

## Step 1: Generate an embed link
1. Sign in to Power BI, then in the left navigation pane, click or tap the report name.
   
    ![Navigate to report](./media/sharepoint-scenario-embed-report/08-01-01-reports.png)
2. Click or tap **File**, then **Embed in SharePoint Online**.
   
    ![Embed in SharePoint Online](./media/sharepoint-scenario-embed-report/08-01-02-embed-spo.png)
3. Copy the embed link from the dialog box to a file, then click or tap **Close**. We will use the link after we create a SharePoint page.
   
    ![Embed link for SharePoint](./media/sharepoint-scenario-embed-report/08-01-03-embed-url.png)

## Step 2: Embed the report
1. Sign in to SharePoint, then click or tap **Site contents**.
   
    ![SharePoint site contents](./media/sharepoint-scenario-embed-report/08-01-04-site-contents.png)
2. You could just include a report on the team home page, but we'll show you how to create a separate page for it also. Click or tap **New**, then **Page**.
   
    ![New SharePoint page](./media/sharepoint-scenario-embed-report/08-01-05-new-page.png)
3. Enter a name for the page, like "Project Analysis".
4. Click or tap ![Plus icon](./media/sharepoint-scenario-embed-report/icon-plus.png) then **Power BI**.
   
    ![Add Power BI page part](./media/sharepoint-scenario-embed-report/08-01-06-add-page-part.png)
5. Click or tap **Add report**.
   
    ![Add report](./media/sharepoint-scenario-embed-report/08-01-07-add-report.png)
6. In the right pane, copy the embed URL into the **Power BI report link** box. Set both **Show Filter Pane** and **Show Navigation Pane** to **On**.
   
    ![Report settings](./media/sharepoint-scenario-embed-report/08-01-08-report-settings.png)
7. The report is now embedded in the page. Click **Publish** to make it available to anyone who can access the underlying report.
   
    ![Report embedding complete](./media/sharepoint-scenario-embed-report/08-01-09-report-complete.png)

## Step 3: Grant access to the report.
If you are using Office 365 Groups as we recommend, make sure users who need access are members of the group workspace within the Power BI service. This ensures that users can view the contents of that group. For more information, see [Collaborate in your Power BI app workspace](/power-bi/service-collaborate-power-bi-workspace).

That wraps up our work in Power BI for this scenario. You started by pulling data from our SharePoint lists into Power BI, and have now come full circle to embedding your Power BI report back into SharePoint.

## Next steps
The next step in this tutorial series is to [run through the workflow we created end-to-end](sharepoint-scenario-summary.md).

### See also

- [SharePoint integration scenarios](sharepoint/scenarios-intro.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]