---
title: "Embed a Power BI report in a model-driven app main form | MicrosoftDocs"
description: Learn how to embed a Power BI report in a model-driven app form
ms.date: 01/21/2025
ms.topic: "how-to"
author: "sriharibs-msft"
ms.subservice: mda-maker
ms.author: "srihas"
ms.reviewer: "matp"
contributors: jasongre
search.audienceType: 
  - maker
---
# Embed a Power BI report in a model-driven app main form

You can use Power BI reports in Power Apps model-driven apps to bring rich reporting and analytics to your main forms and empower your users to accomplish more. This unlocks the power to aggregate data across systems, and tailor it down to the context of a single record.
 
## Prerequisites

Embedding Power BI content is an optional feature and is disabled on all environments by default. You must enable it before you can embed Power BI content. More information: [Enable Power BI visualizations in the organization](/power-platform/admin/use-power-bi#embed--visualizations-on-personal-dashboards).

This feature requires exporting a solution, modifying it to replace the XML snippet, and then importing back into the environment. Be sure to import the changes on your development environment via an unmanaged solution only. Go to [Import, update, and export solutions](../data-platform/import-update-export-solutions.md) for guidance on installing an update to an existing unmanaged solution.

## Embed without contextual filtering

You can use Power BI reports by embedding them, and get the exact same report. This doesn't involve contextualizing them to the current model-driven form, and hence you get the same report on all records of the table. For example, the following report shows the geographic location of all accounts at once, and is useful to show summary information.

> [!div class="mx-imgBorder"] 
> ![Embedded  Power BI report without contextual filtering.](media/embed-powerbi/embed-powerbi-report-in-system-form-unfiltered.png "Embedded  Power BI report without contextual filtering")

You can customize a main form XML `controls` node so that it can host an embedded Power BI report and tile by following these steps:

1. In your development environment, create a solution and add the table that contains the main form where you want the embedded Power BI report to display. Choose the **Select components** option when you add the table to the solution. Then, add just the table's main form.

2. Edit the table's main form in your solution and add a placeholder subgrid where you want to embed your Power BI report.

    - Update the label and name of your subgrid in the form designer.

    > :::image type="content" source="media/embed-powerbi/embed-powerbi-report-placeholder.png" alt-text="Power BI embed placeholder" lightbox="media/embed-powerbi/embed-powerbi-report-placeholder.png":::

3. Export the solution as unmanaged and extract all files in the solution package zip file. Then, edit the customizations.xml file and find the name of your subgrid. Replace the XML code provided inside the `<control>` block in the customizations.xml file. The `rowspan` in the parent `cell` node can be adjusted to change the size of the embedded Power BI report.

    ```xml
    <cell id="{7d18b61c-c588-136c-aee7-03e5e74a09a1}" showlabel="true" rowspan="20" colspan="1" auto="false" solutionaction="Added">
	<labels>
		<label languagecode="1033" description="Accounts (Parent Account)"/>
	</labels>
	<control id="unfilteredreport" classid="{8C54228C-1B25-4909-A12A-F2B968BB0D62}">
		<parameters>
			<PowerBIGroupId>00000000-0000-0000-0000-000000000000</PowerBIGroupId>
			<PowerBIReportId>544c4162-6773-4944-900c-abfd075f6081</PowerBIReportId>
			<TileUrl>https://app.powerbi.com/reportEmbed?reportId=544c4162-6773-4944-900c-abfd075f6081</TileUrl>
		</parameters>
	</control>
    </cell>
    ```
    > [!IMPORTANT]
    > Be sure to use the control `classid="{8C54228C-1B25-4909-A12A-F2B968BB0D62}"` as indicated in the XML sample.

    - Make the following changes to the form XML that you copied into the customizations.xml file for your Power BI report. This table describes the values you need to change to the elements in the previous XML sample.
   </br>

    | Property              | Description                        |
    |-------------------------|-----------------------------------|
    |  **PowerBIGroupId**          |     The Power BI workspace ID. If your report is in **My workspace**, then the workspace ID is 00000000-0000-0000-0000-000000000000. Otherwise, add the workspace ID. You can find the ID of the workspace in the Power BI service URL. More information: [Find the Power BI workspace and report Ids](#find-the-power-bi-workspace-and-report-ids).                 |
    |   **PowerBIReportId**       |    The Power BI report ID. Replace this with the report that you want to embed. You can find the ID of your report in the Power BI service URL. More information: [Find the Power BI workspace and report Ids](#find-the-power-bi-workspace-and-report-ids)    |
    |   **TileUrl**            |    The Power BI report URL that you want to embed. Be sure to use the correct Power BI subdomain name (you might need to replace app.powerbi.com with your own) and report ID (replace *reportId=544c4162-6773-4944-900c-abfd075f6081* with your own). For example, `https://app.powerbi.com/reportEmbed?reportId=544c4162-6773-4944-900c-abfd075f6081`. |

4. Create a zip file out of all the solution files previously extracted. Then, import the solution into the development environment.

## Embed with contextual filtering

You can make Power BI reports more meaningful by applying contextual filters to the current model-driven form, so that the report is filtered based on attributes of the current row. For example, the following report shows the geographic location of an account, by filtering the Power BI report using the account name. This allows a single report to show contextualized information for all rows of the table.

> [!div class="mx-imgBorder"] 
> ![Embedded Power BI report with contextual filtering.](media/embed-powerbi/embed-powerbi-report-in-system-form-filtered.png "Embedded Power BI report with contextual filtering")

The filtering is done by adding a `<PowerBIFilter>` element in the `<parameter>` block as shown here. You can use any attribute of the form's table to construct the filter expression. More information: [Constructing Filters](/javascript/api/overview/powerbi/control-report-filters) to understand how to create your own filters.
	
```xml
<control id="filteredreport" classid="{8C54228C-1B25-4909-A12A-F2B968BB0D62}">
	<parameters>
		<PowerBIGroupId>00000000-0000-0000-0000-000000000000</PowerBIGroupId>
		<PowerBIReportId>544c4162-6773-4944-900c-abfd075f6081</PowerBIReportId>
		<TileUrl>https://xyz.powerbi.com/reportEmbed?reportId=544c4162-6773-4944-900c-abfd075f6081</TileUrl>
		<PowerBIFilter>{"Filter": "[{\"$schema\":\"basic\",\"target\":{\"table\":\"table_name_of_power_bi_dataset\",\"column\":\"power_bi_field\"},\"operator\":\"In\",\"values\":[$a],\"filterType\":1}]", "Alias": {"$a": "field_name_in_powerapps_to_filter"}}</PowerBIFilter>
	</parameters>
</control>
```

Note that this uses the same control as the unfiltered report embedding, and hence the control class ID remains unchanged.

This table describes any additional properties used in the previous XML sample.

|  Property  |    Description  |
|------------|------|
|   **PowerBIFilter**   |  The filter expression that contextualizes the Power BI report by passing the form attributes as parameters. To make it more readable, the filter is constructed as shown here. The filter expression can't be a comma separated list of values.	|

```json
	{
	        "Filter": "[{
	                \"$schema\":\"basic\",
	                \"target\":{
	                        \"table\":\"table_name_of_power_bi_dataset\",
	                        \"column\":\"power_bi_field\"
	                },
	                \"operator\":\"In\",
	                \"values\":[$a, $b],
	                \"filterType\":1
	        }]",
	        "Alias": {
	                "$a": "field1_name_in_powerapps_to_filter",
	                "$b":"field2_name_in_powerapps_to_filter"
	        }
	}
```

The target part of the previous expression identifies the table and the column to apply the filters on. The operator identifies the logic and values identify the data passed from the Power Apps model-driven app. To parameterize in a generic way, the values are constructed by aliasing. In the previous expression, the value of an account's **firstname** and **lastname** are passed, and either of them is searched in the **Account Name** column in the Power BI report. Note that **firstname** and **lastname** are the unique names of attributes of the account table, whose value will be passed here. 

You can create more complex filter expressions by looking at examples from [Constructing Filters](/javascript/api/overview/powerbi/control-report-filters) and providing the appropriate values for $schema and filterType. Be sure to escape every literal in the filter part using *"*, so that the JSON is generated correctly.

## Find the Power BI workspace and report Ids

1. The workspace ID for this example is efc85277-2bdb-47bc-9762-363f64335108.
1. The report ID for this example is 643ab643-7126-4a57-bd82-ca8f1fb676fc.
:::image type="content" source="media/embed-powerbi/power-bi-service-url.png" alt-text="Power BI workspace Id and report Id example" lightbox="media/embed-powerbi/power-bi-service-url.png":::

## Known issues and limitations

- This integration is available only in the Unified Interface client, on supported web browsers and mobile devices.
- Opening this form in the Power Apps form designer won't show the control in a meaningful way. This is because the control is customized outside of the form designer.
- Users will be authenticated into Power BI automatically with their Power Apps username and password. If a Power BI account with matching credentials doesn’t exist, a sign-in prompt is displayed as illustrated here. 

   > [!div class="mx-imgBorder"] 
   > ![Power BI sign in prompt.](media/embed-powerbi/embed-powerbi-report-in-system-form-auth-1.png "Power BI sign in prompt")
   
    No data displays if an incorrect account is used to log into Power BI. To sign in with the correct credentials, sign out, and then sign in again.
  
   > [!div class="mx-imgBorder"] 
   > ![Sign in to Power BI service.](media/embed-powerbi/embed-powerbi-report-in-system-form-auth-2.png "Sign in to Power BI service")
   
   > [!div class="mx-imgBorder"] 
   > ![User that is signed in doesn't have appropriate permission.](media/embed-powerbi/embed-powerbi-report-in-system-form-auth-3.png "User that is signed in doesn't have appropriate permission")

- The view of the report data shown inside Power Apps is the same as Power BI, and Power Apps security roles and privileges don't affect the data that is displayed. Hence, the data is essentially the same as what the creator of the Power BI dataset would see. To apply data access restrictions similar to Power Apps security roles and teams, use [Row-level security (RLS) with Power BI](/power-bi/service-admin-rls).
- If the form doesn’t show the Power BI report after importing the solution and publishing customizations, open it in the model-driven form editor and save it, so that the form JSON is regenerated.
- Embedding a Power BI tile on a form is only supported without contextual filtering.
- Embedding a Power BI report doesn't support cross-tenant references. For example, trying to embed a Power BI report belonging to the Contoso tenant in a model-driven app belonging to the Fabrikam tenant isn't currently supported, even if the report being embedded has been shared with users in the Fabrikam tenant via Power BI.
- Pinned reports as part of Power BI dashboards aren't meant to be interactive. If you want to have interactive Power BI reports, embed them directly instead of pinning them to a dashboard.

### Common issues

- The group ID isn't specified in the `TileUrl` node of the control parameters when it might need to be. This example includes a group ID.
```xml
<parameters>
	<PowerBIGroupId>fd266a4c-9a02-4553-9310-80e05ee844f3</PowerBIGroupId>
	<PowerBIReportId>544c4162-6773-4944-900c-abfd075f6081</PowerBIReportId>
	<TileUrl>https://xyz.powerbi.com/reportEmbed?reportId=544c4162-6773-4944-900c-abfd075f6081&amp;groupId=fd266a4c-9a02-4553-9310-80e05ee844f3</TileUrl>
</parameters>
```
- Fields have different data types in Power BI and Dataverse. They need to be the same type, such as string in Power BI and string in Dataverse.
- String fields don't have escaped quotes in the Power BI filter. Notice ```values``` has ```[\"$a\"]``` rather than ```[$a]```.
```json
	{
	        "Filter": "[{
	                \"$schema\":\"basic\",
	                \"target\":{
	                        \"table\":\"table_name_of_power_bi_dataset\",
	                        \"column\":\"power_bi_field\"
	                },
	                \"operator\":\"In\",
	                \"values\":[\"$a\"],
	                \"filterType\":1
	        }]",
	        "Alias": {
	                "$a": "field_name_in_powerapps_to_filter",
	        }
	}
```

### See also

[Embed a Power BI dashboard in a Power Apps model-driven personal dashboard](../../user/add-powerbi-dashboards.md)

[Use Power BI with Dynamics 365 apps](/power-platform/admin/use-power-bi)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
