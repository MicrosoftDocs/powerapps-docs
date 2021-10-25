---
title: Use OAuth 2.0 implicit grant flow within your portal
description: Learn how to make client-side calls to external APIs and secure them by using OAuth implicit grant flow in your portal.
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/25/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
    - tapanm-msft
    - GitanjaliSingh33msft
    - dileepsinghmicrosoft
    - nickdoelman    
---

# Use OAuth 2.0 implicit grant flow within your portal

This feature allows a customer to make client-side calls to external APIs and secure them by using OAuth implicit grant flow. It provides an endpoint to obtain secure access tokens that will contain user identity information to be used by external APIs for authorization following OAuth 2.0 implicit grant flow. The identity information of a signed-in user is passed in a secured manner to the external AJAX calls. This will not only help developers to pass authentication context but will also help users to secure their APIs by using this mechanism.

> [!NOTE]
> For security best practices, it is recommended to use [custom certificates](admin\manage-custom-certificates.md) for OAuth 2.0 implicit grant flow. Using implicit grant flow without a custom certificate will eventually not be supported.

OAuth 2.0 implicit grant flow supports endpoints that a client can call to get an ID token. Two endpoints are used for this purpose: [authorize](#authorize-endpoint-details) and [token](#token-endpoint-details).

## Authorize endpoint details 

The URL for authorize endpoint is: `<portal_url>/_services/auth/authorize`. The authorize endpoint supports the following parameters:

| Parameter   | Required? | Description                             |
|---------------|-----------|---------------------------------------|
| client_id      | Yes       | A string that is passed when making a call to the authorize endpoint. You must ensure that the client ID is [registered with the portal](#register-client-id-for-implicit-grant-flow). Otherwise, an error is displayed. Client ID is added in claims in the token as `aud` as well as `appid` parameter and can be used by clients to validate that the token returned is for their app.<br>The maximum length is 36 characters. Only alphanumeric characters and hyphens are supported. |
| redirect_uri      | Yes       | URL of the portal where authentication responses can be sent and received. It must be registered for the particular `client_id` used in the call and should be exactly the same value as registered.            |
| state       | No        | A value included in the request that also is returned in the token response. It can be a string of any content that you want to use. Usually, a randomly generated, unique value is used to prevent cross-site-request forgery attacks.<br>The maximum length is 20 characters.              |
| nonce   | No        | A string value sent by the client that is included in the resulting ID token as a claim. The client can then verify this value to mitigate token replay attacks. The maximum length is 20 characters.      |
| response_type         | No        | This parameter supports only `token` as a value. This allows your app to immediately receive an access token from the authorize endpoint, without making a second request to the authorize endpoint.                               |
|||

### Successful response

The authorize endpoint returns the following values in the response URL as a fragment:

- **token**: Token is returned as a JSON Web Token (JWT) digitally signed by the portal’s private key.
- **state**: If a state parameter is included in the request, the same value should appear in the response. The app should verify that the state values in the request and response are identical.
- **expires_in**: The length of time that the access token is valid (in seconds).

For example, a successful response looks as follows:

```
GET https://aadb2cplayground.azurewebsites.net/#token=eyJ0eXAiOiJKV1QiLCJhbGciOI1NisIng1dCI6Ik5HVEZ2ZEstZnl0aEV1Q&expires_in=3599&state=arbitrary_data_you_sent_earlier
```

### Error response

The error in authorize endpoint is returned as a JSON document with the following values:

- **Error ID**: Unique identifier of the error.
- **Error message**: A specific error message that can help you identify the root cause of an authentication error.
- **Correlation ID**: A GUID that is used for debugging purposes. If you have enabled diagnostic logging, correlation ID would be present in server error logs.
- **Timestamp**: Date and time when the error is generated.

The error message is displayed in the default language of the signed-in user. If the user is not signed in, the sign-in page is displayed for the user to sign in. 
For example, an error response looks as follows:

```
{"ErrorId": "PortalSTS0001", "ErrorMessage": "Client Id provided in the request is not a valid client Id registered for this portal. Please check the parameter and try again.", "Timestamp": "4/5/2019 10:02:11 AM", "CorrelationId": "7464eb01-71ab-44bc-93a1-f221479be847" }
```

## Token endpoint details

You can also get a token by making a request to the `/token` endpoint. It is different from the authorization endpoint in the way that authorization endpoint handles the token logic in a separate page (redirect_uri), whereas the token endpoint handles the token logic on the same page. The URL for token endpoint is: `<portal_url>/_services/auth/token`. The token endpoint supports the following parameters:

| Parameter   | Required? | Description                             |
|---------------|-----------|---------------------------------------|
| client_id      | No       | A string that is passed when making a call to the authorize endpoint. You must ensure that the client ID is [registered with the portal](#register-client-id-for-implicit-grant-flow). Otherwise, an error is displayed. Client ID is added in claims in the token as `aud` as well as `appid` parameter and can be used by clients to validate that the token returned is for their app.<br>The maximum length is 36 characters. Only alphanumeric characters and hyphen are supported. |
| redirect_uri      | No       | URL of the portal where authentication responses can be sent and received. It must be registered for the particular `client_id` used in the call and should be exactly the same value as registered.            |
| state       | No        | A value included in the request that also is returned in the token response. It can be a string of any content that you want to use. Usually, a randomly generated, unique value is used to prevent cross-site-request forgery attacks.<br>The maximum length is 20 characters.              |
| nonce   | No        | A string value sent by the client that is included in the resulting ID token as a claim. The client can then verify this value to mitigate token replay attacks. The maximum length is 20 characters.      |
| response_type         | No        | This parameter supports only `token` as a value. This allows your app to immediately receive an access token from the authorize endpoint, without making a second request to the authorize endpoint.                               |
|||

> [!NOTE]
> Even though `client_id`, `redirect_uri`, `state`, and `nonce` parameters are optional, it is recommended to use them in order to make sure your integrations are secure.

### Successful response

The token endpoint returns state and expires_in as response headers, and token in the form body.

### Error response

The error in a token endpoint is returned as a JSON document with the following values:

- **Error ID**: Unique identifier of the error.
- **Error message**: A specific error message that can help you identify the root cause of an authentication error.
- **Correlation ID**: A GUID that is used for debugging purposes. If you have enabled diagnostic logging, correlation ID would be present in server error logs.
- **Timestamp**: Date and time when the error is generated.

The error message is displayed in the default language of the signed-in user. If the user is not signed in, a sign-in page is displayed for the user to sign in. 
For example, an error response looks as follows:

```
{"ErrorId": "PortalSTS0001", "ErrorMessage": "Client Id provided in the request is not a valid client Id registered for this portal. Please check the parameter and try again.", "Timestamp": "4/5/2019 10:02:11 AM", "CorrelationId": "7464eb01-71ab-44bc-93a1-f221479be847" }
```

## Validate ID token

Just getting an ID token is not sufficient to authenticate the user; you must also validate the token's signature and verify the claims in the token based on your app's requirements. The public token endpoint provides the public key of the portal, which can be used to validate the signature of the token provided by the portal. The URL for public token endpoint is: `<portal_url>/_services/auth/publickey`.

## Turn implicit grant flow on or off

By default, implicit grant flow is enabled. If you want to turn off implicit grant flow, set the value of the **Connector/ImplicitGrantFlowEnabled** site setting to **False**.

If this site setting is not available in your portal, you must [create a new site setting](configure/configure-site-settings.md#manage-portal-site-settings) with the appropriate value.

## Configure token validity

By default, the token is valid for 15 minutes. If you want to change the validity of token, set the value of the **ImplicitGrantFlow/TokenExpirationTime** site setting to the required value. The value must be specified in seconds. The maximum value can be 1 hour, and the minimum value must be 1 minute. If an incorrect value is specified (for example, alphanumeric characters), the default value of 15 minutes is used. If you specify a value more than the maximum value or less than the minimum value, the maximum and minimum values are used respectively, by default.

For example, to set the token validity to 30 minutes, set the value of the **ImplicitGrantFlow/TokenExpirationTime** site setting to **1800**. To set the token validity to 1 hour, set the value of the **ImplicitGrantFlow/TokenExpirationTime** site setting to **3600**.

## Register client ID for implicit grant flow

You must register the client ID with the portal for which this flow is allowed. To register a client ID, you must create the following site settings:

|Site setting|Value|
|------|------|
|ImplicitGrantFlow/RegisteredClientId|The valid client ID values that are allowed for this portal. The values must be separated by a semicolon and can contain alphanumeric characters and hyphens. The maximum length is 36 characters.|
|ImplicitGrantFlow/{ClientId}/RedirectUri|The valid redirect URIs that are allowed for a specific client ID. The values must be separated by a semicolon. The URL provided must be of a valid web page of the portal.|
|||

## Sample code

You can use the following sample code to get started with using OAuth 2.0 Implicit Grant with Power Apps portals APIs.

### Use Portal OAuth token with an external Web API

This sample is an ASP.NET based project and is used to validate the ID token issued by Power Apps portals. The complete sample can be found here: [Use Portal OAuth token with an external Web API](https://github.com/microsoft/PowerApps-Samples/tree/master/portals/ExternalWebApiConsumingPortalOAuthTokenSample).

### Authorize Endpoint sample

This sample shows how authorize endpoint returns the ID token as a fragment in the Redirected URL. It also covers state validation supported in Implicit Grant. The sample can be found here: [Authorize Endpoint sample](https://github.com/microsoft/PowerApps-Samples/blob/master/portals/AuthorizeEndpoint.js).

### Token Endpoint sample

This sample shows how you can use the getAuthenticationToken function to fetch an ID token using the Token endpoint in Power Apps portals. The sample can be found here: [Token Endpoint sample](https://github.com/microsoft/PowerApps-Samples/blob/master/portals/TokenEndpoint.js).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]