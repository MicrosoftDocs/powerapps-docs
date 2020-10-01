---
title: "Allow auto-association to a contact record based on email | MicrosoftDocs"
description: "Allow auto-association to a contact record based on email."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/02/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# How to allow auto-association to a contact record based on email 

Customers who have contact records with emails associated then launch a website where their external users will sign in with [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C through an email validation mechanism. The new sign-in should be associated with the existing contact record instead of creating a duplicate record. This functionality only successfully maps a contact that does not have an active identity, and the email address must be unique (not related to multiple contact records). The following site settings are required:

**Name**: Authentication/[Protocol]/[Provider]/AllowContactMappingWithEmail

**Description**: Specifies whether contacts are mapped to a corresponding email. When set to true, this setting associates a unique contact record with a matching email address, and then automatically assigns the external identity provider to the contact after the user has successfully signed in. By default, it is set to *false*.

**Name**: Authentication/UserManager/UserValidator/RequireUniqueEmail

**Description**: Specifies whether a unique email address is needed for validating the user. When an existing contact email address is used to sign-in, the setting must be set to false. By default, it is set to *true* that may cause sign-in attempts to fail for contact records with email address already present.
