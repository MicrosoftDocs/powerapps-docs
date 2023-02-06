---
title: Add custom certificates
description: When extending portals functionality using a client-side API call with OAuth 2.0 implicit grant flow, configure custom certificates for added security.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 11/15/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
---

# Manage custom certificates

[!INCLUDE[cc-pages-ga-banner](../../../includes/cc-pages-ga-banner.md)]

When extending portals functionality using a client-side API call with [OAuth 2.0 implicit grant flow](../oauth-implicit-grant-flow.md), it's best practice to use custom certificates to provide an additional level of security. You can upload you own custom certificates using the Power Apps portals admin center.

> [!IMPORTANT]
> You cannot re-use the same custom certificate to set up a [custom host name](add-custom-domain.md). See [SSL Certificates](manage-ssl-certificates.md).

## Add new certificate

1. Open the [Power Apps portals admin center](admin-overview.md).

1. Select **Manage custom certificates**. The authentication key is displayed along with its expiration date and thumbprint.

1. Select **Add new** to upload a new certificate.

1. Select the upload button underneath **File** to select a .pfx certificate file. After selecting the file, enter the password for your SSL certificate in the **Password** field.

1. Select **OK** to upload the certificate.

    :::image type="content" source="media/manage-custom-certificates/upload-custom-certificate.png" alt-text="Upload a Certificate window with Upload file button and password box.":::

     > [!NOTE]
     > The SSL certificate must meet all of the following requirements:
     > - Signed by a trusted certificate authority
     > - [Exported](/powershell/module/pki/export-pfxcertificate) as a password-protected PFX file.
     > - Contains private key at least 2048 bits long
     > - Contains all intermediate certificates in the certificate chain
     > - Must be SHA2 enabled; SHA1 support is being removed from popular browsers
     > - PFX file must be encrypted with TripleDES encryption; Power Apps portals doesn't support AES-256 encryption
     > - Contains an [Extended Key Usage](https://en.wikipedia.org/w/index.php?title=X.509&section=4#Extensions_informing_a_specific_usage_of_a_certificate) for server authentication (OID = 1.3.6.1.5.5.7.3.1).
     > 
     > The steps to export SSL certificate as a password-protected PFX file may vary depending on your certificate provider. Check with your certificate provider for recommendation. For example, certain providers may suggest using an OpenSSL third-party tool from [OpenSSL](https://www.openssl.org/) or [OpenSSL Binaries](https://wiki.openssl.org/index.php/Binaries) sites. 


    :::image type="content" source="media/manage-custom-certificates/custom-certificates.png" alt-text="Manage custom certificates tab in the Power Apps portals admin center." :::

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
