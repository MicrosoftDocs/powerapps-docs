---
title: "Translate label text for customized tables  | MicrosoftDocs"
description: "Overview of label text translation for custom tables"
ms.custom: ""
ms.date: 08/05/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 7e269d09-4453-490a-b50c-f0795ff6f348
caps.latest.revision: 34
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Translate label text

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

The standard tables include default text for labels that are available in many different languages. However, when you customize a form, such as adding or changing columns, or create custom tables, you may need the labels for those components to appear in different languages. You can import translated label text for customized tables for your apps so that the label text displays in languages other than the base language.

When you translate label text for a form, you are modifying the base language of the form as part of a form customization. When you do this, you create active unmanaged changes to the labels. Subsequently, if you don’t modify the base language translation for a component, such as a column, and then export the translation file, the column's object id won't be exported. This is because the export doesn't see any modifications done to the base language label of that column.

## High-level process

1. Export the translations from the solution that contains the tables that you want to translate label text. Then, open the translations XML file and add the translated text. More information: [Translate customized table and column text into other languages](export-customized-entity-field-text-translation.md)
2. Import the translations. More information: [Import translated table and column text back into an app](import-translated-entity-field-text.md)


## Common issues with translating form label text

<!-- THIS SHOULD GO IN ANOTHER TOPIC ### Active customizations prevent customizations from appearing

Active customizations can prevent customizations from appearing at runtime. For example, managed solution changes don't appear at runtime or some components are missing. This behavior can occur if there is an active unmanaged layer for the component. You can resolve this by removing the component's unmanaged layer. More information: [Remove the unmanaged layer](solution-layers.md#remove-the-unmanaged-layer)  -->

### Form label translations don't appear in the layers

Imported translations may not appear when you view the solution layers for a component. Make sure the translations are on the &lt;Label&gt; level when you view the solution layer. Note that “displayname” tags are at the attribute level, so they will not translate labels. The “DisplayName” tags are actually for form labels and will translate form’s labels. For more information about viewing solution layers, see [Solution layers](solution-layers.md).

### Form label translations don't appear specifically for the base language

The translation export and import feature is a tool for used so your apps can display translated label text for customized components. It isn't designed to be used in managing all labels including the base language. 

On translation export, if no changes were made to the base language label, no translations will be exported in CrmTranslations.xml.

On translation import, if translations for any label in the base language column were changed in CrmTranslations.xml, the changes won't take effect.

If the issue is base language specific, do the following: 
1. Change the translations for the base language using the form designer for each label that was changed.
2. Use translation export and import to add translations for other provisioned languages.
3. Export the active unmanaged solution as managed.
4. Import this solution into the target environment.

### Form Label translation descriptions appear when exporting as unmanaged, but are "" when exporting as managed
This can happen because the label has no translations. The following behavior occurs:
- The unmanaged solution is filled with the display name: &lt;label description="example" languagecode="1033"&gt;
- The managed solution is empty, which is seen as non-existent and falls back to the display name: &lt;label description="" languagecode="1033"&gt;

### See also
[Translate customized table and column text into other languages](export-customized-entity-field-text-translation.md) <br />
[Import translated table and column text back into an app](import-translated-entity-field-text.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]