---
title: "Use Power BI with model-driven apps | MicrosoftDocs"
ms.custom: 
ms.date: 10/14/2019
ms.reviewer: 
ms.service: powerapps
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
author: Mattp123
ms.author: matp
manager: kvivek
search.audienceType: 
  - admin
search.app: 
  - D365CE
  - Powerplatform
---
# Use Power BI

The Power BI cloud service works with Common Data Service apps to provide a self-service analytics solution. Power BI automatically refreshes the app's data displayed. With Power BI Desktop or Microsoft Excel, Power Query for authoring reports and Power BI for sharing dashboards and refreshing data from model-driven apps, your users have a powerful way to work with your app's data.  
  
<a name="PowerBIGetstarted"></a>   
## Get started using Power BI with model-driven apps  
 
The Dynamics 365 apps content packs for Power BI allow you to easily access and analyze your data in model-driven apps in Dynamics 365 (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, Dynamics 365 Project Service Automation).  
  
 To create a Power BI dashboard using a content pack, follow these instructions.  
  
1. If you haven't already done so, [register with Power BI](http://powerbi.com/).  
  
2. After you have signed in to Power BI, in the **Datasets** area select **Get Data**, under **Services** select **Get**, and then select from the following content packs.  
  
   - **Sales Analytics for Dynamics 365**  
  
   - **Customer Service Analytics for Dynamics 365**  
  
   - **Microsoft Dynamics 365 - Social Engagement**  
  
3. For the Sales Analytics and Service Analytics content packs, enter the URL of your instance, such as *<https://OrganizationName.crm.dynamics.com>*, where *OrganizationName* is the organization name of your instance, and select **Next**.  
  
   > [!NOTE]
   >  If your data center is outside of North America the crm.dynamics.com domain name may be different, such as crm2.dynamics.com, crm3.dynamics.com, crm4.dynamics.com, etc. To find the domain name, in the apps web app go to **Settings** > **Customizations** > **Developer Resources**. The URLs listed will indicate the correct domain name.  
  
    For the Marketing content pack, enter the URL as *<https://OrganizationName.marketing.dynamics.com/analytics>*, where *OrganizationName* is the organization name of your instance of Dynamics 365, and select **Next**  
  
4. Under **Authentication method**, select **oAuth2**.  
  
5. Your instance data is imported and several visualizations become available.  
  
> [!TIP]
>  If the content pack you select does not open in your web browser, in the left pane of your Power BI workspace click the content pack under **Dashboards**.  
  
### Content packs available for download.  
 The Dynamics 365 content packs support the app's default out-of-box entities. However, you can customize  the following content packs by downloading the .PBIX file and then using Power BI Desktop to customize the content pack before uploading it to the Power BI service.  
  
- [Download the Dynamics CRM Online Sales Manager .PBIX](http://download.microsoft.com/download/9/2/B/92BCBDCE-CE01-4BC9-A306-2A92653B683E/Sales%20Manager.pbix)  
  
- [Download the Dynamics 365 for Customer Engagement apps (online) Service Manager .PBIX](http://download.microsoft.com/download/9/2/B/92BCBDCE-CE01-4BC9-A306-2A92653B683E/Customer%20Service%20Manager.pbix)  
  
  The Power BI Report Template for Connected Field Service enables users to publish a Power BI report that displays the live heart beat of connected devices.  
  
- [Download the Power BI Report Template for Connected Field Service for Dynamics 365 for Customer Engagement](http://download.microsoft.com/download/E/B/5/EB5ED97A-A36A-4CAE-8C04-333A1E463B4F/PowerBI%20Report%20Template%20for%20Connected%20Field%20Service%20for%20Microsoft%20Dynamics%20365.pbix)  
  
 For information about how to customize the content packs, see [Customize Power BI content packs](customize-power-bi-content-packs.md). 
  
<a name="BPI_embed"></a>   
## Embed Power BI visualizations on personal dashboards  
 Before users can embed Power BI visualizations on personal dashboards, the organization-wide setting must be enabled.  
  
> [!NOTE]
>  By default, Power BI visualization embedding is disabled and must be enabled before users can embed them in personal dashboards.  
  
### Enable Power BI visualizations in the organization  
  
1. Sign-in to Dynamics 365 as a user with the system administrator security role.  
  
2. Go to **Settings** > **Administration** > **System Settings**.  
  
3. On the **Reporting** tab in the **Allow Power BI visualization embedding** option, select **Yes** to enable or **No** to disable.  
  
4. Select **OK**.  
  
To learn more about how to add Power BI tiles to personal dashboards, see [Embed Power BI tiles on your personal dashboard](/powerapps/user/add-powerbi-dashboards#embed--power-bi-tiles-on-your-personal-dashboard).  
  
To learn more about how to add Power BI dashboards to personal dashboards, see [Add or edit Power BI visualizations on your dashboard](/powerapps/user/add-powerbi-dashboards).  
  
<a name="CRMOnline_PBIDesktop"></a>   
## Use Power BI Desktop to connect directly to your instance  
 You can connect to your instance with Power BI Desktop to create custom reports and dashboards for use with the Power BI service.  
  
### Requirements  
  
- Power BI service registration  
  
- Power BI Desktop  
  
- Dynamics 365 instance  
  
### Connect  
  
1. Start Power BI Desktop.  
  
2. From the Home tab, select **Get Data**, and then select **More**.  
  
3. In the Get Data list, select **Dynamics 365 Online**.  
  
4. Enter the Dynamics 365 OData endpoint URL. It should look similar to this URL, where *OrganizationName* is the name of your organization, and **v9.0** is the version. Select **OK**.  
  
    https://<em>OrganizationName</em>.api.crm.dynamics.com/api/data/*v9.0*  
  
> [!IMPORTANT]
> For more information about the different endpoint versions, see [Web API URL and versions](/powerapps/developer/common-data-service/webapi/compose-http-requests-handle-errors#web-api-url-and-versions).
 
> [!TIP]
>  You can find your OData endpoint URL. Go to **Settings** > **Customizations** > **Developer Resources** and locate the URL under **Instance Web API**.  
  
5. In the Access an OData feed dialog select **Organizational account**, and then select **Connect**.  
  
   > [!NOTE]
   >  If you aren't signed in to your instance, select **Sign-in** on the Access OData feed dialog before you select Connect.  
  
6. The organization database entity tables appear in the Power BI Desktop Navigator window. You can select both default and custom entities. For more information about creating reports with Power BI Desktop, see [Power BI Support: Report View in Power BI Desktop](https://powerbi.microsoft.com/documentation/powerbi-desktop-report-view/).  
  
   ![Select entity table](media/pbi-select-entity-table.PNG "Select entity table")  
  
   > [!TIP]
   >  You can use similar steps to connect to Dynamics 365 using Excel Power Query by selecting **From Other Sources** on the **Power Query** tab in Excel.  
  

