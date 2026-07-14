---
title: Microsoft Dataverse business events| Microsoft Docs
description: Learn about how to use business events to connect and integrate business applications.
ms.date: 02/11/2026
author: jaredha
ms.author: jaredha
ms.reviewer: jdaly
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - maker
  - developer
  - flowmaker
contributors:
 - JimDaly
---

# Microsoft Dataverse business events

Events drive automation of business logic and integration with other systems. When something interesting happens in a business application, an event occurs and data describing the event becomes available for subscribers to respond to. Microsoft Dataverse provides capabilities to relay event data to subscribers by using the following applications and technologies:

- Power Automate Flows
- Azure Service Bus
- Azure Event Hub
- Webhooks
- Dataverse plug-ins

Dataverse has a robust event framework to capture system events *within* Dataverse. You can respond to events within the system by using the Dataverse Event Framework. This framework isn't changing. For more information, see [Event framework](event-framework.md).

Dataverse Business events provides new ways to expose events and compose your business logic to respond to them asynchronously, such as the Power Automate Dataverse **When an action is performed** trigger.

Here are some examples:

- You have logic that you want to apply when a sharing operation is performed on a user-owned record. The only way to initiate logic on this `GrantAccess` message that occurs when a record is shared is via the Dataverse Event framework, typically through a plug-in. By using business events, you can *catalog* the table that exposes the `GrantAccess` message.

- A plug-in developer might have some logic in synchronous plug-in code that responds to a certain set of conditions. The developer passes these conditions into Shared Variables for another asynchronous plug-in to initiate some automation. By using a business event, instead of passing those details through the event pipeline shared variables, you can call a custom action containing the details of the event in the parameters. An asynchronous plug-in can then respond to the custom action, or you might choose to use Power Automate instead. You can add other logic to respond to that event. This pattern offers greater flexibility and an opportunity to simplify the logic in your plug-in code.

## Catalogs and custom events

Dataverse business events combines concepts from [Dynamics Finance and Operations Business events](/dynamics365/fin-ops-core/dev-itpro/business-events/home-page) with the Dataverse Event Framework. This combination provides a new way to discover events and create automation when these events occur.

- **Event Catalog**: With so many events available in the system, it can be difficult to locate the right one. An event catalog improves event discovery by associating events with a solution and organizing events into categories. 
    
    A catalog includes only selected, high-value events that are relevant to the solution. You expose an event by adding it to a catalog.

- **Custom Events**: You can create custom actions as custom events because Dataverse processes them by using its event framework.

    These events might represent data changes within Dataverse, or they might not. You can use custom APIs *without any* synchronous logic that exist only to notify listeners that an event of interest occurred. You emit the event by calling the custom action.

## Event catalog

To expose a business event, you must catalog it. For more information, see [Catalog and CatalogAssignment tables](catalog-catalogassignment.md).

A catalog groups business events by the containing solution and categories defined for that solution. The solution publisher selects which events are most relevant for their solution.

A **Catalog** is a hierarchical structure where the top level represents a solution. The next level is a **Category**. You assign relevant tables and events to a category.

For example, the following structure represents a catalog for a solution called *Contoso Customer Management*:

- Contoso Customer Management
  - Tables
    - Account
    - Contact
    - Membership
  - Customer Events
    - Entered Store
    - Visit Web Site
    - Purchase Product
    - Return Product

This example uses **Tables** and **Customer Events** as categories, but you can use any category grouping that makes sense for your solution.

If your solution consists of multiple dependent solutions, you can define the root catalog in the base solution, then add additional categories and assigned events to the dependent solutions.

## Table events

When you assign a table to a category, you include certain operations that are bound to the table. You can't select each operation individually. If the table supports Create, Update, and Delete operations, these events are included.

