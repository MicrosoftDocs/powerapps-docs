---
title: "Open forms, views, dialogs, and reports with a URL (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn more about URL addressable elements that enable you to include links to forms, views, dialogs, and reports in other applications" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Open forms, views, dialogs, and reports with a URL

URL addressable elements enable you to include links to forms, views, dialogs, and reports in other applications. In this manner, you can easily extend other applications, reports, or websites so that users can view information and perform actions without switching applications.  

> [!NOTE]
> - URL addressable forms, views, dialogs, and reports cannot bypass the security. Only licensed users, based on their security roles, can access the data and the records they see.  
> - Use `Xrm.Navigation.`[openForm](clientapi/reference/Xrm-Navigation/openForm.md) when you open forms programmatically within the application by using web resources. Do not use `window.open`.  
> - Outside the application, where pages do not have access to the `Xrm.Navigation.`[openForm](clientapi/reference/Xrm-Navigation/openForm.md) function, use `window.open` or a link to open a specific record or form for a table.  

<a name="BKMK_URLAddressableFormsAndViews"></a>

## URL addressable forms and views

 All forms and views are displayed in the main.aspx page. Query string parameters passed to this page control what will be displayed. For example:  

To open an account record form for where the id is {91330924-802A-4B0D-A900-34FD9D790829}:  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

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
>  Opening forms in a dialog window by using [showModalDialog](/previous-versions/ms536759(v=vs.85)) or [showModelessDialog](https://msdn.microsoft.com/library/ie/ms536761.aspx) is not supported.  
>   
>  Displaying a form within an IFrame embedded in another form is not supported.  

 You will typically use the [getClientUrl](clientapi/reference/Xrm-Utility/getGlobalContext/getClientUrl.md) method to retrieve the organization root Url for Model-driven apps.  

<a name="BKMK_QueryStringParametersForMainForm"></a>   

### Query string parameters for the Main.aspx page  

> [!TIP]
> To get the id value for any record, use the **Send a Link** button the command bar. The following is an example of what will be opened in your email application:  
>   
> `<https://mycrm/myOrg/main.aspx?etc=4&id=%7b899D4FCF-F4D3-E011-9D26-00155DBA3819%7d&pagetype=entityrecord>`.  
>   
> The id parameter passed to the URL is the encoded id value for the record. In this example the id value is `{899D4FCF-F4D3-E011-9D26-00155DBA3819}`. The encoded version of the GUID substitutes opening and closing brackets “{” and “}” with “%7B” and “%7D”, respectively,  

 The following are the query string parameters used with the main.aspx page to open forms or views:  


|  Parameter   |    Description    |
|--------------|------------------------------|
|   **etn**    |  The logical name of the table. **Important:**  Do not use the **etc** (table type code) parameter that contains an integer code for the table. This integer code varies for custom tables in different organizations.  |
| **extraqs**  |  Optional for forms. This parameter contains encoded parameters within this parameter.<br /><br /> Use this parameter to pass values to a form. For more information, see [Set column values using parameters passed to a form](set-field-values-using-parameters-passed-form.md).<br /><br /> When a table has more than one form defined, you can use this parameter to specify which form to open by passing the encoded parameter `formid` with the value equal to the ID value of the form. For example, to open a form with the ID of ‘6009c1fe-ae99-4a41-a59f-a6f1cf8b9daf’, include this value in the `extraqs` parameter: `formid%3D6009c1fe-ae99-4a41-a59f-a6f1cf8b9daf%0D%0A`.     |
| **pagetype** |  The type of page. There are two possible values:<br /><br /> - **entityrecord**<br />  Displays a record form.<br />- **entitylist**<br /> Displays an  view.  |
|    **id**    |   Optional for forms. Use this when you open a specific table record. Pass in the encoded GUID identifier for the table. The encoded version of the GUID substitutes opening and closing brackets “{“ and “}” with “%7B” and “%7D”, respectively, for example `{91330924-802A-4B0D-A900-34FD9D790829}` is `%7B91330924-802A-4B0D-A900-34FD9D790829%7D`.|
|  **viewid**  |   Required for views. This is the ID of the `savedquery` or `userquery` table record that defines the view. The easiest way to get the URL for a view is to copy it. For more information, see [Copy the URL for a View](open-forms-views-dialogs-reports-url.md#BKMK_CopyViewURL).|
| **viewtype** |   Defines the view type. Possible values are as follows:<br /><br /> - **1039**<br />     Use for a system view. The `viewid` represents the Id of a `savedquery` record.<br />- **4230**<br />     Use for a personal view. The `viewid` represents the Id of a `userquery` record.  |
|   `navbar`   | Controls whether the navigation bar is displayed and whether application navigation is available using the areas and subareas defined in the sitemap.<br /><br /> -   `on`<br />     The navigation bar is displayed. This is the default behavior if the `navbar` parameter is not used.<br />-   `off`<br />     The navigation bar is not displayed. People can navigate using other user interface elements or the back and forward buttons.<br />-   `entity`<br />     On a form, only the navigation options for related tables are available. After navigating to a related table, a back button is displayed in the navigation bar to allow returning to the original record. |
|   `cmdbar`   |                                                                                                                Controls whether the command bar is displayed. **Note:**  This capability supports requirements for the Unified Service Desk application. Using this to display a form within an IFrame embedded in another form is not supported. <br /><br /> -   `true`<br />     The command bar is displayed. This is the default.<br />-   `false`<br />     The command bar is hidden.                                                                                                                |

<a name="BKMK_CopyViewURL"></a>   

### Copy the URL for a View  
 Many views in model-driven apps let a user copy the URL for a particular view or send an email with the URL for a particular view embedded in the message. This feature makes communication between users easier, and exposes a way for you to gain access to a URL for a view that users can include in another application, such as a SharePoint site.  

> [!NOTE]
>  Do not use this URL to include the view in application navigation using the site map. For more information, see [Display a view in the application navigation using the Site Map](open-forms-views-dialogs-reports-url.md).  

 The page displayed by the URL includes the full view. This includes the ribbon, but does not include the application navigation.  

##### Get the URL for a View  

1. Open the view you want to use.  

2. On the command bar, click on **Actions** and then click **Email a Link**.  

3. Paste the link into Notepad and edit it to extract only the URL part of the text that you want.  

> [!NOTE]
> - Views that use the user context as a parameter, such as **My Accounts**, cannot be copied.  
>   - The GUID that represents system views for system tables will be the same for each installation. The GUID for custom tables and custom views will be unique for each  installation.  


### Display a view in the application navigation using the Site Map  

When you customize the application navigation using the site map, do not use the view URL that you copied from the application using the steps in [Copy the URL for a view](open-forms-views-dialogs-reports-url.md#BKMK_CopyViewURL) to set as the URL.
That URL displays a page that includes the ribbon and produces undesirable results if used in a `<SubArea>` Url parameter.  

To display a list of table records within the application for a SubArea set the table column value. This displays the default view for that table and provides the correct title and icon.  

However, if you want to have a SubArea element that uses a specific initial default view, use the following Url pattern.  

```xml  
Url=“/main.aspx?appid=e2bc1066-488f-eb11-b1ac-000d3a56ead9&pagetype=entitylist&etn=account&viewid=%7b<GUID value of view id>%7d”  
```  

 When you use this URL, you must also specify appropriate values for `<Titles>` and `<Descriptions>`, and specify an icon for the table.  

> [!NOTE]
> If you specify the view using the `/main.aspx` page, the view selector will still be shown. If the user changes the view, Model-driven apps remembers the user’s most recent selection and the initial default view displays after they close and re-open their browser.  

<a name="BKMK_OpenADialogProcess"></a>   

## Opening a dialog process by using a URL

A common customization is to enable a user to open a specific dialog process in the context of a specific record. For example, you might want to add a custom button to the ribbon for a specific table using the id value for current record as an input parameter for the dialog process.  

To open a dialog you need the following:  

- The unique identifier for the dialog.  

- The logical name for the table the dialog is created for.  

-  The unique identifier for the record you want to have the dialog run against.  

> [!TIP]
>  To get the unique identifier for the dialog, navigate to **Settings**, in the default solution select **Processes**. Select a process and then in the **Actions** options on the command bar, click **Copy a Link**. This will copy a link to edit the dialog to your clipboard, for example, *[organization url]*`/sfa/workflow/edit.aspx?id=%7b6A6E93C9-1FE6-4C07-91A9-E0E2A7C70976%7d`.  

 The following sample shows the URL and query string parameters to open a dialog:  

```
[organization url]/cs/dialog/rundialog.aspx?DialogId=[dialog unique identifier]&EntityName=[table logical name]&ObjectId=[unique identifier for the record]  
```  

 For example, to open the dialog with id ={6A6E93C9-1FE6-4C07-91A9-E0E2A7C70976} with the account record id = {40C9ADFD-90A8-DF11-840E-00155DBA380F}, use the URL in the following example.  

```
[organization url]/cs/dialog/rundialog.aspx?DialogId=%7b6A6E93C9-1FE6-4C07-91A9-E0E2A7C70976%7d&EntityName=account&ObjectId=%7b40C9ADFD-90A8-DF11-840E-00155DBA380F%7d  
```  

> [!TIP]
>  For browsers other than Internet Explorer, if a dialog process is opened from a link, the **Finish** button may not work. The data will be saved, but the user will need to click the **Close** button on the window to close it. This is because other browsers do not provide a `window.close` method if the window is not opened using JavaScript from another window. When possible, use JavaScript and the `window.open` method to open dialog processes rather than simply providing links.  

 You can create a JavaScript function to open the dialog as shown in the following example:  

```javascript  
function openDialogProcess(dialogId, entityName, objectId)  
{  
 var url = Xrm.Page.context.getClientUrl() +  
  "/cs/dialog/rundialog.aspx?DialogId=" +  
  dialogId + "&EntityName=" +  
  entityName + "&ObjectId=" +  
  objectId;  
 window.open(url);  
}  
```  

<a name="BKMK_OpenReportWithURL"></a>   
## Opening a Report by using a URL  
 You can open a report by passing appropriate parameter values to the following URL: `[organization url]/crmreports/viewer/viewer.aspx`.  

 This URL accepts the following parameters:  

 **action**  
 Two possible values for this parameter are `run` or `filter`. When `run` is used, the report will be displayed using the default filters. When `filter` is used, the report will display a filter that the user can edit before choosing the **Run Report** button to view the report.  

 **helpID**  
 This parameter is optional. For reports that are included with model-driven apps the value in this parameter allows the **Help** button to display appropriate content about this report when **Help on This Page** is chosen. The value should correspond to the report `FileName` value.  

 **id**  
 This parameter is the report `ReportId` value.  

 The following examples show URLs that can be used to open reports in model-driven apps.  

 Open the **Neglected Cases** report using the default filter:  
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

 [Set column values using parameters passed to a form](set-field-values-using-parameters-passed-form.md)<br/>
 [Xrm.Navigation.openUrl](./clientapi/reference/xrm-navigation/openurl.md)<br/>
 [Configure a form to accept custom querystring parameters](configure-form-accept-custom-querystring-parameters.md)    
 [Customize the ribbon](customize-commands-ribbon.md)<br/>
 [Client scripting using JavaScript](client-scripting.md)<br/>
 [Web resources](web-resources.md)<br/> 
 [Change application navigation using the SiteMap](../../maker/model-driven-apps/create-site-map-app.md)
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]