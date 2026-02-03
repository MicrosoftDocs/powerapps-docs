---
title: "Troubleshoot issues with Zscaler"
description: "Use this guide when the pac code add-data-source command repeatedly fails behind a Zscaler (or similar SSL‑inspecting) proxy."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 02/02/2026
ms.reviewer: jdaly
ms.topic: article
contributors:
- JimDaly

---
# Troubleshoot Zscaler-related issues

This article provides troubleshooting steps for when the PAC CLI (Power Apps Command Line Interface)  [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) repeatedly fails behind a Zscaler or similar SSL-inspecting proxies.

Zscaler is a cloud-based security platform that performs Secure Socket Layer/Transport Layer Security (SSL/TLS) inspection by decrypting and re-encrypting HTTPS traffic. It acts as a man-in-the-middle (by design) to inspect content for threats. See [Zscaler SSL Inspection Overview](https://help.zscaler.com/zia/about-ssl-inspection)


## Symptoms

The following table lists symptoms that may indicate Zscaler-related issues.

| Symptom| Example Message / Pattern|
| --- | --- |
| Fetch Failed| `TypeError: fetch failed` / `[AddDataSource.ServiceCall.GetConnector.Failure] ... fetch failed` |
| Empty Request Failed| `Error: Request failed: {}` (no body)|
| TLS Handshake / Cert errors | `UNABLE_TO_VERIFY_LEAF_SIGNATURE` / `SELF_SIGNED CERT IN CHAIN` (if debug enabled)|
| Works off corporate network | Command succeeds when disconnected from Zscaler|

## Prerequisites checklist

Before you begin, verify the following:

1. The [latest Power Platform CLI](/power-platform/developer/cli/introduction#install-microsoft-power-platform-cli) is installed. Update it if you aren't sure.
1. You're authenticated to the correct environment. Use [`pac auth create`](/power-platform/developer/cli/reference/auth#pac-auth-create) and [`pac auth list`](/power-platform/developer/cli/reference/auth#pac-auth-list) commands.
1. Installed Node.js version is greater or equal to v22. Older versions have different trust behavior that are more strict.
1. You are able to read read the user certificate store. There are no locked‑down profile restrictions.
1. Your corporate policy permits adding Zscaler root CA to user trust for developer tooling.

## Troubleshooting steps

Use the information in the following sections to troubleshoot.

### Step 1: Validate baseline

To eliminate causes not related to a proxy, run the [`pac env who`](/power-platform/developer/cli/reference/env#pac-env-who) command.

If this command succeeds, general connectivity is fine; failures are isolated to data source calls.

### Step 2: Confirm that Zscaler is installed

Run this command to ensure that the Zscaler certificate exists in the store.

```powershell
Get-ChildItem Cert:\CurrentUser\Root |
    Where-Object { $_.Subject -like "*Zscaler*" } |
    Select-Object Subject, Thumbprint
```

If Zscaler injects its certificate, you see a Zscaler issuer instead of Microsoft.

> [!NOTE]
> When a proxy like Zscaler intercepts HTTPS traffic, it replaces the original server certificate with its own certificate signed by a corporate root CA. This allows the proxy to decrypt, inspect, and re-encrypt traffic. Browsers trust this because the corporate root CA is installed in the system trust store. See [How HTTPS Interception Works](https://www.cisa.gov/news-events/alerts/2017/03/16/https-interception-weakens-tls-security)


### Step 3: Export Zscaler root CA to PEM

Run this command to export the Zscaler Root Certificate Authority (CA) to Privacy Enhanced Mail (PEM)

```powershell
$cert = Get-ChildItem Cert:\CurrentUser\Root |
    Where-Object { $_.Subject -like "*Zscaler*" } |
    Select-Object -First 1

$pem = @(
    '-----BEGIN CERTIFICATE-----'
    [System.Convert]::ToBase64String(
        $cert.RawData,
        [System.Base64FormattingOptions]::InsertLineBreaks
    )
    '-----END CERTIFICATE-----'
) -join "`n"

Set-Content -Path "$env:USERPROFILE\.zscaler-root-ca.pem" -Value $pem
```

Result: `~\.zscaler-root-ca.pem` created.

> [!CAUTION]
> **Protect the PEM file:** Ensure proper file permissions on the exported certificate. If a malicious actor can replace this file, they could intercept HTTPS traffic from Node.js processes. Recommended hardening (removes inheritance then grants read-only): 
>
> ```powershell
> icacls "$env:USERPROFILE\.zscaler-root-ca.pem" /inheritance:r /grant:r "$env:USERNAME:(R)"
> ```
>
> If removing inheritance conflicts with corporate policy or triggers endpoint protection controls, skip `/inheritance:r` and only grant explicit read permission:
>
> ```powershell
> icacls "$env:USERPROFILE\.zscaler-root-ca.pem" /grant:r "$env:USERNAME:(R)"
> ```

#### Windows certificate store and PEM format

The `Get-ChildItem Cert:\CurrentUser\Root` command accesses the Windows Certificate Store via PowerShell's certificate provider. PEM is a Base64-encoded format for certificates. The conversion is necessary because Node.js requires PEM format while Windows stores certificates in DER (Distinguished Encoding Rules) format. See [PowerShell Certificate Provider](/powershell/module/microsoft.powershell.security/about/about_certificate_provider) and [PEM Format RFC](https://datatracker.ietf.org/doc/html/rfc7468)


#### Windows `icacls` command

`icacls` (Integrity Control Access Control List) is a Windows command-line utility for managing file permissions. The parameters used: `/inheritance:r` removes inherited permissions, `/grant:r` replaces existing permissions with read-only access for the specified user. See [icacls Documentation](/windows-server/administration/windows-commands/icacls)


### Step 4: Instruct Node.js to trust the certificate

Run the following script to instruct Node.js to trust the certificate.

```powershell
[System.Environment]::SetEnvironmentVariable('NODE_EXTRA_CA_CERTS', "$env:USERPROFILE\.zscaler-root-ca.pem", 'User')
```

Close & reopen terminal / VS Code to propagate.

> [!CAUTION]
> **Scope impact:** This [NODE_EXTRA_CA_CERTS Environment Variable](#node_extra_ca_certs-environment-variable) affects ALL Node.js processes run by your user account. If the PEM file is tampered with, every Node.js application trusts the modified certificate authority, not just the PAC CLI. Verify the file hash periodically and keep it secured.

#### NODE_EXTRA_CA_CERTS environment variable

This Node.js environment variable specifies a file containing more trusted Certificate Authorities beyond Node.js's built-in list (Mozilla's CA bundle). When set, Node.js trusts certificates signed by CAs in both the built-in list and the specified file. See [Node.js CLI Environment Variables](https://nodejs.org/api/cli.html#node_extra_ca_certsfile)

### Validate fix

Follow these steps to validate that the fix was correctly applied in Steps 3-4 before moving to Step 5.

1. Confirm that the PEM file was created and exists at the expected location

   ```powershell
    Test-Path "$env:USERPROFILE\.zscaler-root-ca.pem" # Expect True
   ```

1. Verify that the environment variable was set correctly and returns the path to the PEM file

    ```powershell
    [System.Environment]::GetEnvironmentVariable(
        'NODE_EXTRA_CA_CERTS',
        'User'
    )
    ```

1. Check that the PEM file has valid content rather than being empty or corrupted

    ```powershell
    Get-Content "$env:USERPROFILE\.zscaler-root-ca.pem" -TotalCount 2
    # First line should be: -----BEGIN CERTIFICATE-----
    ```
    
### Step 5: Re-run the command

Try running the command again.

```powershell
pac code add-data-source -a <apiId> -c <connectionId> [-t <tableName>] [-d <dataset|siteUrl>]
```

Expect connector retrieval success instead of fetch failure.

### (Avoid) Insecure workaround

A final, definitive test that should be avoided is to disable TLS validation temporarily.

This workaround forces Node.js to accept any presented certificate, including self-signed or spoofed certificates. This removes all authenticity and integrity guarantees of HTTPS. It exposes sessions to man-in-the-middle (MITM) attacks, credential harvesting, and content tampering. Never use outside a short-lived diagnostic session.

> [!WARNING]
> **Security Risk:** This completely disables SSL certificate validation for all Node.js HTTPS connections in the current session. Any attacker with network access can perform MITM attacks. Use this workaround ONLY for one-time diagnostic to prove certificate trust is the root cause. Never commit to scripts; never use in production environments; immediately unset after testing.

```powershell
$env:NODE_TLS_REJECT_UNAUTHORIZED = "0"
```

To unset after testing:

```powershell
Remove-Item Env:\NODE_TLS_REJECT_UNAUTHORIZED
```

## Validation

After applying the solution, retry your command. Look for successful connector retrieval:

```
[AddDataSource.ServiceCall.GetConnector.Start] { apiId: 'shared_office365users' }
[AddDataSource.ServiceCall.GetConnector.Success] { apiId: 'shared_office365users' }
```

Instead of:

```
[AddDataSource.ServiceCall.GetConnector.Failure] { apiId: 'shared_office365users', error: 'fetch failed' }
```

## Troubleshooting matrix

If you still experience issues after completing the [Troubleshooting steps](#troubleshooting-steps), investigate the following issues.

### `fetch failed` persists

Reconfirm `NODE_EXTRA_CA_CERTS` set after restarting shell; ensure PEM not zero bytes. Run the commands in [Validate fix](#validate-fix) to validate the file exists and the environment variable is properly set.

### Multiple Zscaler certs

If `Get-ChildItem Cert:\CurrentUser\Root | Where-Object { $_.Subject -like "*Zscaler*" }` returns multiple certificates, identify the root CA (typically named `Zscaler Root CA`). Modify [Step 3](#step-3-export-zscaler-root-ca-to-pem) to select the correct one by issuer name or thumbprint.

### Different proxy product

The solution works for any corporate proxy that performs SSL inspection (Blue Coat, Forcepoint, Netskope, etc.), but [Step 3](#step-3-export-zscaler-root-ca-to-pem) searches for `*Zscaler*` in the certificate subject. Adapt the filter to match your proxy:

```powershell
# For Blue Coat:
$cert = Get-ChildItem Cert:\CurrentUser\Root |
    Where-Object { $_.Subject -like "*Blue Coat*" } |
    Select-Object -First 1

# For Forcepoint:
$cert = Get-ChildItem Cert:\CurrentUser\Root |
    Where-Object { $_.Subject -like "*Forcepoint*" } |
    Select-Object -First 1
```

Then complete Steps 3-4 with the matched certificate.

### Works outside VPN only

When the command only works using an outside VPN, it indicates network-level blocking, not certificate trust issues. Corporate split-tunnel VPN configurations might route Power Platform API traffic through on-premises firewalls that block Node.js/CLI tools or apply restrictive policies to non-browser traffic.

The `NODE_EXTRA_CA_CERTS` fix doesn't help here. Engage your network/security team to:

- Allowlist PAC CLI traffic to `*.powerplatform.com`, `*.dynamics.com`, `*.azure.net`
- Allow direct HTTPS (port 443) from developer workstations to Microsoft cloud services
- Configure split-tunnel rules to bypass inspection/filtering for trusted Microsoft endpoints

#### Split-tunnel / allowlisting guidance

Some enterprise VPNs route only a subset of traffic directly while forcing other destinations through inspection gateways. Power Platform endpoints must be reachable without blocking or SSL interception conflicts. See Microsoft connectivity requirements for [endpoint allowlisting guidance](/power-platform/admin/online-requirements).

### `SELF_SIGNED CERT IN CHAIN`

Certificate chain is incomplete. Either export the full certificate chain (root + intermediates) or request your network team to provide the complete root CA bundle. Some proxies require both root and intermediate CAs to be trusted.

## Notes

Keep these notes in mind to maintain a secure and reliable setup when working behind SSL‑inspecting proxies like Zscaler:

- Repeat export if Zscaler rotates certificates.
- Changes only affect current user scope. There is no system‑wide risk.
- Safe: adds trust; doesn't disable validation.
- Use a dedicated devopment machine if policy restricts certificate export.

## Escalation data

If none of the steps in this article help, before you contact technical support, collect the following information and provide it:

- PAC CLI version: `pac --version`
- Node.js version: `node --version`
- OS + shell (for example, Windows PowerShell 7 / Windows CMD)
- Full command executed (sanitized)
- Sanitized error block (first occurrence)
- Value of `NODE_EXTRA_CA_CERTS` (PowerShell: `[System.Environment]::GetEnvironmentVariable('NODE_EXTRA_CA_CERTS','User')`)
- Presence & hash of PEM file (for example, `Get-FileHash $env:USERPROFILE\.zscaler-root-ca.pem`)

### Related articles

[Power Platform connectivity requirements](/power-platform/admin/online-requirements)  
[Node.js NODE_EXTRA_CA_CERTS documentation](https://nodejs.org/api/cli.html#node_extra_ca_certsfile)

