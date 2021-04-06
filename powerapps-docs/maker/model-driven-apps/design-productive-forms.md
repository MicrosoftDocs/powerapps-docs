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

This article shows you how to design highly efficient and productive forms in a model-driven app, including how to work with main forms, main form dialogs, form component controls, quick create forms, and quick view forms.

Form layout and design are important to building highly efficient and productive forms. However, it is also important to build forms that load quickly and allow for fast navigation within the form and across tabs.  We recommend that you understand how to optimize form performance for best practices on how to make forms load fast in your model-driven app. More information: [Optimize model-driven app form performance](optimize-form-performance.md)

## Working with main forms

A main form in a model-driven app should be used when you are working with and editing a specific record’s data for a table and you want to make sure users interacting with that record stay within the constraints of the table structure.

A form also allows you to build around that data including working and interacting with related records from other tables. One important consideration is how a model-driven form is bound to data. The out-of-box controls for a form are bound to fields from the table. These controls allow you to quickly build a form for creating and editing data, but without more customizations it isn't as flexible if you want to use a form for multiple tasks that need user input or want to take additional action before saving information.

One of the strengths of model-driven forms is the ease of use with standard (out-of-box) controls like lookups, subgrids, and reference panels to quickly view or edit related records. Forms also support custom Power Apps Component Framework controls to extend functionality beyond the standard controls.  Forms primarily support data relationships for a record that are child or secondary relationships; they do not easily support tertiary or higher-order relationships. For example, if you have an account record that has a one-to-one or one-to-many relationship with contacts, you can quickly add interactions with both the parent and child data with a form using lookups that interact with other forms including a main form dialog or embedded forms like a quick view or form component control. We will cover each of the form types in more detail later.

If you need to interact or work with related data of the child record, this is not easily supported without additional work including using a main form dialog to work with related records of the main form dialog or using a custom canvas page.  Multi-entity forms can be created using main form dialogs and/or form component controls, but a main form does not directly support tertiary-related records on the main form.

The layout of a Unified Interface application:

:::image type="content" source="media/unified-interface-layout.png" alt-text="Layout for a Unified Interface app":::

