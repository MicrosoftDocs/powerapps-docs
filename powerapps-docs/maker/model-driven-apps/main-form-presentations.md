---
title: "Model-driven app main form presentations in Power Apps | MicrosoftDocs"
description: "Learn how main forms appear when displayed on different devices"
ms.custom: ""
ms.date: 04/19/2022
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: da3ac59a-5413-46cb-b355-1987e42e3853
caps.latest.revision: 35
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# How model-driven app main forms appear on different devices

There are four types of form.  Main, quick view, quick create, and card.

The main form is a fundamental building block of any model-driven app and is used by all devices used to run them.

A main form can be rendered using a web browser, Dynamics 365 for phones, Dynamics 365 for tablets, or Dynamics 365 for Outlook, and its design adjusts to accommodate the device. This responsive design is an important feature of model-driven apps.

Additionally, the main form is an intrinsic part of the table and it travels with the table as part of any solution. This helps with [application lifecycle management](model-driven-app-glossary.md#application-lifecycle-management).

[Learn more about all the form types](types-forms.md)

[Notes on Microsoft Dynamics 365](model-driven-app-glossary.md#dynamics-365)
  
<a name="BKMK_MainFormPresentations"></a>

## Main form presentation options

Any main forms that exist for a table may be displayed differently depending on the factors in the following table below. When you design a main form, consider how it works in each presentation tool.  
  
|Presentation|Description|  
|------------------|-----------------|  
|**Current**| Most of the standard tables and all custom tables created use the current form, which provides a modern user experience. The current forms have a layout with an improved command bar design, and support features such as AutoSave and business process flows.|  
|**Dynamics 365 for tablets**| Dynamics 365 for tablets presents the content of the main form in a manner optimized for a tablet.|  
|**Dynamics 365 for phones**| Dynamics 365 for phones presents the content of the main form in a manner optimized for a phone.|  
|**Classic**|[Classic forms](#classic-forms) are from earlier versions of Dynamics 365 Customer Engagement apps. They use the ribbon rather than the command bar and the navigation pane on the left side of the form.<br /><br /> These forms have a two-column layout. Notice that there are a few tables that still use the classic forms. More information: [Updated verses classic tables](create-design-forms.md#updated-versus-classic-tables) |  
  
<a name="BKMK_MainFormComponentsForUpdatedEntities"></a>

This diagram represents common components found in main table forms.  
  
![Diagram shows main table form structure.](media/updated-form-diagram.png "Diagram shows main table form structure")  
  
The layout of the form works with a wide range of displays and window sizes. As the width of window decreases, section columns move down so that you can scroll down to work with them instead of being compressed or requiring you to scroll to the right.

The image below illustrate the accounts table main form as it would be viewed through a web browser.

 :::image type="content" source="media/create-and-edit-a-model-driven-form/main-form-accounts.png" alt-text="Sample model-driven app" lightbox="media/create-and-edit-a-model-driven-form/main-form-accounts.png":::  
  
 The following table summarizes available components of the main form for tables.  
  
|Component|Summary|  
|---------------|-------------|  
|**Navigation bar**| In the context of the table, the navigation bar provides access to managing records, such as search, create, and advanced find.  |  
|**Command bar**| The first several commands are displayed followed by a vertical ellipsis that provides a menu to choose additional commands.|  
|**Image**|When a table has an image column and the table **Primary Image** option is set to **Default Image**, an image can be displayed in the header when the form is configured to show the image.|  
|**Header**|Columns placed in the header remain visible when people scroll down through the body of the form.<br /><br /> Up to four columns can be placed in the header. Multiple lines of text, web resources, or iFrames aren’t allowed in the header. The header shares some properties with sections.|  
|**Process Control**|When a table has active business process flows, the process control displays below the header. More information: [Business process flows](/flow/business-process-flows-overview)|  
|**Body**|The body is the scrollable part of the form that contains the sections.|  
|**Tabs**|In the body of the form, tabs provide horizontal separation. Tabs have a label that can be displayed. Tabs contain up to three columns and the width of each column can be set to a percentage of the total width. When you create a new tab, each column is prepopulated with a section.|  
|**Sections**|A section occupies the space available in a tab column. Sections have a label that can be displayed and a line may be shown below the label.<br /><br /> Sections can have up to four columns and include options for displaying how labels for columns in the section are displayed.|  
|**Columns**| Section columns display fields and controls people use to view or edit data in a table record. A section can be formatted to occupy up to four columns within the section.|  
|**Spacer**|A spacer allows for an empty space to be added to a section column.|  
|**Sub-grids**|Subgrids allow for the display of a list within the form. |  
|**Quick View Form**|A quick view form displays data from a record referenced by a lookup column on the form. The table that is the target of the lookup must have a quick view form before one can be added to the form. More information: [Create and edit quick view forms](create-edit-quick-view-forms.md)|  
|**Web Resources**|HTML and Microsoft Silverlight web resources can be added to main forms but they won’t be displayed when using Dynamics 365 for phones and tablets.|  
|**iFrame**|An inline-frame that you configure to show a webpage from another website. **Important:**  <ul><li>When the page displayed in an iFrame is on another domain, browsers apply a higher level of security. This may complicate the requirements for the contents of an iFrame to interact with data in the form.</li><li>Displaying a table form within an iFrame embedded in another table form isn't supported. 
|**Bing Maps**|When this control is present in a form for a table and the system setting **Enable Bing Maps** is enabled with a valid Bing Maps key, this control can be used one time in a form to show the location for one of the addresses in a table. More information: [Configuring Bing maps](configure-bing-maps-legacy.md)|  
  
<a name="BKMK_CRMforTabletsPresentation"></a>   
## Dynamics 365 for phones and tablets forms
Most system tables and custom tables are available for Dynamics 365 for phones and tablets. The main form for these tables is transformed to a presentation optimized for phones or tablets.  
  
<a name="BKMK_EntitiesEnabledForCRMForTablets"></a>   
### Tables enabled for Dynamics 365 for phones and tablets  
Only tables that are enabled for Dynamics 365 for phones and tablets use this presentation of the main form. More information: [Entities displayed in Dynamics 365 for phones and tablets](/dynamics365/customer-engagement/customize/customize-phones-tablets#BKMK_CustomEntity)  
  
### Form design  
Dynamics 365 for phones and tablets takes many of the main form elements and presents them in a way optimized for phones or tablets. The following diagrams show the reflow from the web app to the tablet and phone apps.  
  
 **Web app**  
  
 ![Dynamics 365 form reflow from web app.](media/custon-reflow-web-app.png "Dynamics 365 form reflow from web app")  
  
**Tablet app**  
  
![Dynamics 365 form reflow to tablet app.](media/reflow-tablet-app.png "Dynamics 365 form reflow to tablet app")  
  
**Phone app**  
  
![Dynamics 365 form reflow to phone app.](media/custon-reflow-phone-app.png "Dynamics 365 form reflow to phone app")  
  
The form elements are transformed to a wide panorama layout in  Dynamics 365 for tablets, where users swipe the screen to change elements visible within a view port. In Dynamics 365 for phones, users swipe the screen to see a different column, or pane of elements, and the process control appears over every column.  
  
### View port element  
The following items are always visible within the view port in the context of a form:  
  
**Nav bar**  
The nav bar is a presentation of the sitemap that is optimized for touch. More information: [Change navigation options](/dynamics365/customer-engagement/customize/customize-phones-tablets#BKMK_NavigationOptions)  
  
**Home**  
The home button takes users to the dashboard that is the starting page for Dynamics 365  for phones and tablets.  
  
**Process Control**  
If the table has a business process enabled, it will appear in the top-right corner next to the search control in Dynamics 365 for tablets, and at the top of the screen in Dynamics 365 for phones.  
  
**Search**  
People can tap the search control to open the screen to search for records.  
  
**Command Bar**  
By default, some of the commands that appear in the app running in a web browser don't appear in the Dynamics 365 for phones and tablets apps. Similar to the web application, the command bar is context-sensitive, so the available commands change depending on what is currently viewed or selected. More information [Change commands](/dynamics365/customer-engagement/customize/customize-phones-tablets#BKMK_ChangeCommands)  
  
### Form elements  
The form elements displayed are taken from the main form and presented as a series of panels that users see through the view port.  
  
In Dynamics 365 for tablets, the first panel displays contact information about relationships that exist for the record. In Dynamics 365 for phones, the first panel also displays header columns from the form above the relationship tiles.  
  
![Dynamics 365 for tablets relationships panel.](media/mobile-app-form-relationships.png "Dynamics 365 for tablets relationships panel")  
  
For Contact and User forms, the top item displays a communication card for the record. The communication card provides buttons to initiate communication with the person. For other tables, a communication card is displayed if there's a Contact quick view form embedded in the main form.  
  
You can show additional tiles based on table relationships, but you can’t customize the tiles for the following tables:  
  
|Entity|Tiles|  
|------------|-----------|  
|Account|Owner|  
|Contact|Company Name, Owner|  
|Lead|Owner|  
|Opportunity|Account, Owner|  
  
You can customize the remaining tiles with the form editor. The order is fixed, but you can set which elements are visible in the relationship panel.  
  
In Dynamics 365 for tablets, the second panel begins with the name of the first tab on the form. Any columns that are included within the header are included and then the contents of the first tab. In Dynamics 365 for phones, headers appear in the first column.  
  
![CRM for Tablets Form First Panel.](media/mobile-app-form-first-panel.png "CRM for Tablets Form First Panel")  
  
If there is a process flow active for the form, the third tab displays tasks for the current stage of the process in Dynamics 365 for tablets. In Dynamics 365 for phones, the process control floats above the panes, expands over the user’s current pane when it’s selected, and is always visible and actionable.  
  
The remaining panels of the form contain the contents of the tabs in the form. Any subgrids found display as a separate panel.  
  
The Dynamics 365 for phones and tablets form always displays the labels for tabs and subgrids. The **Display Label on the Form** setting isn't applied.  
  
> [!NOTE]
>  To optimize performance on mobile devices, the number of objects is limited to 5 tabs or 75 columns and 10 subgrids.  
  
Forms for Dynamics 365 for phones and tablets don’t support the following features:  
   
- Bing maps  
  
- Yammer
  
- Activity feeds  
  
- Theming  
  
In addition, table images are visible in list views and contact cards, but not within the actual form.  
  
<a name="BKMK_MultipleForms"></a>   
### Multiple forms  
Dynamics 365 for phones and tablets supports multiple forms but doesn't provide a way for people to switch between forms if they can access more than one. People will see the first form in the form order that they have access to.  
  
For example, if you have the following main forms for the opportunity table and have assigned the following security roles for each one, you’ll see the form order shown in the following table.  
  
|Form Order|Form Name|Security roles|  
|----------------|---------------|--------------------|  
|1|**Sales Form One**|Salesperson|  
|2|**Sales Form Two**|Salesperson and Sales Manager|  
|3|**Sales Form Three**|Sales Manager|  
|4|**Sales Form Four**|Vice President of Sales|  
  
- People with the Salesperson role will always see **Sales Form One**.  
  
- People with the Sales Manager role will always see **Sales Form Two**.  
  
- People with the Vice President of Sales role will always see **Sales Form Four**.  
  
<a name="BKMK_ClassicPresentation"></a>   

## Classic forms

For information about the classic forms available with Dynamics 365 Customer Engagement (on-premises), see [Classic forms](/dynamics365/customerengagement/on-premises/customize/main-form-presentations#classic-forms).
  
## Next steps

 [Create or edit a main form overview](create-edit-main-forms.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
