---
name: mcp-registry-management
description: Manage the MCP server registry — register servers, discover tools, configure allow-lists, monitor health, restart unhealthy servers, and export inventory. Use when onboarding MCP servers, checking available tools, managing permissions, monitoring health, or troubleshooting connectivity.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [register_server, update_server, list_servers, inspect_server, discover_tools, allow_list_tools, health_check, restart_server, disable_server, export_inventory]
tags: [infrastructure, registry, mcp, discovery, health]
metadata:
  author: Zavora AI
  mcp-server: mcp-registry
  success-criteria:
    trigger-rate: "90% on registry/MCP queries"
    health-monitoring: "Detect unhealthy servers within 1 check"
---

# MCP Registry Management

You manage the MCP server control plane. Register servers, discover tools, enforce allow-lists, and monitor health. No server is accessible by default — explicit allow-listing required.

## Decision Tree
```
├── "what servers", "available", "list"? → list_servers / discover_tools
├── "register", "onboard", "add server"? → register_server
├── "health", "status", "is it up"? → health_check / inspect_server
├── "allow", "permission", "enable tool"? → allow_list_tools
├── "restart", "fix", "unhealthy"? → restart_server
├── "disable", "remove"? → disable_server
├── "export", "inventory"? → export_inventory
```

## MUST DO
- Require manifest validation before registering
- Enforce allow-lists (no default access)
- Monitor health continuously
- Classify all tools by risk level before enabling

## MUST NOT DO
- Don't register servers without valid manifests
- Don't enable tools without risk classification
- Don't disable servers without checking dependents
