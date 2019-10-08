---
title: "Embed a Power BI report in a model-driven system form | MicrosoftDocs"
ms.custom: ""
ms.date: 03/05/2019
ms.reviewer: ""
ms.service: crm-online
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 99c795e0-9165-4112-85b1-6b5e1a4aa5ec
caps.latest.revision: 1
author: "prsi-msft"
ms.author: "prsi"
manager: "kvivek"
ms.reviewer: "matp"
tags: 
  - "Links to topic not migrated"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Embed a Power BI report in a model-driven system form
You can use Power BI reports in PowerApps model-driven apps to bring rich reporting and analytics to your system forms and empower your users to accomplish more. This unlocks the power to aggregate data across systems, and tailor it down to the context of a single record.
 
## Prerequisites
Embedding Power BI content is an optional feature and is disabled on all environments by default. You must enable it before you can embed Power BI content. More information: [Enable Power BI visualizations in the organization](https://docs.microsoft.com/dynamics365/customer-engagement/admin/use-power-bi?#enable--visualizations-in-the-organization).

This feature requires exporting a solution, modifying it to add the xml snippet, and then importing back into the environment. Be sure to import the changes on your target environment via a managed solution only. See [Import, update, and export solutions](https://docs.microsoft.com/powerapps/maker/common-data-service/import-update-export-solutions) for guidance on installing an update to an existing managed solution.

## Embed without contextual filtering
You can use your Power BI reports and tiles by simply embedding them, and get the exact same report. This does not involve contextualizing them to the current model-driven form, and hence you get the same report or tile on all records of the entity. For example, the following report shows the geographic location of all accounts at once, and is useful to show summary information.

> [!div class="mx-imgBorder"] 
> ![](media/embed-powerbi/embed-powerbi-report-in-system-form-unfiltered.png "Embed-powerbi-report-in-system-form-unfiltered")

You can embed a section that hosts Power BI reports and tiles in your system forms by adding the following code snippet inside the `<sections>` block of the form XML. Then, import the solution in the target environment. 

```xml
<section id="{d411658c-7450-e1e3-bc80-07021a04bcc2}" locklevel="0" showlabel="true" IsUserDefined="0" name="tab_4_section_1" labelwidth="115" columns="1" layout="varwidth" showbar="false">
	<labels>
		<label languagecode="1033" description="Unfiltered Power BI embedding demo"/>
	</labels>
	<rows>
		<row>
			<cell id="{7d18b61c-c588-136c-aee7-03e5e74a09a1}" showlabel="true" rowspan="20" colspan="1" auto="false">
				<labels>
					<label languagecode="1033" description="Accounts (Parent Account)"/>
				</labels>
				<control id="unfilteredreport" classid="{8C54228C-1B25-4909-A12A-F2B968BB0D62}">
					<parameters>
						<PowerBIGroupId>00000000-0000-0000-0000-000000000000</PowerBIGroupId>
						<PowerBIReportId>544c4162-6773-4944-900c-abfd075f6081</PowerBIReportId>
						<TileUrl>https://xyz.powerbi.com/reportEmbed?reportId=544c4162-6773-4944-900c-abfd075f6081</TileUrl>
					</parameters>
				</control>
			</cell>
		</row>
		<row/>
	</rows>
</section>
```
> [!IMPORTANT]
> Be sure to use the control `classid="{8C54228C-1B25-4909-A12A-F2B968BB0D62}"` as indicated in the XML sample.

 This table describes the properties in the previous example.

|                                                 Property                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         **PowerBIGroupId**                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  The Power BI workspace Id. The user's default workspace is always 00000000-0000-0000-0000-000000000000. You can check the Id of any workspace by looking at its URL. For example, https://xyz.powerbi.com/groups/0ddbe381-256d-44bc-93de-34e47f3d9ab4/.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                               **PowerBIReportId**                                |                             The Power BI report Id. Replace this with the report that you want to embed. You can check the Id of any report by looking at its URL. For example, https://xyz.powerbi.com/groups/me/reports/544c4162-6773-4944-900c-abfd075f6081.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                       **TileUrl**                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        The Power BI report or tile URL that you want to embed. Be sure to use the correct Power BI instance name (replace msit.powerbi.com with your own) and report Id (replace reportId=544c4162-6773-4944-900c-abfd075f6081 with your own). For example, https://xyz.powerbi.com/reportEmbed?reportId=544c4162-6773-4944-900c-abfd075f6081.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Embed with contextual filtering
You can make the Power BI reports and tiles more meaningful by applying contextual filters to the current model-driven form, so that the report or tile is filtered based on attributes of the current record. For example, the following report shows the geographic location of an account, by filtering the Power BI report using the account name. This allows a single report to show contextualized information for all records of the entity.

> [!div class="mx-imgBorder"] 
> ![](media/embed-powerbi/embed-powerbi-report-in-system-form-filtered.png "Embed-powerbi-report-in-system-form-filtered")

The filtering is done by adding a `<PowerBIFilter>` element in the `<parameter>` block as shown here. You can use any attribute of the form's entity to construct the filter expression. More information: [Constructing Filters](https://github.com/Microsoft/PowerBI-JavaScript/wiki/Filters#contructingfilters) to understand how to create your own filters.
	
```xml
<control id="filteredreport" classid="{8C54228C-1B25-4909-A12A-F2B968BB0D62}">
	<parameters>
		<PowerBIGroupId>00000000-0000-0000-0000-000000000000</PowerBIGroupId>
		<PowerBIReportId>544c4162-6773-4944-900c-abfd075f6081</PowerBIReportId>
		<TileUrl>https://xyz.powerbi.com/reportEmbed?reportId=544c4162-6773-4944-900c-abfd075f6081</TileUrl>
		<PowerBIFilter>{"Filter": "[{\"$schema\":\"basic\",\"target\":{\"table\":\"My Active Accounts\",\"column\":\"Account Name\"},\"operator\":\"In\",\"values\":[$a],\"filterType\":1}]", "Alias": {"$a": "name"}}</PowerBIFilter>
	</parameters>
</control>
```

Note that this uses the same control as the unfiltered report embedding, and hence the control class id remains unchanged. 

This table describes any additional properties used in the previous example.

|                                                 Property                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         **PowerBIFilter**                          |        The filter expression that contextualizes the Power BI report by passing the form attributes as parameters. To make it more readable, the filter is constructed as shown here. 	|

```json
	{
	        "Filter": "[{
	                \"$schema\":\"basic\",
	                \"target\":{
	                        \"table\":\"My Active Accounts\",
	                        \"column\":\"Account Name\"
	                },
	                \"operator\":\"In\",
	                \"values\":[$a, $b],
	                \"filterType\":1
	        }]",
	        "Alias": {
	                "$a": "firstname",
	                "$b":"lastname"
	        }
	}
```

The target part of the previous expression identifies the table and the column to apply the filters on. The operator identifies the logic and values identify the data passed from the PowerApps model-driven app. To parameterize in a generic way, the values are constructed by aliasing. In the previous expression, the value of an account's **firstname** and **lastname** are passed, and either of them is searched in the **Account Name** column in the Power BI report. Note that **firstname** and **lastname** are the unique names of attributes of the account entity, whose value will be passed here. 

You can create more complex filter expressions by looking at examples from [Constructing Filters](https://github.com/Microsoft/PowerBI-JavaScript/wiki/Filters#contructingfilters) and providing the appropriate values for $schema and filterType. Be sure to escape every literal in the filter part using *\"*, so that the JSON is generated correctly.

## Known issues and limitations
1. This integration is available only in the Unified Interface client, on supported web browsers and mobile devices.
2. Opening this form in the PowerApps form designer will not show the control in a meaningful way. This is because the control is customized outside of the form designer.
3. Users will be authenticated into Power BI automatically with their PowerApps username and password. If a Power BI account with matching credentials doesn’t exist, a sign in prompt is displayed as illustrated here. 

   > [!div class="mx-imgBorder"] 
   > ![](media/embed-powerbi/embed-powerbi-report-in-system-form-auth-1.png "Embed-powerbi-report-in-system-form-auth-1")

4. No data will display if an incorrect account is used to log into Power BI. To sign in with the correct credentials, sign out, and then sign in again.

   > [!div class="mx-imgBorder"] 
   > ![](media/embed-powerbi/embed-powerbi-report-in-system-form-auth-2.png "Embed-powerbi-report-in-system-form-auth-2")

   > [!div class="mx-imgBorder"] 
   > ![](media/embed-powerbi/embed-powerbi-report-in-system-form-auth-3.png "Embed-powerbi-report-in-system-form-auth-3")

5. The view of the report data shown inside PowerApps is the same as that in Power BI, and PowerApps security roles and privileges don't affect the data that is displayed. Hence, the data is essentially the same as what the creator of the Power BI dataset would see. To apply data access restrictions similar to PowerApps security roles and teams, use [Row-level security (RLS) with Power BI](https://docs.microsoft.com/power-bi/service-admin-rls).
6. If the form doesn’t show the Power BI report after importing the solution and publishing customizations, open it in the model-driven form editor and save it, so that the form JSON is regenerated.


### See also

[Embed a Power BI dashboard in a PowerApps model-driven personal dashboard](https://docs.microsoft.com/dynamics365/customer-engagement/basics/add-edit-power-bi-visualizations-dashboard)

[Use Power BI with Dynamics 365 apps](https://docs.microsoft.com/dynamics365/customer-engagement/admin/use-power-bi)

[Import, update, and export solutions](../common-data-service/import-update-export-solutions.md)
