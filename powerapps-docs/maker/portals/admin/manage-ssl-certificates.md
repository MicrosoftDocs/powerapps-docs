---
title: Add SSL certificates
description: Learn how to add an SSL custom certificate to enable custom domain names for your portal.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/15/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---

# Manage SSL certificates

[!INCLUDE[cc-pages-ga-banner](../../../includes/cc-pages-ga-banner.md)]

You'll need an SSL certificate to set up a [custom host name](add-custom-domain.md). You can upload and update your own custom certificates by using the Power Apps portals admin center.

> [!IMPORTANT]
> You cannot re-use the same SSL certificate for extending portals functionality using a client-side API calls with [OAuth 2.0 implicit grant flow](../oauth-implicit-grant-flow.md). See [Manage Custom Certificates](manage-custom-certificates.md).

## SSL certificate requirements

An SSL certificate is a PFX file that must:

- Be signed by a trusted certificate authority.
- Be [exported](/powershell/module/pki/export-pfxcertificate) as a password-protected PFX file.
- Contain a private key at least 2,048 bits long.
- Contain all intermediate certificates in the certificate chain.
- Be SHA2-enabled; SHA1 support is being removed from popular browsers.
- Be encrypted with Triple DES encryption; Power Apps portals doesn't support AES-256 encryption.
- Contain an [Extended Key Usage](https://en.wikipedia.org/w/index.php?title=X.509&section=4#Extensions_informing_a_specific_usage_of_a_certificate) for server authentication (OID = 1.3.6.1.5.5.7.3.1).

## Add a new certificate

1. Open the [Power Apps portals admin center](admin-overview.md).

1. Select **Manage SSL certificates**. The certificate's subject name is displayed along with expiration date and thumbprint.

   :::image type="content" source="media/manage-ssl-certificates/ssl-certificates.png" alt-text="Manage SSL certificates tab in the Power Apps portals admin center." :::

1. Select **Add new**.

1. In the **Upload a Certificate** dialog, select **Upload file**, browse to select the certificate file, and then enter the password.

    :::image type="content" source="media/manage-custom-certificates/upload-custom-certificate.png" alt-text="Upload a Certificate dialog with an Upload file button and password field.":::

1. Select **OK**.

> [!NOTE]
> 
> The steps to export an SSL certificate as a password-protected PFX file can vary depending on your certificate provider. Check with your certificate provider for recommendations. For example, certain providers might suggest using an OpenSSL third-party tool from the [OpenSSL](https://www.openssl.org/) or [OpenSSL Binaries](https://wiki.openssl.org/index.php/Binaries) sites. 

### See also

[Add a custom domain name](add-custom-domain.md)<br>
[Configure SSL certificates and custom domain names](/training/modules/portals-administration/2-custom-domain)
