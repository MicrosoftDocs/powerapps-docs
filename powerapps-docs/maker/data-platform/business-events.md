---
title: Microsoft Dataverse business events (preview)| Microsoft Docs
description: Learn about how to use business events to connect and integrate business applications.
author: JimDaly
manager: sunilg
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 05/01/2021
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

Microsoft Dataverse has always had a robust event framework to capture system events *within* Dataverse. You have always had the ability to respond to data operations like Create, Update, and Delete of table rows as well as specialized events where data changes occur within the system.

Dataverse business events takes this further in two ways:

- **Custom Events**: In addition to system defined events, you can define custom events which Dataverse will process using its event framework. These events may or may not represent data changes within Dataverse. You can define custom events that describe completed events in external systems. 
- **Catalog Events**: Business events introduces the concept of cataloging events. With so many events available in the system it can be difficult to locate the right one. An event catalog improves event discovery by associating events with a solution and organizing events into categories. A catalog only includes high value events relevant to the solution, so less useful events can be filtered out.

## Custom Events

Use custom API to create custom events. Each custom API will create a new Dataverse message and provide the web service endpoint to call the custom API. The Dataverse event framework provides for step registrations when these APIs are used as well as exposing these as events in Power Automate when they are cataloged.

Not every Custom API can or should be a business event. Custom APIs provide a generic way to create new APIs which can be used for many purposes. A custom business event is an operation which contains data that is useful for subscribers. 

For example, you may have a custom api that encapsulates a set of operations that represent a business process, like *Reassign*, which will change the ownership of one record to another. Or *Escalate* that will raise the priority state of a record and create additional associated tasks. When you use a custom api in this manner, you are defining new events that may be of interest to subscribers.

However, if you create a custom api named *GetImage* to delegate some function of a UI element to the server, it is not going to represent a useful business event.

This is why business events must be cataloged. The owner of the solution that contains the custom api should only catalog those custom api which represent high value events. 

Only custom apis that are defined as actions can be cataloged as custom events. More information: [Create and use Custom APIs](../../developer/data-platform/custom-api.md).

### Custom Process Actions

Custom process actions can also be cataloged as business events. This is for backward compatibility if your solution already uses custom process actions to encapsulate some business logic which would represent a business event. You are not required to migrate this custom action to use Custom API.

However, custom process actions have the following limitations:

- Like any workflow, they can be disabled in the UI.
- They have no way to prevent synchronous plug-in steps to be registered on them, so they are not recommended for external events.

If your custom process action doesn’t contain any logic within the workflow designer and relies only on plug-ins to perform operations, you can probably migrate the custom process action to be a custom api to mitigate these issues. The Power Platform community has already created tooling to help with this. See the [Custom Action to Custom API Converter](https://www.xrmtoolbox.com/plugins/MarkMpn.CustomActionToApiConverter/) XrmToolBox plugin.

### External Events

Custom events can represent events that occur in external systems. Events that occur in external systems have already completed. 

Custom APIs created for external events should align to these principles:

- They should not have any plug-in type specified for the main operation.
- They should not allow any synchronous step registrations. 
    - The custom api Allowed Custom Processing Step Type setting should be set to Async Only. This will prevent any asynchronous steps from being applied for this API.
- They should not have any response properties, only request parameters.
    - With no synchronous logic, there is no way to set response properties.

### Examples

Let’s compare two examples:

#### Scenario A: CustomerPurchase

You have a point-of-sale application and a customer purchase is an important event you want to capture. Perhaps you want to send them an email thanking them for their purchase, and you want to store information on the total amount the customer has spent in Dataverse. You can define a CustomerPurchase business event within Dataverse. Your point-of-sale application can send information about this event to Dataverse. In Dataverse you want to update a record with the total. Then you want to use Power Automate to send an email thanking them for their purchase.

It may seem to be most efficient to implement the logic to calculate the total and update the record in a main operation of the custom API. But introduction of synchronous logic in this way introduces possibility that the logic could fail and return an error to the point-of-sale application calling it. Because the event has already occurred, there is no need to perform any synchronous logic which might cause the Dataverse call to fail. Instead, depend on Power Automate to include all the logic or include another asynchronous plug-in to update the record in Dataverse.

#### Scenario B: VendorPaymentPosted

You have an ERP application has a VendorPaymentPosted event and you simply want to simplify how you centralize your automation logic. You can create a custom api representing this external event and configure the ERP application to call this Dataverse API. When you catalog this custom api as an event, you will be able to use the Dataverse Power Automate connector to use this event as a trigger.

This example expects nothing to be done in Dataverse except enable asynchronous logic to be to be registered for the event.

### Invoking Custom API from external applications

The key requirement to use custom API to send business events is that your application must have the ability to make authorized HTTP requests to Dataverse. For authorization, requests originating from other applications will typically use a special Application User account that must be created in the Dataverse environment. Licensed and authenticated Dataverse users can also use applications to send these requests.

By removing all synchronous logic from the custom api the likelihood of an error causing the operation to fail is extremely low, but not impossible. Your calling application must provide a way to deal with transient errors in the event the Dataverse service isn’t responding, there are network connectivity issues, or service protection limit errors are returned.

To enable authorized calls to Dataverse from your application there must be an Application user configured for the Dataverse environment. More information: [Build web applications using server-to-server (S2S) authentication](../../developer/data-platform/build-web-applications-server-server-s2s-authentication.md).

## Catalog Events

In order for a system action or a custom action to be available as an event, it must be cataloged. More information: [Catalog and CatalogAssignment tables (Preview)](../../developer/data-platform/catalog-catalogassignment.md)

A catalog makes it easier for people to discover the event because they will be grouped by the containing solution and categories defined for that solution. It also excludes low value events.

Solution publishers should provide a catalog that includes the relevant tables containing business data as well as any custom api or custom process actions that represent high-value business events.

The following represents a catalog for a solution called Contoso Customer Management:

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

### Table events

When a table is assigned to a category, certain operations bound to the table will be included. If the table supports Create, Update, and Delete operations, these events will be included. Additional events related to other operations will also be included. For example, if the table is user-owned it participates in security related to the owner. The owner of any record in the table will be able to share it. Operations related to sharing are exposed as GrantAccess, ModifyAccess, and RevokeAccess events.

### Action events

When you associate a Custom API or Custom Process action to a catalog, you can subscribe to that specific operation and receive the data that was used for parameters to that action and any data returned by that action. In the case of an external business event, only data sent as parameters will be available.

## Use Business Events to trigger automation

As business events becomes a common pattern, there will be multiple ways to enable automation.

The first experience where business events will be exposed is in Power Automate Dataverse connector using the **When an action is performed** trigger.

:::image type="content" source="../../developer/data-platform/media/when-an-action-is-performed-trigger.png" alt-text="When an action is performed trigger":::


[!INCLUDE[footer-include](../../includes/footer-banner.md)]