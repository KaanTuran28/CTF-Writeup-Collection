---
title: 🧪 EXAMPLE / TEMPLATE — Practice Lab Basic Enumeration
platform: CTF
category: Web
difficulty: Easy
date: 2026-08-20
tools: nmap, gobuster, curl
---

> **This is a template demonstration, not a real submission.** It exists only to
> show the writeup format defined in [`template.md`](../template.md). It does not
> describe a real, currently-active room on any specific platform, and it contains
> no real flag values. Actual completed writeups will be added here over
> time, following this same format.

## Summary

A generic beginner-friendly enumeration exercise: a single host exposing a web
server and SSH, where the goal is to enumerate hidden content and identify a
misconfiguration that leads to further access.

## Recon

- `nmap -sV -p- <target>` reveals two open ports: 22 (SSH) and 80 (HTTP).
- The web server's default page gives no obvious clues, so directory
  enumeration is the next step: `gobuster dir -u http://<target> -w <wordlist>`.
- Enumeration turns up a hidden `/backup/` directory containing a configuration
  file that was not meant to be publicly accessible.

## Exploitation

- The exposed configuration file contains a set of credentials reused from the
  web application. This is a classic **sensitive data exposure** issue (OWASP
  A01/A05 territory, depending on framing).
- The recovered credentials are valid for the SSH service, giving an initial
  foothold.

## Privilege Escalation

- Not applicable to this example — a real writeup would document the
  enumeration of `sudo -l`, SUID binaries, cron jobs, or kernel version here.

## Key Takeaways

- Always enumerate for backup/config files left behind in web roots
  (`/backup`, `/.git`, `/config.old`, etc.) — a very common real-world finding,
  not just a CTF trope.
- Credential reuse between a web app and system accounts is a recurring theme
  worth checking early.
