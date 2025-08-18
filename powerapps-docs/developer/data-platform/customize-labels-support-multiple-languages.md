---
title: Customize labels to support multiple languages
description: "Learn about customizing labels to support multiple languages."
ms.date: 08/08/2025
ms.reviewer: pehecke
ms.topic: article
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
---
# Customize labels to support multiple languages

When you create customizations in Microsoft Dataverse, you can support multiple languages by using labels.  

<a name="BKMK_UsingLabels"></a>   

## Using labels  

|Microsoft.Xrm.Sdk.dll|Web API|
|----------------|----------------|
|<xref:Microsoft.Xrm.Sdk.Label> class|[Label ComplexType](xref:Microsoft.Dynamics.CRM.Label)|
|<xref:Microsoft.Xrm.Sdk.LocalizedLabel> class|[LocalizedLabel ComplexType](xref:Microsoft.Dynamics.CRM.LocalizedLabel)|

Labels are localized strings displayed to users in the client applications. They are implemented by using `Label` ([Label ComplexType](xref:Microsoft.Dynamics.CRM.Label) or <xref:Microsoft.Xrm.Sdk.Label> class), which supports language packs. Strings that are displayed to users, such as display names or choices, can be stored in multiple languages. Users can select which language they want displayed in forms and views in Dataverse.  

The following table lists all of the table definitions that uses the `Label`.  

|Table definitions property|Description|  
|-----------------------|-----------------|  
|`AttributeMetadata.Description`|Description for a column.|  
|`AttributeMetadata.DisplayName`|Display name for a column.|  
|`EntityMetadata.Description`|Description for a table.|  
|`EntityMetadata.DisplayCollectionName`|Plural display name for a table.|  
|`EntityMetadata.DisplayName`|Display name for a table.|  
|`AssociatedMenuConfiguration.Label`|Label used for a table in a table relationship.|  
|`OptionMetadata.Label`|Label used for a value in a choice, state, or status column.|  

The `Label` can store one string for each installed language. This array is the `LocalizedLabels` property. There must always be a label stored for the base language. The labels for other languages can be **null**. If the user wants to display the user interface in a language and a label does not have a string for that language, the label for the base language is used.  

You can use the `UserLocalizedLabel` property to retrieve the label for the language chosen by the user.  

<a name="BKMK_MessagesToWorkWithLabels"></a>   

## Messages to use with labels

