---
title: "Pass parameters to a URL by using the ribbon (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about passing parameters to a URL by using the ribbon" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.subservice: mda-developer
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Pass parameters to a URL by using the ribbon

Ribbon actions are defined in the `<Actions>` element of a `<CommandDefinition>` element. There are several ways to pass contextual model-driven apps information as query string parameters to a URL by using the ribbon.  
  
-   Use a `<Url>` element. Within the `Url` element, use the **PassParams** parameter.  
  
-   Use a `<Url>` element together with a `<CrmParameter>` element. When used from a `Url` element, the name parameter value must be set.  
  
-   Use a `<JavaScriptFunction>` element together with a `<CrmParameter>` element.  
  
## Use the PassParams parameter to set dynamic values  

 Passing parameters to the target URL by using the **PassParams** parameter provides information to the target application about the context of the record or the user. All the parameters are passed if the ribbon control is configured by using the **PassParams**. The following table lists the parameters that are passed.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

|Parameter|Name|Description|  
|---------------|----------|-----------------|  
|`typename`|Table Name|Name of the table. For custom tables, this includes the customization prefix, for example, new_tablename.|  
|`type`|Entity Type Code|Integer that uniquely identifies the table in the current organization. **Note:**  `Entity Type Code` values are determined by the order in which a table is created in an organization. `Entity Type Codes` for custom tables are usually different in different organizations.|  
|`id`|Object GUID|Globally unique identifier (GUID) that represents a record.|  
|`orgname`|Organization Name|Unique name of the organization.|  
|`userlcid`|User Language Code|Language code identifier that is used by the current user.|  
|`orglcid`|Organization Language Code|Language code identifier that represents the base language for the organization.|  
  
[!INCLUDE[languagecode](../../includes/languagecode.md)]
  
> [!NOTE]
>  We recommend that you use the table name instead of the entity type code because the entity type code may be different between model-driven apps installations.  
  
### Example  
 The following sample shows the URL without parameters:  
  
```  
https://myserver/mypage.aspx  
```  
  
 The following sample shows the parameters included when the ribbon control is presented for the account table, for an organization called ‘AdventureWorksCycle’, when the user’s language and the organization base language is English, and the GUID for the account record is DBD5DBFB-0666-DC11-A5D9-0003FF9CE217:  
  
```  
https://myserver/mypage.aspx?orgname=AdventureWorksCycle&userlcid=1033&orglcid=1033&type=1&typename=account&id=%7BDBD5DBFB-0666-DC11-A5D9-0003FF9CE217%7D  
```  
  
## Use a Querystring parameter in the URL  
 You can include a `querystring` parameter in the URL. This can be very useful if you want to open a specific record or view by using [Open forms, views, dialogs, and reports with a URL](open-forms-views-dialogs-reports-url.md).  
  
> [!NOTE]
>  You will not be able to import the ribbon if the URL includes the ampersand (&) character that is used to separate multiple `querystring` parameters in the URL. This character makes the XML invalid. You must escape the ampersand character in the URL value with "&amp;".  
  
## Reading passed parameters  
 Passed parameters are usually read in the target .aspx page by using the `HttpRequest.QueryString` property. More information: [HttpRequest.QueryString Property](/dotnet/api/system.web.httprequest.querystring)  
  
> [!NOTE]
>  If the target of your URL is a Web resource, it can accept only the parameters identified in the topic [Passing Parameters to HTMLWeb Resources](webpage-html-web-resources.md#BKMK_PassingParametersToWebResources). The only opportunity to pass custom values is by including them within the `data` parameter. Some special handling is required to include multiple values in a single parameter. More information: [Sample: Passing Multiple Values to a Web Page Web Resource Through the Data Parameter](sample-pass-multiple-values-web-resource-through-data-parameter.md)  
  
### See also

 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Open forms and views with a URL](open-forms-views-dialogs-reports-url.md)    
 [Define ribbon tab display rules](define-ribbon-tab-display-rules.md)   
 [Sample: Export ribbon definitions](sample-export-ribbon-definitions.md)




[!INCLUDE[footer-include](../../includes/footer-banner.md)]