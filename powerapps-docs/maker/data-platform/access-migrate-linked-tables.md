---
title: System columns and tables in Dataverse and Dataverse for Teams | Microsoft Docs
description: When you migrate from Access to Dataverse, you will see columns added to tables after the migration and additional linked tables added in Access to support the columns.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
  - model
ms.reviewer: matp
ms.date: 10/18/2021
ms.subservice: dataverse-maker
ms.author: NHelgren
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
---
# System columns and tables in Dataverse and Dataverse for Teams 

Both Dataverse and Dataverse for Teams have several tables and columns that need to be present for data types and features to work properly. These are part of the default organizations and cannot be removed. When migrating from Access to Dataverse, you will see columns added to tables after the migration and additional linked tables added in Access to support the columns. This document will provide an overview of the tables and columns that will be added.

## Tables

The following tables are included in environments of Dataverse and Dataverse for Teams and may appear as a linked table in Access after migration. These tables can't be deleted.

- **Currency**: Used for currency transactions.
- **Users**: Stores users of the environment that use the apps or data. Used in lookup columns that are created by default.
- **Teams**: Stores teams of users in the environment that use the apps or data. Used in lookup columns that are created by default.
- **Business Unit**: Stores business units users belong to in the environment that use the apps or data. Used in lookup columns that are created by default.

> [!NOTE]
> - The tables are present and usable but not displayed by default in Dataverse for Teams.
> - The Currency table is linked in Access only when a currency column is added to the table.

## Columns 

The following columns are included in all tables of Dataverse and Dataverse for Teams and may be visible in Access linked tables. These columns can't be deleted.

- **Primary Name**: A user friendly text string used to identify rows. The name is chosen by the user. In Access you can choose which field you want to use during migration, or it will be picked for you.
- **Primary ID**: A unique identifier string used to identify rows. This is system generated and is the primary key. This column is present and usable but not displayed by default in Dataverse and Dataverse for Teams environments.
- **CreatedBy**: A lookup column to the users table selecting the user who created the row.
- **CreatedBy (Delegate)**: A lookup column to the users table selecting the user who created the row as a delegate for another user.
- **CreatedOn**: A date time column that records the date and time a row was created, stored in UTC format.
- **Currency**: A lookup to the Currency column (logical name Transactioncurrency) to retrieve the details of a transaction currency for the purposes of calculating against the base currency. This column is visible in Access linked tables only when a currency column is added to the table.
- **Exchange Rate**: The exchange rate value retrieved from the transaction currency on the currency table at the time the row was created. The column is visible in Access linked tables only when an exchange rate column is added to the table. This column is present and usable but not displayed by default in Dataverse, Dataverse for Teams environments, or Access linked tables.
- **Import Sequence Number**: The row’s place in the sequence of imported records that added it to the table.
- **ModifiedBy**: A lookup column to the users table selecting the user who modified the row.
- **ModifiedBy (Delegate)**: A lookup column to the users table selecting the user who modified the row as a delegate for another user.
- **ModifiedOn**: A date time column that records the date and time a row was modified, stored in UTC format.
- **Owner**: The unique OwnerID assigned to the user selected as the Owning User from the Users table. This column is present and usable but not displayed by default in Access linked tables.
- **Owning Business Unit**. A lookup to the business unit table to select the appropriate business unit that owns the row.
- **Owning Team**: A lookup to the team table to select the appropriate team that owns the row.
- **Owning User**: A lookup to the user table to select the appropriate user that owns the row.
- **Record Created On**: Date and time that a row was migrated.
- **Status**: An option set that allows a user to pick the state of a row.
- **Status Reason**: An option set related to Status that allows a user to pick the status reason of a row based on the status selected 
- **Time Zone Rule Version**: Internal only used to determine which set of time zone rules apply.
- **UTC Conversion Time Zone Code**: The time zone offset code that was in use at the time the row was created.
- **Version Number**: The version number of a row used to track previous changes if auditing is enabled.