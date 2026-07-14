---
title: "Open apps, forms, views, and reports with a URL"
description: "Learn more about URL addressable elements that enable you to include links to model-driven application forms, views, and reports in other applications"
author: MitiJ
ms.author: mijosh
ms.date: 04/21/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Open apps, forms, views, and reports with a URL

URL addressable elements enable you to include links to model-driven apps, forms, views, and reports in other applications.

> [!NOTE]
> URL addressable apps, forms, views, and reports can't bypass security. Only licensed users, based on their security roles, can access the data and the records they see.

## App URLs

> [!NOTE]
> Embedding a model-driven application within an IFrame in another application isn't supported. See [model-driven app embedding](../../limits-and-config.md#model-driven-app-embedding).

You can open any model-driven application by using the [AppModule.UniqueName](/powerapps/developer/data-platform/reference/entities/appmodule#BKMK_UniqueName) or [AppModule.AppModuleId](/powerapps/developer/data-platform/reference/entities/appmodule#BKMK_AppModuleId) values.

You can retrieve these values using Web API using the following query:

```http
GET [Organization URI]/api/data/v9.1/appmodules?$select=appmoduleid,uniquename
```

More information: [Query data using the Web API](../data-platform/webapi/query/overview.md)

You can use either the `appname` or `appid` query parameters with the Unique Name or AppModuleId values respectively, but you can't use both at the same time.

### Use Unique Name

To open the app by using the Unique Name, append the `appname` query parameter to the `main.aspx` page.

```  
https://myorg.crm.dynamics.com/main.aspx?appname={UniqueName}
``` 

For example, if the Unique Name is `msdyn_SolutionHealthHub`, you can open this app by using this URL:

```  
https://myorg.crm.dynamics.com/main.aspx?appname=msdyn_SolutionHealthHub
``` 

### Using AppModuleId

To open the app by using the AppModuleId, add the `appid` query parameter to the `main.aspx` page.

```
https://myorg.crm.dynamics.com/main.aspx?appid={AppModuleId}
``` 
For example:

```
https://myorg.crm.dynamics.com/main.aspx?appid=00001111-aaaa-2222-bbbb-3333cccc4444
``` 


<a name="BKMK_URLAddressableFormsAndViews"></a>

## URL addressable forms and views

The `main.aspx` page displays all forms and views. Query string parameters you pass to this page control what is displayed. For example:  

To open an account record form where the ID is `{91330924-802A-4B0D-A900-34FD9D790829}`:  

```  
https://myorg.crm.dynamics.com/main.aspx?etn=account&pagetype=entityrecord&id=%7B91330924-802A-4B0D-A900-34FD9D790829%7D  
```  

To open the **Closed Opportunities** view:

 ```  
https://myorg.crm.dynamics.com/main.aspx?etn=opportunity&pagetype=entitylist&viewid=%7b00000000-0000-0000-00AA-000010003006%7d&viewtype=1039  
 ```  

 To open the **Active Contacts** view with no navigation bar or command bar

 ```  
https://myorg.crm.dynamics.com/main.aspx?etn=contact&pagetype=entitylist&viewid={00000000-0000-0000-00AA-000010001004}&viewtype=1039&navbar=off&cmdbar=false  
 ```  

> [!NOTE]
> - Use `Xrm.Navigation.`[navigateTo](clientapi/reference/Xrm-Navigation/navigateTo.md) or `Xrm.Navigation.`[openForm](clientapi/reference/Xrm-Navigation/openForm.md) when you open forms programmatically within the application by using web resources. Don't use `window.open`.  
> - Outside the application, where pages don't have access to the `Xrm.Navigation.openForm` or `Xrm.Navigation.navigateTo` functions, use `window.open` or a link to open a specific record or form for a table. 
>  Displaying a form within an IFrame embedded in another form isn't supported.  

 Typically, you use the [getClientUrl](clientapi/reference/Xrm-Utility/getGlobalContext/getClientUrl.md) method to retrieve the organization root URL for Model-driven apps.  

<a name="BKMK_QueryStringParametersForMainForm"></a>   

### Query string parameters for the Main.aspx page  

> [!TIP]
> To get the ID value for any record, use the **Send a Link** button in the command bar. The following example shows what opens in your email application:  
>   
> `<https://mycrm/myOrg/main.aspx?etc=4&id=%7b899D4FCF-F4D3-E011-9D26-00155DBA3819%7d&pagetype=entityrecord>`.  
>   
> The `id` parameter passed to the URL is the encoded ID value for the record. In this example, the ID value is `{899D4FCF-F4D3-E011-9D26-00155DBA3819}`. The encoded version of the GUID substitutes opening and closing brackets `{` and `}` with `%7B` and `%7D`, respectively.  

 The following table lists the query string parameters used with the main.aspx page to open forms or views:  


|  Parameter   |    Description    |
|----|-----|
|`etn`|The logical name of the table. **Important:**  Don't use the **etc** (table type code) parameter that contains an integer code for the table. This integer code varies for custom tables in different organizations.  |
|`extraqs`|Optional for forms. This parameter contains encoded parameters within this parameter.<br /><br /> Use this parameter to pass values to a form. For more information, see [Set column values using parameters passed to a form](set-field-values-using-parameters-passed-form.md).<br /><br /> When a table has more than one form defined, you can use this parameter to specify which form to open by passing the encoded parameter `formid` with the value equal to the ID value of the form. For example, to open a form with the ID of '6009c1fe-ae99-4a41-a59f-a6f1cf8b9daf', include this value in the `extraqs` parameter: `formid%3D6009c1fe-ae99-4a41-a59f-a6f1cf8b9daf%0D%0A`.     |
|`pagetype`|The type of page. There are two possible values:<br /><br /> - `entityrecord`<br />  Displays a record form.<br />- `entitylist`<br /> Displays a view.  |
|`id`|Optional for forms. Use this parameter when you open a specific table record. Pass in the encoded GUID identifier for the table. The encoded version of the GUID substitutes opening and closing brackets "{" and "}" with "%7B" and "%7D", respectively. For example, `{91330924-802A-4B0D-A900-34FD9D790829}` is `%7B91330924-802A-4B0D-A900-34FD9D790829%7D`.|
|`viewid`|Required for views. This is the ID of the `savedquery` or `userquery` table record that defines the view. The easiest way to get the URL for a view is to copy it. For more information, see [Copy the URL for a View](open-forms-views-dialogs-reports-url.md#BKMK_CopyViewURL).|
|`viewtype`|Defines the view type. Possible values are as follows:<br /><br /> - **1039**<br />     Use for a system view. The `viewid` represents the ID of a `savedquery` record.<br />- **4230**<br />     Use for a personal view. The `viewid` represents the ID of a `userquery` record.  |
|`navbar`| Controls whether the navigation bar is displayed and whether application navigation is available using the areas and subareas defined in the sitemap.<br /><br /> -`on`<br />The navigation bar is displayed. This is the default behavior if the `navbar` parameter isn't used.<br />-`off`<br />The navigation bar isn't displayed. People can navigate by using other user interface elements or the back and forward buttons.<br />-`entity`<br />On a form, only the navigation options for related tables are available. After navigating to a related table, a back button is displayed in the navigation bar to allow returning to the original record.<br /><br />**Important:** This parameter is only supported in single-session model-driven apps. It has no effect in multisession or workspace apps such as Customer Service Workspace, Copilot Service Workspace, or Omnichannel for Customer Service. |
|`cmdbar`|Controls whether the command bar is displayed. **Note:**  This capability supports requirements for the Unified Service Desk application. Using this parameter to display a form within an IFrame embedded in another form isn't supported. <br /><br /> -`true`<br />The command bar is displayed. This is the default.<br />-   `false`<br />The command bar is hidden.|

<a name="BKMK_CopyViewURL"></a>   

### Copy the URL for a view

 Many views in model-driven apps let you copy the URL for a particular view or send an email with the URL for a particular view embedded in the message. This feature makes communication between users easier, and exposes a way for you to gain access to a URL for a view that users can include in another application, such as a SharePoint site.  

> [!NOTE]
>  Don't use this URL to include the view in application navigation by using the site map. For more information, see [Display a view in the application navigation using the Site Map](open-forms-views-dialogs-reports-url.md).  

 The page displayed by the URL includes the full view. This view includes the ribbon, but doesn't include the application navigation.  

##### Get the URL for a view  

1. Open the view you want to use.  
1. On the command bar, select **Actions** and then select **Email a Link**.  
1. Paste the link into Notepad and edit it to extract only the URL part of the text that you want.  

> [!NOTE]
> - You can't copy views that use the user context as a parameter, such as **My Accounts**.  
>   - The GUID that represents system views for system tables is the same for each installation. The GUID for custom tables and custom views is unique for each installation.  


### Display a view in the application navigation using the site map  

When you customize the application navigation by using the site map, don't use the view URL that you copied from the application by using the steps in [Copy the URL for a view](open-forms-views-dialogs-reports-url.md#BKMK_CopyViewURL) to set as the URL.
That URL displays a page that includes the ribbon and produces undesirable results if used in a `<SubArea>` Url parameter.  

To display a list of table records within the application for a SubArea, set the table column value. This value displays the default view for that table and provides the correct title and icon.  

However, if you want to have a SubArea element that uses a specific initial default view, use the following Url pattern.  

```xml  
Url="/main.aspx?appid=11112222-bbbb-3333-cccc-4444dddd5555&pagetype=entitylist&etn=account&viewid=%7b<GUID value of view id>%7d"
```  

 When you use this URL, you must also specify appropriate values for `<Titles>` and `<Descriptions>`, and specify an icon for the table.  

> [!NOTE]
> If you specify the view by using the `/main.aspx` page, the view selector still appears. If the user changes the view, Model-driven apps remembers the user's most recent selection and the initial default view displays after they close and re-open their browser. 

<a name="BKMK_OpenReportWithURL"></a>

## Opening a report by using a URL

 You can open a report by passing appropriate parameter values to the following URL: `[organization url]/crmreports/viewer/viewer.aspx`.  

 This URL accepts the following parameters:  

 **action**  
 Two possible values for this parameter are `run` or `filter`. When you use `run`, the report displays by using the default filters. When you use `filter`, the report displays a filter that the user can edit before choosing the **Run Report** button to view the report.  

 **helpID**  
 This parameter is optional. For reports that are included with model-driven apps, the value in this parameter allows the **Help** button to display appropriate content about this report when **Help on This Page** is chosen. The value should correspond to the report `FileName` value.  

 **id**  
 This parameter is the report `ReportId` value.  

 The following examples show URLs that you can use to open reports in model-driven apps.  

 Open the **Neglected Cases** report by using the default filter: 
 
 ```  
 [organization url]/crmreports/viewer/viewer.aspx?action=run&helpID=Neglected%20Cases.rdl&id=%7b8c9f3e6f-7839-e211-831e-00155db7d98f%7d  
 ```  

 Open the **Top Knowledge Base Articles** report and prompt the user to set filter values:  

 ```  
 [organization url]/crmreports/viewer/viewer.aspx?action=filter&helpID=Top%20Knowledge%20Base%20Articles.rdl&id=%7bd84ec390-7839-e211-831e-00155db7d98f%7d  
 ```  

 The following function shows how to properly encode values in the URL:  

```javascript  
function getReportURL(action,fileName,id) {  
 var orgUrl = GetGlobalContext().getClientUrl();  
 var reportUrl = orgUrl +   
  "/crmreports/viewer/viewer.aspx?action=" +  
  encodeURIComponent(action) +  
  "&helpID=" +  
  encodeURIComponent(fileName) +  
  "&id=%7b" +  
  encodeURIComponent(id) +  
  "%7d";  
 return reportUrl;  
}  
```  

### See also

[Set column values using parameters passed to a form](set-field-values-using-parameters-passed-form.md)   
[Xrm.Navigation.openUrl](./clientapi/reference/xrm-navigation/openurl.md)   
[Configure a form to accept custom querystring parameters](configure-form-accept-custom-querystring-parameters.md)   
[Customize the ribbon](customize-commands-ribbon.md)   
[Client scripting using JavaScript](client-scripting.md)   
[Web resources](web-resources.md)    
[Change application navigation using the SiteMap](../../maker/model-driven-apps/create-site-map-app.md)
 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]
