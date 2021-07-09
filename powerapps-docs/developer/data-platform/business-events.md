---
title: Microsoft Dataverse business events (preview)| Microsoft Docs
description: Learn about how to use business events to connect and integrate business applications.
author: JimDaly
manager: sunilg
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 06/12/2021
ms.author: jdaly
search.audienceType: 
  - maker
  - developer
  - flowmaker
search.app: 
  - PowerApps
  - D365CE
---

# Microsoft Dataverse business events (preview)

Automation of business logic and integration with other systems are driven by events. When something interesting happens in a business application, an event occurs and data describing the event becomes available for subscribers to respond to. Microsoft Dataverse provides capabilities to relay event data to subscribers using the following applications and technologies:

- Power Automate Flows
- Azure Service Bus
- Azure Event Hub
- Web Hooks
- Dataverse plug-ins

Dataverse has a robust event framework to capture system events *within* Dataverse. You can respond to events within the system using the Dataverse Event Framework. This isn't changing. More information [Event framework](event-framework.md)

Dataverse Business events provides new ways to expose events and compose your business logic to respond to them asynchronously, such as the Power Automate Dataverse **When an action is performed** trigger.

Here are some examples:

- You have logic that you want to apply when a sharing operation is performed on a user-owned record. The only way to initiate logic on this `GrantAccess` message that occurs when a record is shared is via the Dataverse Event framework, typically through a plug-in. With business events, you can *catalog* the table which will expose the `GrantAccess` message.

- A plug-in developer may have some logic in a synchronous plug-in code that responds to a certain set of conditions which they pass into Shared Variables for another asynchronous plug-in to initiate some automation. With a business event, instead of passing those details through the event pipeline shared variables, you can call a custom action containing the details of the event in the parameters. An asynchronous plug-in can then respond to the custom action, or you may choose to use Power Automate instead. Other logic can also be added to respond to that event. This pattern offers greater flexibility and an opportunity to simplify the logic in your plug-in code.

## Catalogs and Custom events

Dataverse business events includes concepts from [Dynamics Finance and Operations Business events](/dynamics365/fin-ops-core/dev-itpro/business-events/home-page) together with the Dataverse Event Framework to provide a new way to discover events and create automation when these events occur.

- **Event Catalog**:  With so many events available in the system it can be difficult to locate the right one. An event catalog improves event discovery by associating events with a solution and organizing events into categories. 
    
    A catalog only includes selected, high value events relevant to the solution. Adding an event to a catalog is how you expose the event.

- **Custom Events**: You can create custom actions to be custom events because Dataverse will process them using its event framework.

    These events may or may not represent data changes within Dataverse. You can use custom apis *without any* synchronous logic that exist to only to notify listeners that an event of interest occurred. You emit the event by calling the custom action.

## Event Catalog

To expose a business event it must be cataloged. More information: [Catalog and CatalogAssignment tables](catalog-catalogassignment.md)

A catalog makes it easier to discover the business event because they are grouped by the containing solution and categories defined for that solution. The solution publisher selects which events are most relevant for their solution.

A **Catalog** is a hierarchial structure where the top level represents a solution. Then the next level is a **Category**. Relevant tables and events are then assigned to a Category.

For example, the following represents a catalog for a solution called *Contoso Customer Management*:

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

This example uses **Tables** and **Customer Events** as categories but you can use any category grouping that makes sense for your solution.

If your solution consists of multiple dependent solutions, you may define the root catalog in the base solution, then add additional categories and assigned events to the dependent solutions which add them.

## Table events

When a table is assigned to a category, certain operations bound to the table will be included. You can't select each operation individually. If the table supports Create, Update, and Delete operations, these events will be included.

Additional events related to other operations will also be included. For example, if the table is user-owned it participates in security events. The owner of any record in the table will be able to share it, change sharing capabilities, or stop sharing the record. Operations related to sharing are exposed as `GrantAccess`, `ModifyAccess`, and `RevokeAccess` events. Additional events may also be included depending on the table. If the table is a Virtual Table, and it has been configured to support Virtual Table events, the `OnExternalCreated`, `OnExternalUpdated`, `OnExternalDeleted` events will be included. More information: [Enable Virtual Tables to support Dataverse events](virtual-entities/enable-virtual-table-event-support.md)

