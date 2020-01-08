---
title: "Verify certification dependencies for plug-ins making outbound calls | MicrosoftDocs"
description: "Ensure that any certificates that your code depends on for outbound calls has a valid chain of certificates."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: ryjones
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 01/08/2020
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Verify certification dependencies for plug-ins making outbound calls

**Category**: Maintainability, Supportability

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

You may get this error when your plug-in makes an https call to an external resource:

`WebException: The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel.`


<a name='guidance'></a>

## Guidance



<a name='additional'></a>

## Additional information

When the code in your sandbox plug-in attempts to connect to an external endpoint using https the CDS Sandbox will start TLS/SSL negotiation. The endpoint presents a certificate to use for encryption. If the certificate is within a list of known ROOT certificate authorities trusted by the CDS sandbox, the negotiation can proceed.

If the certificate is not within the list, the site may provide an intermediary certificate


<a name='seealso'></a>

### See also

[Write a plug-in](../../write-plug-in.md) <br /> 
[Set KeepAlive to false when interacting with external hosts in a plug-in](set-keepalive-false-interacting-external-hosts-plugin.md)<br /> 
[Set Timeout when making external calls in a plug-in](set-timeout-for-external-calls-from-plug-ins.md)