The following table lists the messages you can use to work with localized labels to support multiple languages. When you import translations you can generate a report based on the import job in the same way you can when importing a solution. For more information, see [Import an unmanaged solution](/power-platform/alm/solution-api#import-an-unmanaged-solution).  


|Message|Web API Operation|.NET SDK Class|
|-------|-----------------|------------|
|`ExportTranslation`</br>Exports all translations for a specific solution to a compressed file.|[ExportTranslation Action](xref:Microsoft.Dynamics.CRM.ExportTranslation)| <xref:Microsoft.Crm.Sdk.Messages.ExportTranslationRequest> |
|`ImportTranslation`</br>Imports all translations from a compressed file.   |  [ImportTranslation Action](xref:Microsoft.Dynamics.CRM.ImportTranslation)  | <xref:Microsoft.Crm.Sdk.Messages.ImportTranslationRequest> |
|`RetrieveFormattedImportJobResults`</br>Retrieves the results of an ImportJob as an XML document designed to be opened using Office Excel. | [RetrieveFormattedImportJobResults Function](xref:Microsoft.Dynamics.CRM.RetrieveFormattedImportJobResults) | <xref:Microsoft.Crm.Sdk.Messages.RetrieveFormattedImportJobResultsRequest> |
|`RetrieveLocLabels`</br>Retrieves the localized labels for the specified column. | [RetrieveLocLabels Function](xref:Microsoft.Dynamics.CRM.RetrieveLocLabels) | <xref:Microsoft.Crm.Sdk.Messages.RetrieveLocLabelsRequest> |
|`SetLocLabels`</br>Sets the localized labels for the specified column.  |[SetLocLabels Action](xref:Microsoft.Dynamics.CRM.SetLocLabels)|<xref:Microsoft.Crm.Sdk.Messages.SetLocLabelsRequest>|

<a name="BKMK_CustomizingLabelsInBaseLanguage."></a>


## Customize labels in the base language

The customization tools provide ways to edit display names and you can customize these properties programmatically. You can also edit messages. But not every message is exposed. Another way to locate and customize text used in the application is to export the translations, edit the values for the base language and import the translations again. Although this is not the intended purpose of this feature it is a supported way to identify and customize text used in the application. For more information, see [Edit system table messages (preview)](../../maker/data-platform/edit-system-entity-messages.md).  

## Translate customized table and column text

Because you can only perform customizations in the application by using the base language, when you want to provide localized labels for these customizations you must export the text of the labels so that they can be localized for any other languages enabled for the organization.  

### Export customized text for translation

You can export the translations in the web application or by using the `ExportTranslation` message ([ExportTranslation Action](xref:Microsoft.Dynamics.CRM.ExportTranslation) or <xref:Microsoft.Crm.Sdk.Messages.ExportTranslationRequest> class).  

Exported text is saved as a compressed file that contains a `CrmTranslations.xml` that you open by using Office Excel. You can send this file to a linguistic expert, translation agency, or localization firm.
 
### Import translated text

After you have exported the customized table or column text and had it translated, you can import the translated text strings in the Web application by using the `ImportTranslation` message ([ImportTranslation Action](xref:Microsoft.Dynamics.CRM.ImportTranslation) or <xref:Microsoft.Crm.Sdk.Messages.ImportTranslationRequest> class). The file that you import must be a compressed file that contains the `CrmTranslations.xml` and the `[Content_Types].xml` file just as they were exported.  

After you import the completed translations, customized text appears for users who work in the languages that you had the text translated into.  

> [!NOTE]
> Dataverse cannot import translated text that is over 500 characters long. If any of the items in your translation file are longer than 500 characters, the import process will fail. If the import process fails, review the line in the file that caused the failure, reduce the number of characters, and try to import again.  

Because customization is supported only in the base language, you may be working in Dataverse with the base language set as your language preference. To verify that the translated text appears, you must change your language preference for the Dataverse user interface. To perform additional customization work, you must change back to the base language.  

<a name="BKMK_ManagingLanguages"></a>

## Manage languages for your organization

Dataverse enables you to install multiple language packs on a server and allows the user to select a language pack. For more information about how to install language packs, see [Enable Languages](/power-platform/admin/enable-languages). This section contains information about messages used to manage languages installed for your organization.  

The following table lists the messages that you use to work with language packs. Use these messages with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A> method.

|Message|Web API Operation|.NET SDK Class|  
|-------------|-----------------|----------------|  
|`DeprovisionLanguage`</br>Contains the data needed to deprovision a language|[DeprovisionLanguage Action](xref:Microsoft.Dynamics.CRM.DeprovisionLanguage)|<xref:Microsoft.Crm.Sdk.Messages.DeprovisionLanguageRequest>|  
|`ProvisionLanguage`</br>Contains the data needed to provision a new language.|[ProvisionLanguage Action](xref:Microsoft.Dynamics.CRM.ProvisionLanguage)|<xref:Microsoft.Crm.Sdk.Messages.ProvisionLanguageRequest>|  
|`RetrieveAvailableLanguages`</br>Retrieves the list of available languages.|[RetrieveAvailableLanguages Function](xref:Microsoft.Dynamics.CRM.RetrieveAvailableLanguages)|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAvailableLanguagesRequest>|  
|`RetrieveDeprovisionedLanguages`</br>Retrieves the list of language packs installed on the server that have been disabled.|[RetrieveDeprovisionedLanguages Function](xref:Microsoft.Dynamics.CRM.RetrieveDeprovisionedLanguages)|<xref:Microsoft.Crm.Sdk.Messages.RetrieveDeprovisionedLanguagesRequest>|  
|`RetrieveInstalledLanguagePacks`</br>Contains the data needed to retrieve the list of language packs installed on the server.|[RetrieveInstalledLanguagePacks Function](xref:Microsoft.Dynamics.CRM.RetrieveInstalledLanguagePacks)|<xref:Microsoft.Crm.Sdk.Messages.RetrieveInstalledLanguagePacksRequest>|  
|`RetrieveInstalledLanguagePackVersion`</br>Contains the data needed to retrieve the version of an installed language pack.|[RetrieveLicenseInfo Function](xref:Microsoft.Dynamics.CRM.RetrieveInstalledLanguagePacks)|<xref:Microsoft.Crm.Sdk.Messages.RetrieveInstalledLanguagePackVersionRequest>|  
|`RetrieveProvisionedLanguages`</br>Retrieves the list of language packs installed on the server that are enabled.|[RetrieveProvisionedLanguages Function](xref:Microsoft.Dynamics.CRM.RetrieveProvisionedLanguages)|<xref:Microsoft.Crm.Sdk.Messages.RetrieveProvisionedLanguagesRequest>|  
|`RetrieveProvisionedLanguagePackVersion`</br>Retrieves the version of the language packs installed on the server.|[RetrieveProvisionedLanguagePackVersion Function](xref:Microsoft.Dynamics.CRM.RetrieveProvisionedLanguagePackVersion)|<xref:Microsoft.Crm.Sdk.Messages.RetrieveProvisionedLanguagePackVersionRequest>|  

### See also

[Customize table definitions](customize-entity-metadata.md)  
<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>  
<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>  
<xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata>  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