You also include additional events related to other operations. For example, if the table is user-owned, it participates in security events. The owner of any record in the table can share it, change sharing capabilities, or stop sharing the record. Operations related to sharing are exposed as `GrantAccess`, `ModifyAccess`, and `RevokeAccess` events. Additional events might also be included depending on the table. If the table is a Virtual Table, and you configure it to support Virtual Table events, the `OnExternalCreated`, `OnExternalUpdated`, and `OnExternalDeleted` events are included. For more information, see [Enable Virtual Tables to support Dataverse events](virtual-entities/enable-virtual-table-event-support.md).

Add only those tables that contain business data that interest subscribers. Don't try to include every table.

You can include the same table in multiple catalogs. For example, if your solution depends on customer data in the Dataverse Account or Contact tables, include them. Other catalogs might include tables from your solution.

## Custom Events

Use Dataverse custom API to create custom events. Each custom API creates a new Dataverse message and provides the web service endpoint to call the custom API. For more information, see [Create and use Custom APIs](custom-api.md).

Custom business events can only send notifications when an event is completed. The Dataverse event framework provides capabilities to include synchronous logic that can cancel an operation or change the output so that you can extend the behavior of the system. Many of the same messages that business events expose can be extended by using synchronous logic in the Dataverse event framework, but business event notifications only occur when these operations complete successfully.

For example, you might have a custom API that encapsulates a set of operations that represent a business process, like *Reassign*, which changes the ownership of one record to another based on certain criteria. Or *Escalate* that raises the priority state of a record and creates additional associated tasks. When you use a custom API in this manner, you're defining new events that might interest subscribers. *If these operations complete successfully*, asynchronous logic can be triggered on them.

