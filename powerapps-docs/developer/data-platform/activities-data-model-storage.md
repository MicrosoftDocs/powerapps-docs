---
title: "Activities data model and storage | MicrosoftDocs"
description: "This article will help you understand the activities data model and its impact on storage capacity."
ms.date: 07/18/2022
author: DanaMartens
ms.author: dmartens
ms.reviewer: mduelae
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
---

# Activities data model and storage

Activity tables (formerly entities) such as email, phone call, and appointment are stored in the Microsoft Dataverse database with a more sophisticated data model compared to standard tables, which are usually stored in one database table. This article will help you understand the activities data model and its impact on storage capacity. For more details regarding how activities are used, see [Activity tables](activity-entities.md).

## Activities underlying database tables

Activity rows are saved in the Dataverse database across multiple underlying tables. Each activity table stores corresponding rows of data in a base table (ActivityPointerBase) and an extension table that is dedicated for each specific activity type (EmailBase, TaskBase, AppointmentBase, etc.).

### ActivityPointerBase

This table is the base table for each activity in the system. The creation of any activity such as an email, phone call, appointment, or custom activity will create a corresponding row in this table. Because this table contains one row for every activity, it's expected this table may have many rows. 

This table includes all default activity columns such as subject, description, owner, regarding, status, and many more. For a full list of the columns in this table, see [activitypointer EntityType](reference/entities/activitypointer.md). Because each of these columns is included in this base activity table and there is one row for every activity, this is often one of the largest consumers of data capacity. The description column is the same column used to store the email body for an email activity. Because an email body can include a large amount of text, large emails can contribute to the growth in data capacity consumed by this table.

When you access a view such as My Activities or All Activities, the data is retrieved from the ActivityPointerBase table allowing you to see a single view of activities across multiple activity types. 

Any activity in the system is retrievable using the specific activity schema name, and is also retrievable using the activitypointer schema, this functionality is useful when retrieving multiple activities of different activity types.

### ActivityPartyBase

This table contains the party information for each activity. Each activity party represents a person or group associated with an activity. Example: Assume you created an Appointment activity that has one organizer, one owner, two required attendees, one optional attendee, and one regarding object. There would be six corresponding rows stored in this table. Another example of activity parties is all the people on an email activity on the From, To, and Cc lines.

If a row such as a contact is deleted, any activity party rows that reference the contact aren't automatically deleted. This is by design to preserve the original participant data. When you delete an activity row such as an email, all activity party rows associated to that activity are deleted.

More information: [ActivityParty table](activityparty-entity.md) and [activityparty EntityType](reference/entities/activityparty.md).

### ActivityMimeAttachment

This table contains the data to relate an attachment to an activity row.

More information: [activitymimeattachment EntityType ](reference/entities/activitymimeattachment.md)

### EmailSearchBase (internal use)

This table is used for email address resolution. It's for internal use only and contains rows for each email address in the system associated to an email address formatted column.

### EmailHashBase (internal use) 

This table is used for [smart matching](/power-platform/admin/email-message-filtering-correlation) and contains hashes generated for each email message in the system. 

More information: [Use email message filtering and correlation](/power-platform/admin/email-message-filtering-correlation) and [Disable Smart Matching EmailHashBase table population](https://community.dynamics.com/crm/b/crminthefield/posts/disable-smart-matching-emailhashbase-table-population-for-dataverse-environments)

### Difference between schema and storage

There is a difference between the schema exposed for individual activity tables and the underlying storage. Example: If you refer to the [email entity schema](reference/entities/email.md) accessible from SDK, all the table columns will be available and will be surfaced from different underlying tables (base table, extension table, activity party table). However, most of these columns are stored in the base table (ActivityPointerBase), and only custom columns, if any, will be stored in the EmailBase table.

## FAQ

### ActivityPointerBase 

#### Why does ActivityPointerBase have so many rows?

Refer to the base table definition above for more details. 
one row for each activity in the system.

#### Why is ActivityPointerBase consuming so much storage?

One potential cause is having many rows, which contributes to the overall table size. Another potential cause is the length of text in the description column. This is the same description column used for any activity such as the body of an email activity or the description of an appointment activity. 

#### How can I reduce ActivityPointerBase table usage?

ActivityPointerBase contains data that was saved as users create activity rows such as emails, phone calls, tasks, and appointments. As users create more activities, the table will grow. The table contains data saved by users and doesn't contain any internal use data. You can reduce the space used for this table by deleting any old activities that are no longer needed.

### ActivityPartyBase

#### Why does ActivityPartyBase have so many rows?

There's one row for each activity participation. It's easy to have many rows in this table, however the space utilized by these individual rows is minimal.

### Other Questions 

#### Why does an activity extension table consume so much storage?

An extension table extends the base activity table (ActivityPointerBase) for a specific activity table such as Task and is used for storing the data for any custom columns. The Task table stores data for the default attributes inside the ActivityPointerBase table in the database. If you add custom attributes to the Task table, they'll be saved in the TaskBase table in the database. An extension table will have rows only when there's a custom attribute defined for the specific activity. There could be cases where a text field which contains a large amount of text is defined as custom activity attribute and could cause high storage usage. Review the custom attributes defined and the content.

#### Where is the body (description) of an email stored?

The email body is stored in the description column of the ActivityPointerBase table. This attribute is retrievable from both schemas: email and activitypointerbase. However, the data isn't duplicated. It's just surfaced in two locations as needed.

## See also




[!INCLUDE[footer-include](../../includes/footer-banner.md)]