Add only those tables which contain business data that will be of interest to subscribers. You should not try to include every table.

The same table can be included in multiple catalogs. For example, if your solution depends on customer data in the Dataverse Account or Contact tables, you should include them. Other catalogs may include tables from your solution.

## Custom Events

Use Dataverse Custom API to create custom events. Each custom API will create a new Dataverse message and provide the web service endpoint to call the custom API. More information: [Create and use Custom APIs](custom-api.md).

Custom business events can only send notifications when an event is completed. Dataverse event framework provides capabilities to include synchronous logic which can cancel an operation or change the output so that you can extend the behavior of the system. Many of the same messages exposed with business events may be extended using synchronous logic in the Dataverse event framework, but business event notifications only occur when these operations complete successfully.

For example, you may have a custom api that encapsulates a set of operations that represent a business process, like *Reassign*, which will change the ownership of one record to another based on certain criteria. Or *Escalate* that will raise the priority state of a record and create additional associated tasks. When you use a custom api in this manner, you are defining new events that may be of interest to subscribers. *If these operations complete successfully*, asynchronous logic can be triggered on them.

You can also create a custom action purely to enable subscribers to respond to it. [External Events](#external-events) describes a specific case where events originate outside of Dataverse, but you can create custom api as events for use within Dataverse as well using the same settings. If your custom action is intended only for subscribers to respond to, we recommend that the name of your custom action begin with `On`, such as `OnCustomerPurchase` or `OnVendorPaymentPosted`.

Custom API can be used for many different purposes, not all of them are related to operations that represent interesting events for business logic. This is why business events must be cataloged. The owner of the solution that contains the custom api should only catalog those custom api which represent high value events. You should not try to catalog every custom action that is included in your solution.

### Design principles

When you consider custom apis to catalog as business events in your solution use the following design principles.

- **Clear intent**: The intent behind creating a business event must be clearly understood. In other words, what is the reason for creating the business event, and how it will be used by the subscriber?

- **Specific**: The event should be specific so that a subscriber doesn't need to filter whether or not they should respond to it. Do not create generic business events that subscribers may not always respond to.

- **Lightweight**: The event should contain only that data necessary to describe the event. If the subscriber requires additional data, the information in the event should provide the context to allow them to retrieve it if necessary.

- **Not for tranferring data**: If your intent is to transfer data to a recipient and, in effect, realize a data export scenario, you don't have a good use case for business events. In fact, the use of business events for data transfer scenarios is a misuse of the business events.

### Custom Process Actions

The concept of *Custom Action* includes both [Custom API](custom-api.md) and [Custom Process actions](workflow-custom-actions.md). They both create a new API, but how they do it is different. For custom business events, we recommend Custom API.

Custom process actions can also be cataloged as business events. This is for backward compatibility if your solution already uses custom process actions to encapsulate some business logic which would represent a business event. You are not required to migrate this custom action to use Custom API.

However, custom process actions have the following limitations:

- Like any workflow, they can be disabled in the UI. You may not know when someone disables your custom process action until it suddenly stops working.
- Until recently, there was no way to prevent synchronous plug-in steps to be registered on custom process actions, which means anyone could register synchronous steps that could change the behavior of the custom process action or even cancel it. There is now a [IsCustomProcessingStepAllowedForOtherPublishers](/reference/entities/workflow#BKMK_IsCustomProcessingStepAllowedForOtherPublishers) managed property that allows a custom process action to block this. But if you are going to update your custom process action to set this property, you should consider converting it to use Custom API instead.

For more information about how they are different, see [Compare Custom Process Action and Custom API](custom-actions.md#compare-custom-process-action-and-custom-api)

If your custom process action doesn’t contain any logic within the workflow designer and relies only on plug-ins to perform operations, you can probably migrate the custom process action to be a custom api to mitigate these issues. 

The Power Platform community has already created tooling to help with this. See the [Custom Action to Custom API Converter](https://www.xrmtoolbox.com/plugins/MarkMpn.CustomActionToApiConverter/) XrmToolBox plugin.

> [!NOTE]
> Tools created by the community are not supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.

### External Events

Custom events can represent events that occur in external systems. Events that occur in external systems have already completed.

Custom APIs created for external events should align to these principles:

- They should not have any plug-in type specified for the main operation.
- They should not allow any synchronous step registrations. 
    - The custom api [Allowed Custom Processing Step Type](/developer/data-platform/reference/entities/customapi#BKMK_AllowedCustomProcessingStepType) property should be set to **Async Only**. This will prevent any synchronous steps from being applied for this API.
- They should not have any response properties, only request parameters.
    - With no synchronous logic, there is no way to set response properties.

> [!NOTE]
> These settings are not only for events that occur outside of Dataverse. Custom API can be used with these settings to represent events that occur *within* Dataverse as well.

#### Examples

Let’s compare two external event examples:

##### Scenario A: OnCustomerPurchase

You have a point-of-sale application and a customer purchase is an important event you want to capture. Perhaps you want to send them an email thanking them for their purchase, and you want to store information on the total amount the customer has spent in Dataverse. You can define a `OnCustomerPurchase` Custom API within Dataverse. Your point-of-sale application can send information about this event to Dataverse. In Dataverse you want to update a record with the total. Then you want to use Power Automate to send an email thanking them for their purchase.

It may seem to be most efficient to implement the logic to calculate the total and update the record in a main operation of the custom API. But introduction of synchronous logic in this way introduces possibility that the logic could fail and return an error to the point-of-sale application calling it. Because the event has already occurred, there is no need to perform any synchronous logic which might cause the Dataverse call to fail. Instead, depend on Power Automate to include all the logic or include another asynchronous plug-in step on the `OnCustomerPurchase` event to update the record in Dataverse.

##### Scenario B: OnVendorPaymentPosted

You have an ERP application has a `OnVendorPaymentPosted` event and you simply want to simplify how you centralize your automation logic. You can create a custom api representing this external event and configure the ERP application to call this Dataverse API. When you catalog this custom api as an event, you will be able to use the Dataverse Power Automate connector to use this event as a trigger.

This example expects nothing to be done in Dataverse except enable asynchronous logic to be to be registered for the event.

#### Invoking Custom API from external applications

The key requirement to use custom API to send business events is that your application must have the ability to make authorized HTTP requests to Dataverse. For authorization, requests originating from other applications will typically use a special Application User account that must be created in the Dataverse environment. Licensed and authenticated Dataverse users can also use applications to send these requests.

By removing all synchronous logic from the custom api the likelihood of an error causing the operation to fail is extremely low, but not impossible. Your calling application must provide a way to deal with transient errors in the event the Dataverse service isn’t responding, there are network connectivity issues, or service protection limit errors are returned.

To enable authorized calls to Dataverse from your application there must be an Application user configured for the Dataverse environment. More information: [Build web applications using server-to-server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md).

## Use Business Events to trigger automation

As business events becomes a common pattern, there will be multiple ways to enable automation.

The first experience where business events are exposed is in Power Automate Dataverse connector using the [When an action is performed (preview)](/connectors/commondataserviceforapps/#when-an-action-is-performed-(preview)) trigger.

:::image type="content" source="media/when-an-action-is-performed-trigger.png" alt-text="When an action is performed trigger.":::

Within this experience Create, Update, and Delete events are not shown for table events. These events are already available using the [When a row is added, modified or deleted](/connectors/commondataserviceforapps/#when-a-row-is-added,-modified-or-deleted) trigger.


## See Also

[Catalog and CatalogAssignment tables](catalog-catalogassignment.md)<br />
[Enable Virtual Tables to support Dataverse events](virtual-entities/enable-virtual-table-event-support.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]