---
title: "Create solutions that support multiple languages (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Create solutions that support multiple languages

Common Data Service for Apps supports multiple languages. If you want your solution to be installed for organizations that include different base languages or that have multiple languages provisioned, take this into account when planning your solution. The following table lists tactics to use along with solution components to include in a solution that supports multiple languages.  
  
|Tactic|Solution component type|  
|------------|-----------------------------|  
|[String (RESX) web resources](#BKMK_Localizable_Web_Resources)|Web Resources|  
|[Embedded labels](#BKMK_EmbeddedLabels)|Application Navigation (SiteMap) <br />Ribbons|  
|[Export and import translations](#BKMK_ExportAndImportTranslations)|Attributes<br />Charts<br />Dashboards<br />Entity<br />Entity Relationships<br />Forms<br />Messages<br />Option Sets<br />Views|  
|[Localization in base language strings](#BKMK_LocalizationInBaseLanguageStrings)|Contract Templates<br /> Connection Roles<br />Processes (Workflow)<br />Security Roles<br />Field Security Profiles|  
|[Localization not required](#BKMK_LocalizationNotRequired)|SDK Message Processing Steps<br />Service Endpoints|  
|[Separate component for each language](#BKMK_SeparateComponentForEachLanguage)|Article Templates<br />Email Templates<br />Mail Merge Templates<br />Reports<br />Dialogs|  
|[Use XML web resources as language resources](#BKMK_UseXMLWebResourcesAsLanguageResources)|Plug-in Assemblies|  
  
 The following sections provide additional details for each tactic.  

 <a name="BKMK_Localizable_Web_Resources"></a>

 ## String (RESX) web resources
 With string (RESX) web resources added with CDS for Apps developers have a more robust option to create web resources that support multiple languages. More information [String (RESX) web resources](/dynamics365/customer-engagement/developer/resx-web-resources).

 For earlier versions, see [Developer option](https://msdn.microsoft.com/library/hh670609(v=crm.8).aspx#BKMK_DeveloperOption)
  
<a name="BKMK_EmbeddedLabels"></a>   

## Embedded labels  
 Each of the solution components that use this tactic requires that any localized text be included in the solution component.  
  
### Ribbons  
 When a language pack is installed, the application ribbon automatically displays localized text for all of the default text in the ribbon. System labels are defined in a `ResourceId` attribute value that is for internal use only. 
 When you add your own text you should use the `<LocLabels>` element to provide localized text for the languages you support. More information: [Use Localized Labels with Ribbons](/dynamics365/customer-engagement/developer/customize-dev/use-localized-labels-ribbons)  
  
### SiteMap  
 When a language pack is installed, the default text in the application navigation bar automatically displays localized text. 
 To override the default text or to provide your own text, use the `<Titles>` element. 
 The `Titles` element should contain a `<Title>` element that contains localized text for any languages your solution supports. 
 If a `Title` element isn’t available for the user’s preferred language, the title that corresponds to the organization base language is displayed.  
  
 The `<SubArea>` element allows for passing the user’s language preference by using the `userlcid` parameter so that content that is the target 
 of the `SubArea.Url` attribute can be aware of the user’s language preference and adjust accordingly. 
 More information: [Passing Parameters to a URL Using SiteMap](/dynamics365/customer-engagement/developer/customize-dev/pass-parameters-url-using-sitemap)  
  
<a name="BKMK_ExportAndImportTranslations"></a>   

## Export and import translations  
 Localizable labels for the solution components in the following table can be exported for localization.  
  
||||  
|-|-|-|  
|Entities|Attributes|Relationships|  
|Global Option Sets|Entity Messages|Entity Forms|  
|Entity Views (SavedQuery)|Charts|Dashboards|  
  
### Translating labels and display strings  
 You can only perform customizations in the application by using the base language. Therefore, when you want to provide localized labels and display strings for these customizations, you must export the text of the labels so that they can be localized for any other languages enabled for the organization. Use the following steps:  
  
1. Ensure that the organization that you’re working on has all the MUI packs installed and languages provisioned for languages you want to provide translations for.  
  
2. Create your solution and modify the components.  
  
3. After you have finished developing your solution use the “Export Translations” functionality. This generates a Office Excel spreadsheet (CrmTranslations.xml) that contains all the labels that need translation.  
  
4. In the spreadsheet, provide the corresponding translations.  
  
5. Import translations back into the same CDS for Apps organization using the “Import Translations” functionality and publish your changes.  
  
6. The next time the solution is exported it carries all the translations that you provided.  
  
   When a solution is imported, labels for languages that aren’t available in the target system are discarded and a warning is logged.  
  
   If labels for the base language of the target system are not provided in the solution package, the labels of the base language of the source are used instead. For example, if you import a solution that contains labels for English and French with English as the base language, but the target system has Japanese and French with Japanese as the base language, English labels are used instead of Japanese labels. The base languages labels cannot be **null** or empty.  
  
#### Exporting translations  
 Before you export translations you must first install the language packs and provision all the languages you want to have localized. You can export the translations in the web application or by using the <xref:Microsoft.Crm.Sdk.Messages.ExportTranslationRequest> message. For more information, see [Export Customized Entity and Field Text for Translation](/dynamics365/customer-engagement/customize/export-customized-entity-field-text-translation).  
  
#### Translating text  
 When you open the CrmTranslations.xml file in Office Excel you will see the three worksheets listed in the following table.  
  
|Worksheet|Description|  
|---------------|-----------------|  
|Information|Displays information about the organization and solution that the labels and strings were exported from.|  
|Display Strings|Display strings that represent the text of any messages associated with a metadata component. This table includes error messages and strings used for system ribbon elements.|  
|Localized Labels|Displays all of the text for any metadata component labels.|  
  
 You can send this file to a linguistic expert, translation agency, or localization firm. They will need to provide localized strings for any of the empty cells.  
  
> [!NOTE]
>  For custom entities there are some common labels that are shared with system entities, such as **Created On** or **Created By**. Because you have already installed and provisioned the languages, if you export languages for the default solution you may be able to match some labels in your custom entities with localized text for identical labels used by other entities. This can reduce the localization costs and improve consistency.  
  
 After the text in the worksheets has been localized, add both the CrmTranslations.xml and [Content_Types].xml files to a single compressed .zip file. You can now import this file.  
  
 If you prefer to work with the exported files programmatically as an XML document, see [Office 2003 XML Reference Schemas](http://www.microsoft.com/downloads/details.aspx?FamilyID=fe118952-3547-420a-a412-00a2662442d9) for information about the schemas these files use.  
  
#### Importing translated text  
  
> [!IMPORTANT]
>  You can only import translated text back into the same organization it was exported from.  
  
 After you have exported the customized entity or attribute text and had it translated, you can import the translated text strings in the web application by using the <xref:Microsoft.Crm.Sdk.Messages.ImportTranslationRequest> message. The file that you import must be a compressed file that contains the CrmTranslations.xml and the [Content_Types].xml file at the root. For more information, see [Import Translated Entity and Field Text](/dynamics365/customer-engagement/customize/import-translated-entity-field-text).  
  
 After you import the completed translations, customized text appears for users who work in the languages that you had the text translated into.  
  
> [!NOTE]
> CDS for Apps cannot import translated text that is over 500 characters long. If any of the items in your translation file are longer than 500 characters, the import process fails. If the import process fails, review the line in the file that caused the failure, reduce the number of characters, and try to import again.  
  
 Because customization is supported only in the base language, you may be working in CDS for Apps with the base language set as your language preference. To verify that the translated text appears, you must change your language preference for the CDS for Apps user interface. To perform additional customization work, you must change back to the base language.  
  
<a name="BKMK_LocalizationInBaseLanguageStrings"></a>   

## Localization in base language strings  
 Some solution components do not support multiple languages. These components include names or text that can only be meaningful in a specific language. If you create a solution for a specific language, define these solution components for the intended organization base language.  
  
 If you need to support multiple languages, one tactic is to include localization within the base language strings. For example, if you have a Connection Role named “Friend” and you need to support English, Spanish, and German, you might use the text “Friend (Amigo / Freund)” as the name of the connection role. Due to issues of the length of the text there are limitations on how many languages can be supported using this tactic.  
  
 Some solution components in this group are only visible to administrators. Because customization of the system can only be done in the organization base language it is not necessary to provide multiple language versions. **Security Roles** and **Field Security Profile** components belong to this group.  
  
 **Contract Templates** provide a description of a type of service contract. These require text for the **Name** and **Abbreviation** fields. You should consider using names and abbreviations that are unique and appropriate for all users of the organization.  
  
 **Connection Roles** rely on a person selecting descriptive Connection Role categories and names. Because these may be relatively short, it is recommended that you include localization in base language strings.  
  
 **Processes (Workflows)** that are initiated for events can work well as long as they do not need to update records with text that is to be localized. It is possible to use a workflow assembly so that logic that might apply to localized text could use the same strategy as plug-in assemblies ([Use XML Web Resources as Language Resources](#BKMK_UseXMLWebResourcesAsLanguageResources)).  
  
 **On-Demand workflows** require a name so that people can select them. In addition to including localization within the name of the on-demand workflow, another tactic is to create multiple workflows with localized names that each call the same child process. However, all users will see the complete list of on-demand workflows, not just the ones in their preferred user interface language.  
  
<a name="BKMK_LocalizationNotRequired"></a>   
## Localization not required  
 **SDK Message Processing Step** and **Service Endpoint** solution components do not expose localizable text to users. If it is important that these components have names and descriptions that correspond to the organization’s base language, you can create and export a managed solution with names and descriptions in that language.  
  
<a name="BKMK_SeparateComponentForEachLanguage"></a>   
## Separate component for each language  
 The following solution components each may contain a considerable amount of text to be localized:  
  
- Article Templates  
  
- Email Templates  
  
- Mail Merge Templates  
  
- Reports  
  
- Dialogs  
  
  For these types of solution components, the recommended tactic is to create separate components for each language. This means that you typically create a base managed solution that contains your core solution components and then a separate managed solution that contains these solution components for each language. After customers install the base solution, they can install the managed solutions for the languages they have provisioned for the organization.  
  
  Unlike **Processes (Workflows)**, you can create **Dialogs** that will reflect the user’s current language preference settings and display the dialogs only to users of that language.  
  
#### Create a localized dialog box  
  
1. Install the appropriate language pack and provision the language.  
  
    For more information, see [Language Pack Installation Instructions](https://technet.microsoft.com/library/hh699674.aspx).  
  
2. Change your personal options to specify the **User Interface Language** for the language you want for the dialog.  
  
3. Navigate to **Settings** and, in the **Process Center** group, select **Processes**.  
  
4. Click **New** and create the dialog in the language that you specified.  
  
5. After you have created the dialog, change your personal options to specify the organization base language.  
  
6. While using the organization base language you can navigate to the **Solutions** area in **Settings** and add the localized dialog as part of a solution.  
  
   The dialog created in the other language will only be displayed to users who view CDS for Apps using that language.  
  
<a name="BKMK_UseXMLWebResourcesAsLanguageResources"></a>   

## Use XML web resources as language resources  
 Plug-in assembly solution components can send messages to an end user by throwing an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> as well as creating and updating records. Unlike Silverlight web resources, plug-ins cannot use resource files.  
  
 When a plug-in requires localized text, you can use an XML web resource to store the localized strings so the plug-in can access them when needed. The structure of the XML is your option, but you may want to follow the structure used by ASP.NET Resource (.resx) files to create separate XML web resources for each language. For example, the following is an XML web resource named **localizedString.en_US** that follows the pattern used by . resx files.  
  
```xml  
<root>  
 <data name="ErrorMessage">  
  <value>There was an error completing this action. Please try again.</value>  
 </data>  
 <data name="Welcome">  
  <value>Welcome</value>  
 </data>  
</root>  
```  
  
 The following code shows how a localized message can be passed back in a plug-in to display a message to a user. It is for the pre-validation stage of a `Delete` event for the `Account` entity:  
  
```csharp  
protected void ExecutePreValidateAccountDelete(LocalPluginContext localContext)  
  {  
   if (localContext == null)  
   {  
    throw new ArgumentNullException("localContext");  
   }  
   int OrgLanguage = RetrieveOrganizationBaseLanguageCode(localContext.OrganizationService);  
   int UserLanguage = RetrieveUserUILanguageCode(localContext.OrganizationService,  
 localContext.PluginExecutionContext.InitiatingUserId);  
   String fallBackResourceFile = "";  
   switch (OrgLanguage)  
   {  
    case 1033:  
     fallBackResourceFile = "new_localizedStrings.en_US";  
     break;  
    case 1041:  
     fallBackResourceFile = "new_localizedStrings.ja_JP";  
     break;  
    case 1031:  
     fallBackResourceFile = "new_localizedStrings.de_DE";  
     break;  
    case 1036:  
     fallBackResourceFile = "new_localizedStrings.fr_FR";  
     break;  
    case 1034:  
     fallBackResourceFile = "new_localizedStrings.es_ES";  
     break;  
    case 1049:  
     fallBackResourceFile = "new_localizedStrings.ru_RU";  
     break;  
    default:  
     fallBackResourceFile = "new_localizedStrings.en_US";  
     break;  
   }  
   String ResourceFile = "";  
   switch (UserLanguage)  
   {  
    case 1033:  
     ResourceFile = "new_localizedStrings.en_US";  
     break;  
    case 1041:  
     ResourceFile = "new_localizedStrings.ja_JP";  
     break;  
    case 1031:  
     ResourceFile = "new_localizedStrings.de_DE";  
     break;  
    case 1036:  
     ResourceFile = "new_localizedStrings.fr_FR";  
     break;  
    case 1034:  
     ResourceFile = "new_localizedStrings.es_ES";  
     break;  
    case 1049:  
     ResourceFile = "new_localizedStrings.ru_RU";  
     break;  
    default:  
     ResourceFile = fallBackResourceFile;  
     break;  
   }  
   XmlDocument messages = RetrieveXmlWebResourceByName(localContext, ResourceFile);  
   String message = RetrieveLocalizedStringFromWebResource(localContext, messages, "ErrorMessage");  
   throw new InvalidPluginExecutionException(message);  
  }  
  protected static int RetrieveOrganizationBaseLanguageCode(IOrganizationService service)  
  {  
   QueryExpression organizationEntityQuery = new QueryExpression("organization");  
   organizationEntityQuery.ColumnSet.AddColumn("languagecode");  
   EntityCollection organizationEntities = service.RetrieveMultiple(organizationEntityQuery);  
   return (int)organizationEntities[0].Attributes["languagecode"];  
  }  
  protected static int RetrieveUserUILanguageCode(IOrganizationService service, Guid userId)  
  {  
   QueryExpression userSettingsQuery = new QueryExpression("usersettings");  
   userSettingsQuery.ColumnSet.AddColumns("uilanguageid", "systemuserid");  
   userSettingsQuery.Criteria.AddCondition("systemuserid", ConditionOperator.Equal, userId);  
   EntityCollection userSettings = service.RetrieveMultiple(userSettingsQuery);  
   if (userSettings.Entities.Count > 0)  
   {  
    return (int)userSettings.Entities[0]["uilanguageid"];  
   }  
   return 0;  
  }  
  protected static XmlDocument RetrieveXmlWebResourceByName(LocalPluginContext context, string webresourceSchemaName)  
  {  
   context.TracingService.Trace("Begin:RetrieveXmlWebResourceByName, webresourceSchemaName={0}", webresourceSchemaName);  
   QueryExpression webresourceQuery = new QueryExpression("webresource");  
   webresourceQuery.ColumnSet.AddColumn("content");  
   webresourceQuery.Criteria.AddCondition("name", ConditionOperator.Equal, webresourceSchemaName);  
   EntityCollection webresources = context.OrganizationService.RetrieveMultiple(webresourceQuery);  
   context.TracingService.Trace("Webresources Returned from server. Count={0}", webresources.Entities.Count);  
   if (webresources.Entities.Count > 0)  
   {  
    byte[] bytes = Convert.FromBase64String((string)webresources.Entities[0]["content"]);  
    // The bytes would contain the ByteOrderMask. Encoding.UTF8.GetString() does not remove the BOM.  
    // Stream Reader auto detects the BOM and removes it on the text  
    XmlDocument document = new XmlDocument();  
    document.XmlResolver = null;  
    using (MemoryStream ms = new MemoryStream(bytes))  
    {  
     using (StreamReader sr = new StreamReader(ms))  
     {  
      document.Load(sr);  
     }  
    }  
    context.TracingService.Trace("End:RetrieveXmlWebResourceByName , webresourceSchemaName={0}", webresourceSchemaName);  
    return document;  
   }  
   else  
   {  
    context.TracingService.Trace("{0} Webresource missing. Reinstall the solution", webresourceSchemaName);  
    throw new InvalidPluginExecutionException(String.Format("Unable to locate the web resource {0}.", webresourceSchemaName));  
    return null;  
 // This line never reached  
   }  
  }  
  protected static string RetrieveLocalizedStringFromWebResource(LocalPluginContext context, XmlDocument resource, string resourceId)  
  {  
   XmlNode valueNode = resource.SelectSingleNode(string.Format(CultureInfo.InvariantCulture, "./root/data[@name='{0}']/value", resourceId));  
   if (valueNode != null)  
   {  
    return valueNode.InnerText;  
   }  
   else  
   {  
    context.TracingService.Trace("No Node Found for {0} ", resourceId);  
    throw new InvalidPluginExecutionException(String.Format("ResourceID {0} was not found.", resourceId));  
   }  
  }  
```  
  
### See also  
 [Package and Distribute Extensions with Dynamics 365 Solutions](/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions)   
 [Introduction to Solutions](introduction-solutions.md)   
 [Plan For Solution Development](/dynamics365/customer-engagement/developer/plan-solution-development)   
 [Dependency Tracking for Solution Components](dependency-tracking-solution-components.md)   
 [Create, Export, or Import an Unmanaged Solution](create-export-import-unmanaged-solution.md)   
 [Create, Install, and Update a Managed Solution](create-install-update-managed-solution.md)   
 [Uninstall or Delete a solution](uninstall-delete-solution.md)   
 [Solution entities](/dynamics365/customer-engagement/developer/solution-entities)   
 [Localize product property values](/dynamics365/customer-engagement/developer/localize-product-property-values)
