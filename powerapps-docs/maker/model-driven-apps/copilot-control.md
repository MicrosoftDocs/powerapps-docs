---
title: Add the Copilot option to a form
description: Add the Copilot option to a rich text editor in a form. 
author: udaykirang
ms.author: udag
ms.reviewer: shujoshi
ms.topic: how-to 
ms.date: 08/25/2023
ms.custom: bap-template 
ms.subservice: mda-maker
tags: 
search.audienceType: 
  - maker
---

# Add the Copilot option to a rich text editor (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

By default, the Copilot option is available in the toolbox in rich text editor for emails. You can add the Copilot option to rich text editors in other forms by updating the rich text editor configuration file with extra plugins and toolbar values.  

> [!IMPORTANT]
> This is a preview feature
>
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Prerequisites

You must have a valid rich text editor configuration file for your organization.

## Add the Copilot option

Add the Copilot option to the rich text editor toolbar by updating the extra plugins and toolbar values in the configuration file.

1. Open the configuration file for which you want to add the Copilot option.  
1. Add the following values to the respective sections in the configuration file.  

    | Section | Value |
    |---------|-------|
    | `extraPlugins`| `copilotrefinement` |
    | `toolbar` | `CopilotRefinement` |    

    **Example**: 

    ```javascript
        
    "defaultSupportedProps": {
    
    ...    
    
    "extraPlugins": "computedfont,contextmenuadditions,emailrestoreinlineimages,superimage,copyformatting,tableselection,tabletools,tableresize,autolink,quicktable,blockquote,collapser,stickystyles,pastefromword,copilotrefinement",
    
    ...
    
    "toolbar":[{ "items": ["CopyFormatting", "Font", "FontSize", "Bold", "Italic", "Underline", "BGColor", "TextColor", "BulletedList", "NumberedList", "Outdent", "Indent", "Blockquote", "JustifyLeft", "JustifyCenter", "JustifyRight", "Link", "Unlink", "Superscript", "Subscript", "Strike", "Image", "BidiLtr", "BidiRtl", "Undo", "Redo", "RemoveFormat", "Table", "A11yshortcuts", "UserPersonalization","CopilotRefinement"]}]

    },
    ```
    More information on how to update the configuration file is available in [Add the rich text editor control to a model-driven app](rich-text-editor-control.md)     

1. Save and upload the configuration file to your organization and then publish the changes.  

1. Add the richtext editor control to a form. For more information, see the [Advanced configuration](rich-text-editor-control.md#advanced-configuration) section. 

The Copilot option is now available in the rich text editor toolbar on the form.    

### See also

[Use Copilot in rich text editor for email (preview)](../model-driven-apps/use-copilot-email-assist.md)

