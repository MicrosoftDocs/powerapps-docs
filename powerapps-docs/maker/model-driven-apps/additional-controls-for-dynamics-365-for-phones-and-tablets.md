---
title: "List of controls available for model-driven apps | MicrosoftDocs"
description: "A list of controls available for use with Power Apps model-driven apps for web, phones, and tablets"
ms.custom: ""
ms.date: 03/29/2021
ms.reviewer: "matp"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 7920ef78-2540-48ad-ba25-9ce9cb995ed1
caps.latest.revision: 63
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# List of controls available for model-driven apps

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can use a rich set of additional controls to create a more touch-friendly experience on model-driven apps. These include sliders, switches, multimedia player, input masks, calendar, and other controls.  

To use these controls in the form designer:  
  
1. Select the column or grid you want to add the control to.  
  
1. On the **Properties** tab in the left pane, select **Components**.  
  
1. Select **+ Component** to display the available controls, and then select the control you want.  
  
    > [!NOTE]
    >  Different controls are available depending on the column or grid type. For example, star rating controls are only available for whole number columns.  
  
1. Select the devices (web, tablet, and phone) you want the control to appear on.  
  
1. Configure the values for each property.  
  
1. Select **Done** when you’re done configuring the control.  
  
Following are descriptions for each control you can use on forms.  

## AI Builder business card reader

Use the AI Builder business card reader control to detect business cards and extract their information. You can take photos directly in the component or load images that you've taken. More information: [Use the business card reader component in model-driven apps](/ai-builder/business-card-reader-component-model-driven)

## Arc knob  
 The arc knob provides a way for users to enter data by sliding the knob, and shows up on the screen as an arc. The arc knob control provides whole number input and display only. Use this control for any numerical and money columns. You can use touch to change the value, you can also focus on the number and edit it using the keypad.  
  
> [!IMPORTANT]
> - This control will be deprecated in April 2021. More information: [Model-driven app controls deprecation](/power-platform/important-changes-coming#model-driven-app-controls-deprecation)
> - This control isn’t supported on Android 4.2 and 4.3 devices. It impacts the scrolling experience on those versions.  
  
|Property|Description|  
|--------------|-----------------|  
|Max|Set the maximum value to display on the gauge.|  
|Min|Set the minimum value to display on the gauge.|  
|Value|Get or set the value to display on the gauge.|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  

## Auto-complete

 The auto-complete control filters an item list as you type and lets you select a value from the drop-down list. For example, you can use this control to let users choose from a dropdown list of states or countries/regions. This control maps to a **Single Line of Text** type column.  
  
|Property|Description|  
|--------------|-----------------|  
|Column|Shows the column the control is mapped to.|  
|Source|Set the source for the data (Grouped Options, Choice, or View).|  
|Choice|Select the option set for this column.|  
|View|Select the table and view for this column.|  
|Column|Select the column of the view’s primary table to use as the data source.|  

## Barcode scanner

The control opens a native scanner on an Android or iOS device. The scanner automatically detects a barcode when in view. The control can be configured for single line text fields.

:::image type="content" source="media/barcode-scanner-control.png" alt-text="Barcode scanner control in a model-driven app.":::
  
> [!IMPORTANT]
>  
> Currently this control is only available using the classic form designer.

|Property|Description|  
|--------------|-----------------|  
|BarCodeScannerControl_value|Specify the single line text field to enter the data.|  

### Barcode Availability by Device

| Barcode Type | Android | iOS |
|--------------|:-------:|:---:|
|QR_CODE|✔|✔|
|DATA_MATRIX|✔|✔|
|UPC_A|✔|✔|
|UPC_E|✔|✔|
|EAN_8|✔|✔|
|EAN_13|✔|✔|
|CODE_39|✔|✔|
|CODE_93|✔|✔|
|CODE_128|✔|✔|
|CODABAR|✔|✖|
|ITF|✔|✔|
|RSS14|✔|✖|
|RSS_EXPANDED|✔|✖|

## Calendar control V2

The Calendar Control V2 control displays scheduled activities and their associated details in a calendar. You can view, create, and delete your activities in a day, week, or month view. More information: [Add the calendar control to tables](add-calendar-control.md)

:::image type="content" source="media/calendar-v2-control-example.png" alt-text="Example of the version 2 calendar control in a model-driven app.":::

## Choices

 The choice control presents a set of options for your users to choose from when entering data. More information: [Choices](../data-platform/types-of-fields.md#choices) 

## Editable grid

With editable grids, users can do rich in-line editing directly from views and sub-grids whether they're using a web app, tablet, or phone. More information: [Make model-driven app grids (lists) editable using the editable grid control](make-grids-lists-editable-custom-control.md)

## Embedded canvas app control

An embedded canvas app includes rich data integration capabilities that bring in contextual data from the host model-driven form to the embedded canvas app. Display the data you want from a variety of sources right next to data from Microsoft Dataverse. More information: [Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md)

## Flip switch

The flip switch is like an on/off switch, providing a choice between two values.  

> [!IMPORTANT]
>  This control will be deprecated in April 2021. Instead, you can start using the [Toggle](#toggle) control. More information: [Model-driven app controls deprecation](/power-platform/important-changes-coming#model-driven-app-controls-deprecation)
 
|Property|Description|  
|--------------|-----------------|  
|Field|Shows the field that the control is mapped to.|  

## Form component

The form component control lets users edit information of a related table record directly from another table’s form. For example, here's the form component on a separate tab on the main account form, which lets the user edit a contact record without leaving the account form. More information: [Edit related table records directly from another table’s main form](form-component-control.md)

## Input mask  

 With the input mask control, you set the formatting for a column like phone number or credit card to prevent entering invalid data. For example, if you want users to enter a United States phone number in the format +1-222-555-1011, use the input mask +1-000-000-0000.  

> [!NOTE]
>  This only sets formatting to a single line text column.  It does not contain virtual actions like phone calling.  If these actions are required, continue to use the default control.

|Property|Description|  
|--------------|-----------------|  
|Mask|Enter the mask to use for validating data as users enter it. You can use a combination of the following characters for the mask:<br /><br /> 0 – Digit<br /><br /> 9 – Digit or space<br /><br /> # – Digit, sign, or space<br /><br /> L – Letter<br /><br /> I – Letter or space<br /><br /> A – Alphanumeric<br /><br /> A – Alphanumeric or space<br /><br /> < – Converts characters that follow to lower case<br /><br /> > – Converts characters that follow to upper case<br /><br /> &#124; – Disables case conversion<br /><br /> \ – Escapes any character, turning it into a literal<br /><br /> All others – Literals|  
|Column|Shows the column the control is mapped to.|  

## Linear gauge

The linear gauge lets your users input numerical values by dragging a slider instead of typing in the exact quantity. The slider provides whole number input and display only. Use this control for any numerical and money columns.  
  
> [!IMPORTANT]
> This control will be deprecated in April 2021. More information: [Model-driven app controls deprecation](/power-platform/important-changes-coming#model-driven-app-controls-deprecation)

|Property|Description|  
|--------------|-----------------|  
|Max|Set the maximum value to display on the gauge.|  
|Min|Set the minimum value to display on the gauge.|  
|Value|Get or set the value to display on the gauge.|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  

## Linear slider

The linear slider control lets your users input numerical values by dragging a slider and also provides an option for typing in the quantity. The slider provides whole number input and display only. Use this control for any numerical or money column.  

> [!IMPORTANT]
>  This control will be deprecated in April 2021. More information: [Model-driven app controls deprecation](/power-platform/important-changes-coming#model-driven-app-controls-deprecation)
  
|Property|Description|  
|--------------|-----------------|  
|Max|Set the maximum value to display on the slider.|  
|Min|Set the minimum value to display on the slider.|  
|Value|The value to display on the slider.|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  
  
## Multimedia  
You can embed videos to provide a richer customer experience for sales and column people on the go. Use this control to map to a URL column that contains the audio or video link to play in the control.  
  
> [!NOTE]
>  This control is supported on Android versions 4.4 and later.  
>   
>  YouTube videos aren’t currently supported on Windows 8 and Windows 8.1 tablets and phones. On Windows 10, only HTTPS videos (including YouTube) are supported.  
  
 Supported media types include:  
  
-   Streaming MP4 files  
  
-   YouTube videos  
  
-   Azure media  
  
-   Audio streams  
  
 [Privacy notice](use-the-form-editor-legacy.md#BKMK_PrivacyNotices)  
  
|Property|Description|  
|--------------|-----------------|  
|Media|Enter the URL of the media to play in this control.|  
  
## News control

Gain valuable insights from the latest news about your customers, competitors, and contacts. The news control delivers relevant news from Bing News. More information: [Set up and use the news control](stay-current-with-news-control.md)

## Number input  
 Use the number input control to help users enter data quickly. Users only have to tap the plus and minus buttons to change a numeric value in increments you set. Use this control for any numerical or money column. Users can also type a number directly into the column. This column is only supported in edit mode.  

:::image type="content" source="media/number-input-control-example.png" alt-text="Example of the number input control in a model-driven app.":::
  
|Property|Description|  
|--------------|-----------------|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  
|Column|Shows the column the control is mapped to.|  

## Pen control

 Use the pen control to capture written input such as signatures. The pen control can be configured for multiline text columns for use with web, tablet, and phone clients.

:::image type="content" source="media/pen-control-runtime.png" alt-text="Pen control in a model-driven app.":::
  
> [!IMPORTANT]
> The minimum recommended **Maximum Length** specified for the column this control maps to is 15000.  
>  
> Currently this control is only available using the classic form designer.

|Property|Description|  
|--------------|-----------------|  
|PenMode|Specify **PenMode!Draw**, **PenMode!Erase**, or **PenMode!Select** to determine what happens when a user drags a pointing device in a pen control.|  

## Quick view

The quick view control displays data from a record that is selected in a lookup on the form. The data displayed in the control is defined using a quick view form. The data displayed is not editable, but when the primary column is included in the quick view form, it becomes a link to open the related record. More information: [Model-driven app quick view control properties](quick-view-control-properties-legacy.md)

## Radial knob

The radial knob provides a way for users to enter data by sliding the knob, and shows up on the screen as a circle. The radial knob control provides whole number input and display only. Use this control for any numerical or money columns. You can use touch to change the value, or you can use the keypad to focus on the number and edit it.  
  
> [!IMPORTANT]
>  - This control will be deprecated in April 2021. More information: [Model-driven app controls deprecation](/power-platform/important-changes-coming#model-driven-app-controls-deprecation)
>  - This control isn’t supported on Android 4.2 and 4.3 devices. It impacts the scrolling experience on those versions.  
  
|Property|Description|  
|--------------|-----------------|  
|Max|Set the maximum value to display on the gauge.|  
|Min|Set the minimum value to display on the gauge.|  
|Value|Get or set the value to display on the gauge.|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  

## Rich text editor

The rich text editor control provides the app user a WYSIWYG editing area for formatting text. The control's input and output format is HTML. The control allows copied rich text, such as from a web browser or Word, to be pasted into the control. More information: [Add the rich text editor control to a model-driven app](rich-text-editor-control.md)

## Star rating

Use the star rating to provide a visual representation of a rating. The maximum number of stars you can set is five. You can use this control for whole numbers only; it can’t accept decimal values.  

:::image type="content" source="media/star-rating-control-example.png" alt-text="Example of the star rating control in a model-driven app.":::
  
> [!NOTE]
>  Be sure to select the **Hide on web** option for this control.  
  
|Property|Description|  
|--------------|-----------------|  
|Max|Select the maximum number of stars for the control from the dropdown list.|  

## Timeline control

Provide a timeline of recent, relevant news articles and Twitter tweets for an account. More information: [Set up the timeline control](set-up-timeline-control.md) 

:::image type="content" source="media/timeline-control-example.png" alt-text="Example of the timeline control in a model-driven app.":::
  
|Property|Description|  
|--------------|-----------------|  
|CC_Timeline_Title|Property to map for the title of each timeline item.|  
|CC_Timeline_Title_Desc|Description for Title.|  
|CC_Timeline_Label1|Column to be displayed below the title of timeline item.|  
|CC_Timeline_Label1_Desc|Description for Label 1.|  
|CC_Timeline_Label2|Column to be displayed after Label 1.|  
|CC_Timeline_Label2_Desc|Description for Label 2.|  
|CC_Timeline_Label3|Column to be displayed after Label 2.|  
|CC_Timeline_Label3_Desc|Description for Label 3.|  
|CC_Timeline_Label4|Column to be displayed after Label 3.|  
|CC_Timeline_Label4_Desc|Description for Label 4.|  
|CC_Timeline_Label5|Column to be displayed after Label 4.|  
|CC_Timeline_Label5_Desc|Description for Label 5.|  
|CC_Timeline_Timestamp|Column to use for sorting timeline in reverse chronological order.|  
|CC_Timeline_Timestamp_Desc|Description for Timestamp.|  
|CC_Timeline_Group|Column to map for grouping timeline.|  
|CC_Timeline_Group_Desc|Description for Group column.|  
|CC_Timeline_GroupOrder|Order of the group the item belongs to relative to other groups (assign values 1, 2, 3, and so on for groups to be displayed). The group will be displayed in ascending value of group values assigned.|  
|CC_Timeline_GroupOrder_Desc|Description for Group Order column.|  
|CC_Timeline_URL|URL  column to map for displaying the URL of each timeline item.|  
|CC_Timeline_URL_Desc|Description for URL column.|  
|CC_Timeline_ThumbnailURL|Column to map for thumbnail of image/icon to display for each item.|  
|CC_Timeline_ThumbnailURL_Desc|Description for the `ThumbnailURL` column.|  
|CC_Timeline_Filter|Column to map for timeline filter.|  
|CC_Timeline_Filter_Desc|Description for Filter.|  
|CC_Timeline_Footer|Web resource to display as the footer of the timeline.|  
|CC_Timeline_Footer_Desc|Description for Footer column.|  

## Timer control

The timer control shows your users how much time is available to complete an action in the resolution of an active row or how much time has passed since the time to complete the action has passed. More information: [Model-driven app timer control overview](timer-control-legacy.md)

## Toggle

 The toggle control allows users to choose between binary values, such as on/off and yes/no, by toggling the button.

:::image type="content" source="media/toggle-control-example.png" alt-text="Example toggle control in a model-driven app.":::
  
## Website preview

 Use the website preview control to map a URL column and show a preview of the website.  
  
> [!IMPORTANT]
>  - This control will be deprecated in April 2021. More information: [Model-driven app controls deprecation](/power-platform/important-changes-coming#model-driven-app-controls-deprecation)
>  - By enabling this control, you consent to allow your users to share certain identifiable device information with an external system. Data imported from external systems into a Power Apps app or Dynamics 365 apps such as Dynamics 365 Sales or Dynamics 365 Customer Service are subject to our privacy statement at [Microsoft Privacy and Cookies](https://go.microsoft.com/fwlink/p/?LinkId=521839).  
>   
>  [Privacy notices](use-the-form-editor-legacy.md#BKMK_PrivacyNotices)  
  
|Property|Description|  
|--------------|-----------------|  
|Column|Shows the column the control is mapped to.|  

## Next steps
[Tutorial: Use custom controls for data visualizations](use-custom-controls-data-visualizations.md)</br>
[Work with rows in the new calendar view](../../user/calendar-view.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
