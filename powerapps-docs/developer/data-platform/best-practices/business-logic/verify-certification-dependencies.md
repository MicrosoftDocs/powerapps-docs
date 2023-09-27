---
title: "Verify certification dependencies for plug-ins making outbound calls | MicrosoftDocs"
description: "Ensure that any certificates that your code depends on for outbound calls has a valid chain of certificates."
ms.date: 04/03/2022
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
suite: powerapps
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
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

You should verify that the site you want to connect with has a valid chain of certificates. Use one of the online test tools such as [Qualys SSL Labs SSL Server Test](https://www.ssllabs.com/ssltest/analyze.html) to verify that the site provides a valid chain of certificates.


<a name='additional'></a>

## Additional information

You may encounter this when connecting to a new endpoint for the first time or when something about the certificate has changed.

When the code in your plug-in running in the sandbox attempts to connect to an external endpoint using https, the Dataverse Sandbox will start SSL/TLS negotiation. The endpoint presents a certificate to use for encryption. If the certificate has one or more intermediate certificates it must present the entire chain to successfully complete SSL/TLS negotiation. If the complete chain is not presented SSL/TLS communication cannot be established. 

For more information about requirements, see [Server cipher suites and TLS requirements](/power-platform/admin/server-cipher-tls-requirements).


<a name='seealso'></a>

### See also

[Write a plug-in](../../write-plug-in.md) <br /> 
[Set KeepAlive to false when interacting with external hosts in a plug-in](set-keepalive-false-interacting-external-hosts-plugin.md)<br /> 
[Set Timeout when making external calls in a plug-in](set-timeout-for-external-calls-from-plug-ins.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
