---
title: Model-driven app glossary of terms | Microsoft Docs
description: Simple descriptions of commonly used terms when building model-driven apps
ms.collection: get-started
author: Mattp123
ms.topic: overview
ms.component: model
ms.date: 02/03/2022
ms.subservice: mda-maker
ms.author: matp
ms.reviewer: v-roryneary
search.audienceType: 
  - maker
searchScope:
  - "Power Apps"
---
# Model-driven app glossary of common terms

This article contains a glossary of terms for Power Apps model-driven apps.

## Accessibility

Accessibility is a term that is used to refer to the extent to which people with disabilities can use digital products. In the case of model-driven apps, consideration has been paid to matters such as responsive design, how user navigate between fields, how the app behaves in high contrast mode, and how screen readers help users to understand the nature of the application.

[Using screen readers within model-driven apps](../../user/screen-reader.md)

## Admin center

The Power Platform admin center is a unified portal for administrators to manage environments and settings for Power Apps, [Power Automate](#power-automate), and [Dynamics 365](#dynamics-365) apps. Power Platform admin center doesn't cover administration settings and features associated with [Power BI](#power-bi).

[Learn more about the Power Platform admin center](/power-platform/admin/admin-documentation)

[Learn about the Power BI admin center](/power-bi/admin/service-admin-administering-power-bi-in-your-organization)

## App designer

The tool that is used to create and edit model-driven apps. As the modern app designer experience matures, it will replace the classic experience.

Use it to configure the navigation [site map](#site-map), [tables](#table), [forms](#form), and [views](#view) relevant to your app.

[A preview of the new app designer experience](../../maker/model-driven-apps/app-designer-overview.md)

[We can use the classic app designer when we build or edit our apps](../../maker/model-driven-apps/build-first-model-driven-app.md)

## App navigation experience

The way in which [areas](#area), [groups](#group), and [subarea](#subarea) are presented in a model-driven app.  It is also known as the [site map](../model-driven-apps/model-driven-app-glossary.md#site-map)

## Application lifecycle management

The way in which we manage the lifecycle of an application from conception to end of life. From a technical perspective, much of application lifecycle management (ALM) is managed via [solutions](#solution) when delivering model-driven app products.

[Overview of application lifecycle management with Microsoft Power Platform](/power-platform/alm/overview-alm)

## Area

 A part of the [model-driven app navigation experience](../../maker/model-driven-apps/app-navigation.md), apps can have multiple groups and groups can have multiple sub-areas.  The sub-area contains the tables relevant to the application. For apps with more than one area, a switch control is displayed in the lower left navigation pane.

[App navigation in model-driven apps](app-navigation.md)

## Attribute

An attribute is another name for a [column](#column) and is a term commonly used by Power Apps developers. Each [table](#table) in Power Apps corresponds to a database table and each table column in Power Apps corresponds to a column in the database table. 

## Business process flow

Logic built into a given table to ensure that users complete records by updating fields in the correct order.  

While these are authored initially using the [Power Automate](#power-automate) experience, business process flows are experienced within model-driven app as a change in the user interface.

A business process flow is arranged into stages. Each stage defines the columns (fields) that must be completed typically before moving on to the next stage. For example, the default business process flow for the opportunity table has four stages: qualify > develop > propose > close. The current stage in a business process flow is indicated with a dot next to the stage in the sequence of stages from left to right in the flow.

[Business process flows overview](/power-automate/business-process-flows-overview)

## Business rule

Business rules are server-side logic that is used with canvas or model-driven apps to set or clear values in one or more columns in a table. Business rules can also be used to validate stored data or display error messages. Model-driven apps can use business rules to show or hide columns, enable or disable columns, and create recommendations based on business intelligence.

[Learn more about business rules](../../maker/model-driven-apps/create-business-rules-recommendations-apply-logic-form.md)

[Define business rules](/training/modules/define-create-business-rules/1-rules)

## Canvas app

An app which is generated using drag and drop controls configured using Power Fx.  Canvas apps offer the designer significant control over the user experience and can be connected to a wide range of data sources and data services.  

Canvas apps are arranged into screens and controls such as galleries, text boxes, and dropdowns, are placed onto the screens and configured so that they connect to the data sources and to each other correctly.

Whereas a model-driven app comes with many preconfigured features such as forms, views, and a user interface, many Canvas apps are authored from a blank canvas, or a template. There is often more work to be performed and more outright work using code.

Canvas apps are contained within environments and solutions in the same way as model-driven apps.

[Find out more about canvas apps here](../canvas-apps/getting-started.md).

## Chart

A visual representation of a table of data. These can take the form of line, bar, pie, or donut chart.

[Find out more about creating a system chart here](../../maker/model-driven-apps/create-edit-system-chart.md).

## Classic

The classic interface represents the method in which app makers make changes to features within their Microsoft [Dataverse](#dataverse) environment.

The classic interface has been replaced over time by the web-based method of app authoring known as the unified interface.

[About Unified Interface for model-driven apps in Power Apps](/power-platform/admin/about-unified-interface)

## Classic app designer

The modern app designer lets you create model-driven apps and create [canvas apps](#canvas-app) using custom pages.

The modern app designer will soon be the default designer for model-driven apps. Currently, you can still create model-driven apps using the classic app designer.

## Column

A column (formerly called a field), is a field within a Dataverse table (formerly called an entity). Columns are similar to fields in databases and have different data types such as text, number, date, as well as data types less familiar to databases such as phone, email, file, and image.

The column type defines the kind of data required by the column and also the controls, such as date picker or text box, that will be available when using the control.

Columns also appear when creating forms. Form tabs also have columns, and this defines where you can put sections. Additionally, form sections have columns, and these define where you can place table columns (form fields in this case).

[How to create and edit columns](../../maker/data-platform/create-edit-fields.md)

[Add, configure, move, or delete columns on a form](../../maker/model-driven-apps/add-move-or-delete-fields-on-form.md)

## Command bar

The area of a model-driven app that contains basic commands universally used by model-driven apps.

:::image type="content" source="../../developer/model-driven-apps/media/customization-account-grid-command-bar.png" alt-text="Layout for a Unified Interface app.":::

The command bar can be customized. More information: [Customize the command bar using command designer (preview)](use-command-designer.md)

## Component

Components are elements. Components are used when creating the elements that make up a model-driven app. Often these elements will relate to the method of creation of the tables that make up a model-driven app.

Components can be split into data (tables, relationships, columns) UI (site map,forms,views), logic (business process flows, business rules) and visualization (charts, dashboards, and Power BI Tiles).

[Learn more about components](../../maker/model-driven-apps/model-driven-app-components.md)

## Connection

A model-driven app is only connected to the data tables that reside in the same environment.  This connection can be considered native because it never has to be set up within the environment.

Connections exist within the environment to enable other elements of the Power Platform to operate correctly.  Notably, Power Apps [canvas apps](#canvas-app) and [Power Automate](#power-automate) [flows](#flow) have the ability to make use of multiple connections.

## Control

Controls allow you to interact with information contained within records. They typically are visible on forms, where users update data using the control. Examples of controls are calendar, toggle, choices, slider, and editable grids.  In some cases you might want to use different controls depending upon the device employed by the user.

[Find out more about controls](../../maker/model-driven-apps/additional-controls-for-dynamics-365-for-phones-and-tablets.md)

## Dashboard

A container for one or more charts relating to a table.

[Find out more about dashboards here](../../maker/model-driven-apps/create-edit-dashboards.md)

A dashboard allows charts, Power BI reports, and views of tables to be presented to the app user.

[Find out more about how to use Power BI within a model driven app](../../maker/model-driven-apps/use-power-bi.md)

## Data model

A collection of related [tables](model-driven-app-glossary.md#table). In the context of model-driven apps, these are held within the [Dataverse](#dataverse) database.

In a custom [solution](model-driven-app-glossary.md#solution), the data model is often the set of related tables built with the purpose of delivering the overall business application.

## Database

The collective term for all the tables in [Dataverse](#dataverse).

## Dataverse

Microsoft Dataverse is the collective term for the [tables](#table), [workflows](#workflow), [business process flows](#business-process-flow), and related functionality that are provisioned within an environment when a database is created.  

Model-driven apps require a Dataverse database.

A Dataverse database contains data structures most closely associated with databases in addition to being able to hold model-driven apps, [canvas apps](#canvas-app), and [Power Automate](#power-automate) [flows](#flow).

[Find out more about Dataverse here](../../maker/data-platform/data-platform-intro.md)

## Dependency

Dependencies are created when elements of components are reliant on each other for them to work. For example, if a column is used within a view then the view requires the column to exist for it to be able to function. There are many examples of dependencies throughout [Dataverse](#dataverse). Another example is a model-driven app being dependent on a table if that table is used within the app.

Dependencies manifest themselves in numerous ways including when a model-driven app is validated. They also become apparent in the most problematic fashion when trying to delete an aspect of a table, form, view or dashboard.  When this occurs, the dependencies can be viewed by selecting the item to be deleted, and then selecting "show dependencies" on the command bar.

- [Removing dependencies](/power-platform/alm/removing-dependencies)
- [Validate an app](validate-app.md)
- [Delete a column from a table](../data-platform/delete-fields.md)

## Dynamics 365

Microsoft Dynamics 365 is a line of enterprise resource planning (ERP) and customer relationship management (CRM) software applications. Microsoft markets Dynamics 365 applications through a network of reselling partners who provide specialized services.

[Learn more about Microsoft Dynamics 365](/dynamics365/)

## Entity

An entity is the classic way of describing a [table](../model-driven-apps/model-driven-app-glossary.md#table). You'll see this terminology within the classic experiences and elsewhere on the internet.

## Environment

An environment is a space to store, manage, and share your organization's business data, data structures, apps, chatbots, and flows.

You can package up the various elements as solutions, and these solutions can be exported from one environment to another.

An environment can only ever have one [Dataverse](#dataverse) database and all your model-driven apps in the environment use this database.

Often multiple environments are used to enable application lifecycle management. For example you might have development, test, and production environments.

Environments exist within a geographical region and can be a means of ensuring that the data physically stays in the correct geographical region.

[Find out more about environments here](/power-platform/admin/environments-overview)

## Flow

Cloud flows are functionality offered by [Power Automate](#power-automate) that allow automation of tasks to take place based upon triggering of conditions such as recurrence, adding or updating of records or simply selection of buttons by users. Flows can be run with or without the introduction of new parameters.

[Cloud flows](/power-automate/flow-types#cloud-flows)

## Form

Forms provide the user interface (UI) that people use to create, view, or edit table records. Use the form designer in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to create and edit forms.

There are four types of forms: main, quick create, quick view, and card.

More information:

- [Form Types](../../maker/model-driven-apps/types-forms.md)
- [Opening the form designer](../../maker/model-driven-apps/open-form-editor.md)
- [Learn about creating and designing forms](../../maker/model-driven-apps/create-design-forms.md)
- [Add a section to or remove a section from a form](add-move-or-delete-sections-on-form.md)
- [Add a tab to or remove a tab from a form](add-move-or-delete-tabs-on-form.md)

## Form designer

The design experience for creating and editing forms.

[Opening the form designer](../../maker/model-driven-apps/open-form-editor.md)

## Group

A part of the [model-driven app navigation experience](../../maker/model-driven-apps/app-navigation.md). Group names appear as a navigation element in an app with the subarea names (tables) within the group listed beneath it.

## Legacy

This refers to features that have either been deprecated, or the way in which they are authored, has been moved to more modern experience, such as the web-based unified interface.

## Lookup

A lookup is a field type that exists when two tables are related. Lookups can be seen in table views on the many side of a [one-to-many relationship](#relationship). They are generally populated using a form on the many side of the relationship.

- [Learn more about the lookup field user experience](../../user/lookup-field.md)
- [How to configure a lookup](../../maker/model-driven-apps/form-designer-add-configure-lookup.md)

## Main form

Every table has at least one main form. The main form represents the primary method of interaction with a record. The main form is responsive to the device using the form and can contain controls that are optimized to the device whether it is phone, tablet, or web. Main forms are edited using the form designer.

[Learn about other form types](../../maker/model-driven-apps/types-forms.md)

## Monitor

Also know as the app monitor. It lets you understand aspects of the performance of a model-driven app. App monitor can an also be used to monitor [canvas apps](#canvas-app).

- [Learn how to use the app monitor](../../maker/monitor-modelapps.md)
- [Use Monitor to understand form performance](monitor-form-checker.md)

## Page

Modern apps have the concept of pages, which can be either model-driven apps or a canvas-based page using a custom pages. Custom pages allow flexible layout, low-code Power Fx functions, and Power Apps connector data.

It is a tool for enabling model-driven apps and [canvas apps](#canvas-app) to exist together.

- [Working with custom pages](model-app-page-overview.md)
- [Learn about creating modern apps](app-designer-overview.md)

## Power Automate

A Power Platform service that allows users to streamline repetitive tasks. Typically, this automation is performed using cloud [flows](model-driven-app-glossary.md#flow).

Model-driven app [business process flows](model-driven-app-glossary.md#business-process-flow) that direct users to complete table records in a specific fashion, are authored within Power Automate.

[Power Automate flows](#flow) exist within an environment and can also exist within Power Apps [solutions](model-driven-app-glossary.md#solution).

[Learn more about Power Automate](/power-automate/getting-started)

## Power BI

A data visualization tool that has the capacity to be embedded within model-driven apps or to live completely independently of them. Power BI can connect to a very wide range of data sources, of which [Dataverse](#dataverse) is just one.

Power BI Reports don't exist within [Dataverse](#dataverse) environments or inside solutions.

- [Use Power BI within a model driven app](use-power-bi.md)
- [Learn more about Power BI](/power-bi/fundamentals/power-bi-overview)

## Publish

The process by which you make the latest iteration of the app available to users within an environment.

## Publisher

Every solution has a publisher. You specify the publisher when you create a solution. The solution publisher indicates who developed the app, and will define the prefix, such as *Contoso*_MyNewTable, for all the solution assets.

[Learn more about publishers](../../maker/data-platform/create-solution.md#solution-publisher)

## Record

A record contains one or more columns of information about a person, a place, or a thing. For example, a record might contain the name, the email address, and the phone number of a single customer. Other tools refer to a record as a "row" or an "item".  Records exist within [Dataverse](#dataverse) tables.

## Relationship

The way fields in different tables relate to each other. There are three types of relationship:

- One-to-many. For example, one author to many novels.
- Many-to-one. For example, many pages to one book.
- Many-to-many. For example, many books borrowed by many people.

Model-driven apps often contain tables with relationships between them. Where relationships exist, users navigate to the record within the related table. For example, when looking at a sales invoice record, you can open the related account record to investigate details for that account.

[Learn about creating table relationships](../data-platform/create-edit-entity-relationships.md)

## Responsive apps

An app that is responsive will render itself in a way that depends on the device that is accessing the app. This may even mean that there may even be a different control displayed, such as a date picker, depending on whether the user is running the app on a computer, tablet, or phone.

Additionally, tables and fields render themselves according to screen size of the device being used.

## Section

[Tabs](#tab) within forms are arranged into sections. Sections can be arranged into one to four columns and they let you arrange the record metadata in a way that is most relevant to the current tab and the current section.

[Learn more about working with sections](../../maker/model-driven-apps/add-move-or-delete-sections-on-form.md)

## Security role

A security role defines what people can see and do with a record. This relates to create, read, write, delete, update, and append actions.

Security roles are created and users are put into security roles either as individual user names or by using active directory security groups.

You grant access to model-driven apps through security roles.

- [Find out more about security roles](/power-platform/admin/security-roles-privileges#security-roles)
- [General overview of security in Microsoft Dataverse](/power-platform/admin/wp-security)
- [Get started with security roles in Dataverse](/training/modules/get-started-security-roles/)

## Site map

A model-driven app is essentially a collection of tables, dashboards, views, and pages, and these are described via the site map. The site map defines the tables and pages that are included within a model-driven app and the navigation experience users will have when moving between them.

When configuring the navigation experience you're editing the areas, groups, and subarea navigation elements. Tables exist at the level of the subarea, and are arranged into groups. Groups are effectively collections of tables and pages and are visible in the navigation pane. Areas allow you to toggle between visible groups.

Both modern and classic methods of creating a model-driven app include site maps.However, with the modern app designer you can design the site map with a drag and drop experience whereas the classic site map designer doesn't support drag and drop.

To open the site map in the classic site map designer from the modern app building experience, select **Switch to classic**.

[Find out more about app navigation here](../../user/navigation.md)

## Solution

A solution is a wrapper for a very wide range of components including [tables](#table), [cloud flows](#power-automate), and [security roles](#security-role).

When you make a model-driven app, ensure that the assets associated with it are held inside a solution.

Solutions have two forms:

- Managed solutions generally permit only a small amount of customization or no customization at all.
- Unmanaged solutions give makers full control over the project that they are creating.

Unmanaged solutions are used by makers and developers for exporting projects as a managed solution for use in non-development environments, such as a production environment. This allows for a high level of control for [application lifecycle management](#application-lifecycle-management).

- [Find out more about solutions here](../../maker/data-platform/solutions-overview.md)
- [Discover solutions in the context of Dataverse](../../developer\data-platform\introduction-solutions.md)

## Solution explorer

This is the classic experience that makers and customizers can use to view and make changes to most any solution component. More modern experiences are available from make.powerapps.com and the model-driven app designers and solution explorer will eventually be replaced with those modern experiences.

To access the modern solution interface follow these steps:

1. Sign in to make.powerapps.com.
1. Select an [environment](model-driven-app-glossary.md#environment).
1. On the left pane, select **Solutions**, and then open an unmanaged [solution](model-driven-app-glossary.md#solution) where you want to add a model-driven app.  [Create a solution](../data-platform/create-solution.md) if one doesn't already exist.
1. Explore the components of the solution.

[Find out more about solutions here](../../maker/data-platform/solutions-overview.md)

## Subarea

A part of the [model driven app navigation experience](../../user/navigation.md).
Subareas (tables) and pages appear under the group that they're configured within in the app designer.

## Subgrid

Subgrids are areas of main forms that display a list of records from a [Dataverse](#dataverse) table, while remaining on the form. Typically, a subgrid is used to display child records that relate to the parent record currently under review. For example, books written by an author.

While subgrids are displayed in a model-driven app, they are a property of the form.

- [Create a subgrid](form-designer-add-configure-subgrid.md)
- [Subgrid properties - legacy](sub-grid-properties-legacy.md)

## Tab

Every form has at least one tab and these are relevant to how we present table record data. A form can have multiple tabs. This lets you, the maker, offer the user a range of ways of looking at the same record.  This is often a better user experience, or a more logical way of presenting the data in the record.

From a site map perspective a tab is a "group" when using the site map designer versus a subarea for tables and an area to hold subareas.

[Learn more about working with tabs](add-move-or-delete-tabs-on-form.md)

## Table

A table is a method of storing data in columns (or fields) within [Dataverse](#dataverse). Tables where formerly called [entities](model-driven-app-glossary.md#entity).

Tables, in the context of model-driven apps, only exist within a [Dataverse](model-driven-app-glossary.md#dataverse) database.

A single row within a table is known as a [record](model-driven-app-glossary.md#record). For example, a single customer, and the columns describe metadata associated with the customer such as the name, telephone number, or credit limit.

Every model-driven app must contain at least one table. Much of the process of creating a model-driven app is selecting the tables most relevant to solving the business problem.

Tables have [views](model-driven-app-glossary.md#view), [forms](model-driven-app-glossary.md#form) and [business rules](model-driven-app-glossary.md#business-rule) associated with them.

Additionally, tables also have [charts](model-driven-app-glossary.md#chart) as well as [dashboards](model-driven-app-glossary.md#dashboard) where charts are presented.

Tables can relate to other tables and these are defined via the [relationships](model-driven-app-glossary.md#relationship) that have been set up between them.

<!-- When we move tables between environments we move all table elements noted along with the table. This permits a more stable application management lifecycle. -->

[Find out more about configuring tables here](../../maker/data-platform/entity-overview.md)

## Table designer

The design experience for creating and editing tables. This lets you create tables, columns, relationships, business rules, and views.

[Create a custom table using the table designer](../../maker/data-platform/data-platform-create-entity.md)

## Unified Interface

The Unified Interface provides a consistent and accessible user experience across devices—whether on a desktop, laptop, tablet, or phone. The predecessor to the Unified Interface was known as the web interface.

[Find out more about the unified interface here](../../user/unified-interface.md)

## Validate

The process by which an app maker confirms if the model-driven app has all the components required for it to function properly.

[Learn how to validate an app](validate-app.md)

## View

A tabular representation of records in a [Dataverse](#dataverse) table. Tables can have multiple views.

Views can be pre-filtered and it is possible to define the specific views that a model-driven app will make available to users.

Tables can have multiple views associated with them and you can define the table views relevant to a model-driven app at the time that you create them.

[Find out more about views here](../../maker/model-driven-apps/create-edit-views.md)

## Workflow

A classic workflow is a series of functions or methods, called steps, that are performed sequentially and apply to data contained within tables. The workflow can change the processing direction by using conditionals, referred to as conditional branches.

In many cases classic workflows should be replaced by [Power Automate](#power-automate) [flows](#flow).

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
