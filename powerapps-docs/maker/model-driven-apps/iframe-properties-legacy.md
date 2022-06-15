---
title: Add an iframe to a model-driven app main form in Power Apps | MicrosoftDocs
description: Understand the iFrame properties and how to add an iframe to a main form
Keywords: Main form; iFrame properties; Dynamics 365
author: Mattp123
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.subservice: mda-maker
ms.author: matp
manager: kvivek
ms.date: 06/14/2022
ms.topic: how-to
ms.assetid: 1b7e6a0c-18a9-47e2-aa7d-0cffb8c93b19
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Add an iframe to a model-driven app main form

You can add inline frames (iframes) to a form to integrate content from another website within the form.

:::image type="content" source="media/iframe-in-model-app.png" alt-text="Iframe displaying a web page in a model-driven app":::

1.  Expand **Data**, select **Tables**, open the table that you want, and then select **Forms** from the **Data experiences** area.

1. In the list of forms, open a form of type **Main**.

1. In the form designer, select the section of the canvas where you want to add the iframe.

1. On the **Components** left pane, expand **Display**, select **External website**, enter the **Site URL**, and then select **Done**.

   :::image type="content" source="media/add-external-website.png" alt-text="Add external website to a main form by selecting External website.":::
  
   |Tab|Property|Description|  
   |---------|--------------|-----------------|
   |**Display options**|**Label**|**Required**: A label to display for the iFrame.|
   |**Display options**|**Name**|**Required**: A unique name for the iframe. The name can contain only alphanumeric characters and underscores.|
   |**Display options**|**Hide label**|Select if you want the label hidden.|
   |**Display options**|**Hide**|You can hide the iFrame so that it can be made visible by using scripts. More information: [Visibility options](visibility-options-legacy.md)|
   |**Display options**|**URL**|**Required**: The URL for the page to display in the iFrame.|
   |**Formatting**|**Column width**|When the section containing the iframe has more than one column you can set the column to occupy up to the number of columns that the section has.|  
   |**Formatting**|**Component height**|You can control the height of the iframe by specifying a number of rows the control occupies.|  
   |**Formatting**|**Use all available vertical space**|Instead of setting the height by a number of rows, you can allow the iframe height to expand to available space.|  
   |**Formatting**|**Scrolling**|You have three options for scrolling behavior:<br /><br /> - **As Necessary**: Display scrollbars when the size of the iframe is larger than the available space.<br />- **Always**: Always display scrollbars.<br />- **Never**:  Never display scrollbars.|
   |**Formatting**|**Display border**|Display a border around the iframe.|  
   |**Dependencies**|**Table column dependencies**|An iframe may interact with columns in the form using script. If a column is removed from the form the script in the iframe may break. Add any columns referenced by scripts in the iframes to the **Table column dependencies** so that they can't be removed accidentally.|  
   |**Advanced**|**Restrict cross-frame scripting, where supported**|It is considered a security risk to allow pages from a different web site to interact with the app using scripts. Use this option to restrict cross frame scripting for pages you do not have control over.<br /><br />|  
   |**Advanced**|**Pass row object-type code and unique identifiers as parameters**|Data about the organization, user, and the record can be passed to the iframe. More information: [Pass parameters to iFrames](#pass-parameters-to-iframes) |  
  
1. **Save** and **Publish** the form.

> [!NOTE]
> * If the web page doesn't appear in the iframe, it might be because the website doesn't allow iframe rendering. When this occurs, the message *URL* **refused to connect** is displayed in the iframe at runtime.
> * Forms are not designed to be displayed within an iframe.
> * Authentication inside an iFrame, either through a redirection or popups, isn't supported on mobile.

## Pass parameters to iFrames

 Information about the row can be passed by enabling the **Pass row object-type code and unique identifiers as parameters** option. The values passed are:  
  
|Parameter|Description|  
|---------------|-----------------|  
|`orglcid`|The Organization default language LCID.|  
|`orgname`|The name of the organization.|  
|`userlcid`|The user's preferred language LCID|  
|`type`|The table type code. This value can be different for custom tables in different organizations. Use `typename` instead.|  
|`typename`|The table type name.|  
|`id`|The id value of the row. this parameter has no value until the table row is saved.|  

## Add an iframe using the classic form designer

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1.  Expand **Data**, select **Tables**, select the table that you want, and then select the **Forms** tab.

1. In the list of forms, open a form of type **Main**.

1. Select **Switch to classic** to edit the form in the classic form designer.

1. On the **Insert** tab, select **IFRAME** to view iframde properties.

      > [!div class="mx-imgBorder"] 
      > ![iframe properties.](media/iframe-properties.png)
 
|Tab|Property|Description|  
|---------|--------------|-----------------|  
|**General**|**Name**|**Required**: A unique name for the iFrame. The name can contain only alphanumeric characters and underscores.|  
||**URL**|**Required**: The URL for the page to display in the iFrame.|  
||**Pass row object-type code and unique identifiers as parameters**|Data about the organization, user, and the row can be passed to the iFrame. More information: [Pass parameters to iFrames](#pass-parameters-to-iframes) |  
||**Label**|**Required**: A label to display for the iFrame.|  
||**Display label on the Form**|Whether the label should be displayed.|  
||**Restrict cross-frame scripting, where supported**|It is considered a security risk to allow pages from a different web site to interact with the Dynamics 365 application using scripts. Use this option to restrict cross frame scripting for pages you do not have control over.<br /><br />|  
||**Visible by default**|Showing the iFrame is optional and can be controlled using scripts. More information: [Visibility options](visibility-options-legacy.md)|
||**Enable for mobile**|Select the checkbox to enable the iFrame for mobile.|  
|**Formatting**|**Select the number of columns the control occupies**|When the section containing the iFrame has more than one column you can set the column to occupy up to the number of columns that the section has.|  
||**Select the number of rows the control occupies**|You can control the height of the iFrame by specifying a number of rows the control occupies.|  
||**Automatically expand to use available space**|Instead of setting the height by a number of rows, you can allow the iFrame height to expand to available space.|  
||**Select the scrolling type for the iFrame**|You have three options:<br /><br /> - **As Necessary**: Show scrollbars when the size of the iFrame is larger than the available space.<br />- **Always**: Always show scrollbars.<br />- **Never**:  Never show scrollbars.|  
||**Display border**|Display a border around the iFrame.|  
|**Dependencies**|**Dependent columns**|An iFrame may interact with columns in the form using script. If a column is removed from the form the script in the iFrame may break. Add any columns referenced by scripts in the iFrames to the **Dependent columns** so that they cannot be removed accidentally.|

## Next steps

[Use the Main form and its components](use-main-form-and-components.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
