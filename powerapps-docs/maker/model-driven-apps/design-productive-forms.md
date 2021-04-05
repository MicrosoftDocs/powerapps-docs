---
title: "Design productive main forms in model-driven apps | MicrosoftDocs"
description: Learn how to design productive main forms for your model-driven apps.
ms.custom: ""
ms.date: 04/05/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "PowerApps"
author: "mspilde"
ms.author: "mspilde"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Design productive main forms in model-driven apps

Building experiences where tasks can be completed quickly and effectively is crucial to user satisfaction. Model-driven apps provide many options to build highly performant experiences, including application-level options, site map organization options, and many form creation options.

Form layout and design is very important to building highly efficient and productive forms, but it is also important to build forms that load quickly and allow for fast navigation within the form and across tabs.  We recommend that you read how to optimize form performance for best practices on how to make forms load fast in your model-driven app. 

This article will cover how to design highly efficient and productive forms in a model-driven app, including how to work with main forms, main form dialogs, form component controls, quick create forms, and quick view forms.

## Working with main forms

A main form in a model-driven app should be used when you are working with and editing a specific record’s data for a table and you want to make sure users interacting with that record stay within the constraints of the table structure.

A form also allows you to build around that data including working and interacting with related records from other tables. One important consideration is how a model-driven form is bound to data. The out-of-box controls for a form are bound to fields from the table. These allow you to quickly build a form for creating and editing data, but without additional customizations it isn't as flexible if you want to use a form for multiple tasks that need user input or want to take additional action before saving information.

One of the strengths of model-driven forms is the ease of use with standard (out-of-box) controls like lookups, subgrids, and reference panels to quickly view or edit related records. Forms also support custom Power Apps Component Framework controls to extend functionality beyond the standard controls.  Forms primarily support data relationships for a record that are child or secondary relationships; they do not easily support tertiary or higher-order relationships. For example, if you have an account record that has a one-to-one or one-to-many relationship with contacts, you can quickly add interactions with both the parent and child data with a form using lookups that interact with other forms including a main form dialog or embedded forms like a quick view or form component control. We will cover each of the form types in more detail later.

If you need to interact or work with related data of the child record, this is not easily supported without additional work including using a main form dialog to work with related records of the main form dialog or using a custom canvas page.  Multi-entity forms can be created using main form dialogs and/or form component controls, but a main form does not directly support tertiary related records on the main form.

The layout of a Unified Interface application:

:::image type="content" source="media/unified-interface-layout.png" alt-text="Layout for a unified interface app":::

- The application header is not part of the form and is part of the overall page structure of a model-driven app.  The app header contains information about the application including the name, and app level actions that include search, help, assistance, quick create forms, settings (personal and app level for admins), etc.
- The application sitemap is also not part of the main form. It contains navigation across the application to pages that are included in your application and a quick way to access other areas of your application with the area switcher at the bottom of the sitemap.
- The form command bar is also not part of the main form.  It can be configured and set-up using [Ribbon Workbench](https://www.xrmtoolbox.com/plugins/RibbonWorkbench2016/).  You can customize navigation and interaction on the form.  Several out-of-box options include saving, creating a new record, sharing, merging, editing multiple records, etc.
- The form header is part of a form.  It includes the table and record name, the ability to switch to additional forms for the table, four read-only fields of the record are displayed and the tabs included on the form.  Forms will only show in the form select if they are enabled and added to the application. More information: [Create and design model-driven app forms](create-design-forms.md) 
- Form headers also have a mode where you can add more than four fields and provide a simple navigation to edit the fields in the header and any additional field you want a user to easily access form the form header.  Additional tabs should be used to access information that is not primary to the task at hand or to focus the user on data or information that is specific to a given task but is not primary to the job.  Information that is necessary and is primary to working with data should be on the first tab and should never be hidden.
- The form body is the area on the form that should be used to interact with data of the primary record and any related records that are essential to completing a task.  The best practice is to limit the data to the top tasks that need to be done on the first tab and move secondary tasks to additional tabs.  You should also consider [building forms based on specific business needs and roles](design-considerations-main-forms.md) when designing your application.  Also, if there is data that is rarely used you should consider building another form that can be accessed when a user needs to reference the data or information. This will ensure a highly performant form and will help the user stay focused on important tasks that need to be completed.
- The form footer displays the form status and command for saving and popout (displays the form in a new window). Only the form footer width can be customized.  

## Example scenario of productive form design

The following scenario demonstrates the best use of a model-driven main form over data using the available controls.

Imagine a scenario where a salesperson needs to maintain data for an account that also has a primary contact (lookup), additional contacts (subgrid), and a reference panel that user can click through to see lists of related records with access to read-only views (quick view) in the reference panel and the timeline control to quickly access and create activities for that record.  The user accesses all information multiple times a day so the layout and access is vital to drive highly productive forms in the model-driven app.

:::image type="content" source="media/page-layout-unified-interface.png" alt-text="Page layout for a unified interface app":::

### Account data

The first section on the form contains the fields that are used to manage the data and information for that record.  This area will be used for a user to quickly review and edit information they do throughout their workday.  It is important to make sure required fields and most used fields are at the top of this section to drive efficiencies in the job or task related to a record.  In this example, a quick view form of the primary contact is added at the top so users can quickly view and use the information to contact an individual that is important for their daily tasks.

:::image type="content" source="media/primary-contact-quickview.png" alt-text="Quick view form for contact lookup":::

### Related contacts with a subgrid

To the right of the account information section is the contact subgrid.  This gives the user a view of all the contact records they have rights to access that are related to the main record.  This allows the user to quickly access and interact with a related record that is used the most often when working with an account.

:::image type="content" source="media/quickview-subgrid.png" alt-text="Quick view subgrid for contact":::

### Quick access to multiple related records with the reference panel

Next to the contact subgrid is the reference panel.  This control can give even further access to related records that go beyond just the contacts.  This helps drive data density and efficiencies when working across all related records of the main form.  In this example the reference panel includes contacts, opportunities, leads and products.  One limitation of the reference panel is it only uses read-only views of records.  It does not support a main form of a related record like a main form dialog or a form component.  This is best used when you want to quickly view information of a related record.



### See also
[Optimize model-driven app form performance](optimize-form-performance.md)