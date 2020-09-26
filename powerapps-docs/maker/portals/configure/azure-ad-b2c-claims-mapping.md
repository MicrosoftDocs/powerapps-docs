---
title: "Azure AD B2C provider settings for portals | MicrosoftDocs"
description: "Instructions to enable Azure AD B2C provider settings for portals."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/02/2020
ms.author: sandhan
ms.reviewer: tapanm
---


# Claims mapping

When users sign in, either for the first time or subsequently, the federated identity provider provides claims based on its database regarding the users' signing in. These claims are configurable in the identity provider.

### [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C email claims

[!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C sends the email claim as a collection. The portal accepts the first email provided in the collection as the primary email address of the contact.

### Claims to support sign-up scenarios

When a new customer who does not exist in Common Data Service is provisioned, the inbound claims can be used to seed the new contact record that the portal will create. Common claims can include first and last name, email address, and phone number, but they are configurable. The following site setting is required:

**Name**: Authentication/OpenIdConnect/[Federation-Name]/RegistrationClaimsMapping

**Description**: List of logical name/claim pairs to be used to map claim values to attributes in the contact record created during registration.

**Format**: attribute1=claim1,attribute2=claim2,attribute3=claim3

For example:  firstname=<https://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname,lastname=https://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname,jobtitle=jobTitle>

> [!NOTE]
> Ensure that you map the email address to the primary email (emailaddress1) of the contact. If you have added secondary email (emailaddress2) or alternate email (emailaddress3) to the contact record and mapped it to the email, identity information will not be added to the contact and a new one will be created with the email address used for registration set in the primary email (emailaddress1).

### Claims to support sign-in scenarios

The data in Common Data Service and in the identity provider are not directly linked, so the data might get out of sync. The portal should have a list of claims that you want to accept from any sign-in event to update in Common Data Service. These claims can be a subset of, or equal to, the claims coming in from a sign-in scenario. This must be configured separately from sign-in claims mapping, because you might not want to overwrite some key portal attributes. The following site setting is required:

**Name**: Authentication/OpenIdConnect/[Federation-Name]/LoginClaimsMapping

**Description**: List of logical name/claim pairs to be used to map claim values to attributes in the contact record created after sign-in.

**Format**: attribute1=claim1, attribute2=claim2, attribute3=claim3

For example: firstname=<https://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname,lastname=https://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname,jobtitle=jobTitle> 

The claim name is the CLAIM TYPE field listed next to the attribute in the sign-in policies Application claims.

### Allow auto-association to a contact record based on email 

Customers who have contact records with emails associated then launch a website where their external users will sign in with [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C through an email validation mechanism. The new sign-in should be associated with the existing contact record instead of creating a duplicate record. This functionality only successfully maps a contact that does not have an active identity, and the email address must be unique (not related to multiple contact records). The following site settings are required:

**Name**: Authentication/[Protocol]/[Provider]/AllowContactMappingWithEmail

**Description**: Specifies whether contacts are mapped to a corresponding email. When set to true, this setting associates a unique contact record with a matching email address, and then automatically assigns the external identity provider to the contact after the user has successfully signed in. By default, it is set to *false*.

**Name**: Authentication/UserManager/UserValidator/RequireUniqueEmail

**Description**: Specifies whether a unique email address is needed for validating the user. When an existing contact email address is used to sign-in, the setting must be set to false. By default, it is set to *true* that may cause sign-in attempts to fail for contact records with email address already present.
