---
title: Model-driven app glossary of terms | Microsoft Docs
description: Simple descriptions of commonly used terms when building model-driven apps
ms.custom: intro-internal
author: Mattp123
ms.service: powerapps
ms.topic: overview
ms.component: model
ms.date: 07/20/2021
ms.subservice: mda-maker
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
searchScope:
  - "Power Apps"
---
# Model-driven app glossary of common terms

## Accessibility

Accessibility is a term that is used to refer to the extent to which people with disabilities can use digital products. In the case of model-driven apps consideration has been paid to matters such as responsive design, how user navigate between fields, how the app behaves in high contrast mode and how screen readers help users to understand the nature of the application.

[Using screen readers within model-driven apps](../../user/screen-reader.md)

## Admin Center

In the Power Platform admin center is a unified portal for administrators to manage environments and settings for Power Apps, Power Automate and Dynamics customer engagement products.  Please note that it does not cover administration settings and features associated with Power BI.

[Learn more about the Power Platform admin center](https://docs.microsoft.com/en-us/power-platform/admin/admin-documentation)

[Learn about the Power BI admin center](https://docs.microsoft.com/en-us/power-bi/admin/service-admin-administering-power-bi-in-your-organization)

## App Designer

The tool that is used to create model-driven apps.  Given that the model-driven and canvas app building experience are starting to converge the new app designer experience (which delivers the app experience during the build process) will begin to replace the classic experience.

It allows us to configure the navigation site map, the tables required and the forms and views relevant to the app.

[We can use the classic app designer when we build or edit our apps](../../maker/model-driven-apps/build-first-model-driven-app.md)

[A preview of the new app designer experience](../../maker/model-driven-apps/app-designer-overview.md)

## App Navigation Experience

The way in which we areas, groups and sub-groups are presented in a model-driven app.  It is often know as the [site map](../model-driven-apps/model-driven-app-glossary.md#site-map)

## Application Lifecycle Management

The way in which we manage the life cycle of an application from conception to end of life.  From a technical perspective much of this is managed via solutions when delivering model-driven app products.

## Area

 A part of the [model-driven app navigation experience](../../maker/model-driven-apps/app-navigation.md).  Apps can have multiple groups and groups can have multiple sub-areas.  The sub-area contains the tables relevant to the application. For apps with more than one area, a switch control is displayed in the lower left navigation pane.

## Business Process Flow

Logic built into a given table to ensure that users complete records by updating fields in the correct order.  

Whilst these are authored initially using the Power Automate Experience they are experienced within model-driven app as a change in the user interface.

A business process flow is arranged into Stages and each stage defines the columns (fields) that need to be completed at that time.
Business Process Flows express themselves as dots spread across the screen and each dot represents themselves as the relevant stage.

At any stage one or more fields are be updated before progression onto later stages.

[Business process flows overview](https://docs.microsoft.com/en-us/power-automate/business-process-flows-overview)

## Business Rule

Business rules are server-side logic that is used with canvas or model-driven apps to set or clear values in one or many columns in a table. They can also be used to validate stored data or show error messages. Model-driven apps can use business rules to show or hide columns, enable or disable columns, and create recommendations based on business intelligence.

[Learn more about business rules](../../maker/model-driven-apps/create-business-rules-recommendations-apply-logic-form)

[Business rules - Microsoft Learn content](https://docs.microsoft.com/en-us/learn/modules/define-create-business-rules/1-rules)  

## Canvas app

An app which is generated using drag and drop controls configured using Power Fx.  Canvas apps offer the designer significant control over the user experience and can be connected to a very wide range of data sources and data services.  

Canvas apps are arranged into screens and controls such as galleries, text boxes and dropdowns are placed onto the screens and configured so that they connect to the data sources and to each other correctly.

Whereas a model-driven app comes with many preconfigured features such as forms, views and a user interface many Canvas apps are authored from a blank canvas, or a template, so there is often more work to be performed and more outright work using code.

Canvas apps live in Solutions and Environments in the same way as Model-driven apps.

[Find out more about canvas apps here](../canvas-apps/getting-started.md).

## Chart

A visual representation of a table of data.  These can take the form of line, bar, pie chart or donut chart.

[Find out more about creating a system chart here](../../maker/model-driven-apps/create-edit-system-chart.md).

## Classic

The classic interface represents the method in which app developers would make changes to features within their Dataverse environment.

This has been replaced over time by the web-based method of app authoring known as the unified interface.  For many developers now and in the future this will be the only interface they will ever use.

## Classic App Designer

Modern apps allow for the creation of both Canvas apps and model-driven apps.

In due course all model-driven apps will be authored as modern apps.

The ability to create model-driven apps using the app designer remains.  We call this the classic app designer authoring experience.

## Column

A field within a dataverse table (or entity).  Columns are similar to fields in databases and have different data types such as Text, Number, Date as well as data types less familiar to databases such as Phone, Email, File and Image.

The nature of the field type defines the type of data required by the column and also the controls (such as date picker or text box) that will be made available when using the control.

Columns also appear when creating forms.  Form **tabs** also have columns, and this defines where we can put our sections.  Additionally form **sections** have columns, and these define where we can place our table columns (fields in this case).

[How to create and edit columns](../../maker/data-platform/create-edit-fields.md)

[Add, configure, move, or delete columns on a form](../../maker/model-driven-apps/add-move-or-delete-fields-on-form.md)

## Command Bar

The area of a model-driven app that contains basic commands universally used by model driven apps.

:::image type="content" source="../../developer/model-driven-apps/media/customization-account-grid-command-bar.png" alt-text="Layout for a Unified Interface app.":::

## Component

Components are elements used when creating the elements that make up a model-driven app.

Very often these will relate to the method of creation of the tables that make up the model driven app.

Components can be split into Data (tables, relationships, columns) UI (Site Map,forms,views) Logic (Business process flows, rules ..) and Visualization (Charts, dashboards, Power BI Tiles)

[Find out more about components](../../maker/model-driven-apps/model-driven-app-components.md)

## Connection

A model driven app is only ever connected to the data tables that reside in the same environment.  This connection can be considered as being native, as it never need to be set up within an environment.

Connections exist within the environment to enable other elements of the Power Platform to operate correctly.  Notably, canvas Power Apps and Power Automate flows do have the ability to make use of multiple connections.

## Control

Controls allow us to interact with information contained within our records.  They typically manifest themselves within forms, where we have the opportunity to update data.  Examples of controls are calendar, toggle, choices, slider and editable grids.  In some cases we may wish to use different controls depending upon the device employed by the user.

[Find out more about controls](../../maker/model-driven-apps/additional-controls-for-dynamics-365-for-phones-and-tablets.md)

## Dashboard

A container for one or more charts relating to a table.

[Find out more about dashboards here](../../maker/model-driven-apps/create-edit-dashboards.md)

A dashboard allows charts, Power BI reports and views of tables to be presented to the app user.

[Find out more about how to use Power BI within a model driven app](../../maker/model-driven-apps/use-power-bi.md)

## Data Model

A collection of related [tables](model-driven-app-glossary.md#table).  In the context of model-driven apps these are held within the Dataverse database.

Where these are included in a [solution](model-driven-app-glossary.md#solution) these are often a set of related tables built with the purpose of delivering the overall business application.

## Database

The collective term for all the tables in Dataverse.

## Dataverse

Microsoft Dataverse is the collective term for the tables, workflows, business process flows and related functionality that is provisioned within an environment when a database is created.  

Model-driven apps are tied to the Microsoft Dataverse database.

A Dataverse database contains data structures most closely associated with databases in addition to being able to hold model-driven apps, canvas apps, power automate flows.

[Find out more about Dataverse here](../../maker/data-platform/data-platform-intro.md)

## Dependency

Dependencies are created when elements of components are reliant on each other for them to work.  For example if a column is used within a view then the view requires this column to exist for it to be able to function.  There are many examples of this throughout Dataverse, such as a model-driven app being dependent on a table if that table is used within the app.

Dependencies manifest themselves in numerous ways including when a model-driven app is validated.  They also become apparent in the most problematic fashion when trying to delete an aspect of a table, form, view or dashboard.  Where this is the case the dependencies can be reviewed by selecting the item to be deleted and then selecting "show dependencies" in the menu.

[Validate an app](validate-app.md)
[Delete a column from a table](https://docs.microsoft.com/en-us/powerapps/maker/data-platform/delete-fields)

## Dynamics

Microsoft Dynamics is a line of enterprise resource planning (ERP) and customer relationship management (CRM) software applications. Microsoft markets Dynamics applications through a network of reselling partners who provide specialized services.

[Learn more about Microsoft Dynamics](https://docs.microsoft.com/en-us/dynamics365/)

## Entity

An entity is another way of describing a [table](../model-driven-apps/model-driven-app-glossary.md#table).  However you will see elements of this terminology within the product and elsewhere on the internet.

## Environment

An environment is a space to store, manage, and share your organization's business data, data structures, apps, chatbots, and flows.

You can package up the various elements as solutions, and these solutions can be exported from one environment to another.

An environment can only ever have 1 Dataverse database and all your model-driven apps are tied to this database.

Often multiple environments are used to enable application life-cycle management.  For example you might have a development, test and production environment.

Environments are tied to a geographical region and can be a means of ensuring that the data physically stays in the correct geographical region.

[Find out more about environments here](https://docs.microsoft.com/en-us/power-platform/admin/environments-overview)

## Flow

Cloud flows are functionality offered by Power Automate that allow automation of tasks to take place based upon triggering of conditions such as recurrence, adding or updating of records or simply selection of buttons by users.  They can be run with or without the introduction of new parameters.

## Form

Forms provide the user interface (UI) that people use to create, view, or edit table records. Use the form designer in the customization tools to create and edit forms.

There are 4 types of form.  Main, Quick Create, Quick View and Card.

More information:

[Form Types](../../maker/model-driven-apps/types-forms.md)

[Cpening the form designer](../../maker/model-driven-apps/open-form-editor.md)

[Learn about creating and designing forms](../../maker/model-driven-apps/create-design-forms.md)

[Add a section to or remove a section from a form](add-move-or-delete-sections-on-form)

[Add a tab to or remove a tab from a form](add-move-or-delete-tabs-on-form.md)

## Form designer

The design experience for creating and editing forms.

[Cpening the form designer](../../maker/model-driven-apps/open-form-editor.md)

## Group

A part of the [model-driven app navigation experience](../../maker/model-driven-apps/app-navigation.md).
Group names appear as a navigation element in an app with the subarea names (tables) within the group listed beneath it.

## Legacy

This refers to features that have either been deprecated, or the way in which they are authored has been moved to the web based unified interface.


## Lookup

Lookups are a field type that exist when 2 tables that are related to each.  They can be seen in views table on the many side of a one to many relationship.  They are generally populated using a form on the many side of the relationship.

[Learn more about the lookup field user experience](../../user/lookup-field.md)

[How to configure a lookup](../../maker/model-driven-apps/form-designer-add-configure-lookup.md)

## Main form

Every table has at least one main form.  It represents the primary method of interaction with a record.  The main form is responsive to the device using the form and can contain controls that are optimized to the device whether it be phone, tablet or web.  It is edited using the form designer.

[Learn about other form types](../../maker/model-driven-apps/types-forms.md)

## Monitor

Also know as the App Monitor.  It allows us to understand aspects of the performance of our model-driven app, but can an also be used for canvas apps.

[Learn how to use the app monitor](../../maker/monitor-modelapps.md)

[Use Monitor to understand form performance](monitor-form-checker.md)

## Page

Modern apps contain the concept of pages, which can be either model driven apps or a canvas based page which allows flexible layout, low-code Fx functions, and Power Apps connector data.

It is a simpler tool for enabling model-driven apps and canvas apps to live together.

[Learn about creating modern apps](app-designer-overview.md)

## Power Automate

A Microsoft product that allows users to streamline repetitive tasks.  Typically this is performed using cloud [flows](model-driven-app-glossary.md#flow), however in the context of model-driven apps [business process flows](model-driven-app-glossary.md#business-process-flow) that direct users to complete table records in a specific fashion are authored within Power Automate.

Power Automate flows exist within an environment and can also exist within Power Apps [solutions](model-driven-app-glossary.md#solution).

[Learn more about Power Automate](https://docs.microsoft.com/en-us/power-automate/getting-started)

## Power BI

A data visualization tool that has the capacity to be embedded within model-driven apps or to live completely independently of them.  Power BI can connect to a very wide range of data sources, of which Dataverse is just one.

Power BI Reports do not live within Dataverse Environments or inside solutions.

[Use Power BI within a model driven app](use-power-bi.md)

[Learn more about Power BI](https://docs.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)

## Publish

The process by which we make the latest iteration of the app available to users within an environment.

## Publisher

Every solution has a publisher. You specify the publisher when you create a solution.  The solution indicates who developed the app, and will define the prefix (e.g cr8a3_MyNewTable) for all the solution assets.

[Learn more about publishers](../../maker/data-platform/create-solution#solution-publisher)

## Record

A record contains one or more columns of information about a person, a place, or a thing. For example, a record might contain the name, the email address, and the phone number of a single customer. Other tools refer to a record as a "row" or an "item".  Records exist within Dataverse tables.

## Relationship

The way in which fields between tables relate to each other.  There are 3 types of relationship:

- 1 to many (1 Author to many Novels)
- many to 1 (many pages to 1 book)
- Many to Many (many books borrowed by many people).

Model driven apps often contain tables with relationships between them.  Where relationships exist we have the ability to navigate to the record within the related table.  For example, when looking at a sale we might navigate to the account table to investigate details relating to the account.

[Learn about creating table relationships](https://docs.microsoft.com/en-us/powerapps/maker/data-platform/create-edit-entity-relationships)

## Responsive Apps

An app that is **responsive** will render itself in a way that depends on the nature of the device that is accessing the app.  This may even mean that depending on the device there may even be different controls (e.g. a date picker) whether the user is consuming the app on a computer, tablet or mobile. 

Additionally, tables and fields will render themselves according to size of the device being used.

## Section

Tabs within forms are arranged into sections.  Sections can be arranged into 1 to 4 columns, and they allow us to arrange the record metadata in a way that it is most relevant to the current tab and the current section.

[Learn more about working with sections](../../maker/model-driven-apps/add-move-or-delete-sections-on-form.md)

## Security Role

A security role defines what people can see and do with a record.  

This relates to create, read, write, delete, update and append actions.

Security roles are created and users are put into security roles either as individual user names or by using active directory security groups.

We grant access to model-driven apps through security roles.

[Find out more about security roles](https://docs.microsoft.com/en-us/power-platform/admin/security-roles-privileges##%20security-roles)

[General overview of security in Microsoft Dataverse](https://docs.microsoft.com/en-us/power-platform/admin/wp-security)

[Getting started with security roles using content from Microsoft Learn](https://docs.microsoft.com/en-us/learn/modules/get-started-security-roles/)

## Site Map

Site maps define the tables that are included within a model-driven app and the navigation experience by which users will have when moving between those apps.

A model-driven app is essentially a collection of tables, dashboards and views and these are described via the site map.

When configuring the navigation experience we are editing the Areas, Groups and Subgroup navigation elements.  Tables exist at the level of the subgroup, and are arranged into groups.  Groups are effectively collections of tables and are visible in the navigation pane.  Areas allow you to toggle between visible groups.

Both modern and classic methods of creating a model-driven app include site maps, however with a modern app you design the site map with a drag and drop experience whereas with the classic method you build the site map by hand.

To get to the site map from the modern app building experience you need to click switch to classic.

[Find out more about app navigation here](../../user/navigation.md)

## Solution

A solution is a wrapper for a very wide range of components including tables (entities), cloud flows, security roles.

It is considered best practice when developing model-driven apps to ensure that the assets associated with them are held inside solutions.

The exist in 2 forms.  **Managed Solutions** permit only a small amount of customisation whereas **Unmanaged Solutions** give designers full control over the product that they are creating.

Unmanaged Solutions would be used by developers and these would be exported as managed solutions for use in production environments.

This allows for a high level of control around our application lifecycle management.

[Find out more about solutions here](../../maker/data-platform/solutions-overview.md)

[Discover solutions in the context of Dataverse](../../developer\data-platform\introduction-solutions.md)

## Solution Explorer

The name given to the app designers make edits to solution.  Whilst it is a legacy experience it often offers additional functionality with regards to editing aspects of solutions.

It can be viewed through both a classic and a modern interface.

To access the modern interface use the following steps :-

  - Sign in to make.powerapps.com
  - Navigate to an [environment](model-driven-app-glossary.md#environment).
  - Select a [solution](model-driven-app-glossary.md#solution) into which you would like to place a model driven app.  Create a solution if one doesn't already exist.
  - Explore the components of the solution

[Find out more about solutions here](../maker/data-platform/solutions-overview.md)

## Subgrid

Sub-grids are areas of main forms that display data within a Dataverse table, whilst remaining on the form.

Typically this is used to display child records that relate to the parent record currently under review.  For example books written by an author.

Whilst they manifest themselves within a model-driven app they are a property of a form.

[Create a subgrid](form-designer-add-configure-subgrid.md)

[Subgrid properties - legacy](sub-grid-properties-legacy.md)

## Subarea

A part of the [model driven app navigation experience](../../user/navigation.md).
Subareas (tables) and pages appear under the group that they're configured within in the app designer.

## Tab

Every form has at least 1 tab and these are relevant to how we present table record data.  A form can have multiple tabs and this allows us to offer the user a range of ways of looking at the same record.  This is often a better user experience, or a more logical way of presenting the data in the record.

From a site map perspective a tab is a "Group" when using the sitemap designer versus a subarea for tables and an area to hold subareas.

[Learn more about working with tabs](../../maker/model-driven-apps/add-move-or-delete-tabs-on-form.md)

## Table

A table is a method of storing data in columns (or fields) within Dataverse.  We sometimes refer to them [entities](../model-driven-apps/model-driven-app-glossary.md#entity).

Tables, in the context of model-driven apps, only ever exist within a [Dataverse](model-driven-app-glossary.md#dataverse) database.

A single entry within a table is know as a [record](model-driven-app-glossary.md#record), for example a single customer, and the columns describe metadata associated with the customer such as the name, telephone number or credit limit.

Every model-driven app must contain at least one table.  Much of the process of creating a model driven app is selecting the tables most relevant to solving the business problem.

Tables have [views](model-driven-app-glossary.md#view), [forms](model-driven-app-glossary.md#form) and [business rules](model-driven-app-glossary.md#business-rule) associated with them.

Additionally, tables also have [charts](model-driven-app-glossary.md#chart) as well as [dashboards](model-driven-app-glossary.md#dashboard) where table charts a presented.

Tables can relate to other tables and these are defined via the [relationships](model-driven-app-glossary.md#relationship) that have been set up between them.

When we move tables between environments we move all table elements noted along with the table.  This permits a more stable application management lifecycle.

[Find out more about configuring tables here](../../maker/data-platform/entity-overview.md)

## Table designer

The design experience for creating and editing tables.  This allows us to create tables, columns, relationships, business rules and views.

[Create a custom table using the table designer](../../maker/data-platform/data-platform-create-entity)

## Unified Interface

The Unified Interface for model-driven apps provides a consistent and accessible user experience across devices—whether on a desktop, laptop, tablet, or phone.  The predecessor the the unified interface was know as the web interface.

[Find out more about the unified interface here](../../user/unified-interface.md)

## Validate

The process by which we confirm if the model-driven app has all the components required for it to function properly.

[Learn how to validate an app](validate-app.md)

## View

A tabular representation of records in a Dataverse table.  Tables can have multiple views.

Views can be pre-filtered and it is possible to define the specific views that a model driven app will make available to users.

Tables can have multiple views associated with them and we can define the table views relevant to our model-driven apps at the time that we create them.

[Find out more about views here](../../maker/model-driven-apps/create-edit-views.md)

## Workflow

A workflow is a series of functions or methods, called steps, that are performed sequentially and apply to data contained within our tables. The workflow can change the processing direction by using conditionals, referred to as conditional branches.

In many cases workflows can be replaced by Power Automate flows, and vice versa.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