You can also create a custom action purely to enable subscribers to respond to it. [External Events](#external-events) describes a specific case where events originate outside of Dataverse, but you can create custom API as events for use within Dataverse as well by using the same settings. If your custom action is intended only for subscribers to respond to, we recommend that the name of your custom action begin with `On`, such as `OnCustomerPurchase` or `OnVendorPaymentPosted`.

Custom API can be used for many different purposes, not all of them are related to operations that represent interesting events for business logic. This is why business events must be cataloged. The owner of the solution that contains the custom API should only catalog those custom API that represent high value events. Don't try to catalog every custom action that you include in your solution.

### Design principles

When you consider custom APIs to catalog as business events in your solution, use the following design principles.

- **Clear intent**: Clearly understand the intent behind creating a business event. In other words, know the reason for creating the business event and how the subscriber uses it.

- **Specific**: Make the event specific so that a subscriber doesn't need to filter whether or not they should respond to it. Don't create generic business events that subscribers might not always respond to.

- **Lightweight**: Include only the data necessary to describe the event. If the subscriber requires extra data, the information in the event should provide the context to allow them to retrieve it if necessary.

- **Not for transferring data**: If your intent is to transfer data to a recipient and, in effect, realize a data export scenario, don't use business events. Using business events for data transfer scenarios is a misuse of the business events.

### Custom process actions

The concept of *Custom Action* includes both [custom API](custom-api.md) and [Custom Process actions](workflow-custom-actions.md). Both types of custom actions create a new API, but they differ in how they create it. For custom business events, use custom API.

You can also catalog custom process actions as business events. This approach provides backward compatibility if your solution already uses custom process actions to encapsulate some business logic that represents a business event. You're not required to migrate this custom action to use custom API.

However, custom process actions have the following limitations:

- Like any workflow, you can disable them in the UI. You might not know when someone disables your custom process action until it suddenly stops working.
- Until recently, there's no way to prevent synchronous plug-in steps from being registered on custom process actions. This limitation means anyone can register synchronous steps that change the behavior of the custom process action or even cancel it. There's now a [IsCustomProcessingStepAllowedForOtherPublishers](reference/entities/workflow.md#BKMK_IsCustomProcessingStepAllowedForOtherPublishers) managed property that allows a custom process action to block this step. If you're going to update your custom process action to set this property, consider converting it to use custom API instead.

For more information about how they differ, see [Compare Custom Process Action and custom API](custom-actions.md#compare-custom-process-action-and-custom-api).

If your custom process action doesn't contain any logic within the workflow designer and relies only on plug-ins to perform operations, you can probably migrate the custom process action to be a custom api to mitigate these problems. 

The Power Platform community already created tooling to help with this. See the [Custom Action to custom API Converter](https://www.xrmtoolbox.com/plugins/MarkMpn.CustomActionToApiConverter/) XrmToolBox plugin.

> [!NOTE]
> Microsoft doesn't support tools created by the community. If you have questions or problems with community tools, contact the publisher of the tool.

### External events

Custom events can represent events that occur in external systems. Events that occur in external systems have already completed.

Custom APIs created for external events should align to these principles:

- Don't specify any plug-in type for the main operation.
- Don't allow any synchronous step registrations. 
    - Set the Custom API [Allowed Custom Processing Step Type](reference/entities/customapi.md#BKMK_AllowedCustomProcessingStepType) property to **Async Only**. This setting prevents any synchronous steps from being applied for this API.
- Don't include any response properties, only request parameters.
    - Without synchronous logic, there's no way to set response properties.

> [!NOTE]
> These settings aren't only for events that occur outside of Dataverse. You can use Custom API with these settings to represent events that occur *within* Dataverse as well.

#### Examples

Let's compare two external event examples:

##### Scenario A: OnCustomerPurchase

You have a point-of-sale application and a customer purchase is an important event you want to capture. Perhaps you want to send the customer an email thanking them for their purchase, and you want to store information on the total amount the customer has spent in Dataverse. You can define a `OnCustomerPurchase` custom API within Dataverse. Your point-of-sale application can send information about this event to Dataverse. In Dataverse you want to update a record with the total. Then you want to use Power Automate to send an email thanking them for their purchase.

It might seem most efficient to implement the logic to calculate the total and update the record in a main operation of the custom API. But introduction of synchronous logic in this way introduces possibility that the logic could fail and return an error to the point-of-sale application calling it. Because the event already occurred, there's no need to perform any synchronous logic which might cause the Dataverse call to fail. Instead, depend on Power Automate to include all the logic or include another asynchronous plug-in step on the `OnCustomerPurchase` event to update the record in Dataverse.

##### Scenario B: OnVendorPaymentPosted

You have an ERP application that has a `OnVendorPaymentPosted` event and you simply want to simplify how you centralize your automation logic. You can create a custom api representing this external event and configure the ERP application to call this Dataverse API. When you catalog this custom api as an event, you can use the Dataverse Power Automate connector to use this event as a trigger.

This example expects nothing to be done in Dataverse except enable asynchronous logic to be registered for the event.

#### Invoking custom API from external applications

The key requirement to use custom API to send business events is that your application must have the ability to make authorized HTTP requests to Dataverse. For authorization, requests originating from other applications typically use a special Application User account that you create in the Dataverse environment. Licensed and authenticated Dataverse users can also use applications to send these requests.

By removing all synchronous logic from the custom api the likelihood of an error causing the operation to fail is extremely low, but not impossible. Your calling application must provide a way to deal with transient errors in case the Dataverse service isn't responding, there are network connectivity issues, or service protection limit errors are returned.

To enable authorized calls to Dataverse from your application, you must configure an Application user for the Dataverse environment. For more information, see [Build web applications using server-to-server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md).

## Use Business Events to trigger automation

As business events become a common pattern, multiple ways to enable automation emerge.

The first experience where business events are exposed is in Power Automate Dataverse connector by using the [When an action is performed](/connectors/commondataserviceforapps/#when-an-action-is-performed) trigger.

:::image type="content" source="media/when-an-action-is-performed-trigger.png" alt-text="When an action is performed trigger.":::

Within this experience, Create, Update, and Delete events don't appear for table events. These events are already available by using the [When a row is added, modified or deleted](/connectors/commondataserviceforapps/#when-a-row-is-added,-modified-or-deleted) trigger.


## See Also

[Catalog and CatalogAssignment tables](catalog-catalogassignment.md)<br />
[Enable Virtual Tables to support Dataverse events](virtual-entities/enable-virtual-table-event-support.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