- The application header is not part of the form and is part of the overall page structure of a model-driven app.  The app header contains information about the application including the name, and app level actions that include search, help, assistance, quick create forms, settings (personal and app level for admins), etc.
- The application sitemap is also not part of the main form. It contains navigation across the application to pages that are included in your application and a quick way to access other areas of your application with the area switcher at the bottom of the sitemap.
- The form command bar is also not part of the main form.  It can be configured and set-up using the [Ribbon Workbench](https://www.xrmtoolbox.com/plugins/RibbonWorkbench2016/) community plugin for [XrmToolBox](https://www.xrmtoolbox.com/).  You can customize navigation and interaction on the form.  Several out-of-box options include saving, creating a new record, sharing, merging, editing multiple records, etc.
   > [!NOTE]
   > Resources created by the community are not supported by Microsoft. If you have questions or issues with community resources, contact the publisher of the resource.
- The form header is part of a form.  It includes the table and record name, the ability to switch to additional forms for the table, four read-only fields of the record are displayed and the tabs included on the form.  Forms will only show in the form select if they are enabled and added to the application. More information: [Create and design model-driven app forms](create-design-forms.md) 
- Form headers also have a mode where you can add more than four fields and provide a simple navigation to edit the fields in the header and any additional field you want a user to easily access form the form header.  Additional tabs should be used to access information that is not primary to the task at hand or to focus the user on data or information that is specific to a given task but is not primary to the job.  Information that is necessary and is primary to working with data should be on the first tab and should never be hidden.
- The form body is the area on the form that should be used to interact with data of the primary record and any related records that are essential to completing a task.  The best practice is to limit the data to the top tasks that need to be done on the first tab and move secondary tasks to additional tabs.  You should also consider [building forms based on specific business needs and roles](design-considerations-main-forms.md) when designing your application.  Also, if there is data that is rarely used you should consider building another form that can be accessed when a user needs to reference the data or information. This will ensure a highly performant form and will help the user stay focused on important tasks that need to be completed.
- The form footer displays the form status and command for saving and popout (displays the form in a new window). Only the form footer width can be customized.  

## Example scenario of productive form design

The following scenario demonstrates the best use of a model-driven main form over data using the available controls.

Imagine a scenario where a salesperson needs to maintain data for an account that also has a primary contact (lookup), additional contacts (subgrid), and a reference panel that user can select to see lists of related records with access to read-only views (quick view) in the reference panel and the timeline control to quickly access and create activities for that record.  The user accesses all information multiple times a day so the layout and access is vital to drive highly productive forms in the model-driven app.

:::image type="content" source="media/page-layout-unified-interface.png" alt-text="Page layout for a Unified Interface app":::

### Account data

The first section on the form contains the fields that are used to manage the data and information for that record.  This area will be used for a user to quickly review and edit information they do throughout their workday.  It is important to make sure required fields and most used fields are at the top of this section to drive efficiencies in the job or task related to a record.  In this example, a quick view form of the primary contact is added at the top so users can quickly view and use the information to contact an individual that is important for their daily tasks.

:::image type="content" source="media/primary-contact-quickview.png" alt-text="Quick view form for contact lookup":::

### Related contacts with a subgrid

To the right of the account information section is the contact subgrid.  This gives the user a view of all the contact records they have rights to access that are related to the main record.  This allows the user to quickly access and interact with a related record that is used the most often when working with an account.

:::image type="content" source="media/quickview-subgrid.png" alt-text="Quick view subgrid for contact":::

### Quick access to multiple related records with the reference panel

Next to the contact subgrid is the reference panel.  This control can give even further access to related records that go beyond just the contacts.  This helps drive data density and efficiencies when working across all related records of the main form.  In this example the reference panel includes contacts, opportunities, leads, and products.  One limitation of the reference panel is it only uses read-only views of records.  It does not support a main form of a related record like a main form dialog or a form component.  This is best used when you want to quickly view information of a related record.

:::image type="content" source="media/reference-panel.png" alt-text="Reference panel on main form":::

Currently, you add a reference panel control using the classic form designer.  Select the chevron under the sections option and select reference panel.

:::image type="content" source="media/add-reference-panel.png" alt-text="Add a reference panel to a form":::

Below the contact subgrid is the activities timeline wall. The timeline control allows a user to quickly view recent information about activities that have an activity record associated to the account including emails, phone calls, notes, etc.  Users can also send new emails, log new phone calls, add new notes quickly and easily from the control. More information: [Set up the timeline control](set-up-timeline-control.md)

:::image type="content" source="media/timeline-control.png" alt-text="Timeline control in a contact subgrid":::

## Working with data on a main form best practices

- If you need additional requirements added to data on the form that is not configured on the table, it is important to make sure the data that is required is always visible and editable. For example, a required field for your user based on a business rule. If you require a field and make it read-only, it will block users from completing tasks and can create dissatisfaction and frustration for your users. Although, hidden and read-only components are supported by the Power Apps platform, it is important to know that if a user saves data on form with a required field that is not editable, the save will process.  This ensures a user is never blocked from completing a task based on a bad design pattern.

- Hidden fields can be used like read-only fields and are handy when building data dense forms, however, the same applies when working with required fields, you should never hide a required field if it can be null when editing a record.  You can use business rules or events to hide or show fields on a form, however, the form will behave the same as a read-only field when saving.  Model-driven forms will always allow for the save if a field is required but hidden on the form.  

- If data needs to always be available, regardless of the tab a user is on, it is vital to add that data to the header.  It is important to know that the high-density headers in the Unified Interface will only display up to four read-only fields.  However, you can use the high-density headers with a flyout to add additional fields that also allow users to edit fields.  This streamlines the experience to quickly access and edit information that you always want available without multiple clicks or additional navigation.

## Building multi-entity forms

The previous section provided good examples of how to work with data that is directly related to a record. However, what can drive even further efficiencies is working with related data directly from the main form, without navigating away.  This keeps the user in context and reduces friction and improves satisfaction by streamlining experiences using a main form dialog or a form component control.

The following sections walk through several scenarios that show how to build highly performant multi-entity forms. The goal is to streamline user experiences that reduce clicks and unnecessary navigation, and speeds up daily tasks that often require a user to interact with related records on a main form.  This includes using a main form dialog, a main form component control, a quick create form, and a quick view form.

### Using a main form dialog 

Using a main form dialog is powerful when you need to have users access, and more importantly, interact with all of the information of a related record.  This would include when users need to work with a [business process flow](/power-automate/business-process-flows-overview), access to all the tabs, or all of the related records on the form.  This is important when there are business processes that drive requirements on a related record that need to be followed to ensure data integrity. Users need access to timeline activities or need access to related records of the child record without additional navigation.  Note that a main form dialog can be configured directly from the lookup control and can be used on the command bars or with JavaScript using the `navigateTo` client API.  The dialog can be positioned on the left, middle, or right side of the page as a model dialog overlay. More information: [Open main form in a dialog using client API](../../developer/model-driven-apps/customize-entity-forms.md#open-main-form-in-a-dialog-using-client-api)

In this example a user needs to access the primary contact record, update the phone number, add a note in the activities timeline and create a new appointment from the contact form.  To streamline this experience that reduces clicks and unnecessary navigation, the lookup control is configured to open the contact main form as a dialog. This example shows how the main form dialog can use quick create forms from the related record, incorporate duplicate records, and allow the user to fully interact with data on the related record.

:::image type="content" source="media/main-form-dialog.gif" alt-text="Main form dialog for quick create":::

### Using the form component control

Often you only need to edit information on a related record that doesn’t require the user to interact with the entire form and doesn't need additional business process like a business process flow, but you do not want the ability to navigate to the related form. To accomplish this scenario and streamline managing data inline on the main form, you can use a form component control. The form component control provides the user with access to the related record including all the sections, controls, and fields on the related record form. Form components can also be used for specific actions with forms designed for only that task. An example of this is the Microsoft Dynamics Field Service Mobile experience. Form components are used to manage work orders and tasks related to those work orders in a streamlined and more efficient process.

Note that a form component control will use any form that you have created for that record and it will honor any events including loading a form, saving data, on change information.  It will also honor any business rules and actions on the form including opening a main form dialog from a lookup (if you have configured the form to work in that manner).  It will also include any duplicate detection rules and parent child relationships when working with data in the related record form component.  The form control component promotes unsaved changes to the main form and notifies users when a field is required and if there are data entry errors on the related form component.

In this example, a user is editing the primary contact information directly on the account main form and scrolls down the form to create a new appointment for the primary contact without leaving the account form.

:::image type="content" source="media/form-control-component.gif" alt-text="Form control component used to create an appointment without leaving the main form":::

### Using quick create forms

There will be times when you want to create an experience where users can quickly create records without additional navigation or clicks.  A quick create form is a good solution. It can be used in multiple scenarios that include creating appointments from an activity timeline wall, creating a contact from a lookup if a main form dialog isn't needed, or quickly creating a record from a view page, like an account or contact that doesn’t require additional relationships for data integrity (app menu “+” option). More information: [Create or edit model-driven app quick create forms for a streamlined data entry experience](create-edit-quick-create-forms.md)

In the example here, a user needs to quickly create a lead using the “+” menu option in the app header.

:::image type="content" source="media/create-lead.gif" alt-text="Create lead record from view":::

In this example, the quick create form is used to create an appointment for a contact from the timeline wall.

:::image type="content" source="media/create-appt-from-timeline.gif" alt-text="Create an appointment from the timeline control":::

In this example, a user can quickly create an opportunity from a quote record form using a lookup control.

> [!NOTE]
> Opportunity and quote tables require a Dynamics 365 customer engagement app, such as Dynamics 365 Sales.

:::image type="content" source="media/create-opportunity-from-quote.gif" alt-text="Create an opportunity record from a quote record":::

### Using quick view forms for read-only access to related tables

In many scenarios, a user just needs to quickly see information from a related table without having to interact with it.  To facilitate these scenarios, you can use quick-view forms.  The forms can be built to only show the most important information needed to complete tasks that do not require a user to edit the information.  An example of where a quick-view form is used is in the reference panel of a main record.  This demonstrates the power of accessing multiple related records without having to navigate away.  You can also add quick-view forms directly onto a main form when you want related information to be accessed but not edited by a user. More information: [Create a model-driven app quick view form to view information about a related table](create-edit-quick-view-forms.md)

:::image type="content" source="media/quick-view-form.gif" alt-text="Quick view form example":::

### Using form display options to reduce clutter and build focused forms

There are many times when you need to build an experience that focuses the user on the task at hand without additional distraction that could cause inefficiency.  This is especially important when you are working with tables and records that have global components, which are created and automatically added to forms regardless of the task you are trying to build.  While this provides a shareable and easy-to-build infrastructure that drives consistency across an app, it does at times provide unnecessary distraction.

Form display options should be used when you want to lessen the number of actions, focus a user to complete a task, and reduce clutter by removing unnecessary components that can include the command bar, the header body, the form tabs, and the form footer.  All of these types of options are only available via the client API and manual formxml updates. Manual formxml manipulation can cause issues importing solutions if done incorrectly, so do so carefully when designing your form.

Also consider that when you hide certain components like the command bar or the tab list, you will remove navigation that may be necessary to complete a task. Be sure to account for those requirements in your form design with additional controls created using the Power Apps component framework.

In this example, the command bar has been removed to reduce any unnecessary actions when working with an account.  This form has been designed to not need the command bar so the maker has removed it to keep the user on task. More information: [setCommandBarVisible (Client API reference)](../../developer/model-driven-apps/clientapi/reference/formContext-ui-headerSection/setCommandBarVisible.md)

:::image type="content" source="media/form-no-command-bar.png" alt-text="Form in app with no command bar":::

In this example, the header has been removed to promote a dense form that focuses the user on  record details.  This should only be used if the header does not provide additional value or is not needed to display information that does not always need to be available to a user. More information: [setBodyVisible (Client API reference)](../../developer/model-driven-apps/clientapi/reference/formContext-ui-headerSection/setBodyVisible.md)

:::image type="content" source="media/form-no-header.png" alt-text="Form in app without a header":::

In this example, the tabs have been removed.  This can be helpful when you build a form that only has a single tab or you want to focus the user on the first tab of a form without the distractions of additional tabs that can lead to loss in productivity for a specific task. More information: [setTabNavigatorVisible (Client API reference)](../../developer/model-driven-apps/clientapi/reference/formContext-ui-headerSection/setTabNavigatorVisible.md)

:::image type="content" source="media/form-no-tabs.png" alt-text="Form in app without tabs":::

In some scenarios where you want more data density and do not use or need the form footer you can easily remove it to provide more data and information on the form.  This can also help drive consistency as user move from dashboards and view pages where footers are not included on the page.  In this example, the form footer has been removed to reduce clutter and drive data density. More information: [setVisible (Client API reference)](../../developer/model-driven-apps/clientapi/reference/formContext-ui-footerSection/setVisible.md)

:::image type="content" source="media/form-no-footer.png" alt-text="Form in app without a footer":::

### Form display option to use the entire space of a tab

In many scenarios, you may have a form with a tab and a single control and you want that control to take up the entire available space within the body of the form on that tab.  You can do that using the form display option that allows the first control on a page in a tab to expand the full height and width of the form.  All existing reflow rendering across view port sizes from large to small is honored and will behave like a regular form but the control will use the entire space.  In this example, the Dynamics 365 Marketing application supports a full tab layout for the customer journey experience.  The command bar is removed to further reduce clutter and ensure the user is focused on the task of managing customer journey’s in the application. More information: [setContentType (Client API reference)](../../developer/model-driven-apps/clientapi/reference/formContext-ui-tabs/setContentType.md)

:::image type="content" source="media/tab-using-entire-space.png" alt-text="Form with full tab layout":::

### See also
[Optimize model-driven app form performance](optimize-form-performance.md)