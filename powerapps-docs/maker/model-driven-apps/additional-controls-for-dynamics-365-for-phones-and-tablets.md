---
title: "Additional controls for Dynamics 365 for phones and tablets | MicrosoftDocs"
description: "A list of controls available for use with Dynamics 365 for phones and tablets"
ms.custom: ""
ms.date: 05/18/2020
ms.reviewer: "matp"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 7920ef78-2540-48ad-ba25-9ce9cb995ed1
caps.latest.revision: 63
ms.author: "matp"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Custom controls available 

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can use a rich set of additional controls to create a more touch-friendly experience on model-driven apps. These include sliders, switches, multimedia player, input masks, calendar, and other controls.  

To use these controls in the form editor:  
  
1.  Double-click the column or list you want to add the control to.  
  
2.  Select the **Controls** tab.  
  
3.  Select **Add control**.  
  
4.  Select the control you want and then select **Add**.  
  
    > [!NOTE]
    >  Different controls are available depending on the column or list type. For example, slider controls might only be available for numerical or money columns.  
  
5.  Select the devices you want the control to appear on. Controls aren’t available for phone header columns.  
  
6.  Configure the values for each property.  
  
7.  Select **OK** when you’re done configuring the control.  
  
 Following are descriptions for each control you can use on forms.  
  
## Timeline control  
 Provide a timeline of recent, relevant news articles and Twitter tweets for an account.  
  
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
  
## Linear slider  
 The linear slider control lets your users input numerical values by dragging a slider and also provides an option for typing in the quantity. The slider provides whole number input and display only. Use this control for any numerical or money column.  
  
|Property|Description|  
|--------------|-----------------|  
|Max|Set the maximum value to display on the slider.|  
|Min|Set the minimum value to display on the slider.|  
|Value|The value to display on the slider.|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  
  
## Choices  
 The option set control presents a set of choices for your users to choose from when entering data. Use this control for choices with two or three choices only.  
  
|Property|Description|  
|--------------|-----------------|  
|Column|Shows the column that the control is mapped to.|  
  
## Flip switch  
 The flip switch is like an on/off switch, providing a choice between two values.  
 
> [!NOTE]
>  This control will be deprecated in April 2021. Instead, you can start using the toggle control.
 
|Property|Description|  
|--------------|-----------------|  
|Field|Shows the field that the control is mapped to.|  

## Toggle
 The toggle control allows users to switch between on/off values, by toggling the button.
 
|Property|Description|  
|--------------|-----------------|  
|Column|Shows the column that the control is mapped to.|  
  
## Star rating  
 Use the star rating to provide a visual representation of a rating. The maximum number of stars you can set is five. You can use this control for whole numbers only; it can’t accept decimal values.  
  
> [!NOTE]
>  Be sure to select the **Hide on web** option for this control.  
  
|Property|Description|  
|--------------|-----------------|  
|Max|Select the maximum number of stars for the control from the dropdown list.|  
  
## Radial knob  
 The radial knob provides a way for users to enter data by sliding the knob, and shows up on the screen as a circle. The radial knob control provides whole number input and display only. Use this control for any numerical or money columns. You can use touch to change the value, or you can use the keypad to focus on the number and edit it.  
  
> [!NOTE]
>  This control isn’t supported on Android 4.2 and 4.3 devices. It impacts the scrolling experience on those versions.  
  
|Property|Description|  
|--------------|-----------------|  
|Max|Set the maximum value to display on the gauge.|  
|Min|Set the minimum value to display on the gauge.|  
|Value|Get or set the value to display on the gauge.|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  
  
## Website preview  
 Use the website preview control to map a URL column and show a preview of the website.  
  
> [!IMPORTANT]
>  By enabling this control, you consent to allow your users to share certain identifiable device information with an external system. Data imported from external systems into a Power Apps app or Dynamics 365 apps such as Dynamics 365 Sales or Dynamics 365 Customer Service are subject to our privacy statement at [Microsoft Privacy and Cookies](https://go.microsoft.com/fwlink/p/?LinkId=521839).  
>   
>  [Privacy notices](use-the-form-editor-legacy.md#BKMK_PrivacyNotices)  
  
|Property|Description|  
|--------------|-----------------|  
|Column|Shows the column the control is mapped to.|  
  
## Pen control  
 Use the pen control to capture written input such as signatures.  
  
> [!NOTE]
>  The minimum recommended **Maximum Length** specified for the column this control maps to is 15000.  
>   
>  Be sure to select the **Hide on web** option for this control.  
  
|Property|Description|  
|--------------|-----------------|  
|PenMode|Specify **PenMode!Draw**, **PenMode!Erase**, or **PenMode!Select** to determine what happens when a user drags a pointing device in a pen control.|  
  
## Auto-complete  
 The auto-complete control filters an item list as you type and lets you select a value from the drop-down list. For example, you can use this control to let users choose from a dropdown list of states or countries/regions. This control maps to a **Single Line of Text** type column.  
  
|Property|Description|  
|--------------|-----------------|  
|Column|Shows the column the control is mapped to.|  
|Source|Set the source for the data (Grouped Options, Choice, or View).|  
|Choice|Select the option set for this column.|  
|View|Select the table and view for this column.|  
|Column|Select the column of the view’s primary table to use as the data source.|  
  
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
  
## Number input  
 Use the number input control to help users enter data quickly. Users only have to tap the plus and minus buttons to change a numeric value in increments you set. Use this control for any numerical or money column. Users can also type a number directly into the column. This column is only supported in edit mode.  
  
|Property|Description|  
|--------------|-----------------|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  
|Column|Shows the column the control is mapped to.|  
  
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
  
|Property|Description|  
|--------------|-----------------|  
|Max|Set the maximum value to display on the gauge.|  
|Min|Set the minimum value to display on the gauge.|  
|Value|Get or set the value to display on the gauge.|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  
  
## Arc knob  
 The arc knob provides a way for users to enter data by sliding the knob, and shows up on the screen as an arc. The arc knob control provides whole number input and display only. Use this control for any numerical and money columns. You can use touch to change the value, you can also focus on the number and edit it using the keypad.  
  
> [!NOTE]
> This control isn’t supported on Android 4.2 and 4.3 devices. It impacts the scrolling experience on those versions.  
  
|Property|Description|  
|--------------|-----------------|  
|Max|Set the maximum value to display on the gauge.|  
|Min|Set the minimum value to display on the gauge.|  
|Value|Get or set the value to display on the gauge.|  
|Step|Set the amount to add or subtract from the current value when entering data with this control.|  

## Next steps
[Tutorial: Use custom controls for data visualizations](use-custom-controls-data-visualizations.md)</br>
[Work with rows in the new calendar view](../../user/calendar-view.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]