---
title: "Translate localizable text for model-driven apps | MicrosoftDocs"
description: "Learn how to get localizeable text translated to support multiple languages"
ms.custom: ""
ms.date: 03/05/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 3d77d149-819b-45e6-8e70-1fbe54d5c153
caps.latest.revision: 19
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Translate localizable text for model-driven apps

If you have customized table or column text, such as column labels or drop-down list values, you can provide the users in your environment who are not working with the base language version of your environment with this customized text in their preferred languages. 

The process has the following steps:
1. Enable other languages for your environment
2. Export the localizable text
3. Get the localizable text translated
4. Import the localized text

## Enable other languages for your environment

If you haven't already enabled the languages for your environment, use the steps described in [Enable the language](/dynamics365/customer-engagement/admin/enable-languages) to enable them.

> [!IMPORTANT]
> Each language can take several minutes to enable. During this time, other users of the environment may not be able to use your app. You should enable languages at time that will be least disruptive to users.

> [!TIP]
> While you are enabling the languages, note the LCID values used for each language. This value will represent the language in the exported data for the localizable text. Language codes are four-digit or five-digit locale IDs. Valid locale ID values can be found at [Locale ID (LCID) Chart)](/previous-versions/windows/embedded/ms912047(v=winembedded.10)).

## Export the localizable text

The scope of the localizable text that will be exported is the unmanaged solution that contains the localizable text.

<!-- [!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../includes/cc_navigate-solution-from-powerapps-portal.md)] -->

1. From the Power Apps portal select **Solutions**.

2. In the **All Solutions** list select the unmanaged solution that contains the localizable text you want.

3. In the menu bar select **Translations** > **Export Translations**. 

    > [!div class="mx-imgBorder"] 
    > ![Export Translations.](media/export-localizable-text.png "Export Translations")

    You could see an alert that says:
    > Exporting customized labels for translation can take several minutes. Do not click the export link again until the first export has finished. Are you sure that you want to export now?
    
    > Click **OK** if you want to continue.

When the export is completed, save the translations zip file. The file is named something like `CrmTranslations_{0}_{1}.zip`, where `{0}` is the unique name of the solution and `{1}` is the version number of the solution.

## Get the localizable text translated

You can send this file to a linguistic expert, translation agency, or localization firm.

If you have the knowledge to translate the text, or if you just want to see the format, you can extract the zip file that you exported you will see that it contains two XML files. 
 - `[Content_Types].xml`
 - `CrmTranslations.xml`

You can open the CrmTranslations.xml file with Microsoft Office Excel.

> [!TIP]
> Unless you normally open XML files with Excel, it may be easier to open Excel, then choose to open the file by pasting in the path to the extracted CrmTranslations.xml file.

> [!IMPORTANT]
> Make sure you do not change the file format. If you save the file in another format you will not be able to import it back.

When you view the data in Excel, look at the **Localized Labels** tab.

![Exported text for localization.](media/localized-labels-tab-exported-languages.png "Exported text for localization")

Any custom tables or columns will have empty cells for the localizable text. Add the localized values for those items.

> [!NOTE]
> If you have changed the display name or description for any standard table or table column, the localized strings will still reflect the translations for the original value. Those should be localized to reflect the new value.

The **Display Strings** tab contains text that is displayed for other UI elements such as Ribbon commands, error messages, and form labels.

### Updating localizable text in the base language

If you change the display name for any standard table or table column which is included in any special message, you can update information in the **Display Strings** tab to use the customized name.

> [!TIP]
> Although the UI exposed to edit system table messages includes many references to table names, it doesn't include all of them. Using this technique may find more. More information: [Edit system table messages](../data-platform/edit-system-entity-messages.md)

For example, if you change the display name for the Account table to *Company*, search through the base language column in the  **Display Strings** for the following matches: `account`, `accounts`, `Account`, and `Accounts` then make appropriate replacements to `company`, `companies`, `Company`, and `Companies` respectively.

> [!IMPORTANT]
> Do not do a general find/replace in the file for this. You should take care that the matching text actually refers to the names you have changed.


## Import the localized text
Importing the text requires compressing the files and importing them into the system.

### Compress the files

After changes are made to the `CrmTranslations.xml` file, you must compress the file together with the `[Content_Types].xml` file into the zip format. Just select *both files* and then click with the right mouse button to open the context menu. In the context menu, choose **Send to** > **Compressed (zipped) folder**.

### Import the files

From the same unmanaged solution that you exported the translations from, in the menu choose **Translations** > **Import Translations**. 

<!-- ![Import translations.](media/import-translations.png) -->

> [!div class="mx-imgBorder"] 
> ![Import selected file.](media/import-translated-text-dialog.png "Import localized text")

Select the file that contains the compressed translated text and select **Import**.

After the translated text is imported, you should publish all customizations to see the changes in your app(s).

## Community tools

[Easy Translator](https://www.xrmtoolbox.com/plugins/MsCrmTools.Translator/) is a tool that XrmToolBox community developed. Use Easy Translator to export and import translations with contextual information. 

> [!NOTE]
> The community tools are not supported by Microsoft.
> If you have questions about the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).


## Next steps
[Regional and language options for your organization](/dynamics365/customer-engagement/admin/enable-languages)<br />
[Edit system table messages](../data-platform/edit-system-entity-messages.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]