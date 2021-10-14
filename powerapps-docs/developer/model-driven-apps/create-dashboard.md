---
title: "Create a dashboard (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Organization-owned dashboards can be created by using the Microsoft Dataverse web services (SDK) or by customizing the form in Dataverse by editing the customizations.xml file." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: article
ms.assetid: da41f997-1f61-7ea8-db83-5d670d708d67
author: Nkrb # GitHub ID
ms.subservice: mda-developer
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Create a dashboard

Organization-owned dashboards can be created by using the Microsoft Dataverse or by customizing the form in Dataverse by editing the customizations.xml file.  
  
> [!NOTE]
>  Some dashboards that are created by using the SDK or by customizing the form are not supported by the dashboard designer in the Web application. More information: [Limitations: Creating dashboards by using the SDK or through form customization](#Limitations) later in this topic.  
  
 Before creating a dashboard, consider the following:  
  
- **Type of dashboard**: If you want your dashboards to be available across the organization and do not want to manage the access levels at a more detailed level, you might want to create an organization-owned dashboard. However, if you are concerned about the access privileges and security of your dashboard, consider creating a user-owned dashboard where you have more control on who can access it.  
  
     To create organization-owned dashboards, you must have the System Administrator or System Customizer role.  
  
- **Dashboard layout**: While creating dashboards, you have to use the FormXML to define the dashboard components and layout. More information: [Dashboard components and FormXML elements](understand-dashboards-dashboard-components-formxml.md#DashboardComponentsandFormXML). For some sample FormXMLs of different types of dashboards, see [Sample dashboards](sample-dashboards.md).  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

<a name="UsingSDK"></a>   

## Create a dashboard by using the SDK  

 To create a dashboard, create an instance of `SystemForm` for an organization-owned dashboard, or `UserForm` for a user-owned dashboard. The following sample shows how to create an organization-owned dashboard.  
  
 ```csharp
 //This is the language code for U.S. English. If you are running this code
//in a different locale, you will need to modify this value.
int languageCode = 1033;

//We set up our dashboard and specify the FormXml. Refer to the
//FormXml schema in the Microsoft Dynamics CRM SDK for more information.
SystemForm dashboard = new SystemForm
{
    Name = "Sample Dashboard",
    Description = "Sample organization-owned dashboard.",
    FormXml = String.Format(@"<form>
            <tabs>
                <tab name='Test Dashboard' verticallayout='true'>
                    <labels>
                        <label description='Sample Dashboard' languagecode='{0}' />
                    </labels>
                    <columns>
                        <column width='100%'>
                            <sections>
                                <section name='Information Section'
                                    showlabel='false' showbar='false'
                                    columns='111'>
                                    <labels>
                                        <label description='Information Section'
                                            languagecode='{0}' />
                                    </labels>
                                    <rows>
                                        <row>
                                            <cell colspan='1' rowspan='10' 
                                                showlabel='false'>
                                                <labels>
                                                    <label description='Top Opportunitiess - 1'
                                                    languagecode='{0}' />
                                                </labels>
                                                <control id='TopOpportunities'
                                                    classid='{{E7A81278-8635-4d9e-8D4D-59480B391C5B}}'>
                                                    <parameters>
                                                        <ViewId>{1}</ViewId>
                                                        <IsUserView>false</IsUserView>
                                                        <RelationshipName />
                                                        <TargetEntityType>opportunity</TargetEntityType>
                                                        <AutoExpand>Fixed</AutoExpand>
                                                        <EnableQuickFind>false</EnableQuickFind>
                                                        <EnableViewPicker>false</EnableViewPicker>
                                                        <EnableJumpBar>false</EnableJumpBar>
                                                        <ChartGridMode>Chart</ChartGridMode>
                                                        <VisualizationId>{2}</VisualizationId>
                                                        <EnableChartPicker>false</EnableChartPicker>
                                                        <RecordsPerPage>10</RecordsPerPage>
                                                    </parameters>
                                                </control>
                                            </cell>
                                            <cell colspan='1' rowspan='10' 
                                                showlabel='false'>
                                                <labels>
                                                    <label description='Top Opportunities - 2'
                                                    languagecode='{0}' />
                                                </labels>
                                                <control id='TopOpportunities2'
                                                    classid='{{E7A81278-8635-4d9e-8D4D-59480B391C5B}}'>
                                                    <parameters>
                                                        <ViewId>{1}</ViewId>
                                                        <IsUserView>false</IsUserView>
                                                        <RelationshipName />
                                                        <TargetEntityType>opportunity</TargetEntityType>
                                                        <AutoExpand>Fixed</AutoExpand>
                                                        <EnableQuickFind>false</EnableQuickFind>
                                                        <EnableViewPicker>false</EnableViewPicker>
                                                        <EnableJumpBar>false</EnableJumpBar>
                                                        <ChartGridMode>Grid</ChartGridMode>
                                                        <VisualizationId>{2}</VisualizationId>
                                                        <EnableChartPicker>false</EnableChartPicker>
                                                        <RecordsPerPage>10</RecordsPerPage>
                                                    </parameters>
                                                </control>
                                            </cell>
                                        </row>
                                        <row />
                                        <row />
                                        <row />
                                        <row />
                                        <row />
                                        <row />
                                        <row />
                                        <row />
                                        <row />
                                    </rows>
                                </section>
                            </sections>
                        </column>
                    </columns>
                </tab>
            </tabs>
        </form>",
    languageCode,
    defaultOpportunityQuery.SavedQueryId.Value.ToString("B"),
    visualization.SavedQueryVisualizationId.Value.ToString("B")),
    IsDefault = false
};
_dashboardId = service.Create(dashboard);
 ``` 
  
 For a complete sample, see [Sample: Create, retrieve, update, and delete (CRUD) a dashboard](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CRUDOperationsDashboard). For a sample to create a user-owned dashboard, and assign it to another user, see [Sample: Assign a user-owned dashboard to another user](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AssignUserOwnedDashboardToAnother).  
  
<a name="UsingFormCustomization"></a>   

## Create an organization-owned dashboard by customizing the form  

 The customizations.xml file that is exported with an unmanaged solution contains definitions for forms and dashboards. You can add or modify the customizations.xml file to add or update a dashboard.  
  
#### Create a dashboard by customizing a form  
  
1. Log in to Dataverse.  
  
2. Export a solution. For information about doing so, see [Exporting, Preparing to Edit, and Importing the Ribbon](export-prepare-edit-import-ribbon.md).  
  
3. Browse to the customizations.xml file in the exported solution folder, and open it for editing.  
  
4. Browse to the end of the dashboards area in the customizations.xml file by searching for the following tag: `</Dashboards>`  
  
5. Before the `</Dashboards>` tag, add the following to define a new dashboard:  
  
   ```xml  
   <Dashboard>  
      <LocalizedNames>  
         <LocalizedName description="Dashboard_Name" languagecode="1033" />  
      </LocalizedNames>     
      <IsCustomizable>1</IsCustomizable>  
      <IsDefault>0</IsDefault>  
      <FormXml>  
         <forms type="dashboard">  
   *** Dashboard definition goes here. *** // See “Sample Dashboards” topic for the FormXML content to be used here.  
         </forms>  
      </FormXml>  
   </Dashboard>  
   ```  
  
6. Save the customizations.xml file.  
  
7. Import the .zip file as a solution in Dataverse. More information: [Exporting, Preparing to Edit, and Importing the Ribbon](export-prepare-edit-import-ribbon.md).  
  
<a name="Limitations"></a>   

## Limitations: Creating dashboards by using the SDK or through form customization  

 Certain dashboards that are created or modified using the Dataverse or through form customization are not supported by the dashboard designer in the Web application. Avoid the following while creating or modifying a dashboard using the SDK or through form customization.  
  
### General  
  
- **Problem**: You can create a dashboard that contains a tab without any section defined in the FormXML.  
  
  **Resolution**: Make sure that you create a dashboard with at least one section defined for each tab in the FormXML.  
  
- **Problem**: You can create a dashboard that does not have the same number of `<row>` elements for a section as specified in the `rowspan` property of a `<cell>` element of the section in the FormXML. Ideally, the `rowspan` property value of a `<cell>` element and the number of `<row>` elements in a section must be same.  
  
  **Resolution**: Make sure that you create a dashboard that has the same number of `<row>` elements for a section as specified in the `rowspan` property of a `<cell>` element in the section.  
  
### Grids  
 **Problem**: You can create a dashboard that contains grids with the `<AutoExpand>` parameter value set to `Auto` for the grid.  
  
 **Resolution**: Make sure that you specify the `<AutoExpand>` parameter value as `Fixed` for the grids in the FormXML while creating a dashboard.  
  
### IFRAMEs  
 **Problem**: You can create a dashboard that contains an IFRAME. This happens when you do not specify any value for the `<Url>` parameter for the IFRAME control in the FormXML.  
  
 **Resolution**: Make sure that you specify a value for the `<Url>` parameter while creating an IFRAME in the FormXML.  
  
### See also 

 [Dashboards](analyze-data-with-dashboards.md)   
 [Using FormXML for dashboards](understand-dashboards-dashboard-components-formxml.md)   
 [Actions on dashboards](actions-dashboards.md)   
 [Sample dashboards](sample-dashboards.md)   
 [Sample: Create, retrieve, update, and delete (CRUD) a dashboard](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CRUDOperationsDashboardd)   
 [Customize forms](customize-entity-forms.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